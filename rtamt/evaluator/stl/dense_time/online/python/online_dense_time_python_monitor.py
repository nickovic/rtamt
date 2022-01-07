from rtamt.ast.visitor.stl.ASTVisitor import STLASTVisitor
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.exception.ltl.exception import LTLNotImplementedException
from rtamt.operation.stl.dense_time.online.predicate_operation import PredicateOperation
from rtamt.operation.arithmetic.dense_time.online.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.dense_time.online.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.dense_time.online.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.dense_time.online.division_operation import DivisionOperation
from rtamt.operation.stl.dense_time.online.and_operation import AndOperation
from rtamt.operation.stl.dense_time.online.or_operation import OrOperation
from rtamt.operation.stl.dense_time.online.implies_operation import ImpliesOperation
from rtamt.operation.stl.dense_time.online.iff_operation import IffOperation
from rtamt.operation.stl.dense_time.online.xor_operation import XorOperation
from rtamt.operation.stl.dense_time.online.since_operation import SinceOperation
from rtamt.operation.arithmetic.dense_time.online.abs_operation import AbsOperation
from rtamt.operation.arithmetic.dense_time.online.sqrt_operation import SqrtOperation
from rtamt.operation.arithmetic.dense_time.online.pow_operation import PowOperation
from rtamt.operation.arithmetic.dense_time.online.exp_operation import ExpOperation
from rtamt.operation.stl.dense_time.online.not_operation import NotOperation
from rtamt.operation.stl.dense_time.online.once_operation import OnceOperation
from rtamt.operation.stl.dense_time.online.historically_operation import HistoricallyOperation
from rtamt.operation.stl.dense_time.online.constant_operation import ConstantOperation
from rtamt.operation.stl.dense_time.online.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.dense_time.online.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.dense_time.online.since_bounded_operation import SinceBoundedOperation


class STLOnlineDenseTimePythonMonitor(STLASTVisitor):
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
        raise LTLNotImplementedException('Rise operator not implemented in STL dense monitor.')

    def visitFall(self, node, args):
        raise LTLNotImplementedException('Fall operator not implemented in STL dense monitor.')

    def visitConstant(self, node, args):
        monitor = ConstantOperation(node.val)
        self.node_monitor_dict[node.name] = monitor

    def visitPrevious(self, node, args):
        raise LTLNotImplementedException('Previous operator not implemented in STL dense-time monitor.')

    def visitNext(self, node, args):
        raise LTLNotImplementedException('Next operator not implemented in STL dense-time monitor.')

    def visitTimedPrecedes(self, node, args):
        raise STLNotImplementedException('Precedes operator not implemented in STL dense-time monitor.')

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
        raise STLNotImplementedException('Bounded always operator not implemented in STL dense-time monitor.')

    def visitTimedEventually(self, node, args):
        raise STLNotImplementedException('Bounded eventually operator not implemented in STL dense-time monitor.')

    def visitTimedUntil(self, node, args):
        raise STLNotImplementedException('Bounded until operator not implemented in STL dense-time monitor.')

    def visitDefault(self, node, args):
        pass
        
    
        