import operator

from abc import abstractmethod

from rtamt.node.ltl.variable import Variable
from rtamt.node.ltl.constant import Constant

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_evaluator import AbstractEvaluator

class AbstractOnlineEvaluator(AbstractEvaluator):
    def __init__(self):
        super(AbstractOnlineEvaluator, self).__init__()
        self.resetVisitor = AbstractOnlineResetVisitor()
        self.updateVisitor = AbstractOnlineUpdateVisitor()
        self.online_operator_dict = dict()
        return

    def reset(self):
        # reset sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            self.resetVisitor.visitAst(node, self.online_operator_dict)

        # reset spec
        self.resetVisitor.visitAst(self.ast, self.online_operator_dict)
        return

    def set_ast(self, ast):
        self.ast = ast

        # constract online_operator_dict for sub-specs
        for key in self.ast.var_subspec_dict:
            node = self.ast.var_subspec_dict[key]
            self.visitAst(node)

        # constract online_operator_dict for spec
        self.visitAst(self.ast)
        return

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

class AbstractOnlineResetVisitor(AbstractAstVisitor):
    def visitBinary(self, node, online_operator_dict):
        self.visitChildren(node, online_operator_dict)
        operator = online_operator_dict[node.name]
        operator.reset()
        return

    def visitUnary(self, node, online_operator_dict):
        self.visitChildren(node, online_operator_dict)
        operator = online_operator_dict[node.name]
        operator.reset()
        return

    def visitLeaf(self, node, online_operator_dict):
        pass


class AbstractOnlineUpdateVisitor(AbstractAstVisitor):
    def visitBinary(self, node, online_operator_dict):
        sample_left  = self.visit(node.children[0], online_operator_dict)
        sample_right = self.visit(node.children[1], online_operator_dict)
        operator = online_operator_dict[node.name]
        sample_return = operator.update(node, sample_left, sample_right)
        return sample_return

    def visitUnary(self, node, online_operator_dict):
        sample = self.visit(node.children[0], online_operator_dict)
        operator = online_operator_dict[node.name]
        sample_return = operator.update(node, sample)
        return sample_return

    def visitLeaf(self, node, online_operator_dict):
        if isinstance(node, Constant):
            sample_return = self.visitConstant(node, online_operator_dict)
        elif isinstance(node, Variable):
            sample_return = self.visitVariable(node, online_operator_dict)
        return sample_return

    def visitVariable(self, node, online_operator_dict):
        var = self.ast.var_object_dict[node.var]
        if node.field:  #TODO Tom did not understand this line.
            sample_return = operator.attrgetter(node.field)(var)
        else:
            sample_return = var
        return sample_return

    def visitConstant(self, node, online_operator_dict):
        return node.val