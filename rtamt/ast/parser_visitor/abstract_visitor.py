from abc import ABCMeta, abstractmethod

class AbstractVisitor(object):
    __metaclass__ = ABCMeta

    def visitNextLayerNodes(self, node, *args, **kwargs):
        for nodeChild in node.children:
            self.visit(nodeChild, args)

    def visit(self, node, *args, **kwargs):
        out = None
        self.visitNextLayerNodes(node, args)
        out = self.visitHarness(node, args)
        return out

    @abstractmethod
    def visitHarness(self, node, *args, **kwargs):
        pass