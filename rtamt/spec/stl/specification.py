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

from rtamt.spec.stl.node_visitor import STLNodeVisitor
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
        self.visitor = STLNodeVisitor(self)
        self.reseter = STLReset()


    # Parses the STL property
    # string can be either file path containint the STL property
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
        self.visitStlfile(ctx)

        # Create the visitor for the actual spec nodes
        self.top = self.visitor.visitStlfile(ctx)

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

    # This is the visitor part. We will populate
    def visitStlSpecification(self, ctx):
        self.visitChildren(ctx)
        # self.top = self.visitor.visitAssertion(ctx.assertion())

    def visitSpecification(self, ctx):
        self.visitChildren(ctx)
        # The specification name is updated only if it is given
        # by the user
        if not ctx.Identifier() is None:
            self.name = ctx.Identifier().getText()

    def visitAssertion(self, ctx):
        self.visitChildren(ctx)

        implicit = False
        if not ctx.Identifier():
            id = 'out'
            id_head = 'out'
            id_tail = ''
            implicit = True
        else:
            id = ctx.Identifier().getText();
            id_tokens = id.split('.')
            id_head = id_tokens[0]
            id_tokens.pop(0)
            id_tail = '.'.join(id_tokens)

        try:
            var = self.var_object_dict[id_head]
            if (not id_tail):
                if (not isinstance(var, (int, float))):
                    raise STLParseException('Variable {} is not of type int or float'.format(id))
            else:
                try:
                    value = operator.attrgetter(id_tail)(var)
                    if (not isinstance(value, (int, float))):
                        raise STLParseException(
                            'The field {0} of the variable {1} is not of type int or float'.format(id, id_head))
                except AttributeError as err:
                    raise STLParseException(err)
        except KeyError:
            if id_tail:
                raise STLParseException('{0} refers to undeclared variable {1} of unknown type'.format(id, id_head))
            else:
                var = float()
                self.var_object_dict[id] = var
                self.add_var(id)
                if not implicit:
                    logging.warning('The variable {} is not explicitely declared. It is implicitely declared as a '
                                'variable of type float'.format(id))

        self.out_var = id_head;
        self.out_var_field = id_tail;
        self.free_vars.discard(id_head)

    def visitVariableDeclaration(self, ctx):
        # fetch the variable name, type and io signature
        var_name = ctx.identifier().getText()
        var_type = ctx.domainType().getText()

        self.declare_var(var_name, var_type)
        self.var_io_dict[var_name] = 'output'

        self.visitChildren(ctx)

    def visitRosTopic(self, ctx):
        var_name = ctx.Identifier(0).getText()
        topic_name = ctx.Identifier(1).getText()
        self.set_var_topic(var_name, topic_name)

    def visitModImport(self, ctx):
        module_name = ctx.Identifier(0).getText()
        var_type = ctx.Identifier(1).getText()
        self.import_module(module_name, var_type)

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
                raise STLParseException ('The type {} does not seem to be imported.'.format(var_type))
        return var

    def import_module(self, from_name, module_name):
        try:
            module = importlib.import_module(from_name)
            self.modules[module_name] = module
        except ImportError:
            raise STLParseException ('The module {} cannot be loaded'.format(from_name))

    def declare_var(self, var_name, var_type):
        if var_name in self.vars:
            logging.warning('Variable {} was already declared. It is now overriden with the new declaration.'.format(var_name))

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






