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
        self.horizon = 0 #TODO: Tom thinks horizon needs only timed autokmaton.
        self.name = ''
        self.node = None

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
    def evaluator(self): #TODO: Tom thinks perhaps we can separete evaluator or operator.
        """Getter for the online_evaluator"""
        return self.__evaluator

    @evaluator.setter
    def evaluator(self, evaluator): #TODO: Tom thinks perhaps we can separete evaluator or operator.
        """Setter for the online_evaluator"""
        self.__evaluator = evaluator

    @property
    def name(self):
        """Getter for the name"""
        return self.__name

    @name.setter
    def name(self, name):
        """Setter for the name"""
        self.__name = name

    @property
    def horizon(self): #TODO: Tom thinks perhaps we can separete horizon. it needs only timed operator.
        """Getter for the horizon"""
        return self.__horizon

    @horizon.setter
    def horizon(self, horizon): #TODO: Tom thinks perhaps we can separete horizon. it needs only timed operator.
        """Setter for the horizon"""
        self.__horizon = horizon

    @property
    def node(self):
        """Getter for the node"""
        return self.__node

    @node.setter
    def node(self, node):
        """Setter for the horizon"""
        self.__node = node

    def __repr__(self):
        '''Returns representation of the object'''
        return self.__class__.__name__
