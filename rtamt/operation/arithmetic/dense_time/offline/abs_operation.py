from rtamt.operation.abstract_operation import AbstractOperation

class AbsOperation(AbstractOperation):
    def __init__(self):
        self.input = []

    def update(self, input_list):
        out = []

        for in_sample in input_list:
            out_time = in_sample[0]
            out_value = abs(in_sample[1])
            out.append([out_time, out_value])

        return out
