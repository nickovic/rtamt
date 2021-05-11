# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:38:29 2019

@author: NickovicD
"""
import logging
import operator

from decimal import Decimal
from fractions import Fraction

from rtamt import Language
from rtamt.antrl_parser.stl.StlParserVisitor import StlParserVisitor
from rtamt.ast.parser_visitor.ltl.rtamtASTparser import LTLrtamtASTparser
from rtamt.interval.interval import Interval

from rtamt.ast.nodes.variable import Variable
from rtamt.ast.nodes.constant import Constant

from rtamt.ast.nodes.arithmetic.abs import Abs
from rtamt.ast.nodes.arithmetic.addition import Addition
from rtamt.ast.nodes.arithmetic.subtraction import Subtraction
from rtamt.ast.nodes.arithmetic.multiplication import Multiplication
from rtamt.ast.nodes.arithmetic.division import Division

from rtamt.ast.nodes.ltl.predicate import Predicate
from rtamt.ast.nodes.ltl.previous import Previous
from rtamt.ast.nodes.ltl.next import Next
from rtamt.ast.nodes.ltl.neg import Neg
from rtamt.ast.nodes.ltl.conjunction import Conjunction
from rtamt.ast.nodes.ltl.disjunction import Disjunction
from rtamt.ast.nodes.ltl.implies import Implies
from rtamt.ast.nodes.ltl.iff import Iff
from rtamt.ast.nodes.ltl.xor import Xor

from rtamt.ast.nodes.ltl.always import Always
from rtamt.ast.nodes.ltl.eventually import Eventually
from rtamt.ast.nodes.ltl.once import Once
from rtamt.ast.nodes.ltl.historically import Historically
from rtamt.ast.nodes.ltl.since import Since
from rtamt.ast.nodes.ltl.until import Until
from rtamt.ast.nodes.ltl.fall import Fall
from rtamt.ast.nodes.ltl.rise import Rise

from rtamt.ast.nodes.stl.timed_always import TimedAlways
from rtamt.ast.nodes.stl.timed_eventually import TimedEventually
from rtamt.ast.nodes.stl.timed_historically import TimedHistorically
from rtamt.ast.nodes.stl.timed_once import TimedOnce
from rtamt.ast.nodes.stl.timed_since import TimedSince
from rtamt.ast.nodes.stl.timed_until import TimedUntil


from rtamt.exception.stl.exception import STLParseException


class STLrtamtASTparser(LTLrtamtASTparser, StlParserVisitor):

    def __init__(self, spec):
        self.ops = set()
        self.spec = spec

        io_type_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_io_type'
        comp_op_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op'
        if self.spec.language == Language.PYTHON:
            io_type_name = 'rtamt.ast.parser_visitor.io_type'
            comp_op_name = 'rtamt.ast.parser_visitor.comp_op'

        self.io_type_mod = __import__(io_type_name, fromlist=[''])
        self.comp_op_mod = __import__(comp_op_name, fromlist=[''])

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, spec):
        self.__spec = spec

    @property
    def ops(self):
        return self.__ops
    
    @ops.setter
    def ops(self, ops):
        self.__ops = ops


    def visitExprAlways(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Always(child)
            horizon = child.horizon
        else:
            interval = self.visit(ctx.interval())
            node = TimedAlways(child, interval.begin, interval.end)
            horizon = child.horizon + interval.end
        node.horizon = horizon
        return node


    def visitExprEv(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Eventually(child)
            horizon = child.horizon
        else:
            interval = self.visit(ctx.interval())
            node = TimedEventually(child, interval.begin, interval.end)
            horizon = child.horizon + interval.end
        node.horizon = horizon
        return node

    def visitExpreOnce(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Once(child)
        else:
            interval = self.visit(ctx.interval())
            node = TimedOnce(child, interval.begin, interval.end)
        node.horizon = child.horizon
        return node

    def visitExprHist(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Historically(child)
        else:
            interval = self.visit(ctx.interval())
            node = TimedHistorically(child, interval.begin, interval.end)
        node.horizon = child.horizon
        return node

    def visitExprSince(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        if ctx.interval() == None:
            node = Since(child1, child2)
        else:
            interval = self.visit(ctx.interval())
            node = TimedSince(child1, child2, interval.begin, interval.end)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprUntil(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        if ctx.interval() == None:
            node = Until(child1, child2)
            node.horizon = max(child1.horizon, child2.horizon)
        else:
            interval = self.visit(ctx.interval())
            node = TimedUntil(child1, child2, interval.begin, interval.end)
            node.horizon = max(child1.horizon, child2.horizon) + interval.end
        return node

    def visitExprUnless(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        if ctx.interval() == None:
            left = Always(child1)
            right = Until(child1, child2)
            node = Disjunction(left, right)
            node.horizon = max(child1.horizon, child2.horizon)
        else:
            interval = self.visit(ctx.interval())
            left = TimedAlways(child1, 0, interval.end)
            right = TimedUntil(child1, child2, interval.begin, interval.end)
            node = Disjunction(left, right)
            node.horizon = max(child1.horizon, child2.horizon) + interval.end
        return node


    def visitIntervalTimeLiteral(self, ctx):
        text = ctx.literal().getText()
        out = Fraction(Decimal(text))

        if ctx.unit() == None:
            # default time unit is seconds - conversion of the bound to ps
            unit = self.spec.unit
        else:
            unit = ctx.unit().getText()

        out = out * self.spec.U[unit]

        sp = Fraction(self.spec.get_sampling_period())

        out = out / sp

        if out.numerator % out.denominator > 0:
            raise STLParseException('The STL operator bound must be a multiple of the sampling period')

        out = int(out / self.spec.sampling_period)

        return out

    def visitConstantTimeLiteral(self, ctx):
        const_name = ctx.Identifier().getText()

        if const_name not in self.spec.const_val_dict:
            raise STLParseException('Bound {} not declared'.format(const_name))

        val = self.spec.const_val_dict[const_name]

        out = Fraction(Decimal(val))

        if ctx.unit() == None:
            # default time unit is seconds - conversion of the bound to ps
            unit = self.spec.unit
        else:
            unit = ctx.unit().getText()

        out = out * self.spec.U[unit]

        sp = Fraction(self.spec.get_sampling_period())

        out = out / sp

        if out.numerator % out.denominator > 0:
            raise STLParseException('The STL operator bound must be a multiple of the sampling period')

        out = int(out / self.spec.sampling_period)

        return out

    def visitIntervalFloatTimeLiteral(self, ctx):
        text = ctx.literal().getText()
        out = Fraction(Decimal(text))

        if ctx.unit() == None:
            # default time unit is seconds - conversion of the bound to ps
            unit = self.spec.unit
        else:
            unit = ctx.unit().getText()

        out = out * self.spec.U[unit]

        sp = Fraction(self.spec.get_sampling_period())

        out = out / sp

        if out.numerator % out.denominator > 0:
            raise STLParseException('The STL operator bound must be a multiple of the sampling period')

        out = int(out / self.spec.sampling_period)

        return out

    def visitInterval(self, ctx):
        begin = self.visit(ctx.intervalTime(0))
        end = self.visit(ctx.intervalTime(1))
        interval = Interval(begin, end)
        return interval

    def str_to_op_type(self, input):
        if input == "<":
            return self.comp_op_mod.StlComparisonOperator.LESS
        elif input == '<=':
            return self.comp_op_mod.StlComparisonOperator.LEQ
        elif input == ">=":
            return self.comp_op_mod.StlComparisonOperator.GEQ
        elif input == ">":
            return self.comp_op_mod.StlComparisonOperator.GREATER
        elif input == "==":
            return self.comp_op_mod.StlComparisonOperator.EQUAL
        else:
            return self.comp_op_mod.StlComparisonOperator.NEQ




