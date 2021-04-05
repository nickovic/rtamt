from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl.dense_time.offline.intersection as intersect

class SinceOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, *args, **kargs):
        left_list = args[0]
        right_list = args[1]

        iout, last, a, b = intersect.intersection(left_list, right_list, intersect.split)
        if last:
            iout.append(last)

        out = []
        prev = -float("inf")
        for i, sample in enumerate(iout):
            t = sample[0]
            o1_val = sample[1][0]
            o2_val = sample[1][1]
            result = max(min(o1_val, o2_val), min(o1_val, prev))
            if result != prev or i == len(iout) - 1:
                out.append([t, result])
            prev = result

        return out
