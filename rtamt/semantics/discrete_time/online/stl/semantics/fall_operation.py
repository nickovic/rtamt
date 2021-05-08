from rtamt.operation.abstract_operation import AbstractOperation


class FallOperation(AbstractOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        self.prev = float("inf")

    def update(self, sample):
        out = min(self.prev, - sample)
        self.prev = sample

        return out
