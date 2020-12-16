from rtamt.operation.abstract_operation import AbstractOperation

class PreviousOperation(AbstractOperation):
    def __init__(self):
        self.input = float("nan")
        self.prev = float("inf")

    def reset(self):
        self.input = float("nan")
        self.prev = float("inf")

    def addNewInput(self, sample):
        self.input = sample

    def update(self):
        out = self.prev
        self.prev = self.input

        return out
