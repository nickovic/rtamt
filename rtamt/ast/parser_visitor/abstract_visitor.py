from abc import ABCMeta, abstractmethod

class AbstractVisitor(object):
    __metaclass__ = ABCMeta

    def visitChildren(self, node, *args, **kwargs):
        children_out = list()
        for nodeChild in node.children:
            out = self.visit(nodeChild, *args, **kwargs)
            children_out.append(out)
        return children_out

    def visit(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)