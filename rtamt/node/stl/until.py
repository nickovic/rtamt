# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode



class Until(TemporalNode):
    """
    A class for storing STL Since nodes
    Inherits TemporalNode
    """
    def __init__(self, child1, child2, bound=None, is_pure_python=True):
        """Constructor for Until node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
                bound : Interval
        """
        super(Until, self).__init__(bound)

        self.addChild(child1)
        self.addChild(child2)
        self.bound = bound

        self.name = '(' + child1.name + ')until[' + str(bound.begin) + ',' + str(
            bound.end) + '](' + child2.name + ')'

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

