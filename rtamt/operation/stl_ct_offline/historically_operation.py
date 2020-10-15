from rtamt.operation.abstract_operation import AbstractOperation
import numpy

class HistoricallyOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, *args, **kargs):
        pass

    def offline(self, *args, **kargs):
        out = []
        input_list = args[0]

        i=0
        temp_max=0
        while i < len(input_list):
            temp_nums = [ i[1] for i in input_list[i:len(input_list)] ]
            temp_max = max(temp_nums)
            max_indexs = [i for i, x in enumerate(temp_nums) if x == temp_max]
            out.append([input_list[i][0], temp_max])

            if max_indexs[-1] == 0:
                i = i + 1
            elif i+max_indexs[-1] == len(input_list)-1:
                out.append([input_list[-1][0], temp_max])
                break
            else:
                i = i+max_indexs[-1]+1

        return out