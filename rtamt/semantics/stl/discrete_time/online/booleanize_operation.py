from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation

class BooleanizeOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        out = sample*float('inf')
        return out
