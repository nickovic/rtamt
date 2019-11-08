# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_combinatorial_binary_node import StlCombinatorialBinaryNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_xor_node import StlXorNode

class Xor(Node):
    """A class for storing STL Xor nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Xor node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Xor, self).__init__()
        self.addChild(child1)
        self.addChild(child2)
        self.node = StlXorNode()
