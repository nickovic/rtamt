from rtamt.pastifier.xstl.pastifier import XStlPastifier
from rtamt.semantics.xstl.discrete_time.offline.interpreter import XStlDiscreteTimeOfflineInterpreter
from rtamt.semantics.xstl.discrete_time.online.interpreter import XStlDiscreteTimeOnlineInterpreter
from rtamt.spec.abstract_specification import AbstractOnlineSpecification, AbstractOfflineSpecification
from rtamt.syntax.ast.parser.xstl.specification_parser import XStlAst


def XStlDiscreteTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(XStlAst(), XStlDiscreteTimeOnlineInterpreter(),
                                       pastifier=XStlPastifier())
    return spec

def XStlDiscreteTimeOfflineSpecification():
    spec = AbstractOfflineSpecification(XStlAst(), XStlDiscreteTimeOfflineInterpreter())
    return spec

