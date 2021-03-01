from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl.dense_time.online.intersection as intersect

class AndOperation(AbstractOperation):
    def __init__(self):
        self.left = []
        self.right = []
        self.last = []

    def update(self, *args, **kargs):
        out = []
        left_list = self.left + args[0]
        right_list = self.right + args[1]

        out, last, left, right = intersect.intersection(left_list, right_list, intersect.conjunction)

        self.left = left
        self.right = right
        if out:
            self.last = last

        return out

    def update_final(self, *args, **kargs):
        return self.update(args[0], args[1]) + [self.last]
    #
    # def offline(self, *args, **kargs):
    #     out = []
    #     left_list = args[0]
    #     right_list = args[1]
    #
    #     out, last, a, b = intersect.intersection(left_list, right_list, intersect.conjunction)
    #     if last:
    #         out.append(last)
    #
    #     return out
