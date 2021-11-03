from rtamt.operation.abstract_operation import AbstractOperation

class OrOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, left, right):

        out = list(map(max, zip(left,right)))

        return out
