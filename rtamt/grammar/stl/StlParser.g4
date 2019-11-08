parser grammar StlParser ;

options {
	tokenVocab = StlLexer ;
}

stlfile
	: stlSpecification EOF ;

stlSpecification
    : ( spec )? ( modimport )* ( declaration | annotation )* assertion ;
	
spec
	: Specification Identifier #Specification ;

modimport :
        From Identifier Import Identifier #modImport ;

assertion 
	: Identifier EQUAL expression ;

declaration 
	: variableDeclaration                                         #declVariable ;

annotation
        : '@' annotation_type ;

annotation_type
        : ROS_Topic LPAREN Identifier COMMA Identifier RPAREN #rosTopic;

variableDeclaration
	: Constant? ioType? domainType identifier assignment?  ;

assignment
	: EQUAL literal 				#AsgnLiteral
	| EQUAL expression 				#AsgnExpr ;

domainType
	: DomainTypeFloat
	| DomainTypeInt
    | DomainTypeLong
    | DomainTypeComplex
    | Identifier ;

ioType
	: Input
	| Output ;

interval
	: LBRACK intervalTime COLON intervalTime RBRACK ;

intervalTime
	: IntegerLiteral ( unit )?      #intervalTimeLiteral ;

unit
    : SEC | MSEC | USEC | NSEC | PSEC ;

 

// -- O -- O -- O -- O -- O -- O -- O -- O -- O -- O -- O -- O -- O  expression

expression
	: 
	idComp                                                      #ExprIdComp
	| Identifier                                                  #ExprId
	
	| LPAREN expression RPAREN                                  #ExprParen
	| NotOperator expression                                    #ExprNot

    | expression OrOperator expression                          #ExprOrExpr
    | expression AndOperator expression                         #ExprAndExpr
    | expression ImpliesOperator expression                     #ExprImpliesExpr
    | expression IffOperator expression                         #ExprIffExpr
    | expression XorOperator expression                         #ExprXorExpr

	| AlwaysOperator ( interval )? expression                   #ExprAlwaysExpr
    | EventuallyOperator ( interval )? expression               #ExprEvExpr
    | expression UntilOperator interval expression              #ExprUntilExpr
    | HistoricallyOperator ( interval )? expression             #ExprHistExpr
    | OnceOperator ( interval )? expression                     #ExpreOnceExpr
    | expression SinceOperator ( interval )? expression         #ExprSinceExpr
	;
	
idComp
	: Identifier comparisonOp literal    #IdCompInt
	;

comparisonOp
	: LesserOrEqualOperator                                     #CmpOpLs
	| GreaterOrEqualOperator 				    #CmpOpGte
	| LesserOperator                                            #CmpOpLse
	| GreaterOperator                                           #CmpOpGt 
    | EqualOperator                                             #CmpOpEq
    | NotEqualOperator                                          #ComOpNeq
	;
	
literal
	: IntegerLiteral		
	| RealLiteral			
	;

identifier
	: Identifier											 #Id ;

