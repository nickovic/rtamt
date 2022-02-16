from decimal import Decimal
from fractions import Fraction

from rtamt.parser.stl.StlParserVisitor import StlParserVisitor
from rtamt.ast.parser.ltl.parser_visitor import LtlAstParserVisitor
from rtamt.interval.interval import Interval

from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.always import Always
from rtamt.node.ltl.eventually import Eventually
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.historically import Historically
from rtamt.node.ltl.since import Since
from rtamt.node.ltl.until import Until
from rtamt.node.stl.timed_always import TimedAlways
from rtamt.node.stl.timed_eventually import TimedEventually
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince
from rtamt.node.stl.timed_until import TimedUntil
from rtamt.exception.stl.exception import STLParseException


class StlAstParserVisitor(LtlAstParserVisitor, StlParserVisitor):

    def __init__(self):

        LtlAstParserVisitor.__init__(self)
        StlParserVisitor.__init__(self)

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

    def visitConstantTimeLiteral(self, ctx):
        const_name = ctx.Identifier().getText()

        if const_name not in self.const_val_dict:
            raise STLParseException('Bound {} not declared'.format(const_name))

        val = self.const_val_dict[const_name]

        out = Fraction(Decimal(val))

        if ctx.unit() == None:
            # default time unit is seconds - conversion of the bound to ps
            unit = self.unit
        else:
            unit = ctx.unit().getText()

        out = out * self.U[unit]

        sp = Fraction(self.get_sampling_period())

        out = out / sp

        if out.numerator % out.denominator > 0:
            raise STLParseException('The STL operator bound must be a multiple of the sampling period')

        out = int(out / self.sampling_period)

        return out

    def visitInterval(self, ctx):
        begin = self.visit(ctx.intervalTime(0))
        end = self.visit(ctx.intervalTime(1))
        interval = Interval(begin, end)
        return interval

    def get_sampling_period(self):
        return self.sampling_period * self.U[self.sampling_period_unit]

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        self.__unit = unit
