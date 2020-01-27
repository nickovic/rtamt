# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class AbstractOperation:
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)


