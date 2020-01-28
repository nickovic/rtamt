# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:32:57 2019

@author: NickovicD
"""

import os
import logging
import sys
from abc import ABCMeta, abstractmethod


class AbstractSpecification:
    """A class used as a container for specifications

    Attributes:
        name : String
        spec : String - specification text

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names
        publish_var : String - variable name to be published
        publish_var_field : String - variable field to be published

        sampling_period : int - size of the sampling period in ps (default = 10^12 ps = 1s)

        var_object_dict : dict(String,AbstractNode) - dictionary that maps variable names to their Node instances
        modules : dict(String,String) - dictionary that maps module paths to module names
        var_type_dict : dict(String, String) - dictionary that maps var names to var types
        var_io_dict : dict(String, String) - dictionary that maps var names to var io signature
        var_topic_dict : dict(String,String) - dictionaty that mapts var names to ROS topic names

        top : AbstractNode - pointer to the specification parse tree

        evaluator : AbstractEvaluator - pointer to the object that implements the monitoring algorithm

        is_pure_python : Boolean - flag denoting whether to use pure Python or mixed Python/C++ implementation (default = False)

    Methods
        get_spec_from_file - create and populate specification object from the text file
        parse - parse the specification
        update - update the specification
    """
    __metaclass__ = ABCMeta

    def __init__(self, is_pure_python):
        self.name = 'Abstract Specification'
        self.spec = None

        self.vars = set()
        self.free_vars = set()
        self.publish_var = ''
        self.publish_var_field = ''

        self.sampling_period = int(10e12)

        self.var_object_dict = dict()
        self.modules = dict()
        self.var_type_dict = dict()
        self.var_io_dict = dict()
        self.var_topic_dict = dict()

        self.top = None

        self.evaluator = None

        self.is_pure_python = is_pure_python


    # setters and getters
    @property
    def is_pure_python(self):
        return self.__is_pure_python

    @is_pure_python.setter
    def is_pure_python(self, is_pure_python):
        self.__is_pure_python = is_pure_python

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self,spec):
        self.__spec = spec

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def top(self):
        return self.__top
    
    @top.setter
    def top(self, top):
        self.__top = top

    @property
    def sampling_period(self):
        return self.__sampling_period

    @sampling_period.setter
    def sampling_period(self, sampling_period):
        self.__sampling_period = sampling_period

    def set_sampling_period(self, sampling_period, unit):

        if (unit == 's'):
            self.sampling_period = sampling_period * 10e12
        elif (unit == 'ms'):
            self.sampling_period = sampling_period * 10e9
        elif (unit == 'us'):
            self.sampling_period = sampling_period * 10e6
        elif (unit == 'ns'):
            self.sampling_period = sampling_period * 10e3
        elif (unit == 'ps'):
            self.sampling_period = sampling_period
        else:
            logging.error('set_sampling_period: unit {} is not valid. The unit is set to default (s) value'.format(unit))
            self.sampling_period = sampling_period * 10e12



    def get_sampling_frequency(self):
        return 10e12 * 1/self.sampling_period

    @property
    def publish_var(self):
        return self.__publish_var
    
    @publish_var.setter
    def publish_var(self, publish_var):
        self.__publish_var = publish_var

    @property
    def free_vars(self):
        return self.__free_vars

    @free_vars.setter
    def free_vars(self, free_vars):
        self.__free_vars = free_vars

    @property
    def publish_var_field(self):
        return self.__publish_var_field

    @publish_var_field.setter
    def publish_var_field(self, publish_var_field):
        self.__publish_var_field = publish_var_field

    @property
    def vars(self):
        return self.__vars

    @vars.setter
    def vars(self, vars):
        self.__vars = vars

    @property
    def modules(self):
        return self.__modules

    @modules.setter
    def modules(self, modules):
        self.__modules = modules

    def add_input_var(self, input_var):
        self.in_vars.add(input_var)

    def remove_input_var(self, var):
        self.in_vars.discard(var)

    def add_output_var(self, output_var):
        self.out_vars.add(output_var)

    def remove_output_var(self, var):
        self.out_vars.discard(var)

    def add_var(self, var):
        self.vars.add(var)
        
    def add_op(self, op):
        self.ops.add(op)

    def get_var_object(self, name):
        return self.var_object_dict[name]

    def get_spec_from_file(self, path):
        """Opens a text file and returns its content as a string
        Parameters:
            path : String - path to the filename
        Returns
            out : String - file content
        """
        out = None
        if os.path.exists(path):
            f = open(path, "r")
            out = f.read()
            f.close()
        else:
            logging.error('The file %s does not exist.', path)
            sys.exit()
        return out

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def update(self, args):
        pass






