# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:32:57 2019

@author: NickovicD
"""

import logging
from rtamt.spec.stl.specification import STLSpecification
from rtamt.spec.stl_ct.node_init import STLCTNodeInit
from rtamt.spec.stl_ct.evaluator import STLCTEvaluator
from rtamt.spec.stl_ct.offline import STLCTOffline
from rtamt.spec.stl_ct.node_visitor import STLCTNodeVisitor

class STLCTSpecification(STLSpecification):
    """A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:

    """
    def __init__(self,is_pure_python=True):
        """Constructor for STL Specification"""
        super(STLCTSpecification, self).__init__(is_pure_python)
        self.visitor = STLCTNodeVisitor(self)


    def parse(self):
        super(STLCTSpecification, self).parse()
        nodeInit = STLCTNodeInit()
        nodeInit.visit(self.top, None)
        self.evaluator = STLCTEvaluator(self)
        self.offline_evaluator = STLCTOffline(self)
        self.top.accept(self.evaluator)

    def update(self, *args, **kargs):
        for arg in args:
            var_name = arg[0]
            var_object = arg[1]
            self.var_object_dict[var_name] = var_object
        out = self.evaluator.evaluate(self.top, ['update'])
        self.var_object_dict = self.var_object_dict.fromkeys(self.var_object_dict, [])
        return out

    def update_final(self, *args, **kargs):
        for arg in args:
            var_name = arg[0]
            var_object = arg[1]
            self.var_object_dict[var_name] = var_object
        out = self.evaluator.evaluate(self.top, ['final'])
        self.var_object_dict = self.var_object_dict.fromkeys(self.var_object_dict, [])
        return out

    def offline(self, *args, **kargs):
        for arg in args:
            var_name = arg[0]
            var_object = arg[1]
            self.var_object_dict[var_name] = var_object
        out = self.offline_evaluator.offline(self.top, None)
        self.var_object_dict = self.var_object_dict.fromkeys(self.var_object_dict, [])
        return out








