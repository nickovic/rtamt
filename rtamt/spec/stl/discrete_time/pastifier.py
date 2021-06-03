from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLrtamtASTvisitor

from rtamt.spec.ltl.discrete_time.pastifier import LTLPastifier
from rtamt.ast.nodes.variable import Variable

from rtamt.ast.nodes.stl.timed_precedes import TimedPrecedes
from rtamt.ast.nodes.stl.timed_historically import TimedHistorically
from rtamt.ast.nodes.stl.timed_once import TimedOnce
from rtamt.ast.nodes.stl.timed_since import TimedSince

from rtamt.exception.stl.exception import STLException

class STLPastifier(LTLPastifier, STLrtamtASTvisitor):

    def __init__(self):
        pass

    def visit(self, node, *args, **kwargs):
        return STLrtamtASTvisitor.visit(self, node, *args, **kwargs)


    def visitVariable(self, node, *args, **kwargs):
        horizon = args[0]
        node = Variable(node.var, node.field, node.io_type)
        if horizon > 0:
            node = TimedOnce(node, horizon, horizon)
        return node

    def visitTimedEventually(self, node, *args, **kwargs):
        horizon = args[0] - node.end
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        begin = 0
        end = node.end - node.begin
        if end > 0:
            node = TimedOnce(child_node, begin, end)
        else:
            node = child_node
        return node

    def visitTimedAlways(self, node, *args, **kwargs):
        horizon = args[0] - node.end
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        begin = 0
        end = node.end - node.begin
        if end > 0:
            node = TimedHistorically(child_node, begin, end)
        else:
            node = child_node
        return node

    def visitTimedUntil(self, node, *args, **kwargs):
        horizon = args[0] - node.end
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        begin = node.begin
        end = node.end
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def visitTimedOnce(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = TimedOnce(child_node, node.begin, node.end)
        return node

    def visitTimedHistorically(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child_node = children_nodes[0]
        node = TimedHistorically(child_node, node.begin, node.end)
        return node

    def visitTimedSince(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        node = TimedSince(child1_node, child2_node, node.begin, node.end)
        return node

    def visitTimedPrecedes(self, node, *args, **kwargs):
        horizon = args[0]
        children_nodes = self.visitChildren(node, horizon)
        child1_node = children_nodes[0]
        child2_node = children_nodes[1]
        end = node.end
        begin = node.begin
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def visitDefault(self, node):
        raise STLException('STL Pastifier: encountered unexpected type of node.')