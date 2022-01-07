from rtamt.ast.visitor.stl.ASTVisitor import STLASTVisitor
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.operation.stl.discrete_time.offline.predicate_operation import PredicateOperation
from rtamt.operation.arithmetic.discrete_time.offline.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.discrete_time.offline.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.discrete_time.offline.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.discrete_time.offline.division_operation import DivisionOperation
from rtamt.operation.stl.discrete_time.offline.and_operation import AndOperation
from rtamt.operation.stl.discrete_time.offline.or_operation import OrOperation
from rtamt.operation.stl.discrete_time.offline.implies_operation import ImpliesOperation
from rtamt.operation.stl.discrete_time.offline.iff_operation import IffOperation
from rtamt.operation.stl.discrete_time.offline.xor_operation import XorOperation
from rtamt.operation.stl.discrete_time.offline.since_operation import SinceOperation
from rtamt.operation.arithmetic.discrete_time.offline.abs_operation import AbsOperation
from rtamt.operation.arithmetic.discrete_time.offline.sqrt_operation import SqrtOperation
from rtamt.operation.arithmetic.discrete_time.offline.exp_operation import ExpOperation
from rtamt.operation.arithmetic.discrete_time.offline.pow_operation import PowOperation
from rtamt.operation.stl.discrete_time.offline.not_operation import NotOperation
from rtamt.operation.stl.discrete_time.offline.rise_operation import RiseOperation
from rtamt.operation.stl.discrete_time.offline.fall_operation import FallOperation
from rtamt.operation.stl.discrete_time.offline.once_operation import OnceOperation
from rtamt.operation.stl.discrete_time.offline.historically_operation import HistoricallyOperation
from rtamt.operation.stl.discrete_time.offline.always_operation import AlwaysOperation
from rtamt.operation.stl.discrete_time.offline.eventually_operation import EventuallyOperation
from rtamt.operation.stl.discrete_time.offline.previous_operation import PreviousOperation
from rtamt.operation.stl.discrete_time.offline.constant_operation import ConstantOperation
from rtamt.operation.stl.discrete_time.offline.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.discrete_time.offline.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.discrete_time.offline.since_bounded_operation import SinceBoundedOperation
from rtamt.operation.stl.discrete_time.offline.until_operation import UntilOperation
from rtamt.operation.stl.discrete_time.offline.until_bounded_operation import UntilBoundedOperation
from rtamt.operation.stl.discrete_time.offline.always_bounded_operation import AlwaysBoundedOperation
from rtamt.operation.stl.discrete_time.offline.eventually_bounded_operation import EventuallyBoundedOperation
from rtamt.operation.stl.discrete_time.offline.next_operation import NextOperation

class STLOfflineDiscreteTimePythonMonitor(STLASTVisitor):
    def __init__(self):
        self.node_monitor_dict = dict()
        
    def generate(self, node):
        self.visit(node, [])
        return self.node_monitor_dict

    def visitPredicate(self, node, args):
        monitor = PredicateOperation(node.operator)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitVariable(self, node, args):
        pass

    def visitAbs(self, node, args):
        monitor = AbsOperation()
        self.node_monitor_dict[node.name] = monitor
        self.visit(node.children[0], args)

    def visitSqrt(self, node, args):
        monitor = SqrtOperation()
        self.node_monitor_dict[node.name] = monitor
        self.visit(node.children[0], args)

    def visitExp(self, node, args):
        monitor = ExpOperation()
        self.node_monitor_dict[node.name] = monitor
        self.visit(node.children[0], args)

    def visitPow(self, node, args):
        monitor = PowOperation()
        self.node_monitor_dict[node.name] = monitor
        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitAddition(self, node, args):
        monitor = AdditionOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitSubtraction(self, node, args):
        monitor = SubtractionOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitMultiplication(self, node, args):
        monitor = MultiplicationOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitDivision(self, node, args):
        monitor = DivisionOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitNot(self, node, args):
        monitor = NotOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitAnd(self, node, args):
        monitor = AndOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitOr(self, node, args):
        monitor = OrOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitImplies(self, node, args):
        monitor = ImpliesOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitIff(self, node, args):
        monitor = IffOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitXor(self, node, args):
        monitor = XorOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitEventually(self, node, args):
        monitor = EventuallyOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitAlways(self, node, args):
        monitor = AlwaysOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitUntil(self, node, args):
        monitor = UntilOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitOnce(self, node, args):
        monitor = OnceOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitHistorically(self, node, args):
        monitor = HistoricallyOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitSince(self, node, args):
        monitor = SinceOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitRise(self, node, args):
        monitor = RiseOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitFall(self, node, args):
        monitor = FallOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitConstant(self, node, args):
        monitor = ConstantOperation(node.val)
        self.node_monitor_dict[node.name] = monitor

    def visitPrevious(self, node, args):
        monitor = PreviousOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitNext(self, node, args):
        monitor = NextOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedPrecedes(self, node, args):
        raise STLNotImplementedException('Precedes operator not implemented in STL offline monitor.')

    def visitTimedOnce(self, node, args):
        monitor = OnceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedHistorically(self, node, args):
        monitor = HistoricallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedSince(self, node, args):
        monitor = SinceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitTimedAlways(self, node, args):
        monitor = AlwaysBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedEventually(self, node, args):
        monitor = EventuallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedUntil(self, node, args):
        monitor = UntilBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitDefault(self, node, args):
        pass
        
    
        