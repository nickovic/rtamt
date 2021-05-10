from abc import ABCMeta, abstractmethod

class AbstractVisitor(object):
    __metaclass__ = ABCMeta

    def visitNextLayerNodes(self, node, pre_out, *args, **kwargs):
        out = []
        for nodeChild in node.children:
            out.append(self.visit(nodeChild, pre_out, *args, **kwargs))
        return out

    def visit(self, node, *args, **kwargs):
        out = None
        pre_out = self.visitNextLayerNodes(node, out, *args, **kwargs)
        out = self.visitHarness(node, pre_out, *args, **kwargs)
        return out

    @abstractmethod
    def visitHarness(self, node, pre_out, *args, **kwargs):
        out = pre_out
        return out