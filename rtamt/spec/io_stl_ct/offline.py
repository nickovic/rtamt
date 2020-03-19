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

    def offline(self, *args, **kargs):
        for arg in args:
            var_name = arg[0]
            var_object = arg[1]
            self.var_object_dict[var_name] = var_object
        out = self.offline.offline(self.top, None)
        self.var_object_dict = self.var_object_dict.fromkeys(self.var_object_dict, [])
        return out

