from rtamt.operation.abstract_operation import AbstractOperation

class NextOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, samples):
        out = []
        self.nxt = float("inf")
        for i in range(len(samples)-1, -1, -1):
            out_sample = self.nxt
            self.nxt = samples[i]
            out.append(out_sample)
        out.reverse()

        return out
