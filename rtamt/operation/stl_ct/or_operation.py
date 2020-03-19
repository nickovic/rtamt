from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl_ct.intersection as intersect

class OrOperation(AbstractOperation):
    def __init__(self):
        self.left = []
        self.right = []

    def update(self, *args, **kargs):
        out = []
        left_list = args[0]
        right_list = args[1]
        self.left = self.left + left_list
        self.right = self.right + right_list

        out, last = intersect.intersection(self.left, self.right, intersect.disjunction)

        return out

    def offline(self, *args, **kargs):
        out = []
        left_list = args[0]
        right_list = args[1]
        self.left = self.left + left_list
        self.right = self.right + right_list

        out, last = intersect.intersection(self.left, self.right, intersect.disjunction)

        if last:
            out.append(last)

        return out
