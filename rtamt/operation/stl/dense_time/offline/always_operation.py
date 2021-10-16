from rtamt.operation.abstract_operation import AbstractOperation


class AlwaysOperation(AbstractOperation):
    def __init__(self):
        self.next = float("inf")

    def update(self, *args, **kargs):
        out = []
        self.next = float("inf")
        input_list = args[0]

        next = float("nan")

        for i, in_sample in reversed(list(enumerate(input_list))):
            out_time = in_sample[0]
            out_value = min(in_sample[1], self.next)
            self.next = out_value
            if out_value == next and i < len(input_list) - 2:
                out.pop(0)
            out.insert(0, [out_time, out_value])
            next = out_value

        return out
