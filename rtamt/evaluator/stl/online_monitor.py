from rtamt.evaluator.ltl.online_monitor import LTLOnlineMonitor
from rtamt.exception.exception import RTAMTException
from rtamt.enumerations.options import TemporalLogic
from rtamt.spec.stl.discrete_time.visitor import STLVisitor

class STLOnlineMonitor(LTLOnlineMonitor, STLVisitor):
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
        raise RTAMTException('Bounded always operator not implemented in online monitor.')

    def visitTimedEventually(self, node, args):
        raise RTAMTException('Bounded eventually operator not implemented in online monitor.')

    def visitTimedUntil(self, node, args):
        raise RTAMTException('Bounded until operator not implemented in online monitor.')