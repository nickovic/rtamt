from rtamt.operation.abstract_discrete_time_online_operation import AbstractDiscreteTimeOnlineOperation


class FallOperation(AbstractDiscreteTimeOnlineOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        self.__init__()

    def update(self, node, sample):
        sample_return = min(self.prev, - sample)
        self.prev = sample
        return sample_return
