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
from rtamt.parser.stl.StlParserVisitor import StlParserVisitor
from rtamt.spec.ltl.discrete_time.specification_parser import LTLSpecificationParser
from rtamt.interval.interval import Interval

from rtamt.node.ltl.variable import Variable
from rtamt.node.ltl.predicate import Predicate
from rtamt.node.ltl.previous import Previous
from rtamt.node.ltl.next import Next
from rtamt.node.ltl.neg import Neg
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.implies import Implies
from rtamt.node.ltl.iff import Iff
from rtamt.node.ltl.xor import Xor
from rtamt.node.stl.timed_always import TimedAlways
from rtamt.node.stl.timed_eventually import TimedEventually
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince
from rtamt.node.stl.timed_until import TimedUntil
from rtamt.node.ltl.always import Always
from rtamt.node.ltl.eventually import Eventually
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.historically import Historically
from rtamt.node.ltl.since import Since
from rtamt.node.ltl.until import Until
from rtamt.node.arithmetic.abs import Abs
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.constant import Constant

from rtamt.exception.stl.exception import STLParseException


class STLSpecificationParser(LTLSpecificationParser, StlParserVisitor):
    
    def __init__(self, spec):
        self.ops = set()
        self.spec = spec

        io_type_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_io_type'
        comp_op_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op'
        if self.spec.language == Language.PYTHON:
            io_type_name = 'rtamt.enumerations.io_type'
            comp_op_name = 'rtamt.enumerations.comp_op'

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
        else:
            interval = self.visit(ctx.interval())
            node = TimedAlways(child, interval.begin, interval.end)
        return node


    def visitExprEv(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Eventually(child)
        else:
            interval = self.visit(ctx.interval())
            node = TimedEventually(child, interval.begin, interval.end)
        return node

    def visitExpreOnce(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Once(child)
        else:
            interval = self.visit(ctx.interval())
            node = TimedOnce(child, interval.begin, interval.end)
        return node

    def visitExprHist(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Historically(child)
        else:
            interval = self.visit(ctx.interval())
            node = TimedHistorically(child, interval.begin, interval.end)
        return node

    def visitExprSince(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        if ctx.interval() == None:
            node = Since(child1, child2)
        else:
            interval = self.visit(ctx.interval())
            node = TimedSince(child1, child2, interval.begin, interval.end)
        return node

    def visitExprUntil(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        if ctx.interval() == None:
            node = Until(child1, child2)
        else:
            interval = self.visit(ctx.interval())
            node = TimedUntil(child1, child2, interval.begin, interval.end)
        return node

    def visitExprUnless(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())
        if ctx.interval() == None:
            left = Always(child1)
            right = Until(child1, child2)
            node = Disjunction(left, right)
        else:
            left = TimedAlways(child1, 0, interval.end)
            right = TimedUntil(child1, child2, interval.begin, interval.end)
            node = Disjunction(left, right)
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




