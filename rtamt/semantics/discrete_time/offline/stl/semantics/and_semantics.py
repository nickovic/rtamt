from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class AndSemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self):
        pass

    def reset(self):
        pass

    def evaluate(self, left, right):
        out = []

        for i in range(len(left)):
            out_sample = min(left[i], right[i])
            out.append(out_sample)

        return out
