from rtamt.operation.abstract_operation import AbstractOperation
from scipy import signal, interpolate

import numpy

from .tllibs import *

class AlwaysBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, *args, **kargs):
        pass

    def offline(self, *args, **kargs):
        out = []
        input_time_series_list = args[0]
        
        if not input_time_series_list:
            return out

        # data conversion
        input_time_series = numpy.array(input_time_series_list)
        operator_interval = [self.begin, self.end]

        # eval
        robustness = eval_timed_operator_bound(input_time_series, operator_interval, numpy.amin, extrapolation='end', kind='previous')

        # remove duplication
        robustness = remove_duplication(robustness)

        out = robustness.tolist()
        return out