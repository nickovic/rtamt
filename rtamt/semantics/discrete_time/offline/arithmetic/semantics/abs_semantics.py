from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class AbsSemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self):
        pass

    def reset(self):
        pass

    def evaluate(self, samples):

        out = []
        for sample in samples:
            out_sample = abs(sample)
            out.append(out_sample)

        return out