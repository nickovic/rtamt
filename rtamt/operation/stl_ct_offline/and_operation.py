from rtamt.operation.abstract_operation import AbstractOperation
from scipy import signal, interpolate

import numpy

from .tllibs import *

class AndOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, *args, **kargs):
        pass

    def semantics_func(self, normalize_left_time_series, normalize_right_time_series):
        values = numpy.amin(numpy.vstack((normalize_left_time_series[:,1],normalize_right_time_series[:,1])), axis=0)
        robustness = numpy.hstack( (numpy.array([normalize_left_time_series[:,0]]).T, numpy.array([values]).T,) )
        return robustness

    def offline(self, *args, **kargs):
        out = offline_binary_logic_operator_wrapper(self.semantics_func, *args, **kargs)
        return out