from rtamt.operation.abstract_dense_time_online_evaluator import dense_time_online_evaluator_factory
from rtamt.operation.iastl.dense_time.online.ast_visitor import IAStlOutputRobustnessDenseTimeOnlineAstVisitor, \
    IAStlOutputVacuityDenseTimeOnlineAstVisitor, IAStlInputVacuityDenseTimeOnlineAstVisitor, \
    IAStlInputRobustnessDenseTimeOnlineAstVisitor


def IAStlOutputRobustnessDenseTimeOnlineEvaluator():
    iastlDenseTimeOnlineEvaluator = dense_time_online_evaluator_factory(IAStlOutputRobustnessDenseTimeOnlineAstVisitor)()
    return iastlDenseTimeOnlineEvaluator

def IAStlInputRobustnessDenseTimeOnlineEvaluator():
    iastlDenseTimeOnlineEvaluator = dense_time_online_evaluator_factory(IAStlInputRobustnessDenseTimeOnlineAstVisitor)()
    return iastlDenseTimeOnlineEvaluator

def IAStlOutputVacuityDenseTimeOnlineEvaluator():
    iastlDenseTimeOnlineEvaluator = dense_time_online_evaluator_factory(IAStlOutputVacuityDenseTimeOnlineAstVisitor)()
    return iastlDenseTimeOnlineEvaluator

def IAStlInputVacuityDenseTimeOnlineEvaluator():
    iastlDenseTimeOnlineEvaluator = dense_time_online_evaluator_factory(IAStlInputVacuityDenseTimeOnlineAstVisitor)()
    return iastlDenseTimeOnlineEvaluator
