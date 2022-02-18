from abc import abstractmethod

from rtamt.operation.abstract_evaluator import AbstractEvaluator

class AbstractOfflineEvaluator(AbstractEvaluator):
    def __init__(self):
        super(AbstractOfflineEvaluator, self).__init__()
        return

    @abstractmethod
    def evaluate(self, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
