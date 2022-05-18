from antlr4.error.ErrorListener import ErrorListener
from rtamt.exception.ltl.exception import LTLParseException

class LTLParserErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise LTLParseException (str(line) + ":" + str(column) + ": Syntax ERROR, " + str(msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise LTLParseException("Ambiguity ERROR, " + str(configs))

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise LTLParseException("Attempting full context ERROR, " + str(configs))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise LTLParseException("Context ERROR, " + str(configs))
