# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode


class Once(TemporalNode):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child, bound=None, is_pure_python=True):
        """Constructor for Once node

        Parameters:
            child : stl.Node
            bound : Interval
        """

        super(Once, self).__init__(bound)
        self.addChild(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.bound = bound

        if bound == None:
            self.name = 'once(' + child.name + ')'
        else:
            self.name = 'once[' + str(bound.begin) + ',' + str(bound.end) + '](' + child.name + ')'

        if is_pure_python:
            if bound == None:
                name = 'rtamt.operation.stl.once_operation'
                mod = __import__(name, fromlist=[''])
                self.node = mod.OnceOperation()
            else:
                name = 'rtamt.operation.stl.once_bounded_operation'
                mod = __import__(name, fromlist=[''])
                self.node = mod.OnceBoundedOperation(int(bound.begin), int(bound.end))
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            if bound == None:
                name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_once_node'
                mod = __import__(name, fromlist=[''])
                self.node = mod.StlOnceNode()
            else:
                name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_once_bounded_node'
                mod = __import__(name, fromlist=[''])
                self.node = mod.StlOnceBoundedNode(int(bound.begin), int(bound.end))


