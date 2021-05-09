from rtamt.semantics.discrete_time_offline_semanitcs import DiscreteTimeOfflineSemanitcs

class ConstantSemantics(DiscreteTimeOfflineSemanitcs):
    def __init__(self, val):
        self.val = val

    def reset(self):
        pass

    def update(self):
        return self.val
