# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from rtamt.semantics.abstract_operation import AbstractOperation

NOT_IMPLEMENTED = "You should implement this."

class OnlineOperation(AbstractOperation):
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: so far it does nothing. we need to think what we need to do here.

    __metaclass__ = ABCMeta

    def __init__(self):
        super(OnlineOperation, self).__init__()

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def reset(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)