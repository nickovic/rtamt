from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl.dense_time.offline.intersection as intersect

class AndOperation(AbstractOperation):
    def update(self, *args, **kargs):
        left_list = args[0]
        right_list = args[1]

        out, last, a, b = intersect.intersection(left_list, right_list, intersect.conjunction)
        if last:
            out.append(last)

        return out
