lexer grammar LtlLexer ;


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

SQRT
    : 'sqrt' ;

EXP
    : 'exp' ;

POW
    : 'pow' ;

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

NotOperator
	: 'not' | '!';

OrOperator
	: 'or' | '|';

AndOperator
	: 'and' | '&' ;

IffOperator
	: 'iff'
	| '<->' ;

ImpliesOperator
	: 'implies'
	| '->' ;

XorOperator
	: 'xor' ;

RiseOperator
	: 'rise' ;

FallOperator
	: 'fall' ;

AlwaysOperator
	: 'always' | 'G' ;

EventuallyOperator
	: 'eventually' | 'F' ;

UntilOperator
	: 'until' | 'U' ;

UnlessOperator
	: 'unless' | 'W' ;

HistoricallyOperator
	: 'historically' | 'H' ;

OnceOperator
	: 'once' | 'O' ;

SinceOperator
	: 'since' | 'S' ;

NextOperator
	: 'next' | 'X' ;

PreviousOperator
	: 'prev' | 'Y' ;

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


fragment BinaryDigitOrUnderscore
	: BinaryDigit
	| '_' ;

RealLiteral
	: DecimalRealLiteral ;

fragment DecimalRealLiteral
	: Digits '.' Digits? ExponentPart?
	| '.' Digits ExponentPart?
	| Digits ExponentPart
	;

fragment ExponentPart
	: ExponentIndicator SignedInteger ;

fragment ExponentIndicator
	: [eE] ;

fragment SignedInteger
	: Sign? Digit+ ;

fragment Sign
	: [+-] ;


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

