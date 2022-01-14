from abc import ABCMeta

from antlr4 import *
#from antlr4.InputStream import InputStream




# dummys
def InputStream(input):
    return None

class XantrlLexer:
    def __init__(self, input):
        return None

class XantrlParser:
    def specification_file(input):
        return None


# ANTRL auto genrerated parser blank
# /rtamt/rtamt/parser/stl/StlParserVisitor.py
class XANTRLparserVisitor(ParseTreeVisitor):

    def visit(self, tree):
        # dummy
        pass

    # Visit a parse tree produced by StlParser#ExprUntil.
    def visitExprUntil(self, ctx):
        return self.visitChildren(ctx)


# Instance class of X language
# /rtamt/rtamt/ast/parser/stl/discrete_time/specification_parser.py
class XAstParserVisitor(XANTRLparserVisitor):

    __metaclass__ = ABCMeta

    # write only ANTRL parserVisitor over write for each node.
    def visitExprUntil(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = None
        return node


class AbstractAstPaser:

    __metaclass__ = ABCMeta

    def __init__(self, antrlLexer, antrlParser, astPaserVisitor):
        self.antrlLexer = antrlLexer
        self.antrlParser = antrlParser
        self.astPaserVisitor = astPaserVisitor
        return

    def parse(self):
        input_stream = InputStream(self.spec)
        lexer = self.antrlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = self.antrlParser(stream)
        #parser._listeners = [STLParserErrorListener()]
        ctx = parser.specification_file()

        # Create the visitor for the actual spec nodes
        visitor = self.astPaserVisitor()
        self.node = visitor.visit(ctx.specification())

        return self.node

    def declare_var(self, name, type):
        pass


class XAstPaser(AbstractAstPaser):

    __metaclass__ = ABCMeta

    def __init__(self):
        antrlLexer = XantrlLexer
        antrlParser = XantrlParser
        astPaserVisitor = XAstParserVisitor()
        super(XAstPaser, self).__init__(antrlLexer, antrlParser, astPaserVisitor)
        return




xAstPaser = XAstPaser()
xAstPaser.name = 'STL test'
xAstPaser.declare_var('a', 'float') #Where should we put this? ast? or semanitcs?
xAstPaser.spec = 'always(a>=2)'
ast = xAstPaser.parse()