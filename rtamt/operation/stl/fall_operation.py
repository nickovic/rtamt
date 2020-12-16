from rtamt.operation.abstract_operation import AbstractOperation


class FallOperation(AbstractOperation):
    def __init__(self):
        self.prev = float("inf")
        self.input = float("nan")

    def reset(self):
        self.prev = float("inf")
        self.input = float("nan")

    def addNewInput(self, sample):
        self.input = sample

    def update(self):
        out = min(self.prev, - self.input)
        self.prev = self.input

        return out
