from abc import ABCMeta

from antlr4 import *
#from antlr4.InputStream import InputStream

DEBUG = True

#---- closed ----#
# dummys
def InputStream(input):
    return None

class XantrlLexer:
    def __init__(self, input):
        # dummy
        self.a = 100
        print('init XantrlLexer')
        return None

class XantrlParser:
    def __init__(self, input):
        # dummy
        print('intt XantrlParser')
        return None

    def specification_file(self):
        # dummy
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


class AbstractAstPaser:

    __metaclass__ = ABCMeta

    def __init__(self, antrlLexerType, antrlParserType, astPaserVisitorType):
        #TODO we need class check which inherits expected abstrauct class.
        self.antrlLexerType = antrlLexerType
        self.antrlParserType = antrlParserType
        self.astPaserVisitorType = astPaserVisitorType
        return

    def parse(self):
        input_stream = InputStream(self.spec)
        lexer = self.antrlLexerType(input_stream)

        stream = CommonTokenStream(lexer)
        parser = self.antrlParserType(stream)
        #parser._listeners = [STLParserErrorListener()]
        ctx = parser.specification_file()

        # Create the visitor for the actual spec nodes
        visitor = self.astPaserVisitorType()
        self.node = visitor.visit(ctx.specification())

        return self.node

    def declare_var(self, name, type):
        pass


#---- user define ----#
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


class XAstPaser(AbstractAstPaser):

    __metaclass__ = ABCMeta

    def __init__(self):
        #TODO we may explain why we need to write like this.
        antrlLexerType = globals()['XantrlLexer']
        antrlParserType = globals()['XantrlParser']
        astPaserVisitorType = globals()['XAstParserVisitor']
        super(XAstPaser, self).__init__(antrlLexerType, antrlParserType, astPaserVisitorType)
        return




xAstPaser = XAstPaser()
xAstPaser.name = 'STL test'
xAstPaser.declare_var('a', 'float') #Where should we put this? ast? or semanitcs?
xAstPaser.spec = 'always(a>=2)'
node = xAstPaser.parse()
#namePrintNamePrintXAstVistor = NamePrintXAstVistor(node)
#namePrintNamePrintXAstVistor.visit()