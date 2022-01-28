# -*- coding: utf-8 -*-

from rtamt.parser.stl.StlLexer import StlLexer
from rtamt.parser.stl.StlParser import StlParser
from rtamt.ast.parser.stl.dense_time.parser_visitor import StlDenseTimeAstParserVisitor
from rtamt.exception.stl.exception import STLParseException

from rtamt.ast.parser.abstract_ast_parser import ast_factory


def stlDenseTimeAst():
    antrlLexerType = globals()['StlLexer']
    antrlParserType = globals()['StlParser']
    parseExceptionType = globals()['STLParseException']   #optional
    stLAst = ast_factory(StlDenseTimeAstParserVisitor)(antrlLexerType, antrlParserType, parseExceptionType)
    return stLAst
