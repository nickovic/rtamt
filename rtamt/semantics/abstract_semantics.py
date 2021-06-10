# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class AbstractSemantics:
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: so far it does nothing. we need to think what we need to do here.

    __metaclass__ = ABCMeta

    def __init__(self):
        pass
