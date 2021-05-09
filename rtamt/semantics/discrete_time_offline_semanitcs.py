# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from rtamt.semantics.dense_time.dense_time_semantics import DenseTimeSemantics
from rtamt.semantics.offline_evaluator import OfflineEvaluator

NOT_IMPLEMENTED = "You should implement this."

class DiscreteTimeOfflineSemanitcs(DenseTimeSemantics, OfflineEvaluator):
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: impliment DiscreteTime sepsific evaluate, reset

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def reset(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)
