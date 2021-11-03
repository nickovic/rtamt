import collections
from rtamt.operation.abstract_operation import AbstractOperation

class EventuallyBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer_bak = collections.deque([-float("inf")]*(self.end+1), maxlen=(self.end + 1))

    def update(self, samples):
        out = []

        buffer = self.buffer_bak.copy()

        for sample in reversed(samples):
            buffer.append(sample)
            out_sample = max(list(buffer))
            out.append(out_sample)
        out.reverse()

        return out