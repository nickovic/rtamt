# -*- coding: utf-8 -*-
from abc import abstractmethod

from rtamt.operation.abstract_online_operation import AbstractOnlineOperation

class AbstractDenseTimeOnlineOperation(AbstractOnlineOperation):
    """
    Abstract Desne TimeOperation: template for online operation
    """

    @abstractmethod
    def update_final(self):
        raise NotImplementedError(self.NOT_IMPLEMENTED)
