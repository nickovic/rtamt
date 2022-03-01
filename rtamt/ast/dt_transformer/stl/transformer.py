from fractions import Fraction

from rtamt.node.stl.timed_until import TimedUntil

from rtamt.node.stl.timed_always import TimedAlways

from rtamt.node.stl.timed_eventually import TimedEventually

from rtamt.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.interval.interval import Interval
from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince

from rtamt.ast.dt_transformer.ltl.transformer import LtlDiscreteTimeTransformer
from rtamt.exception.stl.exception import STLException, STLParseException


class STLDiscreteTimeTransformer(LtlDiscreteTimeTransformer, StlAstVisitor):

    def __init__(self):
        LtlDiscreteTimeTransformer.__init__(self)

    def visit(self, node, *args, **kwargs):
        return StlAstVisitor.visit(self, node, *args, **kwargs)

    def time_unit_transformer(self, node):
        b = node.begin
        e = node.end
        b_unit = node.begin_unit
        e_unit = node.end_unit
        if len(node.begin_unit) == 0:
            if len(node.end_unit) > 0:
                b_unit = node.end_unit
            else:
                b_unit = self.ast.unit
                e_unit = self.ast.unit

        b = b * self.ast.U[b_unit]
        e = e * self.ast.U[e_unit]

        sp = Fraction(self.sampling_period)
        b = b / sp
        e = e / sp

        if b.numerator % b.denominator > 0:
            raise STLException('The STL operator bound must be a multiple of the sampling period')

        if e.numerator % e.denominator > 0:
            raise STLException('The STL operator bound must be a multiple of the sampling period')

        b = int(b)
        e = int(e)

        return Interval(b, e)

    def visitTimedEventually(self, node, *args, **kwargs):
        bound = self.time_unit_transformer(node)
        node = self.visit(node.children[0])
        node = TimedEventually(node, bound)
        return node

    def visitTimedAlways(self, node, *args, **kwargs):
        bound = self.time_unit_transformer(node)
        node = self.visit(node.children[0])
        node = TimedAlways(node, bound)
        return node

    def visitTimedUntil(self, node, *args, **kwargs):
        bound = self.time_unit_transformer(node)
        child_node_1 = self.visit(node.children[0])
        child_node_2 = self.visit(node.children[0])
        node = TimedUntil(child_node_1, child_node_2, bound)
        return node

    def visitTimedOnce(self, node, *args, **kwargs):
        bound = self.time_unit_transformer(node)
        node = self.visit(node.children[0])
        node = TimedOnce(node, bound)
        return node

    def visitTimedHistorically(self, node, *args, **kwargs):
        bound = self.time_unit_transformer(node)
        node = self.visit(node.children[0])
        node = TimedHistorically(node, bound)
        return node

    def visitTimedSince(self, node, *args, **kwargs):
        bound = self.time_unit_transformer(node)
        child_node_1 = self.visit(node.children[0])
        child_node_2 = self.visit(node.children[0])
        node = TimedSince(child_node_1, child_node_2, bound)
        return node

    def visitTimedPrecedes(self, node, *args, **kwargs):
        bound = self.time_unit_transformer(node)
        child_node_1 = self.visit(node.children[0])
        child_node_2 = self.visit(node.children[0])
        node = TimedPrecedes(child_node_1, child_node_2, bound)
        return node

    def visitDefault(self, node):
        raise STLException('STL Pastifier: encountered unexpected type of node.')