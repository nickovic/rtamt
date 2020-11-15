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
        # ideally func_in={input_time_series_list} class member={operator_interval}
        # In here only eval_func should be decided.

        operator_interval = [self.begin, self.end]

        out = offline_unary_timed_operator_wrapper(operator_interval, numpy.amin, *args, **kargs)

        return out