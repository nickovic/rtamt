from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample
from rtamt.spec.comp_oper import StlComparisonOperator
from rtamt.spec.stl.io_type import StlIOType

class PredicateOperation(AbstractOperation):
    def __init__(self, op, threshold, io_type):
        self.input = Sample()
        self.op = op
        self.threshold = threshold
        self.io_type = io_type

    def addNewInput(self, sample):
        self.input.seq = sample.seq
        self.input.time.sec = sample.time.sec
        self.input.time.msec = sample.time.msec
        self.input.value = sample.value

    def update(self):
        out = Sample()

        if (self.op.value == StlComparisonOperator.EQ.value):
            val = - abs(self.input.value - self.threshold)
        elif (self.op.value == StlComparisonOperator.NEQ.value):
            val = abs(self.input.value - self.threshold)
        elif (self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value):
            val = self.threshold - self.input.value
        elif (self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value):
            val = self.input.value - self.threshold
        else:
            val = float('nan')

        out.time.sec = self.input.time.sec
        out.time.msec = self.input.time.msec
        out.seq = self.input.seq
        out.value = val

        return out