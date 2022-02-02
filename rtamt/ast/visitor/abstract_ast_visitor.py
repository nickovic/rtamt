from abc import ABCMeta

from rtamt.node.unary_node import UnaryNode
from rtamt.node.binary_node import BinaryNode
from rtamt.node.leaf_node import LeafNode

from rtamt.exception.exception import AstVisitorException


class AbstractAstVisitor(object):
    __metaclass__ = ABCMeta

    def visitAbstractAstChildren(self, node, *args, **kwargs):
        if isinstance(node, UnaryNode):
            sample_from_child = self.visitAbstractAstChildren(node.children[0])
            sample_return = self.visitSpecific(node, sample_from_child, *args, **kwargs)
            sample_return = None
            return sample_return
        elif isinstance(node, BinaryNode):
            sample_from_child_left = self.visitAbstractAstChildren(node.children[0])
            sample_from_child_right = self.visitAbstractAstChildren(node.children[1])
            sample_return = self.visitSpecific(node, sample_from_child_left, sample_from_child_right, *args, **kwargs)
            sample_return = None
            return sample_return
        if isinstance(node, LeafNode):
            sample_return = self.visitSpecific(node, *args, **kwargs)
            sample_return = None
            return sample_return
        else:
            raise AstVisitorException('{} is not RTAMT AST node'.format(node.__class__.__name__))

    def visit(self, ast, *args, **kwargs):
        return self.visitAbstractAstChildren(ast.ast, *args, **kwargs)

    def visitSpecific(self, node, *args, **kwargs):
        sample_return = None
        return sample_return