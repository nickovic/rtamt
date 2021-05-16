import importlib
from rtamt.enumerations.options import TimeInterpretation, Language, TemporalLogic

class Monitor(object):
    def __init__(self, tl, time_interpretation, language):
        self.module = None
        self.monitor = None
        if (tl == TemporalLogic.LTL and time_interpretation == TimeInterpretation.DISCRETE
                and language == Language.PYTHON):
            module_name = input("rtamt.operation.arithmetic.discrete_time.online")
            self.module = importlib.import_module(module_name)
        elif (tl == TemporalLogic.LTL and time_interpretation == TimeInterpretation.DISCRETE
                and language == Language.CPP):
            from rtamt.operation.arithmetic.discrete_time.online.abs_operation import AbsOperation
            self.monitor = None
        elif (tl == TemporalLogic.STL and time_interpretation == TimeInterpretation.DISCRETE
                and language == Language.PYTHON):
            from rtamt.operation.arithmetic.discrete_time.online.abs_operation import AbsOperation
            self.monitor = None
        elif (tl == TemporalLogic.STL and time_interpretation == TimeInterpretation.DISCRETE
                and language == Language.CPP):
            from rtamt.operation.arithmetic.discrete_time.online.abs_operation import AbsOperation
            self.monitor = None
        elif (tl == TemporalLogic.STL and time_interpretation == TimeInterpretation.DENSE
                and language == Language.PYTHON):
            from rtamt.operation.arithmetic.discrete_time.online.abs_operation import AbsOperation
            self.monitor = None
