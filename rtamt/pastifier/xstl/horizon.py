from rtamt.pastifier.stl.horizon import StlHorizon
from rtamt.exception.stl.exception import STLException
from rtamt.syntax.ast.visitor.xstl.ast_visitor import XStlAstVisitor


class XStlHorizon(StlHorizon, XStlAstVisitor):

    def __init__(self):
        StlHorizon.__init__(self)

    def visit(self, node, *args, **kwargs):
        return XStlAstVisitor.visit(self, node, *args, **kwargs)

    def visitShift(self, node, *args, **kwargs):
        op_horizon = self.visit(node.children[0], *args, **kwargs)

        if node.val >= 0:
            return op_horizon + node.end
        else:
            return op_horizon

    def visitDefault(self, node):
        raise STLException('STL Pastifier: encountered unexpected type of node.')