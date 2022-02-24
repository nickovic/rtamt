# -*- coding: utf-8 -*-
from rtamt.ast.parser.stl.parser_visitor import StlAstParserVisitor
from rtamt.parser.stl.StlLexer import StlLexer
from rtamt.parser.stl.StlParser import StlParser
from rtamt.ast.parser.abstract_ast_parser import ast_factory
from rtamt.parser.stl.error.parser_error_listener import STLParserErrorListener


def stlAst():
    antrlLexerType = globals()['StlLexer']
    antrlParserType = globals()['StlParser']
    parserErrorListenerType = globals()['STLParserErrorListener']   #optional
    stlAst = ast_factory(StlAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    return stlAst
