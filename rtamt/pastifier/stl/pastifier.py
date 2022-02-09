from rtamt.ast.visitor.stl.ASTVisitor import STLASTVisitor
from rtamt.pastifier.ltl.pastifier import LTLPastifier

from rtamt.node.ltl.variable import Variable
from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince

from rtamt.exception.stl.exception import STLException
from rtamt.pastifier.stl.horizon import STLHorizon


class STLPastifier(LTLPastifier, STLASTVisitor):

    def __init__(self):
        LTLPastifier.__init__(self)

    def visit(self, element, args):
        return STLASTVisitor.visit(self, element, args)

    def pastify(self, element):
        h = STLHorizon()
        horizon = h.visit(element, None)
        return self.visit(element, [horizon])

    def visitVariable(self, element, args):
        horizon = args[0]
        node = Variable(element.var, element.field, element.io_type)
        if horizon > 0:
            node = TimedOnce(node, horizon, horizon)
        return node

    def visitTimedEventually(self, element, args):
        horizon = args[0] - element.end
        node = self.visit(element.children[0], [horizon])
        begin = 0
        end = element.end - element.begin
        if end > 0:
            node = TimedOnce(node, begin, end)
        return node

    def visitTimedAlways(self, element, args):
        horizon = args[0] - element.end
        node = self.visit(element.children[0], [horizon])
        begin = 0
        end = element.end - element.begin
        if end > 0:
            node = TimedHistorically(node, begin, end)
        return node

    def visitTimedUntil(self, element, args):
        horizon = args[0] - element.end
        begin = element.begin
        end = element.end
        child1_node = self.visit(element.children[0], [horizon])
        child2_node = self.visit(element.children[1], [horizon])
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def visitTimedOnce(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = TimedOnce(child_node, element.begin, element.end)
        return node

    def visitTimedHistorically(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = TimedHistorically(child_node, element.begin, element.end)
        return node

    def visitTimedSince(self, element, args):
        child_node_1 = self.visit(element.children[0], args)
        child_node_2 = self.visit(element.children[1], args)
        node = TimedSince(child_node_1, child_node_2, element.begin, element.end)
        return node

    def visitTimedPrecedes(self, element, args):
        end = element.end
        begin = element.begin
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def visitDefault(self, element):
        raise STLException('STL Pastifier: encountered unexpected type of node.')