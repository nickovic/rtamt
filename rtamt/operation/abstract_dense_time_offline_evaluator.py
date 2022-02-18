# -*- coding: utf-8 -*-

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_offline_evaluator import AbstractOfflineEvaluator
from rtamt.operation.dense_time_handler import DenseTimeHandler

from rtamt.exception.exception import RTAMTException

class AbstractDesneTimeOfflineEvaluator(AbstractOfflineEvaluator, DenseTimeHandler):

    def __init__(self):
        super(AbstractDesneTimeOfflineEvaluator, self).__init__()
        return

    #input format
    #a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
    #b = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]
    #dataset = [['a', a], ['b', b]]
    #TODO merge dense and discrete into evaluate AbstractOfflineEvaluator
    def evaluate(self, *args, **kargs):
        # input format check
        self.evaluate_args_check(*args, **kargs)
        self.ast_check()

        dataset = self.get_dataset_from_args(*args, **kargs)

        # update the value of every input variable
        self.ast = self.set_variable_to_ast_from_dataset(self.ast, dataset)

        #TODO move both of spec and sub-specs visit into syntax layer.
        # evaluate modular sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            out = self.visitAst(node)
            self.ast.var_object_dict[key] = out

        # evaluate modular spec
        out = self.visitAst(self.ast)
        self.ast.var_object_dict = self.ast.var_object_dict.fromkeys(self.ast.var_object_dict, [])  #TODO I did not understant it.
        return out


def dense_time_offline_evaluator_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DenseTimeOfflineEvaluator(AbstractDesneTimeOfflineEvaluator, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DenseTimeOfflineEvaluator, self).__init__(*args, **kwargs)
    return DenseTimeOfflineEvaluator