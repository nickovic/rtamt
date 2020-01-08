# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_abs_node import StlAbsNode
from rtamt.operation.arithmetic.abs_operation import AbsOperation

class Abs(Node):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child, is_pure_python):
        """Constructor for Neg node

            Parameters:
                child : stl.Node
        """
        super(Abs, self).__init__()
        self.addChild(child)

        if is_pure_python:
            self.node = AbsOperation()
        else:
            self.node = StlAbsNode()



