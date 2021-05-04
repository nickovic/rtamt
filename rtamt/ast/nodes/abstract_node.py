# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""

class AbstractNode(object):
    """
    Abstract Node: tree-like data structure containing
    arbitrary specifications
    """

    def __init__(self):
        super(object, self).__init__()

        self.children = list()
        self.evaluator = None
        self.horizon = 0 #TODO: Tom thinks horizon needs only timed autokmaton.
        self.name = ''
        self.node = None
