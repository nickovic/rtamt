from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLrtamtASTvisitor

from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.exception.ltl.exception import LTLNotImplementedException

from rtamt.semantics.dense_time.online.arithmetic.operation.addition_operation import AdditionOperation
from rtamt.semantics.dense_time.online.arithmetic.operation.multiplication_operation import MultiplicationOperation
from rtamt.semantics.dense_time.online.arithmetic.operation.subtraction_operation import SubtractionOperation
from rtamt.semantics.dense_time.online.arithmetic.operation.division_operation import DivisionOperation
from rtamt.semantics.dense_time.online.arithmetic.operation.abs_operation import AbsOperation

from rtamt.semantics.dense_time.online.stl.operation.predicate_operation import PredicateOperation
from rtamt.semantics.dense_time.online.stl.operation.and_operation import AndOperation
from rtamt.semantics.dense_time.online.stl.operation.or_operation import OrOperation
from rtamt.semantics.dense_time.online.stl.operation.implies_operation import ImpliesOperation
from rtamt.semantics.dense_time.online.stl.operation.iff_operation import IffOperation
from rtamt.semantics.dense_time.online.stl.operation.xor_operation import XorOperation
from rtamt.semantics.dense_time.online.stl.operation.since_operation import SinceOperation
from rtamt.semantics.dense_time.online.stl.operation.not_operation import NotOperation
from rtamt.semantics.dense_time.online.stl.operation.once_operation import OnceOperation
from rtamt.semantics.dense_time.online.stl.operation.historically_operation import HistoricallyOperation
from rtamt.semantics.dense_time.online.stl.operation.always_operation import AlwaysOperation
from rtamt.semantics.dense_time.online.stl.operation.constant_operation import ConstantOperation
from rtamt.semantics.dense_time.online.stl.operation.once_bounded_operation import OnceBoundedOperation
from rtamt.semantics.dense_time.online.stl.operation.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.semantics.dense_time.online.stl.operation.since_bounded_operation import SinceBoundedOperation


class STLOnlineDenseTimePythonMonitor(STLrtamtASTvisitor):
    def __init__(self):
        STLrtamtASTvisitor.__init__(self)
        self.node_monitor_dict = dict()
        
    def generate(self, node):
        self.visit(node)
        return self.node_monitor_dict

    def visitPredicate(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = PredicateOperation(node.operator)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitVariable(self, node, *args, **kwargs):
        self.visitChildren(node)
        return node

    def visitAbs(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = AbsOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitAddition(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = AdditionOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitSubtraction(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = SubtractionOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitMultiplication(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = MultiplicationOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitDivision(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = DivisionOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitNot(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = NotOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitAnd(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = AndOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitOr(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = OrOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitImplies(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = ImpliesOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitIff(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = IffOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitXor(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = XorOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitEventually(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Eventually operator is not implemented in the STL online monitor.')

    def visitAlways(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Always operator is not implemented in the STL online monitor.')

    def visitUntil(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Until operator is not implemented in the STL online monitor.')

    def visitOnce(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = OnceOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitHistorically(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = HistoricallyOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitSince(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = SinceOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitRise(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Rise operator not implemented in STL dense monitor.')

    def visitFall(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Fall operator not implemented in STL dense monitor.')

    def visitConstant(self, node, *args, **kwargs):
        monitor = ConstantOperation(node.val)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitPrevious(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Previous operator not implemented in STL dense-time monitor.')

    def visitNext(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Next operator not implemented in STL dense-time monitor.')

    def visitTimedPrecedes(self, node, *args, **kwargs):
        raise STLNotImplementedException('Precedes operator not implemented in STL dense-time monitor.')

    def visitTimedOnce(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = OnceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitTimedHistorically(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = HistoricallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitTimedSince(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = SinceBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitTimedAlways(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded always operator not implemented in STL dense-time monitor.')

    def visitTimedEventually(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded eventually operator not implemented in STL dense-time monitor.')

    def visitTimedUntil(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded until operator not implemented in STL dense-time monitor.')

    def visitDefault(self, node, *args, **kwargs):
        return node
        
    
        