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


class STLDenseTimeTransformer(LtlDiscreteTimeTransformer, StlAstVisitor):

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

        b = b * self.ast.U[b_unit] * 1e-9
        e = e * self.ast.U[e_unit] * 1e-9

        return Interval(b, e)