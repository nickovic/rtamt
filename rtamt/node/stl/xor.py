# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node

class Xor(Node):
    """A class for storing STL Xor nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2, is_pure_python=True):
        """Constructor for Xor node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Xor, self).__init__()
        self.addChild(child1)
        self.addChild(child2)

        self.name = '(' + child1.name + ')xor(' + child2.name + ')'