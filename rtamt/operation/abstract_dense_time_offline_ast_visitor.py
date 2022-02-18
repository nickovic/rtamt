# -*- coding: utf-8 -*-

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_offline_evaluator import AbstractOfflineEvaluator

from rtamt.exception.exception import RTAMTException

class AbstractDesneTimeOfflineAstVisitor(AbstractOfflineEvaluator):

    def __init__(self):
        super(AbstractDesneTimeOfflineAstVisitor, self).__init__()
        return

    #input format
    #a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
    #b = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]
    #dataset = [['a', a], ['b', b]]
    def evaluate(self, *args, **kargs):
        # input format check
        if len(args) != 1:
            raise RTAMTException('evaluate: Wrong number of arguments')
        dataset = args[0]

        for data in dataset:
            var_name = data[0]
            var_object = data[1]
            self.ast.var_object_dict[var_name] = var_object

        # evaluate modular sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            out = self.visitAst(node)
            self.ast.var_object_dict[key] = out

        # evaluate modular spec
        out = self.visitAst(self.ast)
        self.ast.var_object_dict = self.ast.var_object_dict.fromkeys(self.ast.var_object_dict, [])  #TODO I did not understant it.
        return out


def dense_time_offline_ast_visitor_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DenseTimeOfflineAstVisitor(AbstractDesneTimeOfflineAstVisitor, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(DenseTimeOfflineAstVisitor, self).__init__(*args, **kwargs)
    return DenseTimeOfflineAstVisitor