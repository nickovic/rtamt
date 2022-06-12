from rtamt.spec.abstract_specification import AbstractOnlineSpecification

def XStlDiscreteTimeOnlineSpecification():
    spec = AbstractOnlineSpecification(XStlAst(), XStlDiscreteTimeOnlineInterpreter(),
                                       pastifier=XStlPastifier())
    return spec

