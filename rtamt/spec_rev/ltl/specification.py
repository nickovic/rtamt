import logging
import importlib

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.spec_rev.abstract_specification import AbstractSpecification

from rtamt.antrl_parser.ltl.LtlLexer import LtlLexer
from rtamt.antrl_parser.ltl.LtlParser import LtlParser
from rtamt.antrl_parser.ltl.error.parser_error_listener import LTLParserErrorListener
from rtamt.ast.parser_visitor.ltl.rtamtASTparser import LTLrtamtASTparser

from rtamt.parser.ltl.error.parser_error_listener import LTLParserErrorListener
from rtamt.exception.stl.exception import STLParseException

from rtamt.spec_rev.ltl.reset import LTLReset #TODO: it shoubd be option
from rtamt.spec_rev.ltl.pastifier import LTLPastifier
from rtamt.evaluator.ltl.online_evaluator import LTLEvaluator
from rtamt.enumerations.options import *


class LTLrevSpecification(AbstractSpecification):
    """A class used as a container for STL specifications

    Attributes:
        name : String

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names

        sampling_period : int - size of the sampling period


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
        super(LTLrevSpecification, self).__init__(LtlLexer, LtlParser, LTLParserErrorListener, LTLrtamtASTparser)

        self.name = 'LTL Specification'

        self.reseter = LTLReset()
        self.semantics = semantics
        self.language = language

    def pastify(self):
        # Translate bounded future STL to past STL
        pastifier = LTLPastifier()
        self.top.accept(pastifier)

        # evaluate modular sub-specs
        for key in self.var_subspec_dict:
            node = self.var_subspec_dict[key]
            node.accept(pastifier)
            node = pastifier.pastify(node)
            self.var_subspec_dict[key] = node

        past = pastifier.pastify(self.top)
        self.top = past

    def update(self, timestamp, list_inputs):
        # timestamp - float
        # inputs - list of [var name, var value] pairs
        # Example:
        # update(3.48, [['a', 2.2], ['b', 3.3]])

        if self.online_evaluator == None:
            self.online_evaluator = LTLEvaluator(self)
            self.top.accept(self.online_evaluator)

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

        return out

    def evaluate(self, *args, **kargs):
        pass

    def reset(self):
        if self.online_evaluator is not None:
            self.reseter.node_monitor_dict = self.online_evaluator.node_monitor_dict
            self.top.accept(self.reseter)
            self.reseter.reset(self.top)
            self.update_counter = int(0)
            self.previous_time = float(0.0)
            self.sampling_violation_counter = int(0)
