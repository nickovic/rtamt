from abc import ABCMeta, abstractmethod

class AbstractVisitor(object):
    __metaclass__ = ABCMeta

    def visit_children(self, node, *args, **kwargs):
        out = []
        for nodeChild in node.children:
            out.append(self.visit(nodeChild, *args, **kwargs))
        out.append(*args)
        return out

    def visit(self, node, *args, **kwargs):
        out = None
        new_args = self.pre_process(node, *args, **kwargs)
        pre_out = self.visit_children(node, *new_args, **kwargs)
        out = self.post_process(node, *pre_out, **kwargs)
        return out

    def pre_process(self, node, *args, **kwargs):
        return args

    def post_process(self, node, *args, **kwargs):
        return args