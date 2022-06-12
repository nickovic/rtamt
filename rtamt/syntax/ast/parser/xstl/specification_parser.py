from rtamt.syntax.ast.parser.abstract_ast_parser import ast_factory


def StlAst():
    antrlLexerType = globals()['XStlLexer']
    antrlParserType = globals()['XStlParser']
    parserErrorListenerType = globals()['STLParserErrorListener']   #optional
    xstlAst = ast_factory(XStlAstParserVisitor)(antrlLexerType, antrlParserType, parserErrorListenerType)
    return xstlAst
