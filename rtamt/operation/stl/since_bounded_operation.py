import collections
from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample

class SinceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.buffer = []
        self.buffer.append(collections.deque(maxlen=(end+1)))
        self.buffer.append(collections.deque(maxlen=(end+1)))

        for i in range(end+1):
            s_left = Sample()
            s_right = Sample()
            s_left.value = float("inf")
            s_left.value = - float("inf")
            self.buffer[0].append(s_left)
            self.buffer[1].append(s_right)

    def addNewInput(self, left, right):
        input = Sample()
        input.seq = left.seq
        input.time.sec = left.time.sec
        input.time.msec = left.time.msec
        input.value = left.value
        self.buffer[0].append(input)

        input = Sample()
        input.seq = right.seq
        input.time.sec = right.time.sec
        input.time.msec = right.time.msec
        input.value = right.value
        self.buffer[1].append(input)

    def update(self):
        out = Sample()

        out.seq = self.input.seq
        out.time.msec = self.input.time.msec
        out.time.sec = self.input.time.sec
        out.value = - float("inf")

        for i in range(self.end-self.begin+1):
            left = float("inf")
            right = self.buffer[1][i].value
            for j in range(self.end-self.begin+1,self.end+1):
                left = min(left, self.buffer[0][j].value)
            out.value = max(out.value, min(left,right))

        return out
