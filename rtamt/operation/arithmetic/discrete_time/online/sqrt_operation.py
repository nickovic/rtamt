import math
from rtamt.operation.abstract_operation import AbstractOperation


class SqrtOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        if sample < 0:
            raise Exception('sqrt: input is smaller than 0.')
        out = math.sqrt(sample)

        return out