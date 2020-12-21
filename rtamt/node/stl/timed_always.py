# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.unary_node import UnaryNode
from rtamt.node.stl.time_bound import TimeBound

class TimedAlways(UnaryNode, TimeBound):
    """A class for storing STL Always nodes
        Inherits TemporalNode
    """

    def __init__(self, child, begin, end, is_pure_python=True):
        """Constructor for Always

        Parameters:
            child : stl.Node
            bound : Interval
        """
        UnaryNode.__init__(self, child)
        TimeBound.__init__(self, begin, end)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'always[' + str(self.begin) + ',' + str(self.end) + '](' + child.name + ')'




