import operator

from rtamt.ast.visitor.stl.ast_visitor import StlAstVisitor

from rtamt.operation.arithmetic.discrete_time.online.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.discrete_time.online.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic.discrete_time.online.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.discrete_time.online.division_operation import DivisionOperation
from rtamt.operation.arithmetic.discrete_time.online.abs_operation import AbsOperation
from rtamt.operation.arithmetic.discrete_time.online.sqrt_operation import SqrtOperation
from rtamt.operation.arithmetic.discrete_time.online.exp_operation import ExpOperation
from rtamt.operation.arithmetic.discrete_time.online.pow_operation import PowOperation

from rtamt.operation.stl.discrete_time.online.predicate_operation import PredicateOperation
from rtamt.operation.stl.discrete_time.online.and_operation import AndOperation
from rtamt.operation.stl.discrete_time.online.or_operation import OrOperation
from rtamt.operation.stl.discrete_time.online.implies_operation import ImpliesOperation
from rtamt.operation.stl.discrete_time.online.iff_operation import IffOperation
from rtamt.operation.stl.discrete_time.online.xor_operation import XorOperation
from rtamt.operation.stl.discrete_time.online.since_operation import SinceOperation
from rtamt.operation.stl.discrete_time.online.not_operation import NotOperation
from rtamt.operation.stl.discrete_time.online.rise_operation import RiseOperation
from rtamt.operation.stl.discrete_time.online.fall_operation import FallOperation
from rtamt.operation.stl.discrete_time.online.once_operation import OnceOperation
from rtamt.operation.stl.discrete_time.online.historically_operation import HistoricallyOperation
from rtamt.operation.stl.discrete_time.online.previous_operation import PreviousOperation
from rtamt.operation.stl.discrete_time.online.once_timed_operation import OnceTimedOperation
from rtamt.operation.stl.discrete_time.online.historically_timed_operation import HistoricallyTimedOperation
from rtamt.operation.stl.discrete_time.online.since_timed_operation import SinceTimedOperation
from rtamt.operation.stl.discrete_time.online.precedes_timed_operation import PrecedesTimedOperation

from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.exception.ltl.exception import LTLNotImplementedException

class StlDiscreteTimeOnlineAstVisitor(StlAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = PredicateOperation(node)
        return

    def visitVariable(self, node, *args, **kwargs):
        var = self.ast.var_object_dict[node.var]
        if node.field:  #TODO Tom did not understand this line.
            sample_return = operator.attrgetter(node.field)(var)
        else:
            sample_return = var
        return sample_return

    def visitAbs(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = AbsOperation()
        return

    def visitSqrt(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = SqrtOperation()
        return

    def visitExp(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = ExpOperation()
        return

    def visitPow(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = PowOperation()
        return

    def visitAddition(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = AdditionOperation()
        return

    def visitSubtraction(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = SubtractionOperation()
        return

    def visitMultiplication(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = MultiplicationOperation()
        return

    def visitDivision(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = DivisionOperation()
        return

    def visitNot(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = NotOperation
        return

    def visitAnd(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = AndOperation()
        return

    def visitOr(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = OrOperation()
        return

    def visitImplies(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = ImpliesOperation()
        return

    def visitIff(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = IffOperation()
        return

    def visitXor(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = XorOperation()
        return

    def visitEventually(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Eventually operator is not implemented in the STL online monitor.')

    def visitAlways(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Always operator is not implemented in the STL online monitor.')

    def visitUntil(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Until operator is not implemented in the STL online monitor.')

    def visitOnce(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = OnceOperation()
        return

    def visitHistorically(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = HistoricallyOperation()
        return

    def visitSince(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = SinceOperation()
        return

    def visitRise(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = RiseOperation()
        return

    def visitFall(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = FallOperation()
        return

    def visitConstant(self, node, *args, **kwargs):
        return node.val

    def visitPrevious(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = PreviousOperation()
        return

    def visitNext(self, node, *args, **kwargs):
        raise LTLNotImplementedException('Next operator not implemented in STL online monitor.')

    def visitTimedPrecedes(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = PrecedesTimedOperation(node.begin, node.end)
        return

    def visitTimedOnce(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = OnceTimedOperation(node.begin, node.end)
        return

    def visitTimedHistorically(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = HistoricallyTimedOperation(node.begin, node.end)
        return

    def visitTimedSince(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = SinceTimedOperation(node.begin, node.end)
        return

    def visitTimedAlways(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded always operator not implemented in STL online monitor.')

    def visitTimedEventually(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded eventually operator not implemented in STL online monitor.')

    def visitTimedUntil(self, node, *args, **kwargs):
        raise STLNotImplementedException('Bounded until operator not implemented in STL online monitor.')
