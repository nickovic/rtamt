
from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation

class VariableOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        self.val = None

    def update(self, *args, **kargs):
        return self.val

    def update_final(self, *args, **kargs):
        out = list()
        return
