# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:32:57 2019

@author: NickovicD
"""

import logging
from rtamt.spec.stl_ct.specification import STLCTSpecification
from rtamt.spec.stl.io_type import StlIOType
from rtamt.spec.io_stl_ct.evaluator import STLIOCTEvaluator
from rtamt.spec.io_stl_ct.offline import STLIOCTOffline


class STLIOCTSpecification(STLCTSpecification):
    """A class used as a container for IO-Aware STL specifications
       Inherits STLSpecification

    Attributes:
        iosem : String

        in_vars : set(String) - set of input variable names
        out_vars : set(String) - set of out variable names
    """
    def __init__(self,is_pure_python=True):
        """Constructor for STL Specification"""
        super(STLIOCTSpecification, self).__init__(is_pure_python)
        self.iosem = 'standard'
        self.in_vars = set()
        self.out_vars = set()


    def parse(self):
        super(STLIOCTSpecification, self).parse()
        # Initialize the evaluator
        self.evaluator = STLIOCTEvaluator(self)
        self.offline_evaluator = STLIOCTOffline(self)
        self.top.accept(self.evaluator)

    @property
    def iosem(self):
        return self.__iosem

    @iosem.setter
    def iosem(self, iosem):
        self.__iosem = iosem

    @property
    def in_vars(self):
        return self.__in_vars

    @in_vars.setter
    def in_vars(self, in_vars):
        self.__in_vars = in_vars

    @property
    def out_vars(self):
        return self.__out_vars

    @out_vars.setter
    def out_vars(self, out_vars):
        self.__out_vars = out_vars

    def visitVariableDeclaration(self, ctx):
        super(STLIOSpecification, self).visitVariableDeclaration(ctx)
        var_name = ctx.identifier().getText()
        var_iotype = 'undefined'
        # If 'var' is input, add to the set of input vars
        # If 'var' is output, add to the set of output vars
        if (not ctx.ioType() is None):
            if (not ctx.ioType().Input() is None):
                var_iotype = 'input'
            elif (not ctx.ioType().Output() is None):
                var_iotype = 'output'
        self.set_var_io_type(var_name, var_iotype)

    def set_var_io_type(self, var_name, var_iotype):
        if not var_name in self.vars:
            logging.warning('The variable {} does not exist'.format(var_name))
        else:
            if var_iotype == 'input':
                self.add_input_var(var_name)
                self.remove_output_var(var_name)
                self.var_io_dict[var_name] = 'input'
            elif var_iotype == 'output':
                self.add_output_var(var_name)
                self.remove_input_var(var_name)
                self.var_io_dict[var_name] = 'output'
            else:
                self.remove_input_var(var_name)
                self.remove_output_var(var_name)
                self.var_io_dict[var_name] = 'undefined'

    def add_input_var(self, input_var):
        self.in_vars.add(input_var)

    def remove_input_var(self, var):
        self.in_vars.discard(var)

    def add_output_var(self, output_var):
        self.out_vars.add(output_var)

    def remove_output_var(self, var):
        self.out_vars.discard(var)





