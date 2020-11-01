from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample
from rtamt.spec.comp_oper import StlComparisonOperator
from rtamt.spec.stl.io_type import StlIOType

class PredicateOperation(AbstractOperation):
    def __init__(self, op):
        self.op = op
        self.reset()

    def reset(self):
        self.left = Sample()
        self.right = Sample()


    def addNewInput(self, left, right):
        self.left.seq = left.seq
        self.left.time.sec = left.time.sec
        self.left.time.msec = left.time.msec
        self.left.value = left.value

        self.right.seq = right.seq
        self.right.time.sec = right.time.sec
        self.right.time.msec = right.time.msec
        self.right.value = right.value

    def update(self):
        out = Sample()

        if (self.op.value == StlComparisonOperator.EQ.value):
            val = - abs(self.left.value - self.right.value)
        elif (self.op.value == StlComparisonOperator.NEQ.value):
            val = abs(self.left.value - self.right.value)
        elif (self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value):
            val = self.right.value - self.left.value
        elif (self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value):
            val = self.left.value - self.right.value
        else:
            val = float('nan')

        out.time.sec = self.left.time.sec
        out.time.msec = self.left.time.msec
        out.seq = self.left.seq
        out.value = val

        return out