from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation
from sys import float_info

class ImpliesOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        if sample_left == 0: sample_left = float_info.max
        sample_return = max(-sample_left, sample_right)
        return sample_return
