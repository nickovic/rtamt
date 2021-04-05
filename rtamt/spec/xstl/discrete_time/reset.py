from rtamt.spec.stl.discrete_time.reset import STLReset
from rtamt.spec.xstl.discrete_time.visitor import XSTLVisitor

class XSTLReset(STLReset, XSTLVisitor):
    def __init__(self, node_monitor_dict=None):
        STLReset.__init__(self, node_monitor_dict)

    def visit(self, element, args):
        XSTLVisitor.visit(self, element, args)

    def visitBackto(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitTimedBackto(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()
