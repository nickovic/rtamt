from rtamt.operation.abstract_operation import AbstractOperation

class PreviousOperation(AbstractOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        self.prev = float("inf")

    def update(self, sample):
        out = self.prev
        self.prev = sample

        return out
