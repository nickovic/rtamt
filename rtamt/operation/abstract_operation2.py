# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta, abstractmethod
import numpy

from .stl_ct_offline.tllibs import *

NOT_IMPLEMENTED = "You should implement this."

class AbstractOperation:
    """
    Abstract Operation: template for any monitoring operation
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)


class timeHandle:
    __metaclass__ = ABCMeta
    interporation_kind = []

    def __init__(self):
        pass

    @abstractmethod
    def time_handle(self, time_seriese):
        raise NotImplementedError(NOT_IMPLEMENTED)

class discreteTime(timeHandle):
    def __init__(self):
        pass

class denseTime(timeHandle):
    def __init__(self):
        self.interporation_kind = 'previous'
        return

class ShapeOperation:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def getter_wrapper(self, *args, **kargs):
        objective_data = self.getter(*args, **kargs)
        return objective_data
    
    @abstractmethod
    def getter(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

class BinaryOperation(ShapeOperation):
    def __init__(self):
        pass

    def getter(self, *args, **kargs):
        left_time_series_list = args[0]
        right_time_series_list = args[1]
    
        # data conversion
        left_time_series = numpy.array(left_time_series_list)
        right_time_series = numpy.array(right_time_series_list)

        return left_time_series, right_time_series

class UniaryOperation(ShapeOperation):
    def __init__(self):
        pass

    @abstractmethod
    def getter(time_seriese):
        raise NotImplementedError(NOT_IMPLEMENTED)


class operation:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

class logic(operation):
    def __init__(self):
        pass


class temporal(operation):
    def __init__(self):
        pass

class evaluation:
    __metaclass__ = ABCMeta
    rob_list = [] 
    extrapolation_kind = 'none'

    def __init__(self):
        pass

    @abstractmethod
    def eval_wrapper(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

class offline(evaluation):
    
    def __init__(self):
        self. extrapolation_kind = 'end'
        return

    def eval_wrapper(self, *args, **kargs):
        return self.eval(self, *args, **kargs)

    @abstractmethod
    def eval(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

class online(evaluation):
    def __init__(self):
        pass

    @abstractmethod
    def update():
        raise NotImplementedError(NOT_IMPLEMENTED)


class interpolation:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def interpolation():
        raise NotImplementedError(NOT_IMPLEMENTED)

class piecewiseConstant(interpolation):
    def __init__(self):
        pass

    def interpolation():
        pass

class piecewiselinear(interpolation):
    def __init__(self):
        pass

    def interpolation():
        pass

# evaluation x timeHandle
class offlineDensetime(offline, denseTime):
    def __init__(self):
        offline.__init__(self)
        denseTime.__init__(self)
    
    def time_handle(self, time_seriese):
        interpolation_func = interpolation_func_gen(time_seriese, self.extrapolation_kind, self.interporation_kind)
        return interpolation_func

# evaluation x ShapeOperation 
class offlineBinaryOperation(offlineDensetime, BinaryOperation):
    def __init__(self):
        offlineDensetime.__init__(self)
        return

    def eval_wrapper(self, *args, **kargs):
        robustness_list = []

        left_time_series, right_time_series = self.getter_wrapper(*args,**kargs)
        if (left_time_series.size == 0) or (right_time_series.size == 0):
            return robustness_list 

        left_interpolation_func = self.time_handle(left_time_series)
        right_interpolation_func = self.time_handle(right_time_series)

        robustness = self.eval(left_interpolation_func, right_interpolation_func)
        robustness_list = robustness.tolist()
        return robustness_list

    @abstractmethod
    def eval(self, left_interpolation_func, right_interpolation_func):
        # [input]
        # left_interpolation_func: left interpolation function
        # right_interpolation_func: right interpolation function

        # [output]
        # robustness: 2D numpy array [[time,value], ...]
        raise NotImplementedError(NOT_IMPLEMENTED)