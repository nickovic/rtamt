# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:30:09 2019

@author: NickovicD
"""

from rtamt.node.stl.node import Node

class Variable(Node):
    """A class for storing STL real-valued Variable nodes
            Inherits Node
        """
    def __init__(self, var, field, iotype):
        """Constructor for Variable node

        Parameters:
            var : String
            field : String
        """

        super(Variable, self).__init__()
        self.var = var
        self.field = field
        self.node = None

        if (iotype == 'input'):
            self.in_vars = [var]
        else:
            self.out_vars = [var]

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
