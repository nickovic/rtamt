import collections
from rtamt.operation.abstract_operation import AbstractOperation


class SinceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

        self.buffer_left = collections.deque(maxlen=(self.end + 1))
        self.buffer_right = collections.deque(maxlen=(self.end + 1))

        for i in range(self.end + 1):
            s_left = float("inf")
            s_right = - float("inf")
            self.buffer_left.append(s_left)
            self.buffer_right.append(s_right)

    def reset(self):
        for i in range(self.end + 1):
            s_left = float("inf")
            s_right = - float("inf")
            self.buffer_left.append(s_left)
            self.buffer_right.append(s_right)

    def update(self, left, right):
        self.buffer_left.append(left)
        self.buffer_right.append(right)
        out = - float("inf")

        for i in range(self.end-self.begin+1):
            left = float("inf")
            right = self.buffer_right[i]
            for j in range(i+1,self.end+1):
                left = min(left, self.buffer_left[j])
            out = max(out, min(left, right))

        return out

