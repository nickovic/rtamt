from rtamt.parser.ltl.LtlLexer import LtlLexer
from rtamt.parser.ltl.LtlParser import LtlParser
from rtamt.ast.parser.ltl.parser_visitor import LtlAstParserVisitor
from rtamt.exception.ltl.exception import LTLParseException

from rtamt.ast.parser.abstract_ast_parser import ast_factory


def LtlAst():
    #TODO we may explain why we need to write like this.
    antrlLexerType = globals()['LtlLexer']
    antrlParserType = globals()['LtlParser']
    parseExceptionType = globals()['LTLParseException']   #optional
    ltLAst = ast_factory(LtlAstParserVisitor)(antrlLexerType, antrlParserType, parseExceptionType)
    return ltLAst
