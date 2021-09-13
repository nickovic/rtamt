import math
from rtamt.operation.abstract_operation import AbstractOperation


class PowOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, left, right):
        out = math.pow(left, right)
        return out