import numpy

from rtamt.operation.abstract_operation import offlineDensetimeUnaryBoundedtimeOperation

from .tllibs import *

class AlwaysBoundedOperation(offlineDensetimeUnaryBoundedtimeOperation):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        return

    def semantics_func(self, time, bounded_time_seriese):
        robustness_value = numpy.amin(bounded_time_seriese[:,1])
        robustness_data_point = numpy.array([time, robustness_value])
        return robustness_data_point

    def eval(self, interpolation_func, interval):
        robustness = eval_unary_timed_operator_bound_dense_time(interpolation_func, interval, self.semantics_func)
        robustness = remove_duplication(robustness) # perhaps I need to put it into wrapper.
        return robustness