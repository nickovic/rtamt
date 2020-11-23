# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:38:29 2019

@author: NickovicD
"""
import logging
import operator

from decimal import Decimal
from fractions import Fraction

from rtamt.parser.stl.StlParserVisitor import StlParserVisitor
from rtamt.interval.interval import Interval

from rtamt.node.stl.variable import Variable
from rtamt.node.stl.predicate import Predicate
from rtamt.node.stl.previous import Previous
from rtamt.node.stl.next import Next
from rtamt.node.stl.neg import Neg
from rtamt.node.stl.conjunction import Conjunction
from rtamt.node.stl.disjunction import Disjunction
from rtamt.node.stl.implies import Implies
from rtamt.node.stl.iff import Iff
from rtamt.node.stl.xor import Xor
from rtamt.node.stl.always import Always
from rtamt.node.stl.eventually import Eventually
from rtamt.node.stl.once import Once
from rtamt.node.stl.historically import Historically
from rtamt.node.stl.until import Until
from rtamt.node.stl.since import Since
from rtamt.node.stl.abs import Abs
from rtamt.node.stl.addition import Addition
from rtamt.node.stl.subtraction import Subtraction
from rtamt.node.stl.multiplication import Multiplication
from rtamt.node.stl.division import Division
from rtamt.node.stl.fall import Fall
from rtamt.node.stl.rise import Rise
from rtamt.node.stl.constant import Constant

from rtamt.exception.stl.exception import STLParseException


class STLNodeVisitor(StlParserVisitor):
    
    def __init__(self, spec):
        self.ops = set()
        self.spec = spec

        io_type_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_io_type'
        comp_op_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op'
        if self.spec.is_pure_python:
            io_type_name = 'rtamt.spec.stl.io_type'
            comp_op_name = 'rtamt.spec.stl.comp_op'

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

    def visitIdCompInt(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        op_type = self.str_to_op_type(ctx.comparisonOp().getText())
        node = Predicate(child1, child2, op_type, self.spec.is_pure_python)

        node.horizon = int(0)
        return node

    def visitExprId(self, ctx):
        id = ctx.Identifier().getText();
        id_tokens = id.split('.')
        id_head = id_tokens[0]
        id_tokens.pop(0)
        id_tail = '.'.join(id_tokens)

        try:
            var = self.spec.var_object_dict[id_head]
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
                self.spec.var_object_dict[id] = var
                self.spec.add_var(id)
                logging.warning('The variable {} is not explicitely declared. It is implicitely declared as a '
                                'variable of type float'.format(id))

        var_io = self.spec.var_io_dict[id_head]
        node = Variable(id_head, id_tail, var_io)
        node.horizon = int(0)

        return node

    def visitExprAddition(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Addition(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprSubtraction(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Subtraction(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprMultiplication(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Multiplication(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprDivision(self, ctx):
        child1 = self.visit(ctx.real_expression(0))
        child2 = self.visit(ctx.real_expression(1))
        node = Division(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprAbs(self, ctx):
        child = self.visit(ctx.real_expression())
        node = Abs(child, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprNot(self, ctx):
        child = self.visit(ctx.expression())
        node = Neg(child, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprRise(self, ctx):
        child = self.visit(ctx.expression())
        node = Rise(child, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprLiteral(self, ctx):
        val = float(ctx.literal().getText())
        node = Constant(val, self.spec.is_pure_python)
        node.horizon = 0
        return node

    def visitExprFall(self, ctx):
        child = self.visit(ctx.expression())
        node = Fall(child, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprAndExpr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Conjunction(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprOrExpr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Disjunction(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprImpliesExpr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Implies(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprIffExpr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Iff(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprXorExpr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = Xor(child1, child2, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprAlwaysExpr(self, ctx):
        child = self.visit(ctx.expression())
        interval = self.visit(ctx.interval())
        horizon = child.horizon + interval.end
        node = Always(child, interval, self.spec.is_pure_python)
        node.horizon = horizon
        return node

    def visitExprUntimedAlwaysExpr(self, ctx):
        child = self.visit(ctx.expression())
        horizon = child.horizon
        interval = None
        node = Always(child, interval, self.spec.is_pure_python)
        node.horizon = horizon
        return node

    def visitExprEvExpr(self, ctx):
        child = self.visit(ctx.expression())
        interval = self.visit(ctx.interval())
        horizon = child.horizon + interval.end
        node = Eventually(child, interval, self.spec.is_pure_python)
        node.horizon = horizon
        return node

    def visitExprUntimedEvExpr(self, ctx):
        child = self.visit(ctx.expression())
        horizon = child.horizon
        interval = None
        node = Eventually(child, interval, self.spec.is_pure_python)
        node.horizon = horizon
        return node

    def visitExprPrevious(self, ctx):
        child = self.visit(ctx.expression())
        node = Previous(child, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprNext(self, ctx):
        child = self.visit(ctx.expression())
        node = Next(child, self.spec.is_pure_python)
        node.horizon = child.horizon + 1
        return node

    def visitExpreOnceExpr(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            interval = None

        else:
            interval = self.visit(ctx.interval())
        node = Once(child, interval, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprHistExpr(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            interval = None

        else:
            interval = self.visit(ctx.interval())
        node = Historically(child, interval, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprSinceExpr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        if ctx.interval() == None:
            interval = None

        else:
            interval = self.visit(ctx.interval())
        node = Since(child1, child2, interval, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprUntilExpr(self, ctx):
        # Parse children
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())

        node = Until(child1, child2, interval, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon) + interval.end
        return node

    def visitExprUnless(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())

        left_interval = Interval(0, interval.end)

        left = Always(child1, left_interval, self.spec.is_pure_python)
        right = Until(child1, child2, interval, self.spec.is_pure_python)
        node = Disjunction(left, right)

        node.horizon = max(child1.horizon, child2.horizon) + interval.end
        return node

    def visitExprParen(self, ctx):
        return self.visit(ctx.expression())

    def visitExpr(self, ctx):
        return self.visit(ctx.expression())
	
    def visitAssertion(self, ctx):
        return self.visit(ctx.topExpression())

    def visitStlfile(self, ctx):
        return self.visit(ctx.stlSpecification())

    def visitStlSpecification(self, ctx):
        return self.visit(ctx.assertion())

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


