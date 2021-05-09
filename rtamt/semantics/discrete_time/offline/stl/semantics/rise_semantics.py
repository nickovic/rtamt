from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class RiseSemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self):
        self.prev = -float("inf")

    def reset(self):
        self.prev = -float("inf")

    def evaluate(self, samples):
        out = []
        for sample in samples:
            out_sample = min(- self.prev, sample)
            self.prev = sample
            out.append(out_sample)

        return out