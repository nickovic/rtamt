from rtamt.spec.ltl.discrete_time.visitor import LTLVisitor

class LTLReset(LTLVisitor):

    def __init__(self, node_monitor_dict=None):
        self.node_monitor_dict = node_monitor_dict

    def reset(self, node):
        return self.visit(node, [])

    def visitConstant(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitPredicate(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitVariable(self, node, *args, **kwargs):
        pass

    def visitAddition(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitMultiplication(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitSubtraction(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitDivision(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitAbs(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitRise(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitFall(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitNot(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitAnd(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitOr(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitImplies(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitIff(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitXor(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitEventually(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitAlways(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitUntil(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitOnce(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitPrevious(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitNext(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitHistorically(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitSince(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = self.node_monitor_dict[node.name]
        monitor.reset()

    def visitDefault(self, node):
        pass