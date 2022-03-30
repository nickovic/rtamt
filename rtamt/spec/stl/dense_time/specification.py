from rtamt.operation.iastl.dense_time.offline.evaluator import IAStlOutputRobustnessDenseTimeOfflineEvaluator, \
    IAStlInputRobustnessDenseTimeOfflineEvaluator, IAStlInputVacuityDenseTimeOfflineEvaluator, \
    IAStlOutputVacuityDenseTimeOfflineEvaluator
from rtamt.operation.iastl.dense_time.online.evaluator import IAStlOutputRobustnessDenseTimeOnlineEvaluator, \
    IAStlInputRobustnessDenseTimeOnlineEvaluator, IAStlOutputVacuityDenseTimeOnlineEvaluator, \
    IAStlInputVacuityDenseTimeOnlineEvaluator
from rtamt.pastifier.stl.pastifier import StlPastifier
from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.ast.parser.stl.specification_parser import StlAst

from rtamt.operation.stl.dense_time.offline.evaluator import StlDenseTimeOfflineEvaluator
from rtamt.operation.stl.dense_time.online.evaluator import StlDenseTimeOnlineEvaluator

from rtamt.enumerations.options import *


def STLDenseTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), StlDenseTimeOfflineEvaluator(), StlDenseTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.OUTPUT_ROBUSTNESS and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlOutputRobustnessDenseTimeOfflineEvaluator(),
                                                  IAStlOutputRobustnessDenseTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.INPUT_ROBUSTNESS and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlInputRobustnessDenseTimeOfflineEvaluator(),
                                                  IAStlInputRobustnessDenseTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.INPUT_VACUITY and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlInputVacuityDenseTimeOfflineEvaluator(),
                                                  IAStlInputVacuityDenseTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.OUTPUT_VACUITY and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlOutputVacuityDenseTimeOfflineEvaluator(),
                                                  IAStlOutputVacuityDenseTimeOnlineEvaluator(), pastifier=StlPastifier())
    else:
        raise Exception()

    return spec

def StlDenseTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), StlDenseTimeOfflineEvaluator())
    return spec

def StlDenseTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(StlAst(), StlDenseTimeOnlineEvaluator(), pastifier=StlPastifier())
    return spec
