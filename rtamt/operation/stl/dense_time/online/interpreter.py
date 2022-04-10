from rtamt.operation.stl.dense_time.online.ast_visitor import StlDenseTimeOnlineAstVisitor
from rtamt.operation.abstract_dense_time_online_interpreter import dense_time_online_interpreter_factory

def StlDenseTimeOnlineInterpreter():
    stlDenseTimeOnlineInterpreter = dense_time_online_interpreter_factory(StlDenseTimeOnlineAstVisitor)()
    return stlDenseTimeOnlineInterpreter
