from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation

class VariableOperation(AbstractOnlineOperation):
    def __init__(self):
        self.sample = None

    def reset(self):
        self.__init__()

    def update(self):
        return self.sample
