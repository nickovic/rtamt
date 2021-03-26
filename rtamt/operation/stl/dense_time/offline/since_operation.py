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

    def update_since(self, *args, **kargs):
        out = []
        a = args[0]
        b = args[1]

        ans = []
        i = j = 1

        hi = None

        prev = -float("inf")
        while len(a) > 1 and len(b) > 1:
            a_start = a[i - 1][0]
            a_end = a[i][0]
            b_start = b[j - 1][0]
            b_end = b[j][0]

            a_val = a[i - 1][1]
            b_val = b[j - 1][1]

            a_val_next = a[i][1]
            b_val_next = b[j][1]

            if a_end < b_end:
                last_val = max(min(a_val_next, b_val), min(a_val_next, prev))
                del (a[i - 1])
            elif a_end > b_end:
                last_val = max(min(a_val, b_val_next), min(a_val, prev))
                del (b[j - 1])
            else:
                last_val = max(min(a_val_next, b_val_next), min(a_val_next, prev))
                del (a[i - 1])
                del (b[j - 1])

            lo = max(a_start, b_start)
            hi = min(a_end, b_end)

            val = float("nan")
            if lo < hi:
                val = max(min(a_val, b_val), min(a_val, prev))
                if val != prev:
                    out.append([lo, val])
                prev = val
                last = [hi, last_val]

        if out:
            out.append(last)

        return out

