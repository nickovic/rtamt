
class AbstractGenerateVisitor(object):
    def __init__(self, rtamtASTvisitor, spec):
        __metaclass__ = rtamtASTvisitor
        self.spec = spec

    def generate(self, node, *args, **kargs):
        self.visit(node, *args)
