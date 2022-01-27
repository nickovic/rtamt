from rtamt.parser.ltl.LtlLexer import LtlLexer
from rtamt.parser.ltl.LtlParser import LtlParser
from rtamt.ast.parser.ltl.paser_visitor import LtlAstParserVisitor

from rtamt.ast.parser.abstract_ast_paser import AbstractAstPaser


class LtlAstParser(AbstractAstPaser, LtlAstParserVisitor):

    def __init__(self):
        #TODO we may explain why we need to write like this.
        antrlLexerType = globals()['LtlLexer']
        antrlParserType = globals()['LtlParser']
        super(LtlAstParser, self).__init__(antrlLexerType, antrlParserType,)
