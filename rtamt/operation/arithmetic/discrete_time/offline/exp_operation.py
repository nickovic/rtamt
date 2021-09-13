import math
from rtamt.operation.abstract_operation import AbstractOperation


class ExpOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, samples):

        out = []
        for sample in samples:
            out_sample = math.exp(sample)
            out.append(out_sample)

        return out