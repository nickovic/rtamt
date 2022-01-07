from rtamt.reset.ltl.reset import LTLReset
from rtamt.ast.visitor.stl.ASTVisitor import STLASTVisitor

class STLReset(LTLReset, STLASTVisitor):

    def __init__(self, node_monitor_dict=None):
        LTLReset.__init__(self, node_monitor_dict)

    def visit(self, element, args):
        STLASTVisitor.visit(self, element, args)

    def visitTimedPrecedes(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitTimedUntil(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitTimedAlways(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitTimedEventually(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitTimedSince(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitTimedHistorically(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitTimedOnce(self, element, args):
        self.visit(element.children[0], args)
        monitor = self.node_monitor_dict[element.name]
        monitor.reset()

    def visitDefault(self, element):
        pass