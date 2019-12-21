# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta

class AbstractOperation:
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def update(self):