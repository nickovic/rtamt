# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from rtamt.node.abstract_node import AbstractNode


class Node(AbstractNode):
    """A class for storing STL nodes
    Inherits AbstractNode

    Attributes
    --------------
    horizon : int
        integer denoting how much in the future the underlying formula must look

    Methods
    --------------
    horizon
        Getter and setter for horizon
    """

    def __init__(self):
        """Constructor for Node"""
        super(Node, self).__init__()
        self.horizon = 0;

    @property
    def horizon(self):
        """Getter for the horizon"""
        return self.__horizon

    @horizon.setter
    def horizon(self, horizon):
        """Setter for the horizon"""
        self.__horizon = horizon