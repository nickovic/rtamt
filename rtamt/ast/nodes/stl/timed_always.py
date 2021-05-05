# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.ast.nodes.unary_node import UnaryNode
from rtamt.ast.nodes.time_bound import TimeBound

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

        self.name = 'always[' + str(self.begin) + ',' + str(self.end) + '](' + child.name + ')'
