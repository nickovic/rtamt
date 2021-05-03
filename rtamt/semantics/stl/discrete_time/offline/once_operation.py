from rtamt.semantics.abstract_semantics import AbstractSemantics

class OnceOperation(AbstractSemantics):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.prev_out = -float("inf")


    def update(self, samples):
        out = []
        for sample in samples:
            out_sample = max(sample, self.prev_out)
            self.prev_out = out_sample
            out.append(out_sample)
        return out

        return out
