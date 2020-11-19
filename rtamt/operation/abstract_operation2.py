# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 2019

@author: Dejan Nickovic
"""
from abc import ABCMeta, abstractmethod
import numpy

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

    def __init__(self):
        pass

    @abstractmethod
    def timeHandle(time_seriese):
        raise NotImplementedError(NOT_IMPLEMENTED)

class discreteTime(timeHandle):
    def __init__(self):
        pass

    def timeHandle(time_seriese):
        pass

class denseTime(timeHandle):
    def __init__(self):
        pass

    def timeHandle(time_seriese):
        pass


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

    def __init__(self):
        pass

    @abstractmethod
    def eval_wrapper(self, *args, **kargs):
        raise NotImplementedError(NOT_IMPLEMENTED)

class offline(evaluation):
    def __init__(self):
        pass

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

# evaluation x ShapeOperation 
class offlineBinaryOperation(offline, BinaryOperation):
    def __init__(self):
        pass

    def eval_wrapper(self, *args, **kargs):
        robustness_list = []

        left_time_series, right_time_series = self.getter_wrapper(*args,**kargs)
        if (left_time_series.size == 0) or (right_time_series.size == 0):
            return robustness_list 

        robustness = self.eval(left_time_series, right_time_series)
        robustness_list = robustness.tolist()
        return robustness_list

    @abstractmethod
    def eval(self, left_time_series, right_time_series):
        raise NotImplementedError(NOT_IMPLEMENTED)