from rtamt.spec.stl.discrete_time.visitor import STLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException, \
    STLParseException
from rtamt.spec.stl.discrete_time.comp_op import StlComparisonOperator as CompOp
from rtamt.lib.rtamt_stl_library_wrapper.stl_comp_op import StlComparisonOperator
from rtamt.lib.rtamt_stl_library_wrapper.stl_combinatorial_binary_node import CombinatorialBinaryOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_not_node import NotOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_addition_node import AdditionOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_predicate_node import PredicateOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_multiplication_node import MultiplicationOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_subtraction_node import SubtractionOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_division_node import DivisionOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_and_node import AndOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_or_node import OrOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_implies_node import ImpliesOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_iff_node import IffOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_xor_node import XorOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_since_node import SinceOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_abs_node import AbsOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_rise_node import RiseOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_fall_node import FallOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_node import OnceOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_node import HistoricallyOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_always_node import AlwaysOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_eventually_node import EventuallyOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_previous_node import PreviousOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_constant_node import ConstantOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_bounded_node import OnceBoundedOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_bounded_node import HistoricallyBoundedOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_since_bounded_node import SinceBoundedOperation
from rtamt.lib.rtamt_stl_library_wrapper.stl_precedes_bounded_node import PrecedesBoundedOperation


class STLOnlineDiscreteTimeCPPMonitor(STLVisitor):

    def __init__(self):
        self.node_monitor_dict = dict()

    def generate(self, node):
        self.visit(node)
        return self.node_monitor_dict

    def visitPredicate(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = PredicateOperation(node.operator)
        self.node_monitor_dict[node.name] = monitor

    def visitVariable(self, node, *args, **kwargs):
        pass

    def visitAbs(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = AbsOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitAddition(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = AdditionOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitSubtraction(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = SubtractionOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitMultiplication(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = MultiplicationOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitDivision(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = DivisionOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitNot(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = NotOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitAnd(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = AndOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitOr(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = OrOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitImplies(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = ImpliesOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitIff(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = IffOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitXor(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = XorOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitEventually(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = EventuallyOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitAlways(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = AlwaysOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitUntil(self, node, *args, **kwargs):
        raise STLNotImplementedException('Until operator is not implemented in the STL online monitor.')

    def visitOnce(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = OnceOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitHistorically(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = HistoricallyOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitSince(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = SinceOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitRise(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = RiseOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitFall(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = FallOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitConstant(self, node, *args, **kwargs):
        monitor = ConstantOperation(node.val)
        self.node_monitor_dict[node.name] = monitor

    def visitPrevious(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = PreviousOperation()
        self.node_monitor_dict[node.name] = monitor

    def visitNext(self, node, *args, **kwargs):
        raise STLNotImplementedException('Next operator not implemented in STL online monitor.')

    def visitTimedPrecedes(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = PrecedesBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedOnce(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = OnceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedHistorically(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = HistoricallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedSince(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = SinceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedAlways(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded always operator not implemented in STL online monitor.')

    def visitTimedEventually(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded eventually operator not implemented in STL online monitor.')

    def visitTimedUntil(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded until operator not implemented in STL online monitor.')

    def visitDefault(self, node, *args, **kwargs):
        pass

    def op_cpp(self, op):
        if op == CompOp.GEQ:
            return StlComparisonOperator.GEQ
        elif op == CompOp.GREATER:
            return StlComparisonOperator.GREATER
        elif op == CompOp.LEQ:
            return StlComparisonOperator.LEQ
        elif op == CompOp.LESS:
            return StlComparisonOperator.LESS
        elif op == CompOp.NEQ:
            return StlComparisonOperator.NEQ
        elif op == CompOp.EQUAL:
            return StlComparisonOperator.EQUAL
        else:
            raise STLParseException('Could not find operator {}!'.format(op))
