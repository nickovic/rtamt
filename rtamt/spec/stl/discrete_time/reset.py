from rtamt.spec.ltl.discrete_time.reset import LTLReset
from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLrtamtASTvisitor

class STLReset(LTLReset, STLrtamtASTvisitor):

    def __init__(self, node_monitor_dict=None):
        LTLReset.__init__(self, node_monitor_dict)

    def visit(self, node, *args, **kwargs):
        STLrtamtASTvisitor.visit(self, node, *args, **kwargs)

    def visitTimedPrecedes(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitTimedUntil(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitTimedAlways(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitTimedEventually(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitTimedSince(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitTimedHistorically(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitTimedOnce(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitDefault(self, node):
        pass