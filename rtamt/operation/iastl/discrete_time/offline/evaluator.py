from rtamt.operation.abstract_discrete_time_offline_evaluator import discrete_time_offline_evaluator_factory
from rtamt.operation.iastl.discrete_time.offline.ast_visitor import IAStlDiscreteTimeOfflineAstVisitor, \
    IAStlOutputRobustnessDiscreteTimeOfflineAstVisitor, IAStlInputRobustnessDiscreteTimeOfflineAstVisitor, \
    IAStlOutputVacuityDiscreteTimeOfflineAstVisitor, IAStlInputVacuityDiscreteTimeOfflineAstVisitor


def IAStlOutputRobustnessDiscreteTimeOfflineEvaluator():
    iastlDiscreteTimeOfflineEvaluator = \
        discrete_time_offline_evaluator_factory(IAStlOutputRobustnessDiscreteTimeOfflineAstVisitor)()
    return iastlDiscreteTimeOfflineEvaluator

def IAStlInputRobustnessDiscreteTimeOfflineEvaluator():
    iastlDiscreteTimeOfflineEvaluator = discrete_time_offline_evaluator_factory(IAStlInputRobustnessDiscreteTimeOfflineAstVisitor)()
    return iastlDiscreteTimeOfflineEvaluator

def IAStlOutputVacuityDiscreteTimeOfflineEvaluator():
    iastlDiscreteTimeOfflineEvaluator = discrete_time_offline_evaluator_factory(IAStlOutputVacuityDiscreteTimeOfflineAstVisitor)()
    return iastlDiscreteTimeOfflineEvaluator

def IAStlInputVacuityDiscreteTimeOfflineEvaluator():
    iastlDiscreteTimeOfflineEvaluator = discrete_time_offline_evaluator_factory(IAStlInputVacuityDiscreteTimeOfflineAstVisitor)()
    return iastlDiscreteTimeOfflineEvaluator
