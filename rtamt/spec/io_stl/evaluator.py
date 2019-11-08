import operator

from rtamt.spec.stl.evaluator import STLEvaluator
from rtamt.spec.io_stl.io_interpretation import IOInterpretation

class STLIOEvaluator(STLEvaluator):
    def __init__(self, dict, spec):
        super(STLIOEvaluator, self).__init__(dict, spec)

    def visitPredicate(self, element, args):
        out_sample = super(STLIOEvaluator, self).visitPredicate(element, args)

        if (self.spec.iosem == IOInterpretation.OUTPUT_ROBUSTNESS and not element.var in self.spec.out_vars):
            out_sample.value = out_sample.value*float('inf')
        elif(self.spec.iosem == IOInterpretation.INPUT_VACUITY and not element.var in self.spec.in_vars):
            out_sample.value = 0
        elif(self.spec.iosem == IOInterpretation.INPUT_ROBUSTNESS and not element.var in self.spec.in_vars):
            out_sample.value = out_sample.value*float('inf')
        elif(self.spec.iosem == IOInterpretation.OUTPUT_VACUITY and not element.var in self.spec.out_vars):
            out_sample.value = 0
        return out_sample

