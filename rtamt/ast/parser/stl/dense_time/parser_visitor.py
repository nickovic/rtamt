from rtamt.ast.parser.stl.parser_visitor import StlAstParserVisitor

class StlDenseTimeAstParserVisitor(StlAstParserVisitor):

    def visitIntervalTimeLiteral(self, ctx):
        text = ctx.literal().getText()
        out = float(text)

        if ctx.unit() != None:
            unit = ctx.unit().getText()
            if (unit == 'ps'):
                out = out * 1e-12
            elif (unit == 'ms'):
                out = out * 1e-3
            elif (unit == 'us'):
                out = out * 1e-6
            elif (unit == 'ns'):
                out = out * 1e-9
            else:
                pass

        return out
