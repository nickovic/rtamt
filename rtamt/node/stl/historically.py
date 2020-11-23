# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode

class Historically(TemporalNode):
    """A class for storing STL Historically nodes
         Inherits TemporalNode
    """
    def __init__(self, child, bound=None, is_pure_python=True):
        """Constructor for Historically node

            Parameters:
                child : stl.Node
                bound : Interval
        """
        super(Historically, self).__init__(bound)
        self.addChild(child)
        self.in_vars = child.in_vars
        self.out_vars = child.out_vars
        self.bound = bound

        if bound == None:
            self.name = 'historically(' + child.name + ')'
        else:
            self.name = 'historically[' + str(bound.begin) + ',' + str(bound.end) + '](' + child.name + ')'


        if is_pure_python:
            if self.bound == None:
                name = 'rtamt.operation.stl.historically_operation'
                mod = __import__(name, fromlist=[''])
                self.node = mod.HistoricallyOperation()
            else:
                name = 'rtamt.operation.stl.historically_bounded_operation'
                mod = __import__(name, fromlist=[''])
                self.node = mod.HistoricallyBoundedOperation(int(bound.begin), int(bound.end))
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            if self.bound == None:
                name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_historically_node'
                mod = __import__(name, fromlist=[''])
                self.node = mod.StlHistoricallyNode()
            else:
                name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_historically_bounded_node'
                mod = __import__(name, fromlist=[''])
                self.node = mod.StlHistoricallyBoundedNode(int(bound.begin), int(bound.end))
