from rtamt.operation.stl.dense_time.online.ast_visitor import StlDenseTimeOnlineAstVisitor
from rtamt.operation.abstract_dense_time_online_evaluator import dense_time_online_evaluator_factory

def StlDenseTimeOnlineEvaluator():
    stlDenseTimeOnlineEvaluator = dense_time_online_evaluator_factory(StlDenseTimeOnlineAstVisitor)()
    return stlDenseTimeOnlineEvaluator
