from abc import ABCMeta

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

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

class XParserErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise

class AbstractAst:

    __metaclass__ = ABCMeta

    def __init__(self, antrlLexerType, antrlParserType, parserErrorListenerType = None):
        self.ast = []
        self.ast_dict = {"req":1, "gnt":2, "rob":3}

        #TODO we need class check which inherits expected abstrauct class.
        self.antrlLexerType = antrlLexerType
        self.antrlParserType = antrlParserType
        self.parserErrorListenerType = parserErrorListenerType
        return

    def parse(self):
        input_stream = InputStream(self.spec)
        lexer = self.antrlLexerType(input_stream)

        stream = CommonTokenStream(lexer)
        parser = self.antrlParserType(stream)
        if self.parserErrorListenerType != None:
            parser._listeners = [self.parserErrorListenerType()]
        ctx = parser.specification_file()

        # Create the visitor for the actual spec nodes
        # self.node = self.visit(ctx.specification()) #temporally comentout

        return

    def print_ast_dict_from_AbstractAst(self):
        print(self.ast_dict)

    def declare_var(self, name, type):
        pass

def ast_factory(AstParserVisitor):
    class Ast(AbstractAst, AstParserVisitor):
        def __init__(self, antrlLexerType, antrlParserType, parserErrorListenerType=None):
            super(Ast, self).__init__(antrlLexerType, antrlParserType, parserErrorListenerType)
    return Ast

#---- user define ----#
# Instance class of X language
# /rtamt/rtamt/ast/parser/stl/discrete_time/specification_parser.py
#TODO we may explain why we need to write like this.
class XAstParserVisitor(XANTRLparserVisitor):

    __metaclass__ = ABCMeta

    # write only ANTRL parserVisitor over write for each node.
    def visitExprUntil(self, ctx):
        child1 = self.visit(ctx.expression(0))
        child2 = self.visit(ctx.expression(1))
        node = None
        return node

    def print_ast_dict_from_XAstParserVisitor(self):
        print(self.ast_dict)


# This function is factory function to instance of Xast class.
# The name rule is class even it is function. However the nameing will avoid user misunderstanding.
def XAst():

    #TODO we may explain why we need to write like this.
    antrlLexerType = globals()['XantrlLexer']
    antrlParserType = globals()['XantrlParser']
    parserErrorListenerType = globals()['XParserErrorListener'] # optional
    xAst = ast_factory(XAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    return xAst

#TODO We may discuss how much programmer need to think here.
# /rtamt/rtamt/ast/visitor/stl/ASTVisitor.py
class AbstructXAstVisitor:
    __metaclass__ = ABCMeta

    def visit(self, node, args):
        # dummy
        pass

    #@abstractmethod
    def visitUntil(self, node, args):
        raise NotImplementedError(NOT_IMPLEMENTED)

    def visitAst(self, ast):
        self.ast = ast
        self.visit(self.ast, "hoge")

    def print_ast_dict_from_AbstructXAstVisitor(self):
        print(self.ast.ast_dict)


#---- user define [Optional]----#
# /rtamt/rtamt/evaluator/stl/dense_time/offline/python/offline_dense_time_python_monitor.py
#TODO exchange some of semantics
class XNamePrintAstVistor(AbstructXAstVisitor):

    __metaclass__ = ABCMeta

    # write AST spesific operation.
    def visitUntil(self, node, args):
        monitor = UntilOperation()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)


xAst = XAst()
xAst.print_ast_dict_from_AbstractAst() #access test
xAst.print_ast_dict_from_XAstParserVisitor() #access test
xAst.name = 'STL test'
xAst.declare_var('a', 'float') #Where should we put this? ast? or semanitcs?
xAst.spec = 'always(a>=2)'
xAst.parse()

namePrintAstVistor = XNamePrintAstVistor()
namePrintAstVistor.visitAst(xAst)
namePrintAstVistor.print_ast_dict_from_AbstructXAstVisitor() #access test

#namePrintAstVistor.visit()