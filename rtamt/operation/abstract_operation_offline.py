# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abstract_operation_online import AbstractOperationOnline

NOT_IMPLEMENTED = "You should implement this."

class AbstractOperationOffline:
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = from abstract_operation_online import AbstractOperationOnline

    def __init__(self):
        pass

    @abstractmethod
    def eval(self, *args, **kargs):
        update(self, *args, **kargs):


