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


    def visitVariable(self, node, pre_out, *args, **kwargs):
        horizon = args[0]
        node = Variable(node.var, node.field, node.io_type)
        if horizon > 0:
            node = TimedOnce(node, horizon, horizon)
        return node

    def visitTimedEventually(self, node, pre_out, *args, **kwargs):
        horizon = args[0] - node.end
        node = self.visit(node.children[0], [horizon])
        begin = 0
        end = node.end - node.begin
        if end > 0:
            node = TimedOnce(node, begin, end)
        return node

    def visitTimedAlways(self, node, pre_out, *args, **kwargs):
        horizon = args[0] - node.end
        node = self.visit(node.children[0], [horizon])
        begin = 0
        end = node.end - node.begin
        if end > 0:
            node = TimedHistorically(node, begin, end)
        return node

    def visitTimedUntil(self, node, pre_out, *args, **kwargs):
        horizon = args[0] - node.end
        begin = node.begin
        end = node.end
        child1_node = self.visit(node.children[0], [horizon])
        child2_node = self.visit(node.children[1], [horizon])
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def visitTimedOnce(self, node, pre_out, *args, **kwargs):
        child_node = self.visit(node.children[0], args)
        node = TimedOnce(child_node, node.begin, node.end)
        return node

    def visitTimedHistorically(self, node, pre_out, *args, **kwargs):
        child_node = self.visit(node.children[0], args)
        node = TimedHistorically(child_node, node.begin, node.end)
        return node

    def visitTimedSince(self, node, pre_out, *args, **kwargs):
        child_node_1 = self.visit(node.children[0], args)
        child_node_2 = self.visit(node.children[1], args)
        node = TimedSince(child_node_1, child_node_2, node.begin, node.end)
        return node

    def visitTimedPrecedes(self, node, pre_out, *args, **kwargs):
        end = node.end
        begin = node.begin
        child1_node = self.visit(node.children[0], args)
        child2_node = self.visit(node.children[1], args)
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def visitDefault(self, node):
        raise STLException('STL Pastifier: encountered unexpected type of node.')