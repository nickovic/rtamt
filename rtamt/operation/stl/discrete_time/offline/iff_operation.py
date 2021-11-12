from rtamt.operation.abstract_operation import AbstractOperation


class IffOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, left, right):

        out = [-abs(l-r) for l,r in zip(left,right)]

        return out