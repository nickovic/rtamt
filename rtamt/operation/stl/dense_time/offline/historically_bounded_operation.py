from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl.dense_time.online.intersection as intersect

class HistoricallyBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.prev = []
        self.residual_start = float("inf")
        self.max = float("inf")
        self.begin = begin
        self.end = end

    def update(self, *args, **kargs):
        out = []
        input_list = args[0]
        ans = []
        self.prev = []
        self.residual_start = float("inf")
        self.max = float("inf")

        i = 1
        begin = self.begin
        end = self.end

        domain_end = float('inf')
        if input_list:
            domain_end = input_list[len(input_list)-1][0]

        while i <= len(input_list):
            if i == 1 and begin > 0:
                out.append((0, input_list[0][0] + begin, float('inf')))

            if i < len(input_list):
                b = (input_list[i - 1][0] + begin, input_list[i][0] + end, input_list[i - 1][1])
            else:
                b = (input_list[i-1][0] + begin, input_list[i-1][0] + end, input_list[i-1][1])

            if not out:
                out.append(b)
            else:
                a = out[len(out) - 1]
                while (a[2] > b[2]) and (b[0] < a[0]):
                    del (out[len(out) - 1])
                    a = out[len(out) - 1]
                if not intersect.intersects(a[0], a[1], b[0], b[1]):
                    out.append(b)
                else:
                    if a[2] <= b[2]:
                        out.append((a[1], b[1], b[2]))
                    else:
                        del (out[len(out) - 1])
                        if b[0] > a[0]:
                            out.append((a[0], b[0], a[2]))
                        out.append((b[0], b[1], b[2]))

            i = i + 1

        prev = float("nan")

        for i, b in enumerate(out):
            if b[2] != prev or i == len(out) - 1:
                ans.append([b[0], b[2]])

            if b[0] <= domain_end < b[1]:
                if b[0] < domain_end:
                    ans.append([domain_end, b[2]])
                break

            if i == len(out) - 1 and b[1] > b[0]:
                ans.append([b[1], b[2]])

            prev = b[2]

        return ans