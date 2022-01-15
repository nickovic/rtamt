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
        print('int XantrlParser')
        return None

    def specification_file(self, input):
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

    def __init__(self, antrlLexer__class__, antrlParser__class__, astPaserVisitor__class__):
        #TODO we need class check which inherits expected abstrauct class.
        self.antrlLexer__class__ = antrlLexer__class__
        self.antrlParser__class__ = antrlParser__class__
        self.astPaserVisitor__class__ = astPaserVisitor__class__
        return

    def parse(self):
        input_stream = InputStream(self.spec)
        lexer = self.antrlLexer__class__(input_stream)
        if DEBUG:
            print(isinstance(lexer, XantrlLexer))
            lexer = XantrlLexer(input_stream)
            print(isinstance(lexer, XantrlLexer))

        stream = CommonTokenStream(lexer)
        parser = self.antrlParser__class__(stream)
        #parser._listeners = [STLParserErrorListener()]
        ctx = parser.specification_file()

        # Create the visitor for the actual spec nodes
        visitor = self.astPaserVisitor__class__()
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
        antrlLexer__class__ = XantrlLexer.__class__
        antrlParser__class__ = XantrlParser.__class__
        astPaserVisitor__class__ = XAstParserVisitor.__class__
        super(XAstPaser, self).__init__(antrlLexer__class__, antrlParser__class__, astPaserVisitor__class__)
        return




xAstPaser = XAstPaser()
xAstPaser.name = 'STL test'
xAstPaser.declare_var('a', 'float') #Where should we put this? ast? or semanitcs?
xAstPaser.spec = 'always(a>=2)'
node = xAstPaser.parse()

#NamePrintAstVistor(node)