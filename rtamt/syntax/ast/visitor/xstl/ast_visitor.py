from rtamt.exception.stl.exception import STLVisitorException
from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor
from rtamt.syntax.node.xstl.shift import Shift


class XStlAstVisitor(StlAstVisitor):

    def visit(self, node, *args, **kwargs):
        if isinstance(node, Shift):
            result = self.visitShift(node, *args, **kwargs)
        else:
            result = super(XStlAstVisitor, self).visit(node, *args, **kwargs)

        return result

    def visitShift(self, node, *args, **kwargs):
        return self.visitChildren(node, *args, **kwargs)

    def raise_exception(self, text):
        raise STLVisitorException(text)
