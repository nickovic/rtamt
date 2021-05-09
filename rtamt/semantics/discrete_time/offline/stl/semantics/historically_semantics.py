from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class HistoricallySemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self):
        self.prev_out = float("inf")

    def reset(self):
        self.prev_out = float("inf")

    def update(self, samples):
        out = []
        for sample in samples:
            out_sample = min(sample, self.prev_out)
            self.prev_out = out_sample
            out.append(out_sample)
        return out

        return out
