from rtamt.operation.abstract_operation import AbstractOperation


class HistoricallyOperation(AbstractOperation):
    def __init__(self):
        self.min = float("inf")

    def update(self, *args, **kargs):
        out = []
        input_list = args[0]

        for in_sample in input_list:
            out_time = in_sample[0]
            out_value = min(in_sample[1], self.min)
            self.min = out_value

            out.append((out_time, out_value))

        return out
