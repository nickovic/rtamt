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
	ABS LPAREN expression RPAREN                                #ExprAbs
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
    | RiseOperator LPAREN expression RPAREN                     #ExprRise
    | FallOperator LPAREN expression RPAREN                     #ExprFall
    | PreviousOperator expression                               #ExprPrevious
    | NextOperator expression                                   #ExprNext

    | expression UntilOperator ( interval )? expression         #ExprUntil
    | expression UnlessOperator ( interval )? expression        #ExprUnless
    | expression SinceOperator ( interval )? expression         #ExprSince

	| expression AndOperator expression                         #ExprAnd
    | expression IffOperator expression                         #ExprIff
	| expression OrOperator expression                          #ExprOr
    | expression ImpliesOperator expression                     #ExprImplies
    | expression XorOperator expression                         #ExprXor

    | LPAREN expression RPAREN                                  #ExprParen
    | literal                                                   #ExprLiteral
    | Identifier                                                #ExprId
	;