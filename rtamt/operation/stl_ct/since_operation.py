from rtamt.operation.abstract_operation import AbstractOperation

class SinceOperation(AbstractOperation):
    def __init__(self):
        self.left = []
        self.right = []

    def update(self, *args, **kargs):
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

            lo = max(a_start, b_start)
            hi = min(a_end, b_end)

            val = float("nan")
            if lo < hi:
                val = max(min(a_val, b_val), min(a_val, prev))
                if val != prev:
                    out.append([lo, val])
                prev = val

            if a_end < b_end:
                del (a[i - 1])
            elif a_end > b_end:
                del (b[j - 1])
            else:
                del (a[i - 1])
                del (b[j - 1])

        return out

