# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_division_node import StlDivisionNode

class Division(Node):
    """A class for storing STL Division nodes
        Inherits Node
    """
    def __init__(self, child1, child2):
        """Constructor for Division node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
        """
        super(Division, self).__init__()

        self.addChild(child1)
        self.addChild(child2)

        self.node = StlDivisionNode()

