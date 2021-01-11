from rtamt.operation.abstract_operation import AbstractOperation

class SinceOperation(AbstractOperation):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.prev_out = -float("inf")

    def update(self, left, right):
        out = []
        for i in range(len(left)):
            out_sample = min(left[i], self.prev_out)
            out_sample = max(out_sample, right[i])
            self.prev_out = out_sample;
            out.append(out_sample)

        return out
