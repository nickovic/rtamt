import math
from rtamt.operation.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation

class ExpOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, node, sample, *args, **kargs):
        sample_result = []

        for i in sample:
            out_time = i[0]
            out_value = math.exp(i[1])
            sample_result.append([out_time, out_value])

        return sample_result

    def update_final(self, node, sample, *args, **kargs):
        return self.update(node, sample, *args, **kargs)