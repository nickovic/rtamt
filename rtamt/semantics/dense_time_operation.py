# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from rtamt.semantics.abstract_time_operation import AbstractTimeOperation

NOT_IMPLEMENTED = "You should implement this."

class DenseTimeOperation(AbstractTimeOperation):
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: standarize time trajectory data structure for Dense time in here.

    __metaclass__ = ABCMeta

    def __init__(self):
        pass
