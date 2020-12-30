import collections
from rtamt.operation.abstract_operation import AbstractOperation

class PrecedesBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

        self.buffer = []
        self.buffer.append(collections.deque(maxlen=(self.end + 1)))
        self.buffer.append(collections.deque(maxlen=(self.end + 1)))

        for i in range(self.end + 1):
            s_left = float("inf")
            s_right = - float("inf")
            self.buffer[0].append(s_left)
            self.buffer[1].append(s_right)

    def reset(self):
        self.buffer = []
        self.buffer.append(collections.deque(maxlen=(self.end + 1)))
        self.buffer.append(collections.deque(maxlen=(self.end + 1)))

        for i in range(self.end + 1):
            s_left = float("inf")
            s_right = - float("inf")
            self.buffer[0].append(s_left)
            self.buffer[1].append(s_right)

    def update(self, left, right):
        self.buffer[0].append(left)
        self.buffer[1].append(right)
        out = - float("inf")

        for i in range(self.begin, self.end+1):
            left = float("inf")
            right = self.buffer[1][i]
            for j in range(0, i):
                left = min(left, self.buffer[0][j])

            out = max(out, min(left, right))

        return out
