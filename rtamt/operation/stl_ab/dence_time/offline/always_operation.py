import numpy

from .abstract_operation import offlineDensetimeUnaryOperation

from .tllibs import *

class AlwaysOperation(offlineDensetimeUnaryOperation):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        return

    def semantics_func(self, time_seriese):
        robustness_value = numpy.amin(time_seriese[:,1])
        robustness_data_point = numpy.array([time_seriese[0,0], robustness_value])
        return robustness_data_point

    def eval(self, interpolation_func):
        robustness = eval_unary_timed_operator_dense_time(interpolation_func, self.semantics_func)
        robustness = remove_duplication(robustness) # perhaps I need to put it into wrapper.
        return robustness   