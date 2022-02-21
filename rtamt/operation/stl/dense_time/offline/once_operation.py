from rtamt.operation.abstract_operation import AbstractOperation


class OnceOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, *args, **kargs):
        out = []
        input_list = args[0]

        prev = -float("inf")

        for i, in_sample in enumerate(input_list):
            out_time = in_sample[0]
            out_value = max(in_sample[1], prev)
            if out_value != prev or i == len(input_list) - 1:
                out.append([out_time, out_value])
            prev = out_value

        return out
