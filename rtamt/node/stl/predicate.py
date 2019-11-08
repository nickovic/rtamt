# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:30:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node
from rtamt.lib.rtamt_stl_library_wrapper.stl_node import StlNode
from rtamt.lib.rtamt_stl_library_wrapper.stl_predicate_node import StlPredicateNode

class Predicate(Node):
    """A class for storing STL real-valued Variable nodes
                Inherits Node

    Attributes:
        var : String
        field : String
        io_type : IOType enumeration (INPUT, OUTPUT or UNKNOWN)
        threshold : double
        operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
    """
    def __init__(self, var, field, io_type, operator, threshold):
        """Constructor for Predicate node

        Parameters:
            var : String
            field : String
            io_type : IOType enumeration (INPUT, OUTPUT or UNKNOWN)
            threshold : double
            operator : OperatorType (LEQ, GEQ, LESS, GREATER, EQ or NEQ)
        """

        super(Predicate, self).__init__()
        self.var = var
        self.field = field
        self.io_type = io_type
        self.operator = operator
        self.threshold = threshold
        self.node = StlPredicateNode(operator, threshold, io_type)

    @property
    def var(self):
        """Getter for var"""
        return self.__var
    
    @var.setter
    def var(self, var):
        """Setter for var"""
        self.__var = var

    @property
    def field(self):
        """Getter for field"""
        return self.__field

    @field.setter
    def field(self, field):
        """Setter for field"""
        self.__field = field
        
    @property
    def io_type(self):
        """Getter for io_type"""
        return self.__io_type
    
    @io_type.setter
    def io_type(self, io_type):
        """Setter for io_type"""
        self.__io_type = io_type
        
    @property
    def operator(self):
        """Getter for operator"""
        return self.__operator
    
    @operator.setter
    def operator(self, operator):
        """Setter for operator"""
        self.__operator = operator
        
    @property
    def threshold(self):
        """Getter for threshold"""
        return self.__threshold
    
    @threshold.setter
    def threshold(self, threshold):
        """Setter for threshold"""
        self.__threshold = threshold
