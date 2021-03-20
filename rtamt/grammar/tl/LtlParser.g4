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

	ABS LPAREN expression RPAREN                                #ExprAbs
	| expression TIMES expression                               #ExprMultiplication
	| expression DIVIDE expression                              #ExprDivision
	| expression PLUS expression                                #ExprAddition
	| expression MINUS expression                               #ExprSubtraction

	| NotOperator expression                                    #ExprNot
	| AlwaysOperator expression                                 #ExprAlways
    | EventuallyOperator expression                             #ExprEv
    | HistoricallyOperator expression                           #ExprHist
    | OnceOperator expression                                   #ExpreOnce
    | RiseOperator LPAREN expression RPAREN                     #ExprRise
    | FallOperator LPAREN expression RPAREN                     #ExprFall
    | PreviousOperator expression                               #ExprPrevious
    | NextOperator expression                                   #ExprNext

    | expression UntilOperator expression                       #ExprUntil
    | expression UnlessOperator expression                      #ExprUnless
    | expression SinceOperator expression                       #ExprSince

	| expression AndOperator expression                         #ExprAnd
    | expression IffOperator expression                         #ExprIff
	| expression OrOperator expression                          #ExprOr
    | expression ImpliesOperator expression                     #ExprImplies
    | expression XorOperator expression                         #ExprXor

	| expression comparisonOp expression              #ExprPredicate

    | LPAREN expression RPAREN                                  #ExprParen
    | literal                                                   #ExprLiteral
    | Identifier                                                #ExprId
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

