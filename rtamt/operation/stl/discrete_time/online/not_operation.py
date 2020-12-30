from rtamt.operation.abstract_operation import AbstractOperation


class NotOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        out = - sample
        return out
