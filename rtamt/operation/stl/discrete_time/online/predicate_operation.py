from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.enumerations.comp_oper import StlComparisonOperator
from rtamt.exception.ltl.exception import LTLException

class PredicateOperation(AbstractOperation):
    def __init__(self, op):
        self.op = op

    def reset(self):
        pass

    def update(self, left, right):
        if self.op.value == StlComparisonOperator.EQ.value:
            val = - abs(left - right)
        elif self.op.value == StlComparisonOperator.NEQ.value:
            val = abs(left - right)
        elif self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value:
            val = right - left
        elif self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value:
            val = left - right
        else:
            raise LTLException('Unknown predicate operation')

        return val

    def sat(self, left, right):
        if self.op.value == StlComparisonOperator.EQ.value:
            val = left == right
        elif self.op.value == StlComparisonOperator.NEQ.value:
            val = left != right
        elif self.op.value == StlComparisonOperator.GEQ.value:
            val = left >= right
        elif self.op.value == StlComparisonOperator.GREATER.value:
            val = left > right
        elif self.op.value == StlComparisonOperator.LEQ.value:
            val = left <= right
        elif self.op.value == StlComparisonOperator.LESS.value:
            val = left < right
        else:
            raise LTLException('Unknown predicate operation')

        return val
