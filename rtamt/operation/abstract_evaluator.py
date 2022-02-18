# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta

from rtamt.exception.exception import RTAMTException

class AbstractEvaluator(object):
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = ABCMeta
    NOT_IMPLEMENTED = "You should implement this."

    def ast_check(self):
        if self.ast is None:
            raise RTAMTException('ast is empty')
        return

    @property
    def ast(self):
        return self.__ast

    @ast.setter
    def ast(self, ast):
        self.__ast = ast
