from rtamt.operation.abstract_operation import AbstractOperation


class HistoricallyOperation(AbstractOperation):
    def __init__(self):
        self.min = float("inf")

    def update(self, *args, **kargs):
        out = []
        input_list = args[0]

        prev = float("nan")


        for in_sample in input_list:
            out_time = in_sample[0]
            out_value = min(in_sample[1], self.min)
            self.min = out_value
            if out_value != prev:
                out.append([out_time, out_value])
            prev = out_value

        return out

    def offline(self, *args, **kargs):
        out = []
        input_list = args[0]

        prev = float("nan")


        for i, in_sample in enumerate(input_list):
            out_time = in_sample[0]
            out_value = min(in_sample[1], self.min)
            self.min = out_value
            if out_value != prev or i == len(input_list) - 1:
                out.append([out_time, out_value])
            prev = out_value

        return out
