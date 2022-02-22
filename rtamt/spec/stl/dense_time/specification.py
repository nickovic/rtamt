from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.ast.parser.stl.dense_time.specification_parser import stlDenseTimeAst

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
        spec = AbstractOfflineOnlineSpecification(stlDenseTimeAst(), StlDenseTimeOfflineEvaluator(), StlDenseTimeOnlineEvaluator(), None)
    else:
        raise Exception()

    return spec

def StlDenseTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(stlDenseTimeAst(), StlDenseTimeOfflineEvaluator())
    return spec

def StlDenseTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(stlDenseTimeAst(), StlDenseTimeOnlineEvaluator())
    return spec
