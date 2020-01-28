import operator

from rtamt.spec.stl.evaluator import STLEvaluator
from rtamt.spec.io_stl.io_interpretation import IOInterpretation

class STLIOEvaluator(STLEvaluator):
    def __init__(self, spec):
        super(STLIOEvaluator, self).__init__(spec)

    def visitPredicate(self, element, args):
        out_sample = super(STLIOEvaluator, self).visitPredicate(element, args)

        if (self.spec.iosem == 'output-robustness' and not element.out_vars):
            out_sample.value = out_sample.value*float('inf')
        elif(self.spec.iosem == 'input-vacuity' and not element.in_vars):
            out_sample.value = 0
        elif(self.spec.iosem == 'input-robustness' and not element.in_vars):
            out_sample.value = out_sample.value*float('inf')
        elif(self.spec.iosem == 'output-vacuity' and not element.out_vars):
            out_sample.value = 0

        return out_sample

