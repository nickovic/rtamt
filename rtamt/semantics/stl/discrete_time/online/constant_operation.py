from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation

class ConstantOperation(AbstractOnlineOperation):
    def __init__(self, val):
        self.val = val

    def reset(self):
        self.__init__()

    def update(self):
        return self.val
