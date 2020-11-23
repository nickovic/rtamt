# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.node import Node


class Implies(Node):
    """A class for storing STL Implies nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2, is_pure_python=True):
        """Constructor for Implies node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        super(Implies, self).__init__()
        self.addChild(child1)
        self.addChild(child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars

        self.name = '(' + child1.name + ')->(' + child2.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.implies_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.ImpliesOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_combinatorial_binary_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_implies_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlImpliesNode()


