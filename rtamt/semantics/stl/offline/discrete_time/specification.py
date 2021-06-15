import logging
import importlib

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.semantics.abstract_offline_specification import AbstractOfflineSpecification
from rtamt.parser.stl.StlLexer import StlLexer
from rtamt.parser.stl.StlParser import StlParser
from rtamt.ast.parser_visitor.stl.rtamtASTparser import STLrtamtASTparser
from rtamt.semantics.discrete_time.offline.stl.eval_visitor import STLOfflineDiscreteTimePythonEvalVisitor

from rtamt.parser.stl.error.parser_error_listener import STLParserErrorListener
from rtamt.exception.stl.exception import STLParseException

from rtamt.spec.stl.discrete_time.reset import STLReset
from rtamt.enumerations.options import *

from rtamt.exception.stl.exception import STLException

class STLDiscreteTimeOfflineSpecification(AbstractOfflineSpecification):

    def __init__(self, semantics=Semantics.STANDARD, language=Language.PYTHON):
        """Constructor for STL Specification"""
        super(STLDiscreteTimeOfflineSpecification, self).__init__(StlLexer, StlParser, STLrtamtASTparser)

        #from LTL discrete TODO:think here is good place or not
        self.semantics = semantics
        self.language = language
        self.in_vars = set()
        self.out_vars = set()
        #---


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


    # Parses the STL property
    # string can be either file path containing the STL property
    # or the textual property itself
    def parse(self):
        if self.spec is None:
            raise STLParseException('STL specification if empty')

        # Parse the STL spec - ANTLR4 magic

        entire_spec = self.modular_spec + self.spec
        input_stream = InputStream(entire_spec)
        lexer = self.lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = self.parser(stream)
        parser._listeners = [STLParserErrorListener()]
        ctx = parser.specification_file()

        # Create the visitor for the actual spec nodes
        visitor = self.rtamtASTparser(self)   #TODO: paser becomes visitor is problematic nameing.
        self.top = visitor.visitSpecification_file(ctx)

        self.normalize = float(self.U[self.unit]) / float(self.U[self.sampling_period_unit])

    def evaluate(self, *args, **kargs):
        if len(args) != 1:
            raise STLException('evaluate: Wrong number of arguments')

        dataset = args[0]

        if not dataset['time']:
            raise STLException('evaluate: The input does not contain the time field')

        length = len(dataset['time'])

        for key in dataset:
            if len(dataset[key]) != length:
                raise STLException('evaluate: The input ' + key + ' does not have the same number of samples as time')

        if self.offline_evaluator is None:
            # Initialize the offline_evaluator
            self.offline_evaluator = STLOfflineDiscreteTimePythonEvalVisitor(self)
            self.top.accept(self.offline_evaluator)
            #self.reseter.node_monitor_dict = self.offline_evaluator.node_monitor_dict

        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        ts = dataset['time']
        for i in range(len(ts) - 1):
            duration = (ts[i+1] - ts[i]) * self.normalize
        tolerance = self.sampling_period * self.sampling_tolerance
        if duration < self.sampling_period - tolerance or duration > self.sampling_period + tolerance:
            self.sampling_violation_counter = self.sampling_violation_counter + 1


        # update the value of every input variable
        for key in dataset:
            if key != 'time':
                self.var_object_dict[key] = dataset[key]

        # evaluate modular sub-specs
        for key in self.var_subspec_dict:
            node = self.var_subspec_dict[key]
            out = self.offline_evaluator.evaluate(node, [length])
            self.var_object_dict[key] = out

        # The evaluation done wrt the discrete counter (logical time)
        out = self.offline_evaluator.evaluate(self.top, [length])

        out_t = []
        for i in range(len(ts)):
            out_sample = [ts[i], out[i]]
            out_t.append(out_sample)
        out = out_t

        return out

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
            raise STLException('Tolerance must be in [0,1]')

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
                var_module = self.modules[var_type]
                class_ = getattr(var_module, var_type)
                var = class_()
            except KeyError:
                raise STLParseException('The type {} does not seem to be imported.'.format(var_type))
        return var

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

    def declare_const(self, const_name, const_type, const_val):
        if const_name in self.vars:
            raise STLParseException('Constant {} already declared'.format(const_name))

        self.const_type_dict[const_name] = const_type
        self.const_val_dict[const_name] = const_val
        self.vars.add(const_name)
