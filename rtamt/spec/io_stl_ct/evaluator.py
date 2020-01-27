import operator

from rtamt.spec.stl_ct.evaluator import STLCTEvaluator
from rtamt.spec.io_stl.io_interpretation import IOInterpretation

class STLIOCTEvaluator(STLCTEvaluator):
    def __init__(self, spec):
        super(STLIOCTEvaluator, self).__init__(spec)

    def visitPredicate(self, element, args):
        out_sample = super(STLIOCTEvaluator, self).visitPredicate(element, args)

        if (self.spec.iosem == IOInterpretation.OUTPUT_ROBUSTNESS and not element.var in self.spec.out_vars):
            out_sample.value = out_sample.value*float('inf')
        elif(self.spec.iosem == IOInterpretation.INPUT_VACUITY and not element.var in self.spec.in_vars):
            out_sample.value = 0
        elif(self.spec.iosem == IOInterpretation.INPUT_ROBUSTNESS and not element.var in self.spec.in_vars):
            out_sample.value = out_sample.value*float('inf')
        elif(self.spec.iosem == IOInterpretation.OUTPUT_VACUITY and not element.var in self.spec.out_vars):
            out_sample.value = 0
        return out_sample

