# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.temporal_node import TemporalNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_always_node import StlAlwaysNode
from rtamt.operation.stl.always_operation import AlwaysOperation


class Always(TemporalNode):
    """A class for storing STL Always nodes
        Inherits TemporalNode
    """

    def __init__(self, child, bound, is_pure_python):
        """Constructor for Always

        Parameters:
            child : stl.Node
            bound : Interval
        """
        super(Always, self).__init__(bound)
        self.addChild(child)

        if is_pure_python:
            self.node = AlwaysOperation()
        else:
            self.node = StlAlwaysNode()




