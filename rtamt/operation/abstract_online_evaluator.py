from abc import abstractmethod

from rtamt.operation.abstract_evaluator import AbstractEvaluator

class AbstractOnlineEvaluator(AbstractEvaluator):
    def __init__(self):
        super(AbstractOnlineEvaluator, self).__init__()
        return

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
