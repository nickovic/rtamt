from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class EventuallySemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self):
        self.prev_out = -float("inf")

    def reset(self):
        self.prev_out = -float("inf")

    def evaluate(self, samples):
        out = []
        for i in range(len(samples)-1, -1, -1):
            out_sample = max(samples[i], self.prev_out)
            self.prev_out = out_sample
            out.append(out_sample)
        out.reverse()
        return out
