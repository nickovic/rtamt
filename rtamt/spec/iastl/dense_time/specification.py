from rtamt.pastifier.stl.pastifier import StlPastifier
from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.ast.parser.stl.specification_parser import StlAst

from rtamt.operation.stl.dense_time.offline.evaluator import StlDenseTimeOfflineEvaluator
from rtamt.operation.stl.dense_time.online.evaluator import StlDenseTimeOnlineEvaluator

from rtamt.enumerations.options import *


def IASTLDenseTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), IAStlDenseTimeOfflineEvaluator(semantics), IAStlDenseTimeOnlineEvaluator(semantics), pastifier=StlPastifier())
    else:
        raise Exception()

    return spec

def IAStlDenseTimeOfflineSpecification(semantics=Semantics.STANDARD):
    spec = AbstractOfflineSpecification(StlAst(), IAStlDenseTimeOfflineEvaluator(semantics))
    return spec

def IAStlDenseTimeOnlineSpecification(semantics=Semantics.STANDARD):
    spec = AbstractOnlineSpecification(StlAst(), IAStlDenseTimeOnlineEvaluator(semantics), pastifier=StlPastifier())
    return spec
