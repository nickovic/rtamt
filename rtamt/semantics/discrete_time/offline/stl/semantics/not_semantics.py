from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class NotSemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, samples):
        out = []
        for sample in samples:
            out_sample = - sample
            out.append(out_sample)
        return out
