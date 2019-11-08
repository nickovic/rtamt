# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""

from rtamt.node.stl.node import Node

class TemporalNode(Node):
    """A class for storing STL Temporal nodes
    Inherits Node

    Attributes
    --------------
    bound : Interval
        Interval of the form [a,b] where a,b : int and 0 <= a <= b

    Methods
    --------------
    bound
        Getter and setter for bound
    """

    def __init__(self, bound):
        """Constructor for TemporalNode

        Parameters:
            bound : Interval
                Temporal bound
        """
        super(TemporalNode, self).__init__()
        self.bound = bound

    @property
    def bound(self):
        """Getter for bound"""
        return self.__bound

    @bound.setter
    def bound(self, bound):
        """Setter for bound"""
        self.__bound = bound