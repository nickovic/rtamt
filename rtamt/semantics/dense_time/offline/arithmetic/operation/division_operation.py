from rtamt.semantics.abstract_operation import AbstractOperation
import rtamt.semantics.dense_time.offline.stl.operation.intersection as intersect

class DivisionOperation(AbstractOperation):
    def __init__(self):
        self.left = []
        self.right = []

    def update(self, left_list, right_list):
        self.left = self.left + left_list
        self.right = self.right + right_list

        out, last, left, right = intersect.intersection(self.left, self.right, intersect.division)
        if last:
            out.append(last)

        return out
