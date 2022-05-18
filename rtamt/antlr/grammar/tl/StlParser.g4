parser grammar StlParser ;
import LtlParser;

options {
	tokenVocab = StlLexer ;
}

interval
	: LBRACK intervalTime ( COLON | COMMA ) intervalTime RBRACK ;

intervalTime
	: literal ( unit )?      #intervalTimeLiteral
	| Identifier ( unit )?   #constantTimeLiteral ;

unit
    : SEC | MSEC | USEC | NSEC ;


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
    | RiseOperator LPAREN expression RPAREN                     #ExprRise
    | FallOperator LPAREN expression RPAREN                     #ExprFall
    | PreviousOperator expression                               #ExprPrevious
    | NextOperator expression                                   #ExprNext
	;
