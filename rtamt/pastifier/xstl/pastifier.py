from rtamt.pastifier.xstl.horizon import XStlHorizon
from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.semantics.interval.interval import Interval
from rtamt.pastifier.ltl.pastifier import LtlPastifier

from rtamt.syntax.node.ltl.variable import Variable
from rtamt.syntax.node.stl.timed_precedes import TimedPrecedes
from rtamt.syntax.node.stl.timed_historically import TimedHistorically
from rtamt.syntax.node.stl.timed_once import TimedOnce
from rtamt.syntax.node.stl.timed_since import TimedSince

from rtamt.exception.stl.exception import STLException
from rtamt.pastifier.stl.horizon import StlHorizon


class XStlPastifier(StlPastifier, XStlAstVisitor):

    def __init__(self):
        StlPastifier.__init__(self)

    def pastify(self, ast):
        h = XStlHorizon()
        horizons = dict()
        for spec in ast.specs:
            horizon = h.visit(spec, None)
            horizons[spec] = horizon
        pastified_specs = []
        for spec in ast.specs:
            horizon = horizons[spec]
            pastified_spec = self.visit(spec, horizon)
            pastified_specs.append(pastified_spec)
        ast.specs = pastified_specs
        return ast

    def visit(self, node, *args, **kwargs):
        return XStlAstVisitor.visit(self, node, *args, **kwargs)

    def visitShift(self, node, *args, **kwargs):
        horizon = args[0]
        if node.val >= 0:
            horizon = args[0] - node.val
        return node

    def visitDefault(self, node):
        raise STLException('STL Pastifier: encountered unexpected type of node.')