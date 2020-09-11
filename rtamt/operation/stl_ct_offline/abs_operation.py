from rtamt.operation.abstract_operation import AbstractOperation

class AbsOperation(AbstractOperation):
    def __init__(self):
        pass

    def offline(self):
        out = []
        input_list = args[0]

        for in_sample in input_list:
            out_time = in_sample[0]
            out_value = abs(in_sample[1])

            out.append([out_time, out_value])

        return out