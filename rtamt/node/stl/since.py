# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:24:09 2019

@author: NickovicD
"""
from rtamt.node.stl.temporal_node import TemporalNode

class Since(TemporalNode):
    """A class for storing STL Since nodes
                Inherits TemporalNode
    """
    def __init__(self, child1, child2, bound=None, is_pure_python=True):
        """Constructor for Since node

            Parameters:
                child1 : stl.Node
                child2 : stl.Node
                bound : Interval
        """

        super(Since, self).__init__(bound)
        self.addChild(child1)
        self.addChild(child2)

        self.in_vars = child1.in_vars + child2.in_vars
        self.out_vars = child1.out_vars + child2.out_vars
        self.bound = bound

        if bound == None:
            self.name = '(' + child1.name + ')since(' + child2.name + ')'
        else:
            self.name = '(' + child1.name + ')since[' + str(bound.begin) + ',' + str(
                bound.end) + '](' + child2.name + ')'

        if is_pure_python:
            if bound == None:
                name = 'rtamt.operation.stl.since_operation'
                mod = __import__(name, fromlist=[''])
                self.node = mod.SinceOperation()
            else:
                name = 'rtamt.operation.stl.since_bounded_operation'
                mod = __import__(name, fromlist=[''])
                self.node = mod.SinceBoundedOperation(int(bound.begin), int(bound.end))
        else:
            name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_node'
            mod = __import__(name, fromlist=[''])

            if bound == None:
                name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_since_node'
                mod = __import__(name, fromlist=[''])
                self.node = mod.StlSinceNode()
            else:
                name = 'rtamt.lib.rtamt_stl_library_wrapper.stl_since_bounded_node'
                mod = __import__(name, fromlist=[''])
                self.node = mod.StlSinceBoundedNode(int(bound.begin), int(bound.end))
