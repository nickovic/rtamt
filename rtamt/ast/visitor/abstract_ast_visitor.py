from abc import ABCMeta

from rtamt.node.binary_node import BinaryNode
from rtamt.node.unary_node import UnaryNode
from rtamt.node.leaf_node import LeafNode

from rtamt.exception.exception import AstVisitorException


class AbstractAstVisitor(object):
    __metaclass__ = ABCMeta

    def visitChildren(self, node, *args, **kwargs):
        result = None
        for nodeChild in node.children:
            result = self.visit(nodeChild, *args, **kwargs)
        return result   # visitChildren reterns only last result

    def visit(self, node, *args, **kwargs):
        if isinstance(node, BinaryNode):
            result = self.visitBinary(node, *args, **kwargs)
        elif isinstance(node, UnaryNode):
            result = self.visitUnary(node, *args, **kwargs)
        elif isinstance(node, LeafNode):
            result = self.visitLeaf(node, *args, **kwargs)
        else:
            raise AstVisitorException('{} is not RTAMT AST node'.format(node.__class__.__name__))
        return result

    def visitAst(self, ast, *args, **kwargs):
        self.ast = ast
        return self.visit(ast.ast, *args, **kwargs)


    def visitBinary(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitUnary(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def visitLeaf(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)
