from rtamt.operation.abstract_operation import AbstractOperation


class NotOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, samples):

        out = [ -sample for sample in samples]

        return out
