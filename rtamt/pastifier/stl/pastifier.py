from rtamt.ast.visitor.stl.ASTVisitor import STLASTVisitor
from rtamt.pastifier.ltl.pastifier import LTLPastifier

from rtamt.node.ltl.variable import Variable
from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince

from rtamt.exception.stl.exception import STLException

class STLPastifier(LTLPastifier, STLASTVisitor):

    def __init__(self):
        pass 
    
    def visit(self, element, args):
        return STLASTVisitor.visit(self, element, args)


    def postVariable(self, out_children, element, args):
        horizon = args[0]
        node = Variable(element.var, element.field, element.io_type)
        if horizon > 0:
            node = TimedOnce(node, horizon, horizon)
        return node

    def postTimedEventually(self, out_children, element, args):
        horizon = args[0] - element.end
        child_node = out_children[0]
        begin = 0
        end = element.end - element.begin
        if end > 0:
            node = TimedOnce(node, begin, end)
        return node

    def postTimedAlways(self, out_children, element, args):
        horizon = args[0] - element.end
        child_node = out_children[0]
        begin = 0
        end = element.end - element.begin
        if end > 0:
            node = TimedHistorically(node, begin, end)
        return node

    def postTimedUntil(self, out_children, element, args):
        horizon = args[0] - element.end
        begin = element.begin
        end = element.end
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def postTimedOnce(self, out_children, element, args):
        child_node = self.visit(element.children[0], args)
        node = TimedOnce(child_node, element.begin, element.end)
        return node

    def postTimedHistorically(self, out_children, element, args):
        child_node = out_children[0]
        node = TimedHistorically(child_node, element.begin, element.end)
        return node

    def postTmedSince(self, out_children, element, args):
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = TimedSince(child1_node, child2_node, element.begin, element.end)
        return node

    def postTimedPrecedes(self, out_children, element, args):
        end = element.end
        begin = element.begin
        child1_node = out_children[0]
        child2_node = out_children[1]
        node = TimedPrecedes(child1_node, child2_node, begin, end)
        return node

    def postDefault(self, out_children, element):
        raise STLException('STL Pastifier: encountered unexpected type of node.')