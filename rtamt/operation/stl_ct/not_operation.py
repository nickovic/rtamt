from rtamt.operation.abstract_operation import AbstractOperation

class NotOperation(AbstractOperation):
    def __init__(self):
        self.input = []
    #  function update
    #  takes as input a list of [timestamp, value] pairs
    #  returns as output a list of [timestamp, value] pairs
    #
    # Example:
    # out = update(in)
    # in - [[4.2, 2.13], [5.7, -3.12], [6.88, 4.55]]
    # out - [[4.2, -2.13], [5.7, 3.12], [6.88, -4.55]]
    def update(self, *args, **kargs):
        out = []
        input_list = args[0]

        for in_sample in input_list:
            out_time = in_sample[0]
            out_value = - in_sample[1]

            out.append([out_time, out_value])

        return out

    def update_final(self, *args, **kargs):
        return self.update(args[0])

    def offline(self, *args, **kargs):
        out = []
        input_list = args[0]

        for in_sample in input_list:
            out_time = in_sample[0]
            out_value = - in_sample[1]

            out.append([out_time, out_value])

        return out
