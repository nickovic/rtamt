# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_precedes_bounded_node import StlPrecedesBoundedNode



class Precedes(TemporalNode):
    """A class for storing STL Precedes nodes - an auxilliary operator need for translating
       bounded future STL formulas to pure past formulas
                Inherits TemporalNode
    """

    def __init__(self, child1, child2, bound):
        """Constructor for Precedes node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
            bound : Interval
        """
        super(Precedes, self).__init__(bound)
        self.addChild(child1)
        self.addChild(child2)
        self.node = StlPrecedesBoundedNode(bound.begin, bound.end)
