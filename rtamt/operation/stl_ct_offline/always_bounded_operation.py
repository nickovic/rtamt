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
        operator_interval = [self.begin, self.end]

        out = offline_binary_timed_operator_wrapper(operator_interval, numpy.amin, *args, **kargs, )

        return out