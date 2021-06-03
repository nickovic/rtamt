from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLrtamtASTvisitor

from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.operation.stl.dense_time.offline.predicate_operation import PredicateOperation
from rtamt.operation.arithmetic.dense_time.offline.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.dense_time.offline.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.dense_time.offline.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.dense_time.offline.division_operation import DivisionOperation
from rtamt.operation.stl.dense_time.offline.and_operation import AndOperation
from rtamt.operation.stl.dense_time.offline.or_operation import OrOperation
from rtamt.operation.stl.dense_time.offline.implies_operation import ImpliesOperation
from rtamt.operation.stl.dense_time.offline.iff_operation import IffOperation
from rtamt.operation.stl.dense_time.offline.xor_operation import XorOperation
from rtamt.operation.stl.dense_time.offline.since_operation import SinceOperation
from rtamt.operation.arithmetic.dense_time.offline.abs_operation import AbsOperation
from rtamt.operation.stl.dense_time.offline.not_operation import NotOperation
from rtamt.operation.stl.dense_time.offline.once_operation import OnceOperation
from rtamt.operation.stl.dense_time.offline.historically_operation import HistoricallyOperation
from rtamt.operation.stl.dense_time.offline.always_operation import AlwaysOperation
from rtamt.operation.stl.dense_time.offline.until_operation import UntilOperation
from rtamt.operation.stl.dense_time.offline.eventually_operation import EventuallyOperation
from rtamt.operation.stl.dense_time.offline.constant_operation import ConstantOperation
from rtamt.operation.stl.dense_time.offline.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl.dense_time.offline.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl.dense_time.offline.since_bounded_operation import SinceBoundedOperation
from rtamt.operation.stl.dense_time.offline.always_bounded_operation import AlwaysBoundedOperation
from rtamt.operation.stl.dense_time.offline.eventually_bounded_operation import EventuallyBoundedOperation
from rtamt.operation.stl.dense_time.offline.until_bounded_operation import UntilBoundedOperation


class STLOfflineDenseTimePythonMonitor(STLrtamtASTvisitor):
    def __init__(self):
        STLrtamtASTvisitor.__init__(self)
        self.node_monitor_dict = dict()
        
    def generate(self, node):
        self.visit(node, [])
        return self.node_monitor_dict

    def visitPredicate(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = PredicateOperation(node.operator)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitVariable(self, node, *args, **kwargs):
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
        self.visitChildren(node)
        monitor = EventuallyOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitAlways(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = AlwaysOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitUntil(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = UntilOperation()
        self.node_monitor_dict[node.name] = monitor
        return node

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
        raise STLNotImplementedException('Rise operator not implemented in STL dense monitor.')

    def visitFall(self, node, *args, **kwargs):
        raise STLNotImplementedException('Fall operator not implemented in STL dense monitor.')

    def visitConstant(self, node, *args, **kwargs):
        monitor = ConstantOperation(node.val)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitPrevious(self, node, *args, **kwargs):
        raise STLNotImplementedException('Previous operator not implemented in STL dense-time monitor.')

    def visitNext(self, node, *args, **kwargs):
        raise STLNotImplementedException('Next operator not implemented in STL dense-time monitor.')

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
        self.visitChildren(node)
        monitor = AlwaysBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitTimedEventually(self, node, *args, **kwargs):
        self.visitChildren(node)
        monitor = EventuallyBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor
        return node

    def visitTimedUntil(self, node, *args, **kwargs):
        monitor = UntilBoundedOperation(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor
        return node


    def visitDefault(self, node, *args, **kwargs):
        pass
        
    
        