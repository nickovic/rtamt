import logging
import importlib

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.spec.abstract_specification import AbstractSpecification

from rtamt.parser.stl.StlLexer import StlLexer
from rtamt.parser.stl.StlParser import StlParser
from rtamt.spec.stl.discrete_time.specification_parser import STLSpecificationParser

from rtamt.parser.stl.error.parser_error_listener import STLParserErrorListener
from rtamt.exception.stl.exception import STLParseException

from rtamt.spec.stl.discrete_time.pastifier import STLPastifier
from rtamt.evaluator.stl.online_evaluator import STLEvaluator
from rtamt.spec.stl.discrete_time.reset import STLReset
from rtamt.enumerations.options import *


class STLDiscreteTimeSpecification(AbstractSpecification):
    """A class used as a container for STL specifications

    Attributes:
        name : String

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names

        sampling_period : int - size of the sampling period in ps (default = 10^12 ps = 1s


        var_object_dict : dict(String,AbstractNode) - dictionary that maps variable names to their Node instances
        modules : dict(String,String) - dictionary that maps module paths to module names

        top : AbstractNode - pointer to the specification parse tree

        online_evaluator : AbstractEvaluator - pointer to the object that implements the monitoring algorithm

        update_counter : int
        previous_time : float
        sampling_violation_counter : int

    """

    def __init__(self, is_pure_python=True, semantics=Semantics.STANDARD, language=Language.PYTHON):
        """Constructor for STL Specification"""
        super(STLDiscreteTimeSpecification, self).__init__(is_pure_python)
        self.name = 'STL Specification'

        self.DEFAULT_TOLERANCE = float(0.1)

        # Default sampling period - 1s
        self.sampling_period = int(1)
        self.sampling_period_unit = 's'

        # Default sampling tolerance
        self.sampling_tolerance = float(0.1)

        self.update_counter = int(0)
        self.previous_time = float(0.0)
        self.sampling_violation_counter = int(0)

        self.normalize = float(1.0)

        self.reseter = STLReset()
        self.semantics = semantics
        self.language = language

        self.in_vars = set()
        self.out_vars = set()

    def set_var_io_type(self, var_name, var_iotype):
        if not var_name in self.vars:
            logging.warning('The variable {} does not exist'.format(var_name))
        else:
            if var_iotype == 'input':
                self.add_input_var(var_name)
                self.remove_output_var(var_name)
                self.var_io_dict[var_name] = 'input'
            elif var_iotype == 'output':
                self.add_output_var(var_name)
                self.remove_input_var(var_name)
                self.var_io_dict[var_name] = 'output'
            else:
                self.remove_input_var(var_name)
                self.remove_output_var(var_name)
                self.var_io_dict[var_name] = 'undefined'

    def add_input_var(self, input_var):
        self.in_vars.add(input_var)

    def remove_input_var(self, var):
        self.in_vars.discard(var)

    def add_output_var(self, output_var):
        self.out_vars.add(output_var)

    def remove_output_var(self, var):
        self.out_vars.discard(var)

    def import_module(self, from_name, module_name):
        try:
            module = importlib.import_module(from_name)
            self.modules[module_name] = module
        except ImportError:
            raise STLParseException('The module {} cannot be loaded'.format(from_name))

    def declare_const(self, const_name, const_type, const_val):
        if const_name in self.vars:
            raise STLParseException('Constant {} already declared'.format(const_name))

        self.const_type_dict[const_name] = const_type
        self.const_val_dict[const_name] = const_val
        self.vars.add(const_name)

    def declare_var(self, var_name, var_type):
        if var_name in self.vars:
            logging.warning(
                'Variable {} was already declared. It is now overriden with the new declaration.'.format(var_name))

        # Associate to variable name 'var' its type 'type'
        self.var_type_dict[var_name] = var_type

        # Add variable name 'var' to the set of variables
        self.add_var(var_name)
        self.free_vars.add(var_name)
        instance = self.create_var_from_name(var_name)
        self.var_object_dict[var_name] = instance

        # Add the default variable topic to var
        self.var_topic_dict[var_name] = 'rtamt/{}'.format(var_name)

        self.var_io_dict[var_name] = 'output'

    def set_var_topic(self, var_name, var_topic):
        if not var_name in self.vars:
            logging.warning(
                'The variable {0} is not declared. Setting its topic name to {1} is ignored.'.format(var_name,
                                                                                                     var_topic))
        else:
            topic = self.var_topic_dict[var_name]
            self.var_topic_dict[var_name] = var_topic

    def create_var_from_name(self, var_name):
        var = None
        var_type = self.var_type_dict[var_name]
        if var_type.encode('utf-8') == 'float'.encode('utf-8'):
            var = float()
        elif var_type.encode('utf-8') == 'int'.encode('utf-8'):
            var = int()
        elif var_type.encode('utf-8') == 'complex'.encode('utf-8'):
            var = complex()
        else:
            try:
                var_module = self.spec.modules[var_type]
                class_ = getattr(var_module, var_type)
                var = class_()
            except KeyError:
                raise STLParseException('The type {} does not seem to be imported.'.format(var_type))
        return var

    @property
    def semantics(self):
        return self.__semantics

    @semantics.setter
    def semantics(self, semantics):
        self.__semantics = semantics

    @property
    def in_vars(self):
        return self.__in_vars

    @in_vars.setter
    def in_vars(self, in_vars):
        self.__in_vars = in_vars

    @property
    def out_vars(self):
        return self.__out_vars

    @out_vars.setter
    def out_vars(self, out_vars):
        self.__out_vars = out_vars

    # Parses the STL property
    # string can be either file path containing the STL property
    # or the textual property itself
    def parse(self):
        if self.spec is None:
            raise STLParseException('STL specification if empty')

        # Parse the STL spec - ANTLR4 magic

        entire_spec = self.modular_spec + self.spec
        input_stream = InputStream(entire_spec)
        lexer = StlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = StlParser(stream)
        parser._listeners = [STLParserErrorListener()]
        ctx = parser.stlfile()

        # Create the visitor for the actual spec nodes
        visitor = STLSpecificationParser(self)
        self.top = visitor.visitStlfile(ctx)

        # Translate bounded future STL to past STL
        pastifier = STLPastifier(self.is_pure_python)
        self.top.accept(pastifier)
        past = pastifier.pastify(self.top)
        self.top = past

        # Initialize the online_evaluator
        self.online_evaluator = STLEvaluator(self)
        self.top.accept(self.online_evaluator)

        self.normalize = float(self.U[self.unit]) / float(self.U[self.sampling_period_unit])


    def update(self, timestamp, list_inputs):
        # timestamp - float
        # inputs - list of [var name, var value] pairs
        # Example:
        # update(3.48, [['a', 2.2], ['b', 3.3]])

        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        if self.update_counter > 0:
            duration = (timestamp - self.previous_time) * self.normalize
            tolerance = self.sampling_period * self.sampling_tolerance
            if duration < self.sampling_period - tolerance or duration > self.sampling_period + tolerance:
                self.sampling_violation_counter = self.sampling_violation_counter + 1

        # update the value of every input variable
        for inp in list_inputs:
            var_name = inp[0]
            var_value = inp[1]
            self.var_object_dict[var_name] = var_value

        # evaluate modular sub-specs
        for key in self.var_subspec_dict:
            node = self.var_subspec_dict[key]
            out = self.online_evaluator.evaluate(node, [])
            self.var_object_dict[key] = out

        # The evaluation done wrt the discrete counter (logical time)
        out = self.online_evaluator.evaluate(self.top, [])

        self.previous_time = timestamp
        self.update_counter = self.update_counter + 1

        return out

    def evaluate(self, *args, **kargs):
        pass

    def reset(self):
        self.top.accept(self.reseter)
        self.reseter.reset(self.top)
        self.update_counter = int(0);
        self.previous_time = float(0.0);
        self.sampling_violation_counter = int(0);


    @property
    def sampling_period(self):
        return self.__sampling_period

    @sampling_period.setter
    def sampling_period(self, sampling_period):
        self.__sampling_period = sampling_period

    @property
    def sampling_period_unit(self):
        return self.__sampling_period_unit

    @sampling_period_unit.setter
    def sampling_period_unit(self, sampling_period_unit):
        self.__sampling_period_unit = sampling_period_unit

    @property
    def sampling_violation_counter(self):
        return self.__sampling_violation_counter

    @sampling_violation_counter.setter
    def sampling_violation_counter(self, sampling_violation_counter):
        self.__sampling_violation_counter = sampling_violation_counter

    def set_sampling_period(self, sampling_period=int(1), unit='s', tolerance=float(0.1)):
        self.sampling_period = sampling_period
        self.sampling_period_unit = unit

        if tolerance < 0.0 or tolerance > 1.0:
            raise STLSpecificationException

        self.sampling_tolerance = tolerance

    def get_sampling_period(self):
        return self.sampling_period * self.U[self.sampling_period_unit]

    def get_sampling_frequency(self):
        return 1e12 * 1/self.sampling_period

    @property
    def update_counter(self):
        return self.__update_counter

    @update_counter.setter
    def update_counter(self, update_counter):
        self.__update_counter = update_counter


    # def offline(self, dataset):
    #     counter = 0
    #     prev_signal_length = 0
    #     signal_length = 0
    #     out = 0
    #
    #     for var_name in dataset:
    #         signal_length = len(dataset[var_name])
    #         if counter > 0 and not (signal_length == prev_signal_length):
    #             raise STLOfflineException('Input signals have different length')
    #         prev_signal_length = signal_length
    #         counter = counter + 1
    #
    #     for i in range(signal_length):
    #         signal_snapshot = []
    #         counter = 0
    #         prev_time = 0
    #         for var_name in dataset:
    #             signal = dataset[var_name]
    #             sample = signal[i]
    #             time = sample[0]
    #             value = sample[1]
    #             if counter > 0 and not (time == prev_time):
    #                 raise STLOfflineException('The time indices do not agree')
    #             signal_snapshot.append((var_name, value))
    #             counter = counter + 1
    #             prev_time = time
    #         out = self.update(time, signal_snapshot)
    #
    #     return out
