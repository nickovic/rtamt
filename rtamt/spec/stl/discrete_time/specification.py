from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.evaluator.stl.offline_evaluator import STLOfflineEvaluator
from rtamt.spec.ltl.discrete_time.specification import LTLDiscreteTimeSpecification

from rtamt.parser.stl.StlLexer import StlLexer
from rtamt.parser.stl.StlParser import StlParser
from rtamt.spec.stl.discrete_time.specification_parser import STLSpecificationParser

from rtamt.parser.stl.error.parser_error_listener import STLParserErrorListener
from rtamt.exception.stl.exception import STLParseException

from rtamt.pastifier.stl.pastifier import STLPastifier
from rtamt.evaluator.stl.online_evaluator import STLOnlineEvaluator
from rtamt.reset.stl.reset import STLReset
from rtamt.enumerations.options import *

from rtamt.exception.stl.exception import STLException

class STLDiscreteTimeSpecification(LTLDiscreteTimeSpecification):
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

    def __init__(self, semantics=Semantics.STANDARD, language=Language.PYTHON):
        """Constructor for STL Specification"""
        super(STLDiscreteTimeSpecification, self).__init__(semantics, language)
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
        ctx = parser.specification_file()

        # Create the visitor for the actual spec nodes
        visitor = STLSpecificationParser(self)
        self.top = visitor.visitSpecification_file(ctx)

        # print('Hello')
        # print(self.unit)
        # print('sampling period unit: ' + str(self.sampling_period_unit))
        # print(self.U[self.unit])
        # print(self.U[self.sampling_period_unit])

        self.normalize = float(self.U[self.unit]) / float(self.U[self.sampling_period_unit])

    def pastify(self):
        # Translate bounded future STL to past STL
        pastifier = STLPastifier()
        self.top.accept(pastifier)
        past = pastifier.pastify(self.top)
        self.top = past

        # evaluate modular sub-specs
        for key in self.var_subspec_dict:
            node = self.var_subspec_dict[key]
            node.accept(pastifier)
            node = pastifier.pastify(node)
            self.var_subspec_dict[key] = node

    def update(self, timestamp, list_inputs):
        # timestamp - float
        # inputs - list of [var name, var value] pairs
        # Example:
        # update(3.48, [['a', 2.2], ['b', 3.3]])

        if self.online_evaluator is None:
            # Initialize the online_evaluator
            self.online_evaluator = STLOnlineEvaluator(self)
            self.top.accept(self.online_evaluator)
            self.reseter.node_monitor_dict = self.online_evaluator.node_monitor_dict

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
        # sample - list of [time, value] pairs
        # inputs - list of [var name, sample] pairs
        # Example:
        # a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        # b = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]
        # evaluate(['a', a], ['b', b])

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
            self.offline_evaluator = STLOfflineEvaluator(self)
            self.top.accept(self.offline_evaluator)
            self.reseter.node_monitor_dict = self.offline_evaluator.node_monitor_dict

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

        out_t = [[a[0],a[1]] for a in zip(ts,out)]
        out = out_t

        return out

    def reset(self):
        if self.online_evaluator is not None:
            self.reseter.node_monitor_dict = self.online_evaluator.node_monitor_dict

            # evaluate modular sub-specs
            for key in self.var_subspec_dict:
                node = self.var_subspec_dict[key]
                self.reseter.reset(node)

            self.top.accept(self.reseter)
            self.reseter.reset(self.top)
            self.update_counter = int(0)
            self.previous_time = float(0.0)
            self.sampling_violation_counter = int(0)


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


