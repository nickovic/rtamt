from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.spec.comp_oper import StlComparisonOperator

class PredicateOperation(AbstractOperation):
    def __init__(self, op):
        self.op = op
        self.left = float("nan")
        self.right = float("nan")

    def reset(self):
        self.left = float("nan")
        self.right = float("nan")

    def addNewInput(self, left, right):
        self.left = left
        self.right = right

    def update(self):
        if self.op.value == StlComparisonOperator.EQ.value:
            val = - abs(self.left - self.right)
        elif self.op.value == StlComparisonOperator.NEQ.value:
            val = abs(self.left - self.right)
        elif self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value:
            val = self.right - self.left
        elif self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value:
            val = self.left - self.right
        else:
            val = float('nan')

        return val
