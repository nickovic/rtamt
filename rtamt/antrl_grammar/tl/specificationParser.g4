parser grammar specificationParser ;

options {
	tokenVocab = specificationLexer
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

modimport
	: From Identifier Import Identifier #modImport
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