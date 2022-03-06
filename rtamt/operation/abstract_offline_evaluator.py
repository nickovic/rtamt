from abc import abstractmethod

from rtamt.operation.abstract_evaluator import AbstractEvaluator

class AbstractOfflineEvaluator(AbstractEvaluator):
    def __init__(self):
        super(AbstractOfflineEvaluator, self).__init__()
        return

    @abstractmethod
    def evaluate(self, dataset):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    def visitSpec(self, node, *args, **kwargs):
        sample_return = self.visit(node, *args, **kwargs)
        self.ast.var_object_dict[node] = sample_return  #TODO subspec name is necessary as a key for var_object_dict.
        return sample_return
