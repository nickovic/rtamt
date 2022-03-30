from rtamt.operation.iastl.dense_time.offline.ast_visitor import IAStlDenseTimeOfflineAstVisitor, \
    IAStlOutputRobustnessDenseTimeOfflineAstVisitor, IAStlInputRobustnessDenseTimeOfflineAstVisitor, \
    IAStlInputVacuityDenseTimeOfflineAstVisitor, IAStlOutputVacuityDenseTimeOfflineAstVisitor
from rtamt.operation.abstract_dense_time_offline_evaluator import dense_time_offline_evaluator_factory

def IAStlOutputRobustnessDenseTimeOfflineEvaluator():
    iastlDenseTimeOfflineEvaluator = dense_time_offline_evaluator_factory(IAStlOutputRobustnessDenseTimeOfflineAstVisitor)()
    return iastlDenseTimeOfflineEvaluator

def IAStlInputRobustnessDenseTimeOfflineEvaluator():
    iastlDenseTimeOfflineEvaluator = dense_time_offline_evaluator_factory(IAStlInputRobustnessDenseTimeOfflineAstVisitor)()
    return iastlDenseTimeOfflineEvaluator

def IAStlInputVacuityDenseTimeOfflineEvaluator():
    iastlDenseTimeOfflineEvaluator = dense_time_offline_evaluator_factory(IAStlInputVacuityDenseTimeOfflineAstVisitor)()
    return iastlDenseTimeOfflineEvaluator

def IAStlOutputVacuityDenseTimeOfflineEvaluator():
    iastlDenseTimeOfflineEvaluator = dense_time_offline_evaluator_factory(IAStlOutputVacuityDenseTimeOfflineAstVisitor)()
    return iastlDenseTimeOfflineEvaluator
