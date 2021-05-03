from rtamt.operation.abstract_operation import AbstractOperation


class AbsOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample):
        out = abs(sample)

        return out