parser grammar StlExtendedParser ;
import StlParser;

options {
	tokenVocab = StlExtendedLexer ;
}

expression
	:
    real_expression                                             #ExprReal
    | expression comparisonOp expression                        #ExprPredicate
	| LPAREN expression RPAREN                                  #ExprParen
	| NotOperator expression                                    #ExprNot

    | expression OrOperator expression                          #ExprOr
    | expression AndOperator expression                         #ExprAnd
    | expression ImpliesOperator expression                     #ExprImplies
    | expression IffOperator expression                         #ExprIff
    | expression XorOperator expression                         #ExprXor

	| AlwaysOperator ( interval )? expression                   #ExprAlways
    | EventuallyOperator ( interval )? expression               #ExprEv
    | expression UntilOperator ( interval )? expression         #ExprUntil
    | expression UnlessOperator ( interval )? expression        #ExprUnless
    | HistoricallyOperator ( interval )? expression             #ExprHist
    | OnceOperator ( interval )? expression                     #ExpreOnce
    | expression SinceOperator ( interval )? expression         #ExprSince
    | expression BacktoOperator ( interval )? expression        #ExprBackto
    | RiseOperator LPAREN expression RPAREN                     #ExprRise
    | FallOperator LPAREN expression RPAREN                     #ExprFall
    | PreviousOperator expression                               #ExprPrevious
    | NextOperator expression                                   #ExprNext
	;
