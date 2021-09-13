import math
from rtamt.operation.abstract_operation import AbstractOperation


class ExpOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        out = math.exp(sample)

        return out