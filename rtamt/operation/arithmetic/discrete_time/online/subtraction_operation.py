from rtamt.operation.abstract_discrete_time_online_operation import AbstractDiscreteTimeOnlineOperation


class SubtractionOperation(AbstractDiscreteTimeOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, node, sample_left, sample_right):
        sample_result = sample_left - sample_right
        return sample_result
