# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:32:57 2019

@author: NickovicD
"""

import os
import logging
import sys
from abc import ABCMeta, abstractmethod
from rtamt.exception.stl.exception import STLSpecificationException
from decimal import Decimal
from fractions import Fraction


class AbstractSpecification:
    """A class used as a container for specifications

    Attributes:
        name : String
        spec : String - specification text

        vars : set(String) - set of variable names
        free_vars : set(String) - set of free variable names
        publish_var : String - variable name to be published
        publish_var_field : String - variable field to be published

        sampling_period : int - size of the sampling period in ps (default = 10^12 ps = 1s

        var_object_dict : dict(String,AbstractNode) - dictionary that maps variable names to their Node instances
        modules : dict(String,String) - dictionary that maps module paths to module names
        var_type_dict : dict(String, String) - dictionary that maps var names to var types
        var_io_dict : dict(String, String) - dictionary that maps var names to var io signature
        var_topic_dict : dict(String,String) - dictionaty that mapts var names to ROS topic names

        top : AbstractNode - pointer to the specification parse tree

        evaluator : AbstractEvaluator - pointer to the object that implements the monitoring algorithm
        offline_evaluator : OfflineEvaluator - pointer to the object that implements the monitoring algorithm

        is_pure_python : Boolean - flag denoting whether to use pure Python or mixed Python/C++ implementation (default = True)

        update_counter : int
        previous_time : float
        sampling_violation_counter : int


    Methods
        get_spec_from_file - create and populate specification object from the text file
        parse - parse the specification
        update - update the specification
    """
    __metaclass__ = ABCMeta

    def __init__(self, is_pure_python):
        self.S_UNIT = int(1000000000)
        self.MS_UNIT = int(1000000)
        self.US_UNIT = int(1000)
        self.NS_UNIT = int(1)

        self.DEFAULT_TOLERANCE = float(0.1)

        self.U = {
            's': self.S_UNIT,
            'ms': self.MS_UNIT,
            'us': self.US_UNIT,
            'ns': self.NS_UNIT
        }

        self.name = 'Abstract Specification'
        self.spec = None

        self.vars = set()
        self.free_vars = set()
        self.publish_var = ''
        self.publish_var_field = ''

        # Default sampling period - 1s
        self.sampling_period = int(1)
        self.sampling_period_unit = 's'

        # Default sampling tolerance
        self.sampling_tolerance = float(0.1)

        # Default unit
        self.unit = 's'

        self.var_object_dict = dict()
        self.modules = dict()
        self.var_type_dict = dict()
        self.var_io_dict = dict()
        self.var_topic_dict = dict()

        self.top = None

        self.evaluator = None
        self.offline_evaluator = None

        self.is_pure_python = is_pure_python

        self.update_counter = int(0)
        self.previous_time = float(0.0)
        self.sampling_violation_counter = int(0)

        self.normalize = float(1.0)

    def reset(self):
        # TODO: add the reset visitor
        self.update_counter = int(0)
        self.previous_time = float(0.0)
        self.sampling_violation_counter = int(0)

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

    @property
    def sampling_period_unit(self):
        return self.__sampling_period_unit

    @sampling_period_unit.setter
    def sampling_period_unit(self, sampling_period_unit):
        self.__sampling_period_unit = sampling_period_unit

    @property
    def sampling_violation_counter(self):
        return self.__sampling_violation_counter

    @sampling_violation_counter.setter
    def sampling_violation_counter(self, sampling_violation_counter):
        self.__sampling_violation_counter = sampling_violation_counter

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        self.__unit = unit

    def set_sampling_period(self, sampling_period=int(1), unit='s', tolerance=float(0.1)):
        self.sampling_period = sampling_period
        self.sampling_period_unit = unit

        if tolerance < 0.0 or tolerance > 1.0:
            raise STLSpecificationException

        self.sampling_tolerance = tolerance

    def get_sampling_period(self):
        return self.sampling_period * self.U[self.sampling_period_unit]

    def get_sampling_frequency(self):
        return 1e12 * 1/self.sampling_period

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

    @property
    def update_counter(self):
        return self.__update_counter

    @update_counter.setter
    def update_counter(self, update_counter):
        self.__update_counter = update_counter

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

    @abstractmethod
    def offline(self, args):
        pass






