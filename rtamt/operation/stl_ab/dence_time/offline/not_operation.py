import numpy

from rtamt.operation.abstract_operation import offlineDensetimeUnaryOperation

from .tllibs import *

class NotOperation(offlineDensetimeUnaryOperation):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        return

    def eval(self, input_interpolation_func):
        time_series = interpolation_func2time_series(input_interpolation_func)
        times = time_series[:,0]
        values = time_series[:,1]

        robustness = times_values2time_series(times, -values)
        robustness = remove_duplication(robustness) # perhaps I need to put it into wrapper.

        return robustness
