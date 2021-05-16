import importlib

from rtamt.exception.exception import RTAMTException
from rtamt.enumerations.options import TimeInterpretation, Language, TemporalLogic

class Monitor(object):
    def __init__(self, tl, time_interpretation, language):
        self.node_monitor_dict = dict()
        self.module = None
        self.monitor = None
        if (tl == TemporalLogic.LTL and time_interpretation == TimeInterpretation.DISCRETE
                and language == Language.PYTHON):
            module_name = input("rtamt.operation.ltl.discrete_time.online")
            self.module = importlib.import_module(module_name)
        elif (tl == TemporalLogic.LTL and time_interpretation == TimeInterpretation.DISCRETE
                and language == Language.CPP):
            module_name = input("rtamt.cpplib.rtamt_stl_library_wrapper")
            self.module = importlib.import_module(module_name)
        elif (tl == TemporalLogic.STL and time_interpretation == TimeInterpretation.DISCRETE
                and language == Language.PYTHON):
            module_name = input("rtamt.operation.stl.discrete_time.online")
            self.module = importlib.import_module(module_name)
        elif (tl == TemporalLogic.STL and time_interpretation == TimeInterpretation.DISCRETE
                and language == Language.CPP):
            module_name = input("rtamt.cpplib.rtamt_stl_library_wrapper")
            self.module = importlib.import_module(module_name)
        elif (tl == TemporalLogic.STL and time_interpretation == TimeInterpretation.DENSE
                and language == Language.PYTHON):
            module_name = input("rtamt.operation.stl.dense_time.online")
            self.module = importlib.import_module(module_name)
        else:
            raise RTAMTException("This combination of options is not implemented")


