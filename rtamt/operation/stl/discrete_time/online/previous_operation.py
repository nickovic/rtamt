from rtamt.operation.abstract_online_operation import AbstractOnlineOperation


class PreviousOperation(AbstractOnlineOperation):
    def __init__(self):
        self.prev = float("inf")

    def reset(self):
        self.prev = float("inf")

    def update(self, node, sample):
        sample_return = self.prev
        self.prev = sample

        return sample_return
