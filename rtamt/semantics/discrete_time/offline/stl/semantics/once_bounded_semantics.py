import collections
from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class OnceBoundedSemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer = collections.deque(maxlen=(self.end + 1))

        for i in range(self.end + 1):
            val = - float("inf")
            self.buffer.append(val)

    def reset(self):
        self.buffer = collections.deque(maxlen=(self.end + 1))

        for i in range(self.end + 1):
            val = - float("inf")
            self.buffer.append(val)

    def evaluate(self, samples):
        out = []

        for sample in samples:
            self.buffer.append(sample)
            out_sample = -float("inf")
            for i in range(self.end - self.begin + 1):
                out_sample = max(out_sample, self.buffer[i])
            out.append(out_sample)

        return out

        return out
