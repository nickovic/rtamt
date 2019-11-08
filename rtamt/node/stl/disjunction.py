# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_combinatorial_binary_node import StlCombinatorialBinaryNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_or_node import StlOrNode

class Disjunction(Node):
    """A class for storing STL Or nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Or node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Disjunction, self).__init__()
        self.addChild(child1)
        self.addChild(child2)
        self.node = StlOrNode()


