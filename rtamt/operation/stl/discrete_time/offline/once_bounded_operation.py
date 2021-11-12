import collections
from rtamt.operation.abstract_operation import AbstractOperation

class OnceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, samples):
        samples = [-float("inf") for j in range(self.end)] + samples
        out = [max(samples[j - self.end:j - self.begin+ 1]) for j in range(self.end, len(samples))]
        return out
