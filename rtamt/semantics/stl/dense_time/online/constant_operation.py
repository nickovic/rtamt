
from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation

class ConstantOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self, val):
        self.val = val
        self.is_first_sample = True

    def update(self, *args, **kargs):
        if self.is_first_sample:
            out = [[0, self.val], [float("inf"), self.val]]
        else:
            out = list()
        return out

    def update_final(self, *args, **kargs):
        out = list()
        return
