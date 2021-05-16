from rtamt.evaluator.ltl.offline_monitor import LTLOfflineMonitor
from rtamt.exception.exception import RTAMTException
from rtamt.enumerations.options import TemporalLogic
from rtamt.spec.stl.discrete_time.visitor import STLVisitor

class STLOfflineMonitor(LTLOfflineMonitor, STLVisitor):
    def __init__(self, time_interpretation, language, node):
        LTLMonitor.__init__(self, TemporalLogic.LTL, time_interpretation, language)
        STLVisitor.__init__(self)
        self.generate(node)

    def visitTimedPrecedes(self, node, args):
        monitor = self.module.PrecedesBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitTimedOnce(self, node, args):
        monitor = self.module.OnceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedHistorically(self, node, args):
        monitor = self.module.HistoricallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedSince(self, node, args):
        monitor = self.module.SinceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitTimedAlways(self, node, args):
        monitor = self.module.AlwaysBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedEventually(self, node, args):
        monitor = self.module.EventuallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedUntil(self, node, args):
        monitor = self.module.UntilBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)