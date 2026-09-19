from rtamt.semantics.abstract_dense_time_online_operation import AbstractDenseTimeOnlineOperation
import math


class LnOperation(AbstractDenseTimeOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample, *args, **kargs):
        sample_result = []

        for in_sample in sample:
            out_time = in_sample[0]
            out_value = math.log(in_sample[1])
            sample_result.append([out_time, out_value])

        return sample_result

    def update_final(self, sample, *args, **kargs):
        return self.update(sample, *args, **kargs)
