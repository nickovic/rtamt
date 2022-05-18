parser grammar LtlParser ;

options {
	tokenVocab = LtlLexer
	;
}

specification_file
	: specification EOF
	;

specification
    : ( spec )? ( modimport )* ( declaration | annotation )* ( assertion )+
    ;

spec
	: Specification Identifier #SpecificationId
	;

modimport :
        From Identifier Import Identifier #modImport
        ;

assertion 
	: (Identifier EQUAL)? expression
	;

declaration 
	: variableDeclaration                                         #declVariable
	| constantDeclaration                                         #declConstant
	;

annotation
        : '@' annotation_type ;

annotation_type
        : ROS_Topic LPAREN Identifier COMMA Identifier RPAREN #rosTopic
        ;

variableDeclaration
	: ioType? domainType Identifier assignment?
	;

constantDeclaration
	: Constant domainType Identifier EQUAL literal
	;

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

real_expression:
    Identifier                                                  #ExprId
    | literal                                                   #ExprLiteral
    | real_expression PLUS real_expression                      #ExprAddition
	| real_expression MINUS real_expression                     #ExprSubtraction
	| real_expression TIMES real_expression                     #ExprMultiplication
	| real_expression DIVIDE real_expression                    #ExprDivision

	| ABS LPAREN real_expression RPAREN                         #ExprAbs
	| SQRT LPAREN real_expression RPAREN                        #ExprSqrt
	| EXP LPAREN real_expression RPAREN                         #ExprExp
	| POW LPAREN real_expression COMMA real_expression RPAREN   #ExprPow
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

