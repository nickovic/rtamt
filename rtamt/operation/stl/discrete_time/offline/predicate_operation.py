from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.enumerations.comp_oper import StlComparisonOperator

class PredicateOperation(AbstractOperation):
    def __init__(self, op):
        self.op = op

    def reset(self):
        pass

    def update(self, left, right):

        out = []
        for i in range(len(left)):
            if self.op.value == StlComparisonOperator.EQ.value:
                val = - abs(left[i] - right[i])
            elif self.op.value == StlComparisonOperator.NEQ.value:
                val = abs(left[i] - right[i])
            elif self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value:
                val = right[i] - left[i]
            elif self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value:
                val = left[i] - right[i]
            else:
                val = float('nan')
            out.append(val)

        return out
