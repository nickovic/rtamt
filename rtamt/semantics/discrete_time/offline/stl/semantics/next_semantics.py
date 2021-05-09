from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class NextSemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self):
        self.nxt = float("inf")

    def reset(self):
        self.nxt = float("inf")

    def evaluate(self, samples):
        out = []
        for i in range(len(samples)-1, -1, -1):
            out_sample = self.nxt
            self.nxt = samples[i]
            out.append(out_sample)
        out.reverse()

        return out
