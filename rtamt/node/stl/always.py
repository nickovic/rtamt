# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""

from rtamt.node.stl.temporal_node import TemporalNode



class Always(TemporalNode):
    """A class for storing STL Always nodes
        Inherits TemporalNode
    """

    def __init__(self, child, bound=None, is_pure_python=True):
        """Constructor for Always

        Parameters:
            child : stl.Node
            bound : Interval
        """
        super(Always, self).__init__(bound)
        self.addChild(child)

        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.bound = bound

        if bound == None:
            self.name = 'always(' + child.name + ')'
        else:
            self.name = 'always[' + str(bound.begin) + ',' + str(bound.end) + '](' + child.name + ')'

        if is_pure_python:
            name = 'rtamt.operation.stl.always_operation'
            mod = __import__(name, fromlist=[''])
            self.node = mod.AlwaysOperation()
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_always_node'
            mod = __import__(name, fromlist=[''])
            self.node = mod.StlAlwaysNode()




