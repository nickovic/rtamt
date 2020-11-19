from rtamt.operation.abstract_operation2 import offlineBinaryOperation
from scipy import signal, interpolate

import numpy

from .tllibs import *

class AndOperation(offlineBinaryOperation):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kargs):
        pass

    def semantics_func(self, normalize_left_time_series, normalize_right_time_series):
        values = numpy.amin(numpy.vstack((normalize_left_time_series[:,1],normalize_right_time_series[:,1])), axis=0)
        robustness = numpy.hstack( (numpy.array([normalize_left_time_series[:,0]]).T, numpy.array([values]).T,) )
        return robustness

    def eval(self, left_interpolation_func, right_interpolation_func):
        robustness = eval_binary_logic_operator_dense_time(left_interpolation_func, right_interpolation_func, self.semantics_func)
        
        robustness = remove_duplication(robustness) # perhaps I need to put it into wrapper.
        return robustness