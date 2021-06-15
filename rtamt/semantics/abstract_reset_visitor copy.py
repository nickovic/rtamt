
class AbstractEvalVisitor(object):
    def __init__(self, rtamtASTvisitor):
        __metaclass__ = rtamtASTvisitor

    def reset(self, node, *args, **kargs):
        sample = self.visit(node, *args)
