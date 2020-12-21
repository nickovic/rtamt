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
from rtamt.node.arithmetic.abs import Abs
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.constant import Constant

from rtamt.exception.stl.exception import STLParseException


class STLSpecificationParser(StlParserVisitor):
    
    def __init__(self, spec):
        self.ops = set()
        self.spec = spec

        io_type_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_io_type'
        comp_op_name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op'
        if self.spec.language == Language.PYTHON:
            io_type_name = 'rtamt.spec.stl.discrete_time.io_type'
            comp_op_name = 'rtamt.spec.stl.discrete_time.comp_op'

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

        # Identifier is a constant
        if id in self.spec.const_val_dict:
            val = self.spec.const_val_dict[id]
            node = Constant(float(val))
        # Identifier is either an input variable or a sub-formula
        elif id in self.spec.var_subspec_dict:
                node = self.spec.var_subspec_dict[id]
                return node
        else:
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


    def visitVariableDeclaration(self, ctx):
        # fetch the variable name, type and io signature
        var_name = ctx.identifier().getText()
        var_type = ctx.domainType().getText()

        self.spec.declare_var(var_name, var_type)
        self.spec.var_io_dict[var_name] = 'output'

        # If 'var' is input, add to the set of input vars
        # If 'var' is output, add to the set of output vars
        if (not ctx.ioType() is None):
            if (not ctx.ioType().Input() is None):
                var_iotype = 'input'
            elif (not ctx.ioType().Output() is None):
                var_iotype = 'output'
        self.spec.set_var_io_type(var_name, var_iotype)

        self.visitChildren(ctx)

    def visitConstantDeclaration(self, ctx):
        # fetch the variable name, type and io signature
        const_name = ctx.identifier().getText()
        const_type = ctx.domainType().getText()
        const_value = ctx.literal().getText()

        self.spec.declare_const(const_name, const_type, const_value)

        self.spec.visitChildren(ctx)

    def visitRosTopic(self, ctx):
        var_name = ctx.Identifier(0).getText()
        topic_name = ctx.Identifier(1).getText()
        self.spec.set_var_topic(var_name, topic_name)

    def visitModImport(self, ctx):
        module_name = ctx.Identifier(0).getText()
        var_type = ctx.Identifier(1).getText()
        self.spec.import_module(module_name, var_type)

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
        node = TimedAlways(child, interval.begin, interval.end, self.spec.is_pure_python)
        node.horizon = horizon
        return node

    def visitExprUntimedAlwaysExpr(self, ctx):
        child = self.visit(ctx.expression())
        horizon = child.horizon
        node = Always(child, self.spec.is_pure_python)
        node.horizon = horizon
        return node

    def visitExprEvExpr(self, ctx):
        child = self.visit(ctx.expression())
        interval = self.visit(ctx.interval())
        horizon = child.horizon + interval.end
        node = TimedEventually(child, interval.begin, interval.end, self.spec.is_pure_python)
        node.horizon = horizon
        return node

    def visitExprUntimedEvExpr(self, ctx):
        child = self.visit(ctx.expression())
        horizon = child.horizon
        node = Eventually(child, self.spec.is_pure_python)
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
            node = Once(child, self.spec.is_pure_python)
        else:
            interval = self.visit(ctx.interval())
            node = TimedOnce(child, interval.begin, interval.end, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprHistExpr(self, ctx):
        child = self.visit(ctx.expression())
        if ctx.interval() == None:
            node = Historically(child, self.spec.is_pure_python)
        else:
            interval = self.visit(ctx.interval())
            node = TimedHistorically(child, interval.begin, interval.end, self.spec.is_pure_python)
        node.horizon = child.horizon
        return node

    def visitExprSinceExpr(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        if ctx.interval() == None:
            node = Since(child1, child2, self.spec.is_pure_python)
        else:
            interval = self.visit(ctx.interval())
            node = TimedSince(child1, child2, interval.begin, interval.end, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon)
        return node

    def visitExprUntilExpr(self, ctx):
        # Parse children
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())

        node = TimedUntil(child1, child2, interval.begin, interval.end, self.spec.is_pure_python)
        node.horizon = max(child1.horizon, child2.horizon) + interval.end
        return node

    def visitExprUnless(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        interval = self.visit(ctx.interval())

        left = TimedAlways(child1, 0, interval.end, self.spec.is_pure_python)
        right = TimedUntil(child1, child2, interval.begin, interval.end, self.spec.is_pure_python)
        node = Disjunction(left, right)

        node.horizon = max(child1.horizon, child2.horizon) + interval.end
        return node

    def visitExprParen(self, ctx):
        return self.visit(ctx.expression())

    def visitExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitAssertion(self, ctx):
        out = self.visit(ctx.topExpression())

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
                if not implicit:
                    logging.warning('The variable {} is not explicitly declared. It is implicitly declared as a '
                                    'variable of type float'.format(id))

        self.spec.out_var = id_head;
        self.spec.out_var_field = id_tail;
        self.spec.free_vars.discard(id_head)
        return out

    def visitStlfile(self, ctx):
        return self.visit(ctx.stlSpecification())

    def visitStlSpecification(self, ctx):
        return self.visitChildren(ctx)
        # return self.visit(ctx.assertion())

    def visitSpecification(self, ctx):
        self.visitChildren(ctx)
        # The specification name is updated only if it is given
        # by the user
        if not ctx.Identifier() is None:
            self.spec.name = ctx.Identifier().getText()

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




