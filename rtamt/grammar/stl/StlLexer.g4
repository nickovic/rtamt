lexer grammar StlLexer ;


// Rules prefixed with fragment can be called only from other lexer rules;
// they are not tokens in their own right.

// Separators

MINUS
    : '-' ;

PLUS
    : '+' ;

TIMES
    : '*' ;

DIVIDE
    : '/' ;

LPAREN
	: '(' ;

RPAREN
	: ')' ;

LBRACE
	: '{' ;

RBRACE
	: '}' ;

LBRACK
	: '[' ;

RBRACK
	: ']' ;

SEMICOLON
	: ';' ;

COLON
	: ':' ;

COMMA
	: ',' ;

DOT
	: '.' ;

AT
        : '@' ;

ABS
    : 'abs' ;

SEC
    : 's' ;

MSEC
    : 'ms' ;

USEC
    : 'us' ;

NSEC
    : 'ns' ;

PSEC
    : 'ps' ;

ROS_Topic
        : 'topic' ;

        
Import
        : 'import' ;

Input
	: 'input' ;

Output
	: 'output' ;

Internal
	: 'internal' ;

Constant
	: 'const' ;

DomainTypeReal
	: 'real' ;

DomainTypeFloat
	: 'float' ;

DomainTypeLong
	: 'long' ;

DomainTypeComplex
	: 'complex' ;

DomainTypeInt
	: 'int' ;

DomainTypeBool
	: 'bool' ;

Assertion
	: 'assertion' ;
	
Specification
	: 'specification';

From
	: 'from' ;

// Boolean operators
NotOperator
	: 'not' ;

OrOperator
	: 'or' ;

AndOperator
	: 'and' ;

IffOperator
	: 'iff'
	| '<->' ;

ImpliesOperator
	: 'implies'
	| '->' ;

XorOperator
	: 'xor' ;

// Event operators
RiseOperator
	: 'rise' ;

FallOperator
	: 'fall' ;

// Future temporal operators
AlwaysOperator
	: 'always' ;

EventuallyOperator
	: 'eventually' ;

UntilOperator
	: 'until' ;

// Past temporal operators
HistoricallyOperator
	: 'historically' ;

OnceOperator
	: 'once' ;

SinceOperator
	: 'since' ;

//----------------
//added
NextOperator
	: 'next' ;

//added
OracleOperator
	: 'oracle' ;
//----------------

PreviousOperator
	: 'prev' ;

EqualOperator
	: '==' ;

NotEqualOperator
	: '!==' ;

GreaterOrEqualOperator
	: '>=' ;

LesserOrEqualOperator
	: '<=' ;

GreaterOperator
	: '>' ;

LesserOperator
	: '<' ;

EQUAL
	: '=' ;

// Literals
BooleanLiteral
	: (TRUE | FALSE) ;

TRUE
	: ('true' | 'TRUE');

FALSE
	: ('false' | 'FALSE');

// Integer Literals

IntegerLiteral
	: DecimalNumeral
	| HexNumeral
	| BinaryNumeral ;

fragment DecimalNumeral
	: '0'
	| NonZeroDigit (Digits? | Underscores Digits) ;

fragment Digits
	: Digit (DigitsAndUnderscores? Digit)? ;

fragment Digit
	: '0'
	| NonZeroDigit ;

fragment NonZeroDigit
	: [1-9] ;

fragment DigitsAndUnderscores
	: DigitOrUnderscore+ ;

fragment DigitOrUnderscore
	: Digit
	| '_' ;

fragment Underscores
	: '_'+ ;

fragment HexNumeral
	: '0' [xX] HexDigits ;

fragment HexDigits
	: HexDigit (HexDigitsAndUnderscores? HexDigit)? ;

fragment HexDigit
	: [0-9a-fA-F] ;

fragment HexDigitsAndUnderscores
	: HexDigitOrUnderscore+ ;

fragment HexDigitOrUnderscore
	: HexDigit
	| '_' ;

fragment BinaryNumeral
	: '0' [bB] BinaryDigits ;

fragment BinaryDigits
	: BinaryDigit (BinaryDigitsAndUnderscores? BinaryDigit)? ;

fragment BinaryDigit
	: [01] ;

fragment BinaryDigitsAndUnderscores
	: BinaryDigitOrUnderscore+ ;

// long bytes = 0b11010010_01101001_10010100_10010010;

fragment BinaryDigitOrUnderscore
	: BinaryDigit
	| '_' ;

// Floating-Point Literals

RealLiteral
	: DecimalRealLiteral ;

fragment DecimalRealLiteral
	: Digits '.' Digits? ExponentPart?
	| '.' Digits ExponentPart?
	| Digits ExponentPart
//	|	Digits FloatTypeSuffix
	;

fragment ExponentPart
	: ExponentIndicator SignedInteger ;

fragment ExponentIndicator
	: [eE] ;

fragment SignedInteger
	: Sign? Digit+ ;

fragment Sign
	: [+-] ;

// Identifier (must appear after all keywords in the grammar)

Identifier
	: ((IdentifierStart)(IdentifierPart)*) ;


fragment IdentifierStart
	: (LetterOrUnderscore | '$') ;

fragment IdentifierPart
	: ( IdentifierStart | Digit | '.' | '/' ) ;

fragment LetterOrUnderscore
	: (Letter | '_') ;

fragment Letter
	: [A-Za-z] ;



// Whitespace and comments
//
LINE_TERMINATOR
	: [\n] -> skip ;

WHITESPACE
	: [ \t\r\u000C]+ -> skip ;

COMMENT
	: '/*' .*? '*/' -> skip ;

LINE_COMMENT
	: '//' ~[\r\n]* -> skip ;

