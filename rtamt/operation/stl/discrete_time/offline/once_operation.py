from rtamt.operation.abstract_operation import AbstractOperation


class OnceOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, samples):
        out = []
        prev_out = -float("inf")
        for sample in samples:
            out_sample = max(sample, prev_out)
            prev_out = out_sample
            out.append(out_sample)
        return out
