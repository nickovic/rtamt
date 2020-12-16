# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.unary_node import UnaryNode
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

        if is_pure_python:
            name = 'rtamt.operation.stl.always_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.AlwaysOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_always_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlAlwaysNode()




