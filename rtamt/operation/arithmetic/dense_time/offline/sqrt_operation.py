import math
from rtamt.operation.abstract_operation import AbstractOperation

class SqrtOperation(AbstractOperation):
    def __init__(self):
        self.input = []

    def update(self, input_list):
        out = []

        for in_sample in input_list:
            if in_sample[0] < 0:
                raise Exception('sqrt: the input is smaller than 0.')
            out_time = in_sample[0]
            out_value = math.sqrt(in_sample[1])
            out.append([out_time, out_value])

        return out
