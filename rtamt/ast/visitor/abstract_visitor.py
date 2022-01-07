from abc import ABCMeta

class AbstractVisitor(object):
    __metaclass__ = ABCMeta

    def visitChildren(self, node, *args, **kwargs):
        children_output = list()
        for nodeChild in node.children:
            output = self.visit(nodeChild, *args, **kwargs)
            children_output.append(output)
        return children_output

    def visit(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)