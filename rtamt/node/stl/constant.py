# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:30:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node

class Constant(Node):
    """A class for storing STL real-valued Constant nodes
                Inherits Node

    Attributes:
        val : double
    """
    def __init__(self, val, is_pure_python=True):
        """Constructor for Const node

        Parameters:
            val : double
        """

        super(Constant, self).__init__()
        self.val = val

        self.name = str(val)

        if is_pure_python:
            name = 'rtamt.operation.stl.constant_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.ConstantOperation(val)
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_constant_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlConstantNode(val)

    @property
    def val(self):
        """Getter for val"""
        return self.__val
    
    @val.setter
    def val(self, val):
        """Setter for child"""
        self.__val = val
        
