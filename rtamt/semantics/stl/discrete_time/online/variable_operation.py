from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation

class VariableOperation(AbstractOnlineOperation):
    def __init__(self):
        self.sample = None

    def reset(self):
        pass

    def update(self):
        return self.sample
