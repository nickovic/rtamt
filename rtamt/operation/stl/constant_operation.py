from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample
from rtamt.operation.sample import Time

class ConstantOperation(AbstractOperation):
    def __init__(self, val):
        self.val = val
        self.time = 0

    def reset(self):
        self.time = 0

    def update(self):
        out = Sample()
        out.seq = self.time
        out.value = self.val
        return out