from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation
import collections

class ShiftOperation(AbstractOnlineOperation):
    def __init__(self, val):
        self.val = val
        self.buffer = collections.deque(maxlen=(self.val + 1))

        self.reset()

    def reset(self):
        for i in range(self.val + 1):
            val = - float("inf")
            self.buffer.append(val)

    def update(self, sample):
        self.buffer.append(sample)
        return self.buffer[0]