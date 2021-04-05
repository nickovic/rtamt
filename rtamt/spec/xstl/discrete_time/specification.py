from antlr4 import *
from antlr4.InputStream import InputStream
from rtamt.parser.xstl.error.parser_error_listener import STLExtendedParserErrorListener
from rtamt.spec.stl.discrete_time.specification import STLDiscreteTimeSpecification
from rtamt.parser.xstl.StlExtendedLexer import StlExtendedLexer
from rtamt.parser.xstl.StlExtendedParser import StlExtendedParser
from rtamt.exception.stl.exception import STLParseException
from rtamt.evaluator.stl.online_evaluator import STLOnlineEvaluator
from rtamt.enumerations.options import *
from rtamt.spec.xstl.discrete_time.pastifier import XSTLPastifier
from rtamt.spec.xstl.discrete_time.reset import XSTLReset
from rtamt.spec.xstl.discrete_time.specification_parser import XSTLSpecificationParser
from rtamt.exception.exception import RTAMTException


class XSTLDiscreteTimeSpecification(STLDiscreteTimeSpecification):
    def __init__(self, semantics=Semantics.STANDARD, language=Language.PYTHON):
        """Constructor for STL Specification"""
        STLDiscreteTimeSpecification.__init__(semantics, language)
        self.reseter = XSTLReset()


    # Parses the STL property
    # string can be either file path containing the STL property
    # or the textual property itself
    def parse(self):
        if self.spec is None:
            raise STLParseException('XSTL specification if empty')

        # Parse the STL spec - ANTLR4 magic

        entire_spec = self.modular_spec + self.spec
        input_stream = InputStream(entire_spec)
        lexer = StlExtendedLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = StlExtendedParser(stream)
        parser._listeners = [STLExtendedParserErrorListener()]
        ctx = parser.specification_file()

        # Create the visitor for the actual spec nodes
        visitor = XSTLSpecificationParser(self)
        self.top = visitor.visitSpecification_file(ctx)

        self.normalize = float(self.U[self.unit]) / float(self.U[self.sampling_period_unit])

    def pastify(self):
        # Translate bounded future STL to past STL
        pastifier = XSTLPastifier()
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
        raise RTAMTException('Offline monitoring algorithm not implemented.')

