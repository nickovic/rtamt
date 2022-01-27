from rtamt.parser.ltl.LtlLexer import LtlLexer
from rtamt.parser.ltl.LtlParser import LtlParser
from rtamt.ast.parser.ltl.paser_visitor import LtlAstParserVisitor
from rtamt.exception.ltl.exception import LTLParseException

from rtamt.ast.parser.abstract_ast_parser import AbstractAst


class LtlAst(AbstractAst, LtlAstParserVisitor):

    def __init__(self):
        #TODO we may explain why we need to write like this.
        antrlLexerType = globals()['LtlLexer']
        antrlParserType = globals()['LtlParser']
        parseExceptionType = globals()['LTLParseException']   #optional
        super(LtlAst, self).__init__(antrlLexerType, antrlParserType, parseExceptionType)
