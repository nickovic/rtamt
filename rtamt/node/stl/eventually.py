# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.temporal_node import TemporalNode




class Eventually(TemporalNode):
    """A class for storing STL Eventually nodes
            Inherits TemporalNode
    """
    def __init__(self, child, bound):
        """Constructor for Eventually node

        Parameters:
            child : stl.Node
            bound : Interval
        """
        super(Eventually, self).__init__(bound)
        self.addChild(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.bound = bound
