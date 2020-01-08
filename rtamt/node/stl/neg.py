# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node
from rtamt.lib.rtamt_stl_library_wrapper.stl_not_node import StlNotNode
from rtamt.operation.stl.not_operation import NotOperation

class Neg(Node):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child, is_pure_python):
        """Constructor for Neg node

            Parameters:
                child : stl.Node
        """
        super(Neg, self).__init__()
        self.addChild(child)

        if is_pure_python:
            self.node = StlNotNode()
        else:
            self.node = NotOperation()


