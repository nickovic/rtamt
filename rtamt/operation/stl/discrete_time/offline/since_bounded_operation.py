import collections
from rtamt.operation.abstract_operation import AbstractOperation


class SinceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, left, right):
        out = []
        self.buffer_left = collections.deque(maxlen=(self.end + 1))
        self.buffer_right = collections.deque(maxlen=(self.end + 1))

        for i in range(self.end + 1):
            s_left = float("inf")
            s_right = - float("inf")
            self.buffer_left.append(s_left)
            self.buffer_right.append(s_right)

        for i in range(len(left)):
            self.buffer_left.append(left[i])
            self.buffer_right.append(right[i])
            out_sample = - float("inf")

            for j in range(self.end-self.begin+1):
                c_left = float("inf")
                c_right = self.buffer_right[j]
                for k in range(j+1, self.end+1):
                    c_left = min(c_left, self.buffer_left[k])
                out_sample = max(out_sample, min(c_left, c_right))
            out.append(out_sample)
        return out

