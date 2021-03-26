from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl.dense_time.offline.intersection as intersect

class MultiplicationOperation(AbstractOperation):
    def __init__(self):
        self.left = []
        self.right = []

    def update(self, left_list, right_list):
        self.left = self.left + left_list
        self.right = self.right + right_list

        out, last, left, right = intersect.intersection(self.left, self.right, intersect.multiplication)
        if last:
            out.append(last)

        return out
