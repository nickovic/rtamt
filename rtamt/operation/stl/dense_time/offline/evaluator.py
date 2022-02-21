from rtamt.operation.stl.dense_time.offline.ast_visitor import StlDenseTimeOfflineAstVisitor
from rtamt.operation.abstract_dense_time_offline_evaluator import dense_time_offline_evaluator_factory

def StlDenseTimeOfflineEvaluator():
    stlDenseTimeOfflineEvaluator = dense_time_offline_evaluator_factory(StlDenseTimeOfflineAstVisitor)()
    return stlDenseTimeOfflineEvaluator
