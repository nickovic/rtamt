import operator

from rtamt.spec.stl_ct.offline import STLCTOffline
from rtamt.spec.io_stl.io_interpretation import IOInterpretation

class STLIOCTOffline(STLCTOffline):
    def __init__(self, spec):
        super(STLIOCTOffline, self).__init__(spec)

    def visitPredicate(self, element, args):
        out_sample = super(STLIOCTOffline, self).visitPredicate(element, args)

        out = []
        if (self.spec.iosem == 'output-robustness' and not element.out_vars):
            for tuple in out_sample:
                ntuple = [tuple[0], tuple[1]*float('inf')]
                out.append(ntuple)
        elif(self.spec.iosem == 'input-vacuity' and not element.in_vars):
            for tuple in out_sample:
                ntuple = [tuple[0], 0]
                out.append(ntuple)
        elif(self.spec.iosem == 'input-robustness' and not element.in_vars):
            for tuple in out_sample:
                ntuple = [tuple[0], tuple[1]*float('inf')]
                out.append(ntuple)
        elif(self.spec.iosem == 'output-vacuity' and not element.in_vars):
            for tuple in out_sample:
                ntuple = [tuple[0], 0]
                out.append(ntuple)
        else:
            out = out_sample

        return out

