from rtamt.operation.abstract_operation import AbstractOperation

class PreviousOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, samples):
        out = []
        self.prev = float("inf")
        for sample in samples:
            out_sample = self.prev
            self.prev = sample
            out.append(out_sample)

        return out
