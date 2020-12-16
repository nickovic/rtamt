from rtamt.operation.abstract_operation import AbstractOperation


class ConstantOperation(AbstractOperation):
    def __init__(self, val):
        self.val = val

    def reset(self):
        pass

    def update(self):
        return self.val
