from rtamt.operation.abstract_operation import AbstractOperation

class SinceOperation(AbstractOperation):
    def __init__(self):
        self.left = []
        self.right = []
        self.prev = -float("inf")
        self.last = []

    def update(self, *args, **kargs):
        out = []
        a = self.left + args[0]
        b = self.right + args[1]

        i = j = 1

        last = self.last

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
                last_val = max(min(a_val_next, b_val), min(a_val_next, self.prev))
                del (a[i - 1])
            elif a_end > b_end:
                last_val = max(min(a_val, b_val_next), min(a_val, self.prev))
                del (b[j - 1])
            else:
                last_val = max(min(a_val_next, b_val_next), min(a_val_next, self.prev))
                del (a[i - 1])
                del (b[j - 1])

            lo = max(a_start, b_start)
            hi = min(a_end, b_end)

            val = float("nan")
            if lo < hi:
                val = max(min(a_val, b_val), min(a_val, self.prev))
                #if not (self.last == [lo, val]):
                out.append([lo, val])
                self.prev = val
                last = [hi, last_val]

        self.left = a
        self.right = b
        self.last = last

        return out

    def update_final(self, *args, **kargs):
        return self.update(args[0], args[1]) + [self.last]
    #
    # def offline(self, *args, **kargs):
    #     out = []
    #     a = args[0]
    #     b = args[1]
    #
    #     ans = []
    #     i = j = 1
    #
    #     hi = None
    #
    #     prev = -float("inf")
    #     while len(a) > 1 and len(b) > 1:
    #         a_start = a[i - 1][0]
    #         a_end = a[i][0]
    #         b_start = b[j - 1][0]
    #         b_end = b[j][0]
    #
    #         a_val = a[i - 1][1]
    #         b_val = b[j - 1][1]
    #
    #         a_val_next = a[i][1]
    #         b_val_next = b[j][1]
    #
    #         if a_end < b_end:
    #             last_val = max(min(a_val_next, b_val), min(a_val_next, prev))
    #             del (a[i - 1])
    #         elif a_end > b_end:
    #             last_val = max(min(a_val, b_val_next), min(a_val, prev))
    #             del (b[j - 1])
    #         else:
    #             last_val = max(min(a_val_next, b_val_next), min(a_val_next, prev))
    #             del (a[i - 1])
    #             del (b[j - 1])
    #
    #         lo = max(a_start, b_start)
    #         hi = min(a_end, b_end)
    #
    #         val = float("nan")
    #         if lo < hi:
    #             val = max(min(a_val, b_val), min(a_val, prev))
    #             if val != prev:
    #                 out.append([lo, val])
    #             prev = val
    #             last = [hi, last_val]
    #
    #     if out:
    #         out.append(last)
    #
    #
    #     return out

