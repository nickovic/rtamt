# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from rtamt.semantics.discrete_time_semantics import DiscreteTimeSemantics
from rtamt.semantics.online_evaluator import OnlineEvaluator

NOT_IMPLEMENTED = "You should implement this."

class DiscreteTimeOnlineSemanitcs(DiscreteTimeSemantics, OnlineEvaluator):
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: impliment DiscreteTime sepsific evaluate, reset

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

