from rtamt.spec.stl.visitor import STLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.operation.stl.predicate_operation import PredicateOperation
from rtamt.operation.arithmetic.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.division_operation import DivisionOperation
from rtamt.operation.stl.and_operation import AndOperation
from rtamt.operation.stl.or_operation import OrOperation
from rtamt.operation.stl.implies_operation import ImpliesOperation
from rtamt.operation.stl.iff_operation import IffOperation
from rtamt.operation.stl.xor_operation import XorOperation
from rtamt.operation.stl.since_operation import SinceOperation
from rtamt.operation.arithmetic.abs_operation import AbsOperation
from rtamt.operation.stl.not_operation import NotOperation
from rtamt.operation.stl.rise_operation import RiseOperation
from rtamt.operation.stl.fall_operation import FallOperation
from rtamt.operation.stl.once_operation import OnceOperation
from rtamt.operation.stl.historically_operation import HistoricallyOperation
from rtamt.operation.stl.always_operation import AlwaysOperation
from rtamt.operation.stl.eventually_operation import EventuallyOperation
from rtamt.operation.stl.previous_operation import PreviousOperation
from rtamt.operation.stl.constant_operation import ConstantOperation
from rtamt.operation.stl.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.since_bounded_operation import SinceBoundedOperation
from rtamt.operation.stl.precedes_bounded_operation import PrecedesBoundedOperation

class STLOnlineDiscreteTimeCPPMonitor(STLVisitor):
    def __init__(self):
        self.node_monitor_dict = dict()
        
    def generate(self, node):
        self.visit(node)
        return self.node_monitor_dict

    def visitPredicate(self, node, args):
        monitor = PredicateOperation(node.operator)
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitVariable(self, node, args):
        pass

    def visitAbs(self, node, args):
        monitor = AbsOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitAddition(self, node, args):
        monitor = AdditionOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitSubtraction(self, node, args):
        monitor = SubtractionOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitMultiplication(self, node, args):
        monitor = MultiplicationOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitDivision(self, node, args):
        monitor = DivisionOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitNot(self, node, args):
        monitor = NotOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitAnd(self, node, args):
        monitor = AndOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitOr(self, node, args):
        monitor = OrOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitImplies(self, node, args):
        monitor = ImpliesOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitIff(self, node, args):
        monitor = IffOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitXor(self, node, args):
        monitor = XorOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitEventually(self, node, args):
        monitor = EventuallyOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitAlways(self, node, args):
        monitor = AlwaysOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitUntil(self, node, args):
        raise STLNotImplementedException('Until operator is not implemented in the STL online monitor.')

    def visitOnce(self, node, args):
        monitor = OnceOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitHistorically(self, node, args):
        monitor = HistoricallyOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitSince(self, node, args):
        monitor = SinceOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitRise(self, node, args):
        monitor = RiseOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitFall(self, node, args):
        monitor = FallOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitConstant(self, node, args):
        monitor = ConstantOperation(node.value)
        self.node_monitor_dict[node] = monitor

    def visitPrevious(self, node, args):
        monitor = PreviousOperation()
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitNext(self, node, args):
        raise STLNotImplementedException('Next operator not implemented in STL online monitor.')

    def visitTimedPrecedes(self, node, args):
        monitor = PrecedesBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitTimedOnce(self, node, args):
        monitor = OnceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitTimedHistorically(self, node, args):
        monitor = HistoricallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])

    def visitTimedSince(self, node, args):
        monitor = SinceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node] = monitor

        self.visit(node.children[0])
        self.visit(node.children[1])

    def visitTimedAlways(self, node, args):
        raise STLNotImplementedException('Bounded always operator not implemented in STL online monitor.')

    def visitTimedEventually(self, node, args):
        raise STLNotImplementedException('Bounded eventually operator not implemented in STL online monitor.')

    def visitTimedUntil(self, node, args):
        raise STLNotImplementedException('Bounded until operator not implemented in STL online monitor.')

    def visitDefault(self, node, args):
        pass
        
    
        