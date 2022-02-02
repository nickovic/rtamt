from abc import ABCMeta

from rtamt.node.unary_node import UnaryNode
from rtamt.node.binary_node import BinaryNode
from rtamt.node.leaf_node import LeafNode

from rtamt.exception.exception import AstVisitorException


class AbstractAstVisitor(object):
    __metaclass__ = ABCMeta

    def visitChildren(self, node, *args, **kwargs):
        if isinstance(node, UnaryNode):
            sample_from_child = self.visit(node.children[0])
            #sample_return = node.interrupt(sample_from_child, *args, **kwargs)
            sample_return = None
            return sample_return
        elif isinstance(node, BinaryNode):
            sample_from_child_left = self.visit(node.children[0])
            sample_from_child_right = self.visit(node.children[1])
            #sample_return = node.interrupt(sample_from_child_left, sample_from_child_right, *args, **kwargs)
            sample_return = None
            return sample_return
        if isinstance(node, LeafNode):
            #sample_return = node.interrupt(*args, **kwargs)
            sample_return = None
            return sample_return
        else:
            raise AstVisitorException('{} is not ANTRL4 AST node'.format(node.__class__.__name__))


    def visit(self, node, *args, **kwargs):
        sample_return = self.visitChildren(node, *args, **kwargs)
        return sample_return