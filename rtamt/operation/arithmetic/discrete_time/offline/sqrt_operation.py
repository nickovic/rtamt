import math
from rtamt.operation.abstract_operation import AbstractOperation


class SqrtOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, samples):

        out = []
        for sample in samples:
            if sample < 0:
                raise Exception('sqrt: sample is smaller than 0.')
            out_sample = math.sqrt(sample)
            out.append(out_sample)

        return out