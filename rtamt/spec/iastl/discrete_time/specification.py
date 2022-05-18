from rtamt.semantics.stl.discrete_time.online.interpreter import StlDiscreteTimeOnlineInterpreter
from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.syntax.ast.parser.stl.specification_parser import StlAst

from rtamt.semantics.stl.discrete_time.offline.interpreter import StlDiscreteTimeOfflineInterpreter
from rtamt.semantics.iastl.discrete_time.online.interpreter import IAStlDiscreteTimeOnlineInterpreter
from rtamt.semantics.enumerations.options import *
from rtamt.pastifier.stl.pastifier import StlPastifier


def IASTLDiscreteTimeSpecification(semantics=Semantics.STANDARD, language=Language.PYTHON):
    """
    A class used as a container for STL continuous time specifications
       Inherits STLSpecification

    Attributes:
    """
    if semantics == Semantics.STANDARD and language == Language.PYTHON:
        spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter(), StlDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    else:
        spec = AbstractOfflineOnlineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter(), IAStlDiscreteTimeOnlineInterpreter(semantics), pastifier=StlPastifier())
    return spec


def StlDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), StlDiscreteTimeOfflineInterpreter())
    return spec

def IAStlOutputRobustnessDiscreteTimeOnlineSpecification(semantics=Semantics.STANDARD):
    if semantics == Semantics.STANDARD:
        spec = AbstractOnlineSpecification(StlAst(), StlDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    elif semantics == Semantics.OUTPUT_ROBUSTNESS:
        spec = AbstractOnlineSpecification(StlAst(), IAStlOutputRobustnessDiscreteTimeOnlineInterpreter(), pastifier=StlPastifier())
    return spec

