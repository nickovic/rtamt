# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class AbstractOnlineOperation:
    """
    Abstract Operation: template for online operation
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def reset(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)
