from rtamt.operation.abstract_online_operation import AbstractOnlineOperation
from rtamt.enumerations.comp_oper import StlComparisonOperator
from rtamt.exception.ltl.exception import LTLException


class PredicateOperation(AbstractOnlineOperation):
    def __init__(self, op):
        self.op = op

    def reset(self):
        pass

    def update(self, node, sample_left, sample_right):
        if self.op.value == StlComparisonOperator.EQ.value:
            sample_return = - abs(sample_left - sample_right)
        elif self.op.value == StlComparisonOperator.NEQ.value:
            sample_return = abs(sample_left - sample_right)
        elif self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value:
            sample_return = sample_right - sample_left
        elif self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value:
            sample_return = sample_left - sample_right
        else:
            raise LTLException('Unknown predicate operation')

        return sample_return

    def sat(self, sample_left, sample_right):
        if self.op.value == StlComparisonOperator.EQ.value:
            sample_return = sample_left == sample_right
        elif self.op.value == StlComparisonOperator.NEQ.value:
            sample_return = sample_left != sample_right
        elif self.op.value == StlComparisonOperator.GEQ.value:
            sample_return = sample_left >= sample_right
        elif self.op.value == StlComparisonOperator.GREATER.value:
            sample_return = sample_left > sample_right
        elif self.op.value == StlComparisonOperator.LEQ.value:
            sample_return = sample_left <= sample_right
        elif self.op.value == StlComparisonOperator.LESS.value:
            sample_return = sample_left < sample_right
        else:
            raise LTLException('Unknown predicate operation')

        return sample_return
