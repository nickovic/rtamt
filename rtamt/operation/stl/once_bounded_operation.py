import collections
from rtamt.operation.abstract_operation import AbstractOperation

class OnceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.input = float("nan")
        self.buffer = collections.deque(maxlen=(self.end + 1))

        for i in range(self.end + 1):
            val = - float("inf")
            self.buffer.append(val)

    def reset(self):
        self.input = float("nan")
        self.buffer = collections.deque(maxlen=(self.end + 1))

        for i in range(self.end + 1):
            val = - float("inf")
            self.buffer.append(val)

    def addNewInput(self, sample):
        self.input = sample
        self.buffer.append(self.input)

    def update(self):
        out = -float("inf")
        for i in range(self.end-self.begin+1):
            out = max(out, self.buffer[i])

        return out
