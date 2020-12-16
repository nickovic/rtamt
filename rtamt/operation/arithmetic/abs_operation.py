from rtamt.operation.abstract_operation import AbstractOperation


class AbsOperation(AbstractOperation):
    def __init__(self):
        self.input = float("nan")

    def reset(self):
        self.input = float("nan")

    def addNewInput(self, sample):
        self.input = sample

    def update(self):
        out = abs(self.input)

        return out