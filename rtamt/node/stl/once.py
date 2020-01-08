# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_node import StlOnceNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_once_bounded_node import StlOnceBoundedNode
from rtamt.operation.stl.once_operation import OnceOperation
from rtamt.operation.stl.once_bounded_operation import OnceBoundedOperation

class Once(TemporalNode):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child, bound, is_pure_python):
        """Constructor for Once node

        Parameters:
            child : stl.Node
            bound : Interval
        """

        super(Once, self).__init__(bound)
        self.addChild(child)

        if is_pure_python:
            if bound == None:
                self.node = OnceOperation()
            else:
                self.node = OnceBoundedOperation(int(bound.begin), int(bound.end))
        else:
            if bound == None:
                self.node = StlOnceNode()
            else:
                self.node = StlOnceBoundedNode(int(bound.begin), int(bound.end))


