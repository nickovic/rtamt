# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta

class AbstractNode:
    """
    Abstract Node: tree-like data structure containing
    arbitrary specifications
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.children = list()
        self.evaluator = None

    def addChild(self, child):
        self.children.append(child)

    def accept(self, visitor):
        """accept: recursive function needed to implement node visitors
        Inputs:
        visitor - Visitor object
        """
        for child in self.children:
            child.accept(visitor)

    @property
    def evaluator(self):
        """Getter for the evaluator"""
        return self.__evaluator

    @evaluator.setter
    def evaluator(self, evaluator):
        """Setter for the evaluator"""
        self.__evaluator = evaluator

    def __repr__(self):
        '''Returns representation of the object'''
        return self.__class__.__name__
