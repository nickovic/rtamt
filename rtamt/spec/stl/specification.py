# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:32:57 2019

@author: NickovicD
"""

import logging
import importlib
import operator

from antlr4 import *
from antlr4.InputStream import InputStream

from rtamt.spec.abstract_specification import AbstractSpecification

from rtamt.parser.stl.StlLexer import StlLexer
from rtamt.parser.stl.StlParser import StlParser
from rtamt.parser.stl.StlParserVisitor import StlParserVisitor

from rtamt.parser.stl.error.parser_error_listener import STLParserErrorListener
from rtamt.exception.stl.exception import STLParseException
from rtamt.exception.stl.exception import STLOfflineException

from rtamt.spec.stl.specification_parser import STLSpecificationParser
from rtamt.spec.stl.pastifier import STLPastifier
from rtamt.spec.stl.evaluator import STLEvaluator
from rtamt.spec.stl.reset import STLReset


class STLSpecification(AbstractSpecification,StlParserVisitor):
    """A class used as a container for STL specifications

    Attributes:
        name : String

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names

        var_object_dict : dict(String,AbstractNode) - dictionary that maps variable names to their Node instances
        modules : dict(String,String) - dictionary that maps module paths to module names

        top : AbstractNode - pointer to the specification parse tree

        evaluator : AbstractEvaluator - pointer to the object that implements the monitoring algorithm
    """
    def __init__(self, is_pure_python = True):
        """Constructor for STL Specification"""
        super(STLSpecification, self).__init__(is_pure_python)
        self.name = 'STL Specification'
        self.reseter = STLReset()


    # Parses the STL property
    # string can be either file path containing the STL property
    # or the textual property itself
    def parse(self):
        if self.spec is None:
            raise STLParseException ('STL specification if empty')

        # Parse the STL spec - ANTLR4 magic
        input_stream = InputStream(self.spec)
        lexer = StlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = StlParser(stream)
        parser._listeners = [STLParserErrorListener()]
        ctx = parser.stlfile()

        # Visit the parse tree and populate spec fields
        # self.visitStlfile(ctx)

        # Create the visitor for the actual spec nodes
        visitor = STLSpecificationParser(self)
        self.top = visitor.visitStlfile(ctx)

        # Translate bounded future STL to past STL
        pastifier = STLPastifier(self.is_pure_python)
        self.top.accept(pastifier)
        past = pastifier.pastify(self.top)
        self.top = past

        # Initialize the evaluator
        self.evaluator = STLEvaluator(self)
        self.top.accept(self.evaluator)

        self.normalize = float(self.U[self.unit]) / float(self.U[self.sampling_period_unit])

    def update(self, *args, **kargs):
        # args[0] : timestamp - float
        # args[1] : inputs - list of [var name, var value] pairs
        # Example:
        # update(3.48, [['a', 2.2], ['b', 3.3]])
        timestamp = args[0]
        inputs = args[1]

        # Check if the difference between two consecutive timestamps is between
        # the accepted tolerance - if not, increase the violation counter
        if self.update_counter > 0:
            duration = (timestamp - self.previous_time) * self.normalize
            tolerance = self.sampling_period * self.sampling_tolerance
            if duration < self.sampling_period-tolerance or duration > self.sampling_period+tolerance:
                self.sampling_violation_counter = self.sampling_violation_counter + 1

        for inp in inputs:
            var_name = inp[0]
            var_value = inp[1]
            self.var_object_dict[var_name] = var_value

        # The evaluation done wrt the discrete counter (logical time)
        out = self.evaluator.evaluate(self.top, [self.update_counter])

        self.previous_time = timestamp
        self.update_counter = self.update_counter + 1

        return out

    def reset(self):
        self.top.accept(self.reseter)
        self.reseter.reset(self.top)
        self.update_counter = 0;
        self.previous_time = 0.0;
        self.sampling_violation_counter = 0;

    def offline(self, dataset):
        counter = 0
        prev_signal_length = 0
        signal_length = 0
        out = 0

        for var_name in dataset:
            signal_length = len(dataset[var_name])
            if counter > 0 and not (signal_length == prev_signal_length):
                raise STLOfflineException('Input signals have different length')
            prev_signal_length = signal_length
            counter = counter + 1

        for i in range(signal_length):
            signal_snapshot = []
            counter = 0
            prev_time = 0
            for var_name in dataset:
                signal = dataset[var_name]
                sample = signal[i]
                time = sample[0]
                value = sample[1]
                if counter > 0 and not (time == prev_time):
                    raise STLOfflineException('The time indices do not agree')
                signal_snapshot.append((var_name, value))
                counter = counter + 1
                prev_time = time
            out = self.update(time, signal_snapshot)

        return out






