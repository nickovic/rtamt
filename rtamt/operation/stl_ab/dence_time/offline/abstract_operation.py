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
        super().__init__()
        return

    def getter(self, *args, **kargs):
        left_time_series_list = args[0]
        right_time_series_list = args[1]
    
        # data conversion
        left_time_series = numpy.array(left_time_series_list)
        right_time_series = numpy.array(right_time_series_list)

        return left_time_series, right_time_series

class UniaryOperation(ShapeOperation):
    def __init__(self):
        super().__init__()
        return

    def getter(self, *args, **kargs):
        time_series_list = args[0]
        
        # data conversion
        time_series = numpy.array(time_series_list)

        return time_series

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
        self. extrapolation_kind = 'none'
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
class offlineDensetimeBinaryOperation(offlineDensetime, BinaryOperation):
    def __init__(self):
        offlineDensetime.__init__(self)
        return

    def eval_wrapper(self, *args, **kargs):
        robustness_list = []

        left_time_series, right_time_series = self.getter_wrapper(*args,**kargs)
        if (left_time_series.size <= 1) or (right_time_series.size <= 1):
            return robustness_list 

        left_interpolation_func = self.time_handle(left_time_series)
        right_interpolation_func = self.time_handle(right_time_series)

        robustness = self.eval(left_interpolation_func, right_interpolation_func)
        robustness_list = robustness.tolist()
        return robustness_list

    @abstractmethod
    def eval(self, left_interpolation_func, right_interpolation_func):
        # [input]
        # left_interpolation_func: left data with interpolation function
        # right_interpolation_func: right data with interpolation function

        # [output]
        # robustness: 2D numpy array [[time,value], ...]
        raise NotImplementedError(NOT_IMPLEMENTED)

class offlineDensetimeUnaryOperation(offlineDensetime, UniaryOperation):
    def __init__(self, *args, **kargs):
        offlineDensetime.__init__(self)
        UniaryOperation.__init__(self)
        return

    def eval_wrapper(self, *args, **kargs):
        robustness_list = []

        time_series = self.getter_wrapper(*args,**kargs)
        if time_series.size == 0:   #TODO: this code is problematic. it works for unbound time get [x,x] only
            return robustness_list
        elif time_series.shape == (1,2):
            robustness = time_series
        else:
            interpolation_func = self.time_handle(time_series)
            robustness = self.eval(interpolation_func)

        robustness_list = robustness.tolist()
        return robustness_list

    @abstractmethod
    def eval(self, input_interpolation_func):
        # [input]
        # interpolation_func: input data with interpolation function

        # [output]
        # robustness: 2D numpy array [[time,value], ...]
        raise NotImplementedError(NOT_IMPLEMENTED)

class offlineDensetimeUnaryBoundedtimeOperation(offlineDensetimeUnaryOperation):
    interval = []

    def __init__(self, *args, **kargs):
        super().__init__()
        begin = args[0]
        end = args[1]
        self.interval = [begin, end]
        return

    def eval_wrapper(self, *args, **kargs):
        robustness_list = []

        time_series = self.getter_wrapper(*args,**kargs)
        if (time_series.size == 0 or time_series.shape == (1,2)):
            return robustness_list 

        interpolation_func = self.time_handle(time_series)

        robustness = self.eval(interpolation_func, self.interval)
        robustness_list = robustness.tolist()
        return robustness_list

    @abstractmethod
    def eval(self, input_interpolation_func, interval):
        # [input]
        # interpolation_func: input data with interpolation function
        # interval: time interval for bouned time operation

        # [output]
        # robustness: 2D numpy array [[time,value], ...]
        raise NotImplementedError(NOT_IMPLEMENTED)
