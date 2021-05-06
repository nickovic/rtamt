parser grammar arithmeticParser ;

options {
	tokenVocab = arithmeticLexer
	;
}

real_expression:
    Identifier                                                  #ExprId
    | literal                                                   #ExprLiteral
    | real_expression PLUS real_expression                      #ExprAddition
	| real_expression MINUS real_expression                     #ExprSubtraction
	| real_expression TIMES real_expression                     #ExprMultiplication
	| real_expression DIVIDE real_expression                    #ExprDivision

	| ABS LPAREN real_expression RPAREN                         #ExprAbs
	;