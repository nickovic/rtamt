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
        # get inputs
        input_list = args[0]
        ans = []
        out = self.prev
        self.prev = []

        begin = self.begin
        end = self.end

        if input_list:
            # update when the residuals start in this iteration
            self.residual_start = input_list[len(input_list) - 1][0] + begin
            if out:
                # update the last previous sample with current knowledge
                last_prev = out[len(out) - 1]
                first_now = input_list[0]
                del (out[len(out) - 1])
                out.append((last_prev[0], first_now[0] + end, last_prev[2]))

        i = 1
        while len(input_list) >= i:
            if i == len(input_list):
                b = (input_list[i - 1][0] + begin, input_list[i - 1][0] + end, input_list[i - 1][1])
            else:
                b = (input_list[i - 1][0] + begin, input_list[i][0] + end, input_list[i - 1][1])

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
                        out.append((a[0], b[0], a[2]))
                        out.append((b[0], b[1], b[2]))
            i = i + 1

        prev = float("nan")

        for i, b in enumerate(out):
            if b[1] <= self.residual_start:
                if b[2] != prev or i == len(out) - 1:
                    ans.append([b[0], b[2]])
            elif b[0] < self.residual_start < b[1]:
                if b[2] != prev or i == len(out) - 1:
                    ans.append([b[0], b[2]])
                self.prev.append((self.residual_start, b[1], b[2]))
            else:
                self.prev.append(b)

            prev = b[2]

        return ans

    def update_final(self, *args, **kargs):
        ans = []

        ans = self.update(args[0])

        out = self.prev

        for i, b in enumerate(out):
            ans.append([b[0], b[2]])
        return ans

    # def offline(self, *args, **kargs):
    #     out = []
    #     input_list = args[0]
    #     ans = []
    #
    #     i = 1
    #     begin = self.begin
    #     end = self.end
    #
    #     while i < len(input_list):
    #         b = (input_list[i - 1][0] + begin, input_list[i][0] + end, input_list[i - 1][1])
    #         last = (input_list[i][0] + end, input_list[i][0] + end, input_list[i][1])
    #
    #         if not out:
    #             out.append(b)
    #         else:
    #             a = out[len(out) - 1]
    #             while (a[2] > b[2]) and (b[0] <= a[0]):
    #                 del (out[len(out) - 1])
    #                 a = out[len(out) - 1]
    #             if not intersect.intersects(a[0], a[1], b[0], b[1]):
    #                 out.append(b)
    #             else:
    #                 if a[2] <= b[2]:
    #                     out.append((a[1], b[1], b[2]))
    #                 else:
    #                     del (out[len(out) - 1])
    #                     out.append((a[0], b[0], a[2]))
    #                     out.append((b[0], b[1], b[2]))
    #         if i == len(input_list) - 1:
    #             out.append(last)
    #         i = i + 1
    #
    #     prev = float("nan")
    #     for i, b in enumerate(out):
    #         if b[2] != prev or i == len(out) - 1:
    #             ans.append([b[0], b[2]])
    #         prev = b[2]
    #
    #     return ans
