import collections
from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample

class OnceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.reset()

    def reset(self):
        self.input = Sample()
        self.buffer = collections.deque(maxlen=(self.end+1))

        for i in range(self.end+1):
            s = Sample()
            s.value = - float("inf")
            self.buffer.append(s)

    def addNewInput(self, sample):
        self.input = Sample()

        self.input.seq = sample.seq
        self.input.time.sec = sample.time.sec
        self.input.time.msec = sample.time.msec
        self.input.value = sample.value

        self.buffer.append(self.input)


    def update(self):
        out = Sample()
        out.seq = self.input.seq
        out.time.msec = self.input.time.msec
        out.time.sec = self.input.time.sec

        out.value = -float("inf")
        for i in range(self.end-self.begin+1):
            out.value = max(out.value, self.buffer[i].value)

        return out