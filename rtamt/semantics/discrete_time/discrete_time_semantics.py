# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from rtamt.semantics.abstract_semantics import AbstractSemantics

NOT_IMPLEMENTED = "You should implement this."

class DiscreteTimeSemantics(AbstractSemantics):
    """
    Abstract Operation: template for any monitoring operation
    """
    #TODO: standarize time trajectory data structure for Discrete time in here.

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

