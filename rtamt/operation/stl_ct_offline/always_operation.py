from rtamt.operation.abstract_operation import AbstractOperation
import numpy

class AlwaysOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, *args, **kargs):
        pass

    def offline(self, *args, **kargs):
        out = []
        input_list = args[0]

        i=0
        while i < len(input_list):
            temp_nums = [ i[1] for i in input_list[i:len(input_list)] ]
            temp_min = min(temp_nums)
            min_indexs = [i for i, x in enumerate(temp_nums) if x == temp_min]
            out.append([input_list[i][0], temp_min])

            if min_indexs[-1] == 0:
                i = i + 1
            elif i+min_indexs[-1] == len(input_list)-1:
                out.append([input_list[-1][0], temp_min])
                break
            else:
                i = i+min_indexs[-1]+1

        return out