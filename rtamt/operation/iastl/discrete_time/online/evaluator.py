from rtamt.operation.iastl.discrete_time.online.ast_visitor import IAStlOutputRobustnessDiscreteTimeOnlineAstVisitor, \
    IAStlOutputVacuityDiscreteTimeOnlineAstVisitor, IAStlInputVacuityDiscreteTimeOnlineAstVisitor, \
    IAStlInputRobustnessDiscreteTimeOnlineAstVisitor
from rtamt.operation.abstract_discrete_time_online_evaluator import discrete_time_online_evaluator_factory


def IAStlOutputRobustnessDiscreteTimeOnlineEvaluator():
    iastlDiscreteTimeOnlineEvaluator = discrete_time_online_evaluator_factory(IAStlOutputRobustnessDiscreteTimeOnlineAstVisitor)()
    return iastlDiscreteTimeOnlineEvaluator


def IAStlOutputVacuityDiscreteTimeOnlineEvaluator():
    iastlDiscreteTimeOnlineEvaluator = discrete_time_online_evaluator_factory(IAStlOutputVacuityDiscreteTimeOnlineAstVisitor)()
    return iastlDiscreteTimeOnlineEvaluator


def IAStlInputRobustnessDiscreteTimeOnlineEvaluator():
    iastlDiscreteTimeOnlineEvaluator = discrete_time_online_evaluator_factory(IAStlInputRobustnessDiscreteTimeOnlineAstVisitor)()
    return iastlDiscreteTimeOnlineEvaluator


def IAStlInputVacuityDiscreteTimeOnlineEvaluator():
    iastlDiscreteTimeOnlineEvaluator = discrete_time_online_evaluator_factory(IAStlInputVacuityDiscreteTimeOnlineAstVisitor)()
    return iastlDiscreteTimeOnlineEvaluator
