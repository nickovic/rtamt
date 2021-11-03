from rtamt.operation.abstract_operation import AbstractOperation


class ImpliesOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, left, right):

        out = [max(-l,r) for l,r in zip(left,right)]

        return out
