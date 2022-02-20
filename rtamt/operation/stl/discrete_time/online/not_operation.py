from rtamt.operation.abstract_discrete_time_online_operation import AbstractDiscreteTimeOnlineOperation


class NotOperation(AbstractDiscreteTimeOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, node, sample):
        sample_return = - sample
        return sample_return
