# -*- coding: utf-8 -*-

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_offline_evaluator import AbstractOfflineEvaluator
from rtamt.operation.dense_time_evaluator import DenseTimeEvaluator

from rtamt.exception.exception import RTAMTException

class AbstractDesneTimeOfflineEvaluator(AbstractOfflineEvaluator, DenseTimeEvaluator):

    def __init__(self):
        super(AbstractDesneTimeOfflineEvaluator, self).__init__()
        return

    #input format
    #a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
    #b = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]
    #dataset = [['a', a], ['b', b]]
    #TODO merge dense and discrete into evaluate AbstractOfflineEvaluator
    def evaluate(self, dataset):
        # check ast exists
        self.exist_ast()

        # update the value of every input variable
        self.set_variable_to_ast_from_dataset(dataset)

        #TODO move both of spec and sub-specs visit into syntax layer.
        # evaluate modular sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            rob = self.visitAst(node)
            self.ast.var_object_dict[key] = rob

        # evaluate modular spec
        rob = self.visitAst(self.ast)

        self.ast.var_object_dict = self.ast.var_object_dict.fromkeys(self.ast.var_object_dict, [])  #TODO I did not understant it.
        return rob


def dense_time_offline_evaluator_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DenseTimeOfflineEvaluator(AbstractDesneTimeOfflineEvaluator, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DenseTimeOfflineEvaluator, self).__init__(*args, **kwargs)
    return DenseTimeOfflineEvaluator