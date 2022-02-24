from rtamt.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.pastifier.ltl.pastifier import LtlPastifier

from rtamt.node.ltl.variable import Variable
from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince

from rtamt.exception.stl.exception import STLException
from rtamt.pastifier.stl.horizon import StlHorizon


class STLPastifier(LtlPastifier, StlAstVisitor):

    def __init__(self):
        LtlPastifier.__init__(self)

    def pastify(self, ast):
        h = StlHorizon()
        horizons = dict()
        for spec in ast.specs:
            horizon = h.visit(spec, None)
            horizons[spec] = horizon
        pastified_specs = []
        for spec in ast.specs:
            horizon = horizons[spec]
            pastified_spec = self.visit(spec, [horizon])
            pastified_specs.append(pastified_spec)
        return pastified_specs

    def visit(self, node, *args, **kwargs):
        return StlAstVisitor.visit(self, node, *args, **kwargs)

    def visitVariable(self, node, *args, **kwargs):
        horizon = args[0]
        node = Variable(node.var, node.field, node.io_type)
        if horizon > 0:
            node = TimedOnce(node, horizon, horizon)
        return node

    def visitTimedEventually(self, node, *args, **kwargs):
        horizon = args[0] - node.end
        node = self.visit(node.children[0], [horizon])
        begin = 0
        end = node.end - node.begin
        if end > 0:
            node = TimedOnce(node, begin, end)
        return node

    def visitTimedAlways(self, node, *args, **kwargs):
        horizon = args[0] - node.end
        node = self.visit(node.children[0], [horizon])
        begin = 0
        end = node.end - node.begin
        if end > 0:
            node = TimedHistorically(node, begin, end)
        return node

    def visitTimedUntil(self, node, *args, **kwargs):
        horizon = args[0] - node.end
        begin = node.begin
        end = node.end
        child1_node = self.visit(node.children[0], [horizon])
        child2_node = self.visit(node.children[1], [horizon])
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def visitTimedOnce(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = TimedOnce(child_node, node.begin, node.end)
        return node

    def visitTimedHistorically(self, node, *args, **kwargs):
        child_node = self.visit(node.children[0], *args, **kwargs)
        node = TimedHistorically(child_node, node.begin, node.end)
        return node

    def visitTimedSince(self, node, *args, **kwargs):
        child_node_1 = self.visit(node.children[0], *args, **kwargs)
        child_node_2 = self.visit(node.children[1], *args, **kwargs)
        node = TimedSince(child_node_1, child_node_2, node.begin, node.end)
        return node

    def visitTimedPrecedes(self, node, *args, **kwargs):
        end = node.end
        begin = node.begin
        child1_node = self.visit(node.children[0], *args, **kwargs)
        child2_node = self.visit(node.children[1], *args, **kwargs)
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def visitDefault(self, node):
        raise STLException('STL Pastifier: encountered unexpected type of node.')