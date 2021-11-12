from rtamt.operation.abstract_operation import AbstractOperation
# import numpy as np

class XorOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, left, right):

        out = [abs(l-r) for l,r in zip(left,right)]

        return out
