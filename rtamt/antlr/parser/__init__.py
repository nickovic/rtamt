from importlib.metadata import version, PackageNotFoundError
from packaging.version import parse as V

def _get_antlr_runtime_version():
    try:
        return version("antlr4-python3-runtime")
    except PackageNotFoundError:
        return None

_antlr_runtime_version = _get_antlr_runtime_version()

if _antlr_runtime_version is None:
    raise ImportError(
        "antlr4-python3-runtime package is not installed. Please install it to use rtamt/antlr/parser."
    )

print('I am here')

if V(_antlr_runtime_version) <= V("4.9.3"):
    from rtamt.antlr.parser.ltl.antlr_4_9 import LtlLexer, LtlParser, LtlParserVisitor
    from rtamt.antlr.parser.stl.antlr_4_9 import StlParser, StlParserVisitor
    print('Imported 4.9.3')
else:
    from rtamt.antlr.parser.ltl.antlr_4_13 import LtlLexer, LtlParser, LtlParserVisitor
    from rtamt.antlr.parser.stl.antlr_4_13 import StlParser, StlParserVisitor
    print('Imported 4.13')

__all__ = [
    "LtlLexer",
    "LtlParser",
    "LtlParserVisitor",
    "StlParser",
    "StlParserVisitor"]