from abc import ABCMeta

class AbstractASTVisitor(object):
    __metaclass__ = ABCMeta

    def visit(self, node, *args, **kwargs):
        result = None
        for child_node in node.children:
            result = self.visit(child_node, *args, **kwargs)
        return result