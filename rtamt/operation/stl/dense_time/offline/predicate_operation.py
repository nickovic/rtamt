from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.enumerations.comp_oper import StlComparisonOperator
from rtamt.operation.arithmetic.dense_time.offline.subtraction_operation import SubtractionOperation
from rtamt.exception.ltl.exception import LTLException


class PredicateOperation(AbstractOperation):
    def __init__(self, op):
        self.op = op
        self.sub = SubtractionOperation()

    def update(self, *args, **kargs):
        out = []
        self.sub = SubtractionOperation()
        input_list_1 = args[0]
        input_list_2 = args[1]
        input_list = self.sub.update(input_list_1, input_list_2)


        prev = float("nan")
        for i, in_sample in enumerate(input_list):
            if self.op.value == StlComparisonOperator.EQ.value:
                out_val = - abs(in_sample[1])
            elif self.op.value == StlComparisonOperator.NEQ.value:
                out_val = abs(in_sample[1])
            elif self.op.value == StlComparisonOperator.LEQ.value or self.op.value == StlComparisonOperator.LESS.value:
                out_val = - in_sample[1]
            elif self.op.value == StlComparisonOperator.GEQ.value or self.op.value == StlComparisonOperator.GREATER.value:
                out_val = in_sample[1]
            else:
                out_val = float('nan')

            if out_val != prev or i == len(input_list) - 1:
                out.append([in_sample[0], out_val])
            prev = out_val

        return out

    def sat(self, *args, **kargs):
        out = []
        input_list_1 = args[0]
        input_list_2 = args[1]
        input_list = self.sub.update(input_list_1, input_list_2)

        prev = float("nan")
        for i, in_sample in enumerate(input_list):
            if self.op.value == StlComparisonOperator.EQ.value:
                out_val = True if in_sample[0] == 0 else False
            elif self.op.value == StlComparisonOperator.NEQ.value:
                out_val = False if in_sample[0] == 0 else True
            elif self.op.value == StlComparisonOperator.LEQ.value:
                out_val = True if in_sample[0] <= 0 else False
            elif self.op.value == StlComparisonOperator.LESS.value:
                out_val = True if in_sample[0] < 0 else False
            elif self.op.value == StlComparisonOperator.GEQ.value:
                out_val = True if in_sample[0] >= 0 else False
            elif self.op.value == StlComparisonOperator.GREATER.value:
                out_val = True if in_sample[0] > 0 else False
            else:
                raise LTLException('Unknown predicate operation')

            if out_val != prev or i == len(input_list) - 1:
                out.append([in_sample[0], out_val])
            prev = out_val

        return out

