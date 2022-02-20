# -*- coding: utf-8 -*-
from abc import abstractmethod

from rtamt.operation.abstract_online_operation import AbstractOnlineOperation


class AbstractDiscreteTimeOnlineOperation(AbstractOnlineOperation):
    """
    Abstract Discrete Operation: template for online operation
    """

    @abstractmethod
    def reset(self):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
