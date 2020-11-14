from rtamt.operation.abstract_operation import AbstractOperation
from scipy import signal, interpolate

import numpy

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
        t = numpy.array([ i[0] for i in input_list ])
        p = numpy.array([ i[1] for i in input_list ])
        t = numpy.append(t, numpy.Inf)  # if you don't need to extrapolation of end of traj. you can remove here. 
        p = numpy.append(p, p[-1])
        interpolate_traj = interpolate.interp1d(t, p, kind='previous') # interporlation is piecewise constant.

        # inflection time set
        ## (inflection time, interval start, interval end)
        intsi = numpy.array([t[0], t[0]+self.begin, t[0]+self.end])
        tT = numpy.array([t]).T
        its1 = numpy.hstack((tT-self.end, tT-(self.end-self.begin), tT))
        its2 = numpy.hstack((tT-self.begin, tT, tT+(self.end-self.begin)))
        its = numpy.vstack((intsi, its1,its2))
        its = numpy.unique(its, axis=0)
        
        ## cutting out of range
        index = (t[0] <= its) & (its <= t[-1])
        index = [numpy.amin(index, axis=1)]
        its = its[index]

        # calc rob for each its
        robs = numpy.empty([its.shape[0],2])
        for i in range(its.shape[0]):
            it = its[i]
            time = it[0]
            begin = it[1]
            end = it[2]
            tt = t[(begin<t)&(t<end)] 
            eval_times = numpy.hstack((begin, tt, end))
            rob = min(interpolate_traj(eval_times))
            robs[i] = numpy.array([time,rob])

        # remove duplication
        diff = numpy.diff(robs[:,1])
        index = (diff !=0)
        index = numpy.hstack((True, index))
        robs = robs[index]

        out = robs.tolist()
        return out