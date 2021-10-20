from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl.dense_time.online.intersection as intersect

class XorOperation(AbstractOperation):
    def __init__(self):
        self.left = []
        self.right = []
        self.last = []

    def update(self, *args, **kargs):
        left_list = args[0]
        right_list = args[1]
        self.left = []
        self.right = []
        self.last = []

        self.left = self.left + left_list
        self.right = self.right + right_list

        out, last, left, right = intersect.intersection(self.left, self.right, intersect.xor)

        if last:
            out.append(last)

        return out
