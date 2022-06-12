from rtamt.antlr.parser.xstl.XStlParserVisitor import XStlParserVisitor
from rtamt.syntax.ast.parser.stl.parser_visitor import StlAstParserVisitor
from rtamt.syntax.node.xstl.shift import Shift


class XStlAstParserVisitor(StlAstParserVisitor, XStlParserVisitor):

    def __init__(self):
        StlAstParserVisitor.__init__(self)
        XStlParserVisitor.__init__(self)

    def visitExprShift(self, ctx):
        child = self.visit(ctx.expression())
        val = self.visit(ctx.literal())
        node = Shift(child, val)
        return node
