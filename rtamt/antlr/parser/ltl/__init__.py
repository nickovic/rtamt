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

if V(_antlr_runtime_version) <= V("4.9.3"):
    from rtamt.antlr.parser.ltl.antlr_4_9 import LtlLexer, LtlParser, LtlParserVisitor
else:
    from rtamt.antlr.parser.ltl.antlr_4_13 import LtlLexer, LtlParser, LtlParserVisitor

__all__ = [
    "LtlLexer",
    "LtlParser",
    "LtlParserVisitor"]