from rtamt.spec.abstract_specification import AbstractOfflineSpecification, AbstractOnlineSpecification, AbstractOfflineOnlineSpecification

from rtamt.syntax.ast.parser.stl.specification_parser import StlAst

from rtamt.semantics.filtering_stl.discrete_time.offline.interpreter import FilteringStlDiscreteTimeOfflineInterpreter

from rtamt.semantics.enumerations.options import *
from rtamt.pastifier.stl.pastifier import StlPastifier


def FilteringStlDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(StlAst(), FilteringStlDiscreteTimeOfflineInterpreter())
    return spec

