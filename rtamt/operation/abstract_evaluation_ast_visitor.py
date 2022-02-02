# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta, abstractmethod

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor

class AbstractEvluationAstVisitor(AbstractAstVisitor):
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        #TODO we may impliment something in here, otherwise it is just inheriting AbstractAstVisitor.
        pass
