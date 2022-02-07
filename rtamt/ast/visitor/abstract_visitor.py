from abc import ABCMeta

from abc import ABCMeta, abstractmethod

from rtamt.node.unary_node import UnaryNode
from rtamt.node.binary_node import BinaryNode
from rtamt.node.leaf_node import LeafNode

class AbstractASTVisitor(object):
    __metaclass__ = ABCMeta

    NOT_IMPLEMENTED = "You should implement this."

    def visit(self, node, *args, **kwargs):
        out_pre = self.pre(node, *args, **kwargs)
        out_children = self.visitChildren(node, *args, **kwargs)
        out_post = self.post(out_children, node, *args, **kwargs)
        return out_post

    def visitChildren(self, node, *args, **kwargs):
        out_children = list()
        for node_child in node.children:
            out = self.visit(node_child, *args, **kwargs)
            out_children.append(out)
        return out_children

    def pre(self, node, *args, **kwargs):
        return None

    def post(self, out_children, node, *args, **kwargs):
        return None