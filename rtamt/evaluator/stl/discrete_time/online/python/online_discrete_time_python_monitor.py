from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLrtamtASTvisitor
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

class STLOnlineDiscreteTimePythonMonitor(STLrtamtASTvisitor):
    def __init__(self):
        self.node_monitor_dict = dict()

    def generate(self, node):
        self.visit(node, [])
        return self.node_monitor_dict

    def visitPredicate(self, node, pre_out, *args, **kwargs):
        monitor = PredicateOperation(node.operator)
        self.node_monitor_dict[node.name] = monitor

    def visitVariable(self, node, pre_out, *args, **kwargs):
        pass

    def visitAbs(self, node, pre_out, *args, **kwargs):
        monitor = AbsOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitAddition(self, node, pre_out, *args, **kwargs):
        monitor = AdditionOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitSubtraction(self, node, pre_out, *args, **kwargs):
        monitor = SubtractionOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitMultiplication(self, node, pre_out, *args, **kwargs):
        monitor = MultiplicationOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitDivision(self, node, pre_out, *args, **kwargs):
        monitor = DivisionOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitNot(self, node, pre_out, *args, **kwargs):
        monitor = NotOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitAnd(self, node, pre_out, *args, **kwargs):
        monitor = AndOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitOr(self, node, pre_out, *args, **kwargs):
        monitor = OrOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitImplies(self, node, pre_out, *args, **kwargs):
        monitor = ImpliesOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitIff(self, node, pre_out, *args, **kwargs):
        monitor = IffOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitXor(self, node, pre_out, *args, **kwargs):
        monitor = XorOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitEventually(self, node, pre_out, *args, **kwargs):
        raise LTLNotImplementedException('Eventually operator is not implemented in the STL online monitor.')

    def visitAlways(self, node, pre_out, *args, **kwargs):
        raise LTLNotImplementedException('Always operator is not implemented in the STL online monitor.')

    def visitUntil(self, node, pre_out, *args, **kwargs):
        raise LTLNotImplementedException('Until operator is not implemented in the STL online monitor.')

    def visitOnce(self, node, pre_out, *args, **kwargs):
        monitor = OnceOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitHistorically(self, node, pre_out, *args, **kwargs):
        monitor = HistoricallyOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitSince(self, node, pre_out, *args, **kwargs):
        monitor = SinceOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitRise(self, node, pre_out, *args, **kwargs):
        monitor = RiseOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitFall(self, node, pre_out, *args, **kwargs):
        monitor = FallOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitConstant(self, node, pre_out, *args, **kwargs):
        monitor = ConstantOperation(node.val)
        self.node_monitor_dict[node.name] = monitor

    def visitPrevious(self, node, pre_out, *args, **kwargs):
        monitor = PreviousOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitNext(self, node, pre_out, *args, **kwargs):
        raise LTLNotImplementedException('Next operator not implemented in STL online monitor.')

    def visitTimedPrecedes(self, node, pre_out, *args, **kwargs):
        monitor = PrecedesBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedOnce(self, node, pre_out, *args, **kwargs):
        monitor = OnceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedHistorically(self, node, pre_out, *args, **kwargs):
        monitor = HistoricallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedSince(self, node, pre_out, *args, **kwargs):
        monitor = SinceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedAlways(self, node, pre_out, *args, **kwargs):
        raise STLNotImplementedException('Bounded always operator not implemented in STL online monitor.')

    def visitTimedEventually(self, node, pre_out, *args, **kwargs):
        raise STLNotImplementedException('Bounded eventually operator not implemented in STL online monitor.')

    def visitTimedUntil(self, node, pre_out, *args, **kwargs):
        raise STLNotImplementedException('Bounded until operator not implemented in STL online monitor.')

    def visitDefault(self, node, pre_out, *args, **kwargs):
        pass
