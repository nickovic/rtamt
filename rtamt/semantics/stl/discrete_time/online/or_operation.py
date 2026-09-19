from rtamt.semantics.abstract_online_operation import AbstractOnlineOperation
class OrOperation(AbstractOnlineOperation):
    def __init__(self):
        pass

    def reset(self):
        self.__init__()

    def update(self, sample_left, sample_right):
        sample_return = max(sample_left, sample_right)
        return sample_return
