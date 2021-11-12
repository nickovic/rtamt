from rtamt.operation.abstract_operation import AbstractOperation

class HistoricallyOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, samples):
        out = []
        prev_out = float("inf")

        for sample in samples:
            out_sample = min(sample, prev_out)
            prev_out = out_sample
            out.append(out_sample)
        return out

