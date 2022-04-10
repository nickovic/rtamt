from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.ast.parser.stl.specification_parser import StlAst

from rtamt.operation.stl.discrete_time.offline.interpreter import StlDiscreteTimeOfflineInterpreter
from rtamt.operation.stl.discrete_time.online.interpreter import StlDiscreteTimeOnlineInterpreter
from rtamt.operation.iastl.discrete_time.online.interpreter import IAStlOutputRobustnessDiscreteTimeOnlineInterpreter, \
    IAStlInputRobustnessDiscreteTimeOnlineInterpreter, IAStlInputVacuityDiscreteTimeOnlineInterpreter, \
    IAStlOutputVacuityDiscreteTimeOnlineInterpreter
from rtamt.operation.iastl.discrete_time.offline.interpreter import IAStlOutputRobustnessDiscreteTimeOfflineInterpreter, \
    IAStlInputRobustnessDiscreteTimeOfflineInterpreter, IAStlInputVacuityDiscreteTimeOfflineInterpreter, \
    IAStlOutputVacuityDiscreteTimeOfflineInterpreter
from rtamt.enumerations.options import *
from rtamt.pastifier.stl.pastifier import StlPastifier


def STLDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter(), StlDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    elif semantics == Semantics.OUTPUT_ROBUSTNESS and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlOutputRobustnessDiscreteTimeOfflineInterpreter(),
                                                  IAStlOutputRobustnessDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    elif semantics == Semantics.INPUT_ROBUSTNESS and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlInputRobustnessDiscreteTimeOfflineInterpreter(),
                                                  IAStlInputRobustnessDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    elif semantics == Semantics.INPUT_VACUITY and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlInputVacuityDiscreteTimeOfflineInterpreter(),
                                                  IAStlInputVacuityDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    elif semantics == Semantics.OUTPUT_VACUITY and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlOutputVacuityDiscreteTimeOfflineInterpreter(),
                                                  IAStlOutputVacuityDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    else:
        raise Exception()
    return spec



def StlDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter())
    return spec

def StlOutputRobustnessDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineInterpreter())
    return spec

def StlInputVacuityDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineInterpreter())
    return spec

def StlInputRobustnessDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineInterpreter())
    return spec

def StlOutputVacuityDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineInterpreter())
    return spec

def StlDiscreteTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(StlAst(), StlDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    return spec

def StlOutputRobustnessDiscreteTimeOnlineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOnlineInterpreter())
    return spec

def StlInputVacuityDiscreteTimeOnlineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOnlineInterpreter())
    return spec

def StlInputRobustnessDiscreteTimeOnlineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOnlineInterpreter())
    return spec

def StlOutputVacuityDiscreteTimeOnlineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOnlineInterpreter())
    return spec

def StlDiscreteTimeOnlineSpecificationCpp():
    from rtamt.operation.stl.discrete_time.online.cpp.interpreter import StlDiscreteTimeOnlineInterpreterCpp
    spec = AbstractOnlineSpecification(StlAst(), StlDiscreteTimeOnlineInterpreterCpp(), pastifier=StlPastifier())
    return spec