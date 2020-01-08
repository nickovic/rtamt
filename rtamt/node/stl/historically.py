# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_node import StlHistoricallyNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_historically_bounded_node import StlHistoricallyBoundedNode
from rtamt.operation.stl.historically_operation import HistoricallyOperation
from rtamt.operation.stl.historically_bounded_operation import HistoricallyBoundedOperation

class Historically(TemporalNode):
    """A class for storing STL Historically nodes
         Inherits TemporalNode
    """
    def __init__(self, child, bound, is_pure_python):
        """Constructor for Historically node

            Parameters:
                child : stl.Node
                bound : Interval
        """
        super(Historically, self).__init__(bound)
        self.addChild(child)

        if is_pure_python:
            if self.bound == None:
                self.node = HistoricallyOperation()
            else:
                self.node = HistoricallyBoundedOperation(bound.begin, bound.end)
        else:
            if self.bound == None:
                self.node = StlHistoricallyNode()
            else :
                self.node = StlHistoricallyBoundedNode(bound.begin, bound.end)
