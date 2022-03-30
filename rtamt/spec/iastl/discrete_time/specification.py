from rtamt.operation.stl.discrete_time.online.evaluator import StlDiscreteTimeOnlineEvaluator
from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.ast.parser.stl.specification_parser import StlAst

from rtamt.operation.stl.discrete_time.offline.evaluator import StlDiscreteTimeOfflineEvaluator
from rtamt.operation.iastl.discrete_time.online.evaluator import IAStlDiscreteTimeOnlineEvaluator
from rtamt.enumerations.options import *
from rtamt.pastifier.stl.pastifier import StlPastifier


def IASTLDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineEvaluator(), StlDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    else:
        spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineEvaluator(), IAStlDiscreteTimeOnlineEvaluator(semantics), pastifier=StlPastifier())
    return spec


def StlDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), StlDiscreteTimeOfflineEvaluator())
    return spec

def IAStlOutputRobustnessDiscreteTimeOnlineSpecification(semantics=Semantics.STANDARD):
    if semantics == Semantics.STANDARD:
        spec = AbstractOnlineSpecification(StlAst(), StlDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    elif semantics == Semantics.OUTPUT_ROBUSTNESS:
        spec = AbstractOnlineSpecification(StlAst(), IAStlOutputRobustnessDiscreteTimeOnlineEvaluator(), pastifier=StlPastifier())
    return spec

