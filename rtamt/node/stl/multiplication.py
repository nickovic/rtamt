# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node
from rtamt.lib.rtamt_stl_library_wrapper.stl_multiplication_node import StlMultiplicationNode
from rtamt.operation.arithmetic.multiplication_operation import MultiplicationOperation

class Multiplication(Node):
    """A class for storing STL Multiplication nodes
        Inherits Node
    """
    def __init__(self, child1, child2, is_pure_python):
        """Constructor for Multiplication node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Multiplication, self).__init__()

        self.addChild(child1)
        self.addChild(child2)

        if is_pure_python:
            self.node = MultiplicationOperation()
        else:
            self.node = StlMultiplicationNode()

