from abc import abstractmethod

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
            self.resetVisitor.visitAst(node)

        # reset spec
        self.resetVisitor.visitAst(self.ast)
        return

    @abstractmethod
    def reset(self, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    @abstractmethod
    def update(self, *args, **kargs):
        raise NotImplementedError(self.NOT_IMPLEMENTED)

    def ast(self, ast):
        print('hogehoge')
        self.__ast = ast


class AbstractOnlineResetVisitor(AbstractAstVisitor):
    def visit(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        operator = self.online_operator_dict[node.name]
        operator.reset()
        return


class AbstractOnlineUpdateVisitor(AbstractAstVisitor):
    def visitBinary(self, node, *args, **kwargs):
        sample_left  = self.visit(node.children[0], *args, **kwargs)
        sample_right = self.visit(node.children[1], *args, **kwargs)
        operator = self.online_operator_dict[node.name]
        sample_return = operator.update(node, sample_left, sample_right, *args, **kwargs)
        return sample_return

    def visitUnary(self, node, *args, **kwargs):
        sample = self.visit(node.children[0], *args, **kwargs)
        operator = self.online_operator_dict[node.name]
        sample_return = operator.update(node, sample, *args, **kwargs)
        return sample_return

    def visitLeaf(self, node, *args, **kwargs):
        operator = self.online_operator_dict[node.name]
        sample_return = operator.update(node, *args, **kwargs)
        return sample_return
