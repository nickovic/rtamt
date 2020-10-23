# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node

class Abs(Node):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child, is_pure_python=True):
        """Constructor for Neg node

            Parameters:
                child : stl.Node
        """
        super(Abs, self).__init__()
        self.addChild(child)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars

        self.name = 'abs(' + child.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.arithmetic.abs_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.AbsOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_abs_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlAbsNode()



