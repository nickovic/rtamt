from rtamt.syntax.ast.parser.abstract_ast_parser import ast_factory
from rtamt.syntax.ast.parser.xstl.parser_visitor import XStlAstParserVisitor
from rtamt.antlr.parser.xstl.XStlLexer import XStlLexer
from rtamt.antlr.parser.xstl.XStlParser import XStlParser
from rtamt.antlr.parser.xstl.error.parser_error_listener import XSTLParserErrorListener


def XStlAst():
    antrlLexerType = globals()['XStlLexer']
    antrlParserType = globals()['XStlParser']
    parserErrorListenerType = globals()['XSTLParserErrorListener']   #optional
    xstlAst = ast_factory(XStlAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    return xstlAst
