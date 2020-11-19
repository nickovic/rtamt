from rtamt.operation.abstract_operation2 import offlineDensetimeBinaryOperation
from scipy import signal, interpolate

import numpy

from .tllibs import *

class AndOperation(offlineDensetimeBinaryOperation):
    def __init__(self):
        super().__init__()

    def semantics_func(self, normalize_left_time_series, normalize_right_time_series):
        values = numpy.amin(numpy.vstack((normalize_left_time_series[:,1],normalize_right_time_series[:,1])), axis=0)
        robustness = numpy.hstack( (numpy.array([normalize_left_time_series[:,0]]).T, numpy.array([values]).T,) )
        return robustness

    def eval(self, left_interpolation_func, right_interpolation_func):
        robustness = eval_binary_logic_operator_dense_time(left_interpolation_func, right_interpolation_func, self.semantics_func)
        
        robustness = remove_duplication(robustness) # perhaps I need to put it into wrapper.
        return robustness