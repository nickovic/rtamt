import collections
from rtamt.semantics.abstract_semantics import AbstractSemantics

class HistoricallyBoundedOperation(AbstractSemantics):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer = collections.deque(maxlen=(self.end + 1))

        for i in range(self.end+1):
            val = float("inf")
            self.buffer.append(val)

    def reset(self):
        self.buffer = collections.deque(maxlen=(self.end + 1))

        for i in range(self.end + 1):
            val = float("inf")
            self.buffer.append(val)

    def update(self, samples):
        out = []

        for sample in samples:
            self.buffer.append(sample)
            out_sample = float("inf")
            for i in range(self.end-self.begin+1):
                out_sample = min(out_sample, self.buffer[i])
            out.append(out_sample)

        return out
