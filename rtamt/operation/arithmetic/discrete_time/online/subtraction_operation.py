from rtamt.operation.abstract_online_operation import AbstractOnlineOperation


class SubtractionOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        pass

    def update(self, sample_left, sample_right):
        sample_result = sample_left - sample_right
        return sample_result
