from rtamt.operation.abstract_operation import AbstractOperation


class HistoricallyOperation(AbstractOperation):
    def __init__(self):
        self.prev = float("inf")

    def update(self, *args, **kargs):
        out = []
        input_list = args[0]

        for in_sample in input_list:
            out_time = in_sample[0]
            out_value = min(in_sample[1], self.prev)

            out.append([out_time, out_value])
            self.prev = out_value

        return out

    def update_final(self, *args, **kargs):
        return self.update(args[0])

    # def offline(self, *args, **kargs):
    #     out = []
    #     input_list = args[0]
    #
    #     prev = float("nan")
    #
    #
    #     for i, in_sample in enumerate(input_list):
    #         out_time = in_sample[0]
    #         out_value = min(in_sample[1], self.prev)
    #         self.prev = out_value
    #         if out_value != prev or i == len(input_list) - 1:
    #             out.append([out_time, out_value])
    #         prev = out_value
    #
    #     return out
