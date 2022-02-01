# -*- coding: utf-8 -*-

from rtamt.parser.stl.StlLexer import StlLexer
from rtamt.parser.stl.StlParser import StlParser
from rtamt.parser.stl.error.parser_error_listener import STLParserErrorListener
from rtamt.ast.parser.stl.discrete_time.parser_visitor import StlDiscreteTimeAstParserVisitor
from rtamt.ast.parser.abstract_ast_parser import ast_factory


def stlDiscreteTimeAst():
    antrlLexerType = globals()['StlLexer']
    antrlParserType = globals()['StlParser']
    parserErrorListenerType = globals()['STLParseException']   #optional
    stLAst = ast_factory(StlDiscreteTimeAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    return stLAst
