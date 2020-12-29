# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.node import Node

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
        self.add_child(child1)
        self.add_child(child2)

        self.name = '(' + child1.name + ')xor(' + child2.name + ')'