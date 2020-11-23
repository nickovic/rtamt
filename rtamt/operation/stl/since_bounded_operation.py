import collections
from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.sample import Sample

class SinceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.reset()

    def reset(self):
        self.buffer_left = collections.deque(maxlen=(self.end+1))
        self.buffer_right = collections.deque(maxlen=(self.end+1))
        self.input = Sample()

        for i in range(self.end+1):
            s_left = Sample()
            s_right = Sample()
            s_left.value = float("inf")
            s_right.value = - float("inf")
            self.buffer_left.append(s_left)
            self.buffer_right.append(s_right)

    def addNewInput(self, left, right):
        self.input = Sample()
        self.input.seq = left.seq
        self.input.time.sec = left.time.sec
        self.input.time.msec = left.time.msec
        self.input.value = left.value
        self.buffer_left.append(self.input)

        self.input = Sample()
        self.input.seq = right.seq
        self.input.time.sec = right.time.sec
        self.input.time.msec = right.time.msec
        self.input.value = right.value
        self.buffer_right.append(self.input)

    def update(self):
        out = Sample()

        out.seq = self.input.seq
        out.time.msec = self.input.time.msec
        out.time.sec = self.input.time.sec
        out.value = - float("inf")

        for i in range(self.end-self.begin+1):
            left = float("inf")
            right = self.buffer_right[i].value
            for j in range(i+1,self.end+1):
                left = min(left, self.buffer_left[j].value)
            out.value = max(out.value, min(left,right))

        return out
