import math
from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation


class NegateOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        sample_result = - sample
        return sample_result