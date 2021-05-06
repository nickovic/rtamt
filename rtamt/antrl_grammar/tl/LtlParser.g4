parser grammar LtlParser ;
import arithmeticParser, specifcationParser ;

options {
	tokenVocab = LtlLexer
	;
}

assignment
	: EQUAL literal 				#AsgnLiteral
	| EQUAL expression 				#AsgnExpr
	;

domainType
	: DomainTypeFloat
	| DomainTypeInt
    | DomainTypeLong
    | DomainTypeComplex
    | Identifier
    ;

ioType
	: Input
	| Output
	;


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

	| AlwaysOperator expression                                 #ExprAlways
    | EventuallyOperator expression                             #ExprEv
    | expression UntilOperator expression                       #ExprUntil
    | expression UnlessOperator expression                      #ExprUnless
    | HistoricallyOperator expression                           #ExprHist
    | OnceOperator expression                                   #ExpreOnce
    | expression SinceOperator expression                       #ExprSince
    | RiseOperator LPAREN expression RPAREN                     #ExprRise
    | FallOperator LPAREN expression RPAREN                     #ExprFall
    | PreviousOperator expression                               #ExprPrevious
    | NextOperator expression                                   #ExprNext
	;

comparisonOp
	: LesserOrEqualOperator                                     #Leq
	| GreaterOrEqualOperator 				                    #Geq
	| LesserOperator                                            #Less
	| GreaterOperator                                           #Greater
    | EqualOperator                                             #Eq
    | NotEqualOperator                                          #Neq
	;

literal
	: IntegerLiteral
	| RealLiteral
	| MINUS literal
	;

identifier
	: Identifier											 #Id
	;

