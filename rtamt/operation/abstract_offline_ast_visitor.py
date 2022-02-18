# -*- coding: utf-8 -*-

from rtamt.ast.visitor.abstract_ast_visitor import AbstractAstVisitor
from rtamt.operation.abstract_evaluation_ast_visitor import AbstractEvluationAstVisitor

from rtamt.exception.exception import AstVisitorException

class AbstractOfflineAstVisitor(AbstractEvluationAstVisitor):
    """
    Abstract Operation: template for any monitoring operation
    """
    def __init__(self):
        pass

    def eval(self, ast, *args, **kwargs):
        sample_return, self.ast = self.visitBottomUp(ast, *args, **kwargs)
        return sample_return, self.ast


def offline_ast_visitor_factory(AstVisitor):
    if not issubclass(AstVisitor, AbstractAstVisitor):  # type check
        raise AstVisitorException('{} is not RTAMT AST visitor'.format(AstVisitor.__name__))

    class OfflineAstVisitor(AbstractOfflineAstVisitor, AstVisitor):
        def __init__(self, *args, **kwargs):
            super(OfflineAstVisitor, self).__init__(*args, **kwargs)
    return OfflineAstVisitor