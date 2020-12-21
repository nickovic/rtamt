from rtamt.operation.abstract_operation import AbstractOperation


class DivisionOperation(AbstractOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, left, right):
        out = left / right
        return out