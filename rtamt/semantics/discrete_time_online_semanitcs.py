# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from rtamt.semantics.dense_time.dense_time_semantics import DenseTimeSemantics
from rtamt.semantics.online_evaluator import OnlineEvaluator

NOT_IMPLEMENTED = "You should implement this."

class DiscreteTimeOnlineSemanitcs(DenseTimeSemantics, OnlineEvaluator):
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: impliment DiscreteTime sepsific evaluate, reset

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def reset(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)
