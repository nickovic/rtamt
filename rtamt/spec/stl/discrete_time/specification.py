from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.ast.parser.stl.discrete_time.specification_parser import stlDiscreteTimeAst

from rtamt.operation.stl.discrete_time.offline.evaluator import StlDiscreteTimeOfflineEvaluator
from rtamt.operation.stl.discrete_time.online.evaluator import StlDiscreteTimeOnlineEvaluator
from rtamt.enumerations.options import *


def STLDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(stlDiscreteTimeAst(), StlDiscreteTimeOfflineEvaluator(), StlDiscreteTimeOnlineEvaluator(), None)
    else:
        raise Exception()
    return spec


def StlDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(stlDiscreteTimeAst(), StlDiscreteTimeOfflineEvaluator())
    return spec

def StlDiscreteTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(stlDiscreteTimeAst(), StlDiscreteTimeOnlineEvaluator())
    return spec

