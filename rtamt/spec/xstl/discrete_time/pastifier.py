from rtamt.node.xstl.backto import Backto
from rtamt.node.xstl.timed_backto import TimedBackto
from rtamt.spec.stl.discrete_time.pastifier import STLPastifier
from rtamt.exception.stl.exception import STLException
from rtamt.spec.xstl.discrete_time.visitor import XSTLVisitor


class XSTLPastifier(STLPastifier, XSTLVisitor):

    def __init__(self):
        STLPastifier.__init__()
    
    def visit(self, element, args):
        return XSTLVisitor.visit(self, element, args)

    def visitTimedBackto(self, element, args):
        child_node_1 = self.visit(element.children[0], args)
        child_node_2 = self.visit(element.children[1], args)
        node = TimedBackto(child_node_1, child_node_2, element.begin, element.end)
        return node

    def visitBackto(self, element, args):
        child_node_1 = self.visit(element.children[0], args)
        child_node_2 = self.visit(element.children[1], args)
        node = Backto(child_node_1, child_node_2, element.begin, element.end)
        return node

    def visitDefault(self, element):
        raise STLException('XSTL Pastifier: encountered unexpected type of node.')