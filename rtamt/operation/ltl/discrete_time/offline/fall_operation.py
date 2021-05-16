from rtamt.operation.abstract_operation import AbstractOperation


class FallOperation(AbstractOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        self.prev = float("inf")

    def update(self, samples):
        out = []
        for sample in samples:
            out_sample = min(self.prev, - sample)
            self.prev = sample
            out.append(out_sample)

        return out
