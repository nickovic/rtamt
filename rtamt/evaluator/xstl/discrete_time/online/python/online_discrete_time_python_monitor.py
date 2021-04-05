from rtamt.evaluator.stl.discrete_time.online.python.online_discrete_time_python_monitor import \
    STLOnlineDiscreteTimePythonMonitor
from rtamt.operation.xstl.discrete_time.online.backto_bounded_operation import BacktoBoundedOperation
from rtamt.operation.xstl.discrete_time.online.backto_operation import BacktoOperation
from rtamt.spec.xstl.discrete_time.visitor import XSTLVisitor

class XSTLOnlineDiscreteTimePythonMonitor(STLOnlineDiscreteTimePythonMonitor, XSTLVisitor):
    def __init__(self):
        STLOnlineDiscreteTimePythonMonitor.__init__()

    def visitBackto(self, node, args):
        monitor = BacktoOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitTimedBackto(self, node, args):
        monitor = BacktoBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)
