# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_node import StlHistoricallyNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_bounded_node import StlHistoricallyBoundedNode

class Historically(TemporalNode):
    """A class for storing STL Historically nodes
         Inherits TemporalNode
    """
    def __init__(self, child, bound):
        """Constructor for Historically node

            Parameters:
                child : stl.Node
                bound : Interval
        """
        super(Historically, self).__init__(bound)
        self.addChild(child)

        if self.bound == None:
            self.node = StlHistoricallyNode()
        else :
            self.node = StlHistoricallyBoundedNode(bound.begin, bound.end)
