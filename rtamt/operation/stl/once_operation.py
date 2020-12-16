from rtamt.operation.abstract_operation import AbstractOperation


class OnceOperation(AbstractOperation):
    def __init__(self):
        self.prev_out = -float("inf")
        self.input = float("nan")

    def reset(self):
        self.prev_out = -float("inf")
        self.input = float("nan")

    def addNewInput(self, sample):
        self.input = sample

    def update(self):
        out = max(self.input, self.prev_out)
        self.prev_out = out
        return out
