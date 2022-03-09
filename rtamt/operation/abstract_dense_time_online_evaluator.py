# -*- coding: utf-8 -*-
import operator

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_online_evaluator import AbstractOnlineEvaluator, AbstractOnlineUpdateVisitor
from rtamt.operation.dense_time_evaluator import DenseTimeEvaluator

from rtamt.exception.exception import RTAMTException

class AbstractDenseTimeOnlineEvaluator(AbstractOnlineEvaluator, DenseTimeEvaluator):

    def __init__(self):
        AbstractOnlineEvaluator.__init__(self)
        DenseTimeEvaluator.__init__(self)
        self.updateVisitor = DenseTimeOnlineUpdateVisitor()
        return

    #input format
    #a = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
    #b = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]
    #dataset = [['a', a], ['b', b]]
    #TODO merge dense and discrete into update AbstractOnlineEvaluator
    def update(self, dataset):
        # check ast exists
        self.exist_ast()

        # update the value of every input variable
        self.set_variable_to_ast_from_dataset(dataset)

        # evaluate spec forest
        rob = self.updateVisitor.visitAst(self.ast, self.online_operator_dict, self.ast.var_object_dict)[0]

        self.ast.var_object_dict = self.ast.var_object_dict.fromkeys(self.ast.var_object_dict, [])  #TODO I did not understant it.

        return rob




class DenseTimeOnlineUpdateVisitor(AbstractOnlineUpdateVisitor):
    def visitVariable(self, node, online_operator_dict, var_object_dict):
        var = var_object_dict[node.var]
        if node.field:  #TODO Tom did not understand this line.
            sample_return = operator.attrgetter(node.field)(var)
        else:
            sample_return = var
        return sample_return

    def visitConstant(self, node, online_operator_dict, var_object_dict):
        sample_return = [[0, node.val], [float("inf"), node.val]]
        return sample_return

def dense_time_online_evaluator_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise RTAMTException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class DenseTimeOnlineEvaluator(AbstractDenseTimeOnlineEvaluator, AstVisitor):
        def __init__(self, *args, **kwargs):
            AbstractDenseTimeOnlineEvaluator.__init__(self, *args, **kwargs)
            AstVisitor.__init__(self)

        #def set_ast(self, ast):
        #    AbstractDenseTimeOnlineEvaluator.set_ast(self, ast)

        #    # init dict of online operators
        #    self.online_operator_dict = dict()

        #    AstVisitor.visitAst(self, self.ast)

        #    return


    return DenseTimeOnlineEvaluator
