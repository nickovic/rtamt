parser grammar TimeParser ;

options {
	tokenVocab = TimeLexer
	;
}

unit
    : SEC | MSEC | USEC | NSEC ;

intervalTime
	: literal ( unit )?      #intervalTimeLiteral
	| Identifier ( unit )?   #constantTimeLiteral ;

interval
	: LBRACK intervalTime ( COLON | COMMA ) intervalTime RBRACK ;