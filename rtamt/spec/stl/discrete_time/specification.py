from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.ast.parser.stl.specification_parser import StlAst

from rtamt.operation.stl.discrete_time.offline.evaluator import StlDiscreteTimeOfflineEvaluator
from rtamt.operation.stl.discrete_time.online.evaluator import StlDiscreteTimeOnlineEvaluator
from rtamt.operation.iastl.discrete_time.online.evaluator import IAStlOutputRobustnessDiscreteTimeOnlineEvaluator, \
    IAStlInputRobustnessDiscreteTimeOnlineEvaluator, IAStlInputVacuityDiscreteTimeOnlineEvaluator, \
    IAStlOutputVacuityDiscreteTimeOnlineEvaluator
from rtamt.operation.iastl.discrete_time.offline.evaluator import IAStlOutputRobustnessDiscreteTimeOfflineEvaluator, \
    IAStlInputRobustnessDiscreteTimeOfflineEvaluator, IAStlInputVacuityDiscreteTimeOfflineEvaluator, \
    IAStlOutputVacuityDiscreteTimeOfflineEvaluator
from rtamt.enumerations.options import *
from rtamt.pastifier.stl.pastifier import StlPastifier


def STLDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineEvaluator(), StlDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.OUTPUT_ROBUSTNESS and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlOutputRobustnessDiscreteTimeOfflineEvaluator(),
                                                  IAStlOutputRobustnessDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.INPUT_ROBUSTNESS and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlInputRobustnessDiscreteTimeOfflineEvaluator(),
                                                  IAStlInputRobustnessDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.INPUT_VACUITY and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlInputVacuityDiscreteTimeOfflineEvaluator(),
                                                  IAStlInputVacuityDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.OUTPUT_VACUITY and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlOutputVacuityDiscreteTimeOfflineEvaluator(),
                                                  IAStlOutputVacuityDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    else:
        raise Exception()
    return spec



def StlDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), StlDiscreteTimeOfflineEvaluator())
    return spec

def StlOutputRobustnessDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineEvaluator())
    return spec

def StlInputVacuityDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineEvaluator())
    return spec

def StlInputRobustnessDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineEvaluator())
    return spec

def StlOutputVacuityDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineEvaluator())
    return spec

def StlDiscreteTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(StlAst(), StlDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    return spec

def StlOutputRobustnessDiscreteTimeOnlineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOnlineEvaluator())
    return spec

def StlInputVacuityDiscreteTimeOnlineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOnlineEvaluator())
    return spec

def StlInputRobustnessDiscreteTimeOnlineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOnlineEvaluator())
    return spec

def StlOutputVacuityDiscreteTimeOnlineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOnlineEvaluator())
    return spec

def StlDiscreteTimeOnlineSpecificationCpp():
    from rtamt.operation.stl.discrete_time.online.cpp.evaluator import StlDiscreteTimeOnlineEvaluatorCpp
    spec = AbstractOnlineSpecification(StlAst(), StlDiscreteTimeOnlineEvaluatorCpp(), pastifier=StlPastifier())
    return spec