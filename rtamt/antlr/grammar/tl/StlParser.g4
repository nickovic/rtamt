parser grammar StlParser ;
import LtlParser;

options {
	tokenVocab = LtlLexer ;
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
	LPAREN expression RPAREN                                    #ExprParen

	| ABS LPAREN expression RPAREN                              #ExprAbs
	| SQRT LPAREN expression RPAREN                             #ExprSqrt
	| EXP LPAREN expression RPAREN                              #ExprExp
	| POW LPAREN expression COMMA expression RPAREN             #ExprPow

    | expression TIMES expression                               #ExprMultiplication
	| expression DIVIDE expression                              #ExprDivision
	| expression PLUS expression                                #ExprAddition
	| expression MINUS expression                               #ExprSubtraction

	| expression comparisonOp expression                        #ExprPredicate

	| NotOperator expression                                    #ExprNot

	| AlwaysOperator ( interval )? expression                   #ExprAlways
    | EventuallyOperator ( interval )? expression               #ExprEv
    | HistoricallyOperator ( interval )? expression             #ExprHist
    | OnceOperator ( interval )? expression                     #ExpreOnce

    | PreviousOperator expression                               #ExprPrevious
    | NextOperator expression                                   #ExprNext
    | StrongPreviousOperator expression                         #ExprStrongPrevious
    | StrongNextOperator expression                             #ExprStrongNext

    | expression UntilOperator ( interval )? expression         #ExprUntil
    | expression UnlessOperator ( interval )? expression        #ExprUnless
    | expression SinceOperator ( interval )? expression         #ExprSince

    | expression AndOperator expression                         #ExprAnd
    | expression OrOperator expression                          #ExprOr
    | expression ImpliesOperator expression                     #ExprImplies
    | expression IffOperator expression                         #ExprIff
    | expression XorOperator expression                         #ExprXor

    | RiseOperator LPAREN expression RPAREN                     #ExprRise
    | FallOperator LPAREN expression RPAREN                     #ExprFall

    | Identifier                                                 #ExprId
    | literal                                                    #ExprLiteral
	;