# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_node import StlOnceNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_bounded_node import StlOnceBoundedNode

class Once(TemporalNode):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child, bound):
        """Constructor for Once node

        Parameters:
            child : stl.Node
            bound : Interval
        """

        super(Once, self).__init__(bound)
        self.addChild(child)

        if bound == None:
            self.node = StlOnceNode()
        else:
            self.node = StlOnceBoundedNode(int(bound.begin), int(bound.end))


