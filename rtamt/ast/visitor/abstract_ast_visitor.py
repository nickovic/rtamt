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
            next_node = node.children[0]
            return [next_node]
        elif isinstance(node, BinaryNode):
            next_node_left = node.children[0]
            next_node_right = node.children[1]
            return [next_node_left, next_node_right]
        if isinstance(node, LeafNode):
            raise AstVisitorException('Do not call visitAbstractAst in LeafNode!')
        else:
            raise AstVisitorException('{} is not RTAMT AST node'.format(node.__class__.__name__))

    def visitAbstractAstChildrenBottomUp(self, node, *args, **kwargs):
        if isinstance(node, UnaryNode):
            sample = self.visitAbstractAstChildrenBottomUp(node.children[0])
            sample_return = self.visitSpecific(node, sample, *args, **kwargs)
            return sample_return
        elif isinstance(node, BinaryNode):
            sample_left = self.visitAbstractAstChildrenBottomUp(node.children[0])
            sample_right = self.visitAbstractAstChildrenBottomUp(node.children[1])
            sample_return = self.visitSpecific(node, sample_left, sample_right, *args, **kwargs)
            return sample_return
        if isinstance(node, LeafNode):
            sample_return = self.visitSpecific(node, *args, **kwargs)
            return sample_return
        else:
            raise AstVisitorException('{} is not RTAMT AST node'.format(node.__class__.__name__))

    def visitAbstractAstChildrenTopDown(self, node, *args, **kwargs):
        if isinstance(node, UnaryNode):
            self.visitSpecific(node, *args, **kwargs)
            self.visitAbstractAstChildrenTopDown(node.children[0])
        elif isinstance(node, BinaryNode):
            self.visitSpecific(node, *args, **kwargs)
            self.visitAbstractAstChildrenTopDown(node.children[0])
            self.visitAbstractAstChildrenTopDown(node.children[1])
        if isinstance(node, LeafNode):
            self.visitSpecific(node, *args, **kwargs)
        else:
            raise AstVisitorException('{} is not RTAMT AST node'.format(node.__class__.__name__))

    def visitManual(self, ast, *args, **kwargs):
        self.ast = ast
        self.visitAbstractAstChildren(self.ast.ast, *args, **kwargs)
        return None, self.ast

    def visitBottomUp(self, ast, *args, **kwargs):
        self.ast = ast
        sample_return = self.visitAbstractAstChildrenBottomUp(self.ast.ast, *args, **kwargs)
        return sample_return, self.ast

    def visitTopDown(self, ast, *args, **kwargs):
        self.ast = ast
        self.visitAbstractAstChildrenTopDown(self.ast.ast, *args, **kwargs)
        return None, self.ast

    @abstractmethod
    def visitSpecific(self, node, *args, **kwargs):
        sample_return = None
        return sample_return