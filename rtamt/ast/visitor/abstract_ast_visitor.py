from abc import ABCMeta

from rtamt.node.unary_node import UnaryNode
from rtamt.node.binary_node import BinaryNode
from rtamt.node.leaf_node import LeafNode

from rtamt.exception.exception import AstVisitorException


class AbstractAstVisitor(object):
    __metaclass__ = ABCMeta

    def visitAbstractAstChildren(self, node, *args, **kwargs):
        if isinstance(node, UnaryNode):
            sample_from_child = self.abstractAstVisit(node.children[0])
            #sample_return = node.interrupt(sample_from_child, *args, **kwargs)
            print(node.__class__.__name__)
            sample_return = None
            return sample_return
        elif isinstance(node, BinaryNode):
            sample_from_child_left = self.abstractAstVisit(node.children[0])
            sample_from_child_right = self.abstractAstVisit(node.children[1])
            #sample_return = node.interrupt(sample_from_child_left, sample_from_child_right, *args, **kwargs)
            print(node.__class__.__name__)
            sample_return = None
            return sample_return
        if isinstance(node, LeafNode):
            #sample_return = node.interrupt(*args, **kwargs)
            print(node.__class__.__name__)
            sample_return = None
            return sample_return
        else:
            raise AstVisitorException('{} is not ANTRL4 AST node'.format(node.__class__.__name__))

    def abstractAstVisit(self, node, *args, **kwargs):
        sample_return = self.visitAbstractAstChildren(node, *args, **kwargs)
        return sample_return

    def visit(self, ast, *args, **kwargs):
        return self.abstractAstVisit(ast.ast, *args, **kwargs)