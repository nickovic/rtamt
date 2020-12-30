from rtamt.operation.abstract_operation import AbstractOperation

class XorOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, left, right):
        out = abs(left - right)
        return out
