from rtamt.operation.abstract_operation import AbstractOperation

class AlwaysOperation(AbstractOperation):
    def __init__(self):
        self.prev_out = float("inf")

    def reset(self):
        self.prev_out = float("inf")

    def update(self, samples):
        out = []
        for i in range(len(samples)-1, -1, -1):
            out_sample = min(samples[i], self.prev_out)
            self.prev_out = out_sample
            out.append(out_sample)
        out.reverse()
        return out
