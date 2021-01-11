from rtamt.operation.abstract_operation import AbstractOperation

class SinceOperation(AbstractOperation):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.prev_out = -float("inf")

    def update(self, left, right):
        out = min(left, self.prev_out)
        out = max(out, right)

        self.prev_out = out;
        return out
