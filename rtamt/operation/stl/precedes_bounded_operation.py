import collections
from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample

class PrecedesBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

        self.reset()

    def reset(self):
        self.buffer = []
        self.buffer.append(collections.deque(maxlen=(self.end+1)))
        self.buffer.append(collections.deque(maxlen=(self.end+1)))
        self.input = Sample()

        for i in range(self.end+1):
            s_left = Sample()
            s_right = Sample()
            s_left.value = float("inf")
            s_right.value = - float("inf")
            self.buffer[0].append(s_left)
            self.buffer[1].append(s_right)

    def addNewInput(self, left, right):
        self.input = Sample()
        self.input.seq = left.seq
        self.input.time.sec = left.time.sec
        self.input.time.msec = left.time.msec
        self.input.value = left.value
        self.buffer[0].append(self.input)

        self.input = Sample()
        self.input.seq = right.seq
        self.input.time.sec = right.time.sec
        self.input.time.msec = right.time.msec
        self.input.value = right.value
        self.buffer[1].append(self.input)

    def update(self):
        out = Sample()

        out.seq = self.input.seq
        out.time.msec = self.input.time.msec
        out.time.sec = self.input.time.sec
        out.value = - float("inf")

        for i in range(self.begin, self.end+1):
            left = float("inf")
            right = self.buffer[1][i].value
            for j in range(0, i):
                left = min(left, self.buffer[0][j].value)

            out.value = max(out.value, min(left, right))

        return out
