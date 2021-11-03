from rtamt.operation.abstract_operation import AbstractOperation

class AndOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, left, right):

        out = list(map(min, zip(left,right)))

        return out
