from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.spec.comp_oper import StlComparisonOperator


class PredicateOperation(AbstractOperation):
    def __init__(self, op, threshold, io_type):
        self.op = op
        self.threshold = threshold
        self.io_type = io_type

    def update(self, *args, **kargs):
        out = []
        input_list = args[0]

        prev = float("nan")
        for in_sample in input_list:
            if self.op.value == StlComparisonOperator.EQ.value:
                out_val = - abs(in_sample[1] - self.threshold)
            elif self.op.value == StlComparisonOperator.NEQ.value:
                out_val = abs(in_sample[1] - self.threshold)
            elif self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value:
                out_val = self.threshold - in_sample[1]
            elif self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value:
                out_val = in_sample[1] - self.threshold
            else:
                out_val = float('nan')

            if out_val != prev:
                out.append([in_sample[0], out_val])
            prev = out_val

        return out

    def offline(self, *args, **kargs):
        out = []
        input_list = args[0]

        prev = float("nan")
        for i, in_sample in enumerate(input_list):
            if self.op.value == StlComparisonOperator.EQ.value:
                out_val = - abs(in_sample[1] - self.threshold)
            elif self.op.value == StlComparisonOperator.NEQ.value:
                out_val = abs(in_sample[1] - self.threshold)
            elif self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value:
                out_val = self.threshold - in_sample[1]
            elif self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value:
                out_val = in_sample[1] - self.threshold
            else:
                out_val = float('nan')

            if out_val != prev or i == len(input_list) - 1:
                out.append([in_sample[0], out_val])
            prev = out_val

        return out
