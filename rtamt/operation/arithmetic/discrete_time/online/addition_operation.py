from rtamt.operation.abstract_operation import AbstractOperation


class AdditionOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, left, right):
        out = left + right
        return out
