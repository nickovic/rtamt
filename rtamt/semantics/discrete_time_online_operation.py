# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from rtamt.semantics.discrete_time_operation import DiscreteTimeOperation
from rtamt.semantics.online_operation import OnlineOperation

NOT_IMPLEMENTED = "You should implement this."

class DiscreteTimeOnlineOperation(DiscreteTimeOperation, OnlineOperation):
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: impliment DiscreteTime sepsific evaluate, reset

    __metaclass__ = ABCMeta

    def __init__(self):
        pass
