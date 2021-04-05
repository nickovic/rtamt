from rtamt.evaluator.stl.discrete_time.online.python.online_discrete_time_python_monitor import \
    STLOnlineDiscreteTimePythonMonitor
from rtamt.spec.stl.discrete_time.visitor import STLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.exception.ltl.exception import LTLNotImplementedException
from rtamt.operation.stl.discrete_time.online.predicate_operation import PredicateOperation
from rtamt.operation.arithmetic.discrete_time.online.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.discrete_time.online.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.discrete_time.online.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.discrete_time.online.division_operation import DivisionOperation
from rtamt.operation.stl.discrete_time.online.and_operation import AndOperation
from rtamt.operation.stl.discrete_time.online.or_operation import OrOperation
from rtamt.operation.stl.discrete_time.online.implies_operation import ImpliesOperation
from rtamt.operation.stl.discrete_time.online.iff_operation import IffOperation
from rtamt.operation.stl.discrete_time.online.xor_operation import XorOperation
from rtamt.operation.stl.discrete_time.online.since_operation import SinceOperation
from rtamt.operation.arithmetic.discrete_time.online.abs_operation import AbsOperation
from rtamt.operation.stl.discrete_time.online.not_operation import NotOperation
from rtamt.operation.stl.discrete_time.online.rise_operation import RiseOperation
from rtamt.operation.stl.discrete_time.online.fall_operation import FallOperation
from rtamt.operation.stl.discrete_time.online.once_operation import OnceOperation
from rtamt.operation.stl.discrete_time.online.historically_operation import HistoricallyOperation
from rtamt.operation.stl.discrete_time.online.always_operation import AlwaysOperation
from rtamt.operation.stl.discrete_time.online.eventually_operation import EventuallyOperation
from rtamt.operation.stl.discrete_time.online.previous_operation import PreviousOperation
from rtamt.operation.stl.discrete_time.online.constant_operation import ConstantOperation
from rtamt.operation.stl.discrete_time.online.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.discrete_time.online.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.discrete_time.online.since_bounded_operation import SinceBoundedOperation
from rtamt.operation.stl.discrete_time.online.precedes_bounded_operation import PrecedesBoundedOperation
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
        monitor = TimedBacktoOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)
