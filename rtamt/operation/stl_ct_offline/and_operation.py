from rtamt.operation.abstract_operation import AbstractOperation
from scipy import signal, interpolate

import numpy

class AndOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, *args, **kargs):
        pass

    def offline(self, *args, **kargs):
        out = []
        left_list = args[0]
        right_list = args[1]

        if (not left_list) or (not right_list):
            return out

        # data conversion
        tl = numpy.array([ i[0] for i in left_list ])
        pl = numpy.array([ i[1] for i in left_list ])
        tlinf = numpy.append(tl, numpy.Inf)  # if you don't need to extrapolation of end of traj. you can remove here. 
        plinf = numpy.append(pl, pl[-1])
        left_interpolate_traj = interpolate.interp1d(tlinf, plinf, kind='previous') # interporlation is piecewise constant.

        tr = numpy.array([ i[0] for i in right_list ])
        pr = numpy.array([ i[1] for i in right_list ])
        trinf = numpy.append(tr, numpy.Inf)  # if you don't need to extrapolation of end of traj. you can remove here. 
        prinf = numpy.append(pr, pr[-1])
        right_interpolate_traj = interpolate.interp1d(trinf, prinf, kind='previous') # interporlation is piecewise constant.

        # inflection time set
        its = numpy.hstack((tl, tr))
        its = numpy.unique(its, axis=0)
        
        ## cutting out of range
        index = ((tlinf[0] <= its) & (its <= tlinf[-1])) & ((trinf[0] <= its) & (its <= trinf[-1]))
        its = its[index]

        # calc rob for each its
        left_robs = left_interpolate_traj(its)
        right_robs = right_interpolate_traj(its)
        robs = numpy.amin(numpy.vstack((left_robs,right_robs)), axis=0)
        robs = numpy.hstack((numpy.array([its]).T, numpy.array([robs]).T))

        # remove duplication
        diff = numpy.diff(robs[:,1])
        index = (diff !=0)
        index = numpy.hstack((True, index))
        robs = robs[index]

        out = robs.tolist()
        return out