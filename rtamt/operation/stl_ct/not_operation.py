from rtamt.operation.abstract_operation import AbstractOperation

class NotOperation(AbstractOperation):
    def __init__(self):
        self.input = []

    def update(self, *args, **kargs):
        out = []
        input_list = args[0]

        for in_sample in input_list:
            self.input.append(in_sample)

        for in_sample in self.input:
            out_time = in_sample[0]
            out_value = - in_sample[1]
            self.input.remove(in_sample)

            out.append((out_time, out_value))

        return out
