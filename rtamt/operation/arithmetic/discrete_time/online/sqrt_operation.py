import math
from rtamt.operation.abstract_discrete_time_online_operation import AbstractDiscreteTimeOnlineOperation


class SqrtOperation(AbstractDiscreteTimeOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, node, sample):
        if sample < 0:
            raise Exception('sqrt: input is smaller than 0.')
        sample_result = math.sqrt(sample)
        return sample_result