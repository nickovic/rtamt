from rtamt import LTLNotImplementedException
from rtamt.spec.ltl.discrete_time.visitor import LTLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException

from rtamt.semantics.discrete_time.online.arithmetic.operation.addition_operation import AdditionOperation
from rtamt.semantics.discrete_time.online.arithmetic.operation.multiplication_operation import MultiplicationOperation
from rtamt.semantics.discrete_time.online.arithmetic.operation.subtraction_operation import SubtractionOperation
from rtamt.semantics.discrete_time.online.arithmetic.operation.division_operation import DivisionOperation
from rtamt.semantics.discrete_time.online.arithmetic.operation.abs_operation import AbsOperation

from rtamt.semantics.discrete_time.online.stl.operation.predicate_operation import PredicateOperation
from rtamt.semantics.discrete_time.online.stl.operation.and_operation import AndOperation
from rtamt.semantics.discrete_time.online.stl.operation.or_operation import OrOperation
from rtamt.semantics.discrete_time.online.stl.operation.implies_operation import ImpliesOperation
from rtamt.semantics.discrete_time.online.stl.operation.iff_operation import IffOperation
from rtamt.semantics.discrete_time.online.stl.operation.xor_operation import XorOperation
from rtamt.semantics.discrete_time.online.stl.operation.since_operation import SinceOperation
from rtamt.semantics.discrete_time.online.stl.operation.not_operation import NotOperation
from rtamt.semantics.discrete_time.online.stl.operation.rise_operation import RiseOperation
from rtamt.semantics.discrete_time.online.stl.operation.fall_operation import FallOperation
from rtamt.semantics.discrete_time.online.stl.operation.once_operation import OnceOperation
from rtamt.semantics.discrete_time.online.stl.operation.historically_operation import HistoricallyOperation
from rtamt.semantics.discrete_time.online.stl.operation.always_operation import AlwaysOperation
from rtamt.semantics.discrete_time.online.stl.operation.eventually_operation import EventuallyOperation
from rtamt.semantics.discrete_time.online.stl.operation.previous_operation import PreviousOperation
from rtamt.semantics.discrete_time.online.stl.operation.constant_operation import ConstantOperation

class LTLOnlineDiscreteTimePythonMonitor(LTLVisitor):
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
        raise LTLNotImplementedException('Eventually operator is not implemented in the STL online monitor.')

    def visitAlways(self, node, args):
        raise LTLNotImplementedException('Always operator is not implemented in the STL online monitor.')

    def visitUntil(self, node, args):
        raise LTLNotImplementedException('Until operator is not implemented in the STL online monitor.')

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
        raise LTLNotImplementedException('Next operator not implemented in STL online monitor.')

    def visitDefault(self, node, args):
        pass
        
    
        