# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:32:57 2019

@author: NickovicD
"""

import logging
from rtamt.spec.stl.specification import STLSpecification
from rtamt.spec.stl_ct.node_init import STLCTNodeInit


class STLCTSpecification(STLSpecification):
    """A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:

    """
    def __init__(self,is_pure_python=False):
        """Constructor for STL Specification"""
        super(STLCTSpecification, self).__init__(is_pure_python)


    def parse(self):
        super(STLCTSpecification, self).parse()
        nodeInit = STLCTNodeInit()
        nodeInit.visit(self.top, None)








