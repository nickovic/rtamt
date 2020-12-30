from rtamt.operation.abstract_operation import AbstractOperation


class OnceOperation(AbstractOperation):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.prev_out = -float("inf")


    def update(self, sample):
        out = max(sample, self.prev_out)
        self.prev_out = out
        return out
