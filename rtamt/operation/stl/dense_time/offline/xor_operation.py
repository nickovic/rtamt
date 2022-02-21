from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl.dense_time.online.intersection as intersect

class XorOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, *args, **kargs):
        left_list = args[0]
        right_list = args[1]

        out, last, left, right = intersect.intersection(left_list, right_list, intersect.xor)

        if last:
            out.append(last)

        return out
