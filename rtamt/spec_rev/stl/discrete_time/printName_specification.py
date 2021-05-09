import logging
import importlib

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.evaluator.stl.offline_evaluator import STLOfflineEvaluator
from rtamt.ast.parser_visitor.stl.printNameVisitor import PrintNameVisitor

from rtamt.spec_rev.ltl.specification import LTLrevSpecification

from rtamt.antrl_parser.stl.StlLexer import StlLexer
from rtamt.antrl_parser.stl.StlParser import StlParser
from rtamt.ast.parser_visitor.stl.rtamtASTparser import STLSpecificationParser

from rtamt.parser.stl.error.parser_error_listener import STLParserErrorListener
from rtamt.exception.stl.exception import STLParseException

#from rtamt.spec.stl.discrete_time.pastifier import STLPastifier
#from rtamt.evaluator.stl.online_evaluator import STLOnlineEvaluator
from rtamt.spec.stl.discrete_time.reset import STLReset
from rtamt.enumerations.options import *

from rtamt.exception.stl.exception import STLException

class PrintNameSpecification(LTLrevSpecification):
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
        LTLrevSpecification.__init__(self, semantics, language)
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

    def printName(self, *args, **kargs):
        printNameVisitor = PrintNameVisitor()
        printNameVisitor.visit(self.top)

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
