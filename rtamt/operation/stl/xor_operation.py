from rtamt.operation.abstract_operation import AbstractOperation

class XorOperation(AbstractOperation):
    def __init__(self):
        self.input = []
        self.input.append(float("nan"))
        self.input.append(float("nan"))

    def reset(self):
        self.input[0] = float("nan")
        self.input[1] = float("nan")

    def addNewInput(self, left, right):
        self.input[0] = left
        self.input[1] = right

    def update(self):
        out = abs(self.input[0] - self.input[1])
        return out
