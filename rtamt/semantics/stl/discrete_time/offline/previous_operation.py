from rtamt.operation.abstract_operation import AbstractOperation

class PreviousOperation(AbstractOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        self.prev = float("inf")

    def update(self, samples):
        out = []
        for sample in samples:
            out_sample = self.prev
            self.prev = sample
            out.append(out_sample)

        return out
