from rtamt.operation.abstract_operation import AbstractOperation

class NotOperation(AbstractOperation):
    def update(self, *args, **kargs):
        out = []
        input_list = args[0]

        for in_sample in input_list:
            out_time = in_sample[0]
            out_value = - in_sample[1]

            out.append([out_time, out_value])

        return out
