from rtamt.operation.abstract_operation import AbstractOperation

class SinceOperation(AbstractOperation):
    def __init__(self):
        self.input = []
        self.input.append(float("nan"))
        self.input.append(float("nan"))
        self.prev_out = -float("inf")

    def reset(self):
        self.input = []
        self.input.append(float("nan"))
        self.input.append(float("nan"))
        self.prev_out = -float("inf")

    def addNewInput(self, left, right):
        self.input[0] = left
        self.input[1] = right

    def update(self):
        out = min(self.input[0], self.prev_out)
        out = max(out, self.input[1])

        self.prev_out = out;
        return out
