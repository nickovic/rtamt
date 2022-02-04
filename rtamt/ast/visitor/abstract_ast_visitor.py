from abc import ABCMeta, abstractmethod

from rtamt.node.unary_node import UnaryNode
from rtamt.node.binary_node import BinaryNode
from rtamt.node.leaf_node import LeafNode

from rtamt.exception.exception import AstVisitorException


class AbstractAstVisitor(object):
    __metaclass__ = ABCMeta

    NOT_IMPLEMENTED = "You should implement this."

    def visitAbstractAstChildren(self, node, *args, **kwargs):
        if isinstance(node, UnaryNode):
            sample = self.visitAbstractAstChildren(node.children[0])
            sample_return = self.visitSpecific(node, sample, *args, **kwargs)
            return sample_return
        elif isinstance(node, BinaryNode):
            sample_left = self.visitAbstractAstChildren(node.children[0])
            sample_right = self.visitAbstractAstChildren(node.children[1])
            sample_return = self.visitSpecific(node, sample_left, sample_right, *args, **kwargs)
            return sample_return
        if isinstance(node, LeafNode):
            sample_return = self.visitSpecific(node, *args, **kwargs)
            return sample_return
        else:
            raise AstVisitorException('{} is not RTAMT AST node'.format(node.__class__.__name__))

    def visit(self, ast, *args, **kwargs):
        self.ast = ast
        sample_return = self.visitAbstractAstChildren(self.ast.ast, *args, **kwargs)
        return sample_return, self.ast

    @abstractmethod
    def visitSpecific(self, node, *args, **kwargs):
        sample_return = None
        return sample_return