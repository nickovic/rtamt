import math
from rtamt.operation.abstract_online_operation import AbstractOnlineOperation


class ExpOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        sample_result = math.exp(sample)
        return sample_result