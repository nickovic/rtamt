import logging
import importlib

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.spec_rev.abstract_offline_specification import AbstractOfflineSpecification

from rtamt.antrl_parser.stl.StlLexer import StlLexer
from rtamt.antrl_parser.stl.StlParser import StlParser
from rtamt.ast.parser_visitor.stl.rtamtASTparser import STLrtamtASTparser
from rtamt.parser.stl.error.parser_error_listener import STLParserErrorListener
from rtamt.exception.stl.exception import STLParseException

from rtamt.semantics.discrete_time.offline.stl.offline_evaluator import STLOfflineEvaluator
from rtamt.spec.stl.discrete_time.reset import STLReset
from rtamt.enumerations.options import *

from rtamt.exception.stl.exception import STLException

class STLDiscreteTimeOfflineSpecification(AbstractOfflineSpecification):
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
        self.semantics = semantics #TODO: re-think the declearation is here?
        self.language = language
        super(STLDiscreteTimeOfflineSpecification, self).__init__(StlLexer, StlParser, STLParserErrorListener, STLrtamtASTparser, STLOfflineEvaluator)
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

        self.reseter = STLReset()   #TODO: the location is not correct.


    # Parses the STL property
    # string can be either file path containing the STL property
    # or the textual property itself
    def parse(self):
        super(STLrevDiscreteTimeSpecification, self).parse()

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

        #TODO: this should be done in AbstractOfflineSpecification! but because of difficulty of call evaluator, we could not.
        if self.offline_evaluator is None:
            # Initialize the offline_evaluator
            self.offline_evaluator = self.RtamtOfflineEvaluator(self)
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


