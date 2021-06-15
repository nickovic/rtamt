from rtamt.semantics.abstract_eval_visitor import AbstractEvalVisitor
from rtamt.exception.stl.exception import STLNotImplementedException

import operator
from rtamt.enumerations.options import *
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLrtamtASTvisitor

from rtamt.semantics.discrete_time.offline.arithmetic.operation.addition_operation import AdditionOperation
from rtamt.semantics.discrete_time.offline.arithmetic.operation.multiplication_operation import MultiplicationOperation
from rtamt.semantics.discrete_time.offline.arithmetic.operation.subtraction_operation import SubtractionOperation
from rtamt.semantics.discrete_time.offline.arithmetic.operation.division_operation import DivisionOperation
from rtamt.semantics.discrete_time.offline.arithmetic.operation.abs_operation import AbsOperation

from rtamt.semantics.discrete_time.offline.stl.operation.predicate_operation import PredicateOperation
from rtamt.semantics.discrete_time.offline.stl.operation.and_operation import AndOperation
from rtamt.semantics.discrete_time.offline.stl.operation.or_operation import OrOperation
from rtamt.semantics.discrete_time.offline.stl.operation.implies_operation import ImpliesOperation
from rtamt.semantics.discrete_time.offline.stl.operation.iff_operation import IffOperation
from rtamt.semantics.discrete_time.offline.stl.operation.xor_operation import XorOperation
from rtamt.semantics.discrete_time.offline.stl.operation.since_operation import SinceOperation
from rtamt.semantics.discrete_time.offline.stl.operation.not_operation import NotOperation
from rtamt.semantics.discrete_time.offline.stl.operation.rise_operation import RiseOperation
from rtamt.semantics.discrete_time.offline.stl.operation.fall_operation import FallOperation
from rtamt.semantics.discrete_time.offline.stl.operation.once_operation import OnceOperation
from rtamt.semantics.discrete_time.offline.stl.operation.historically_operation import HistoricallyOperation
from rtamt.semantics.discrete_time.offline.stl.operation.always_operation import AlwaysOperation
from rtamt.semantics.discrete_time.offline.stl.operation.eventually_operation import EventuallyOperation
from rtamt.semantics.discrete_time.offline.stl.operation.previous_operation import PreviousOperation
from rtamt.semantics.discrete_time.offline.stl.operation.constant_operation import ConstantOperation
from rtamt.semantics.discrete_time.offline.stl.operation.once_bounded_operation import OnceBoundedOperation
from rtamt.semantics.discrete_time.offline.stl.operation.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.semantics.discrete_time.offline.stl.operation.since_bounded_operation import SinceBoundedOperation
from rtamt.semantics.discrete_time.offline.stl.operation.until_operation import UntilOperation
from rtamt.semantics.discrete_time.offline.stl.operation.until_bounded_operation import UntilBoundedOperation
from rtamt.semantics.discrete_time.offline.stl.operation.always_bounded_operation import AlwaysBoundedOperation
from rtamt.semantics.discrete_time.offline.stl.operation.eventually_bounded_operation import EventuallyBoundedOperation
from rtamt.semantics.discrete_time.offline.stl.operation.next_operation import NextOperation

class STLOfflineDiscreteTimePythonEvalVisitor(STLrtamtASTvisitor):
    def __init__(self, spec):
        super(STLOfflineDiscreteTimePythonEvalVisitor, self).__init__(spec)

    def visitPredicate(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = PredicateOperation(node.operator)
        out_sample = monitor.update(in_sample_1, in_sample_2)
        sat_samples = monitor.sat(in_sample_1, in_sample_2)
        out = []

        if self.spec.time_interpretation == TimeInterpretation.DENSE:
            if self.spec.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars:
                for i, sample in enumerate(sat_samples):
                    val = float("inf") if sample==True else -float("inf")
                    out.append([out_sample[i][0], val])
            elif self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars:
                for i, sample in enumerate(sat_samples):
                    out.append([out_sample[i][0], 0.0])
            elif self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars:
                for i, sample in enumerate(sat_samples):
                    val = float("inf") if sample == True else - float("inf")
                    out.append([out_sample[i][0], val])
            elif self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars:
                for i, sample in enumerate(sat_samples):
                    out.append([out_sample[i][0], 0.0])
            else:
                out = out_sample
        else:
            if self.spec.semantics == Semantics.OUTPUT_ROBUSTNESS and not node.out_vars:
                for i, sample in enumerate(sat_samples):
                    val = float("inf") if sample==True else -float("inf")
                    out.append(val)
            elif self.spec.semantics == Semantics.INPUT_VACUITY and not node.in_vars:
                for i, sample in enumerate(sat_samples):
                    out.append(0.0)
            elif self.spec.semantics == Semantics.INPUT_ROBUSTNESS and not node.in_vars:
                for i, sample in enumerate(sat_samples):
                    val = float("inf") if sample == True else - float("inf")
                    out.append(val)
            elif self.spec.semantics == Semantics.OUTPUT_VACUITY and not node.out_vars:
                for i, sample in enumerate(sat_samples):
                    out.append(0.0)
            else:
                out = out_sample

        return out


    def visitVariable(self, node, *args, **kwargs):
        var = self.spec.var_object_dict[node.var]
        if node.field:
            value = []
            for v in var:
                val = operator.attrgetter(node.field)(v[1])
                value.append([v[0], val])
        else:
            value = var

        return value

    def visitAbs(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = AbsOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitAddition(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = AdditionOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitSubtraction(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = SubtractionOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitMultiplication(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = MultiplicationOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitDivision(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = DivisionOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitNot(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = NotOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitAnd(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = AndOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitOr(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = OrOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitImplies(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = ImpliesOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitIff(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = IffOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitXor(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = XorOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitEventually(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = EventuallyOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitAlways(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = AlwaysOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitUntil(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = UntilOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitOnce(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = OnceOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitHistorically(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = HistoricallyOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitSince(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = SinceOperation()
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitRise(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = RiseOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitFall(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = FallOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitConstant(self, node, *args, **kwargs):
        monitor = ConstantOperation(node.val)
        out_sample = monitor.update()
        if len(args) > 0:
            length = args[0][0]
            out = []
            for i in range(length):
                out.append(out_sample)
            out_sample = out

        return out_sample

    def visitPrevious(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = PreviousOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitNext(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = NextOperation()
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedPrecedes(self, node, *args, **kwargs):
        raise STLNotImplementedException('Precedes operator not implemented in STL offline monitor.')

    def visitTimedOnce(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = OnceBoundedOperation(node.begin, node.end)
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedHistorically(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = HistoricallyBoundedOperation(node.begin, node.end)
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedSince(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = SinceBoundedOperation(node.begin, node.end)
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitTimedAlways(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = AlwaysBoundedOperation(node.begin, node.end)
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedEventually(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample = children_out[0]

        monitor = EventuallyBoundedOperation(node.begin, node.end)
        out_sample = monitor.update(in_sample)

        return out_sample

    def visitTimedUntil(self, node, *args, **kwargs):
        children_out = self.visitChildren(node, *args, **kwargs)
        in_sample_1 = children_out[0]
        in_sample_2 = children_out[1]

        monitor = UntilBoundedOperation(node.begin, node.end)
        out_sample = monitor.update(in_sample_1, in_sample_2)

        return out_sample

    def visitDefault(self, node, *args, **kwargs):
        return node
