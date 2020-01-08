# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_subtraction_node import StlSubtractionNode
from rtamt.operation.arithmetic.subtraction_operation import SubtractionOperation

class Subtraction(Node):
    """A class for storing STL Subtraction nodes
        Inherits Node
    """
    def __init__(self, child1, child2, is_pure_python):
        """Constructor for Subtraction node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Subtraction, self).__init__()

        self.addChild(child1)
        self.addChild(child2)

        if is_pure_python:
            self.node = SubtractionOperation()
        else:
            self.node = StlSubtractionNode()

