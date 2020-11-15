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
        input_list = args[0]
        
        if not input_list:
            return out

        # data conversion
        input_array = numpy.array(input_list)
        t = input_array[:,0]
        x = input_array[:,1]
        operator_interval = [self.begin, self.end]

        # eval
        robs = eval_timed_operator_bound(t, x, operator_interval, numpy.amin, extrapolation='end', kind='previous')

        # remove duplication
        robs = remove_duplication(robs)

        out = robs.tolist()
        return out