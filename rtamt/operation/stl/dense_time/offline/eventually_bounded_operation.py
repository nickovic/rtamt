from rtamt.operation.abstract_operation import AbstractOperation
import rtamt.operation.stl.dense_time.online.intersection as intersect

class EventuallyBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.prev = []
        self.residual_start = -float("inf")
        self.max = - float("inf")
        self.begin = begin
        self.end = end

    def update(self, *args, **kargs):
        out = []
        input_list = args[0]
        ans = []
        self.prev = []
        self.residual_start = -float("inf")
        self.max = - float("inf")

        i = len(input_list) - 1
        begin = self.begin
        end = self.end

        domain_end = float('inf')
        if input_list:
            domain_end = input_list[len(input_list)-1][0]

        while i >= 0:
            if i > 0:
                b = (input_list[i - 1][0] - end, input_list[i][0] - begin, input_list[i - 1][1])
            else:
                b = (input_list[i][0] - end, input_list[i][0] - begin, input_list[i][1])

            if not out:
                out.insert(0, b)
            else:
                a = out[0]
                while (a[2] < b[2]) and (b[1] > a[1]):
                    out.pop(0)
                    a = out[0]
                if not intersect.intersects(a[0], a[1], b[0], b[1]):
                    out.insert(0, b)
                else:
                    if a[2] >= b[2]:
                        out.insert(0, (b[0], a[0], b[2]))
                    else:
                        out.pop(0)
                        if (a[1] > b[1]):
                            out.insert(0, (b[1], a[1], a[2]))
                        out.insert(0, (b[0], b[1], b[2]))

            i = i - 1

        for i, b in enumerate(out):
            if b[0] <= 0 and b[1] > 0:
                ans.append([0, b[2]])
            elif b[0] > 0:
                ans.append([b[0], b[2]])

            if i == len(out) - 1:
                ans.append([b[1], b[2]])

        return ans
