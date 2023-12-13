# Generated from rtamt/antlr/grammar/tl/LtlParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,75,253,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        1,3,1,43,8,1,1,1,5,1,46,8,1,10,1,12,1,49,9,1,1,1,1,1,5,1,53,8,1,
        10,1,12,1,56,9,1,1,1,4,1,59,8,1,11,1,12,1,60,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,3,4,73,8,4,1,4,1,4,1,5,1,5,3,5,79,8,5,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,3,8,92,8,8,1,8,1,8,1,8,3,8,
        97,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,109,8,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,3,13,153,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,5,13,179,8,13,10,13,12,13,182,9,13,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,3,14,215,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,5,14,229,8,14,10,14,12,14,232,9,14,1,15,
        1,15,1,15,1,15,1,15,1,15,3,15,240,8,15,1,16,1,16,1,16,1,16,1,16,
        3,16,247,8,16,1,17,1,17,1,18,1,18,1,18,0,2,26,28,19,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,0,3,2,0,32,36,71,71,1,0,27,
        28,1,0,67,68,283,0,38,1,0,0,0,2,42,1,0,0,0,4,62,1,0,0,0,6,65,1,0,
        0,0,8,72,1,0,0,0,10,78,1,0,0,0,12,80,1,0,0,0,14,83,1,0,0,0,16,91,
        1,0,0,0,18,98,1,0,0,0,20,108,1,0,0,0,22,110,1,0,0,0,24,112,1,0,0,
        0,26,152,1,0,0,0,28,214,1,0,0,0,30,239,1,0,0,0,32,246,1,0,0,0,34,
        248,1,0,0,0,36,250,1,0,0,0,38,39,3,2,1,0,39,40,5,0,0,1,40,1,1,0,
        0,0,41,43,3,4,2,0,42,41,1,0,0,0,42,43,1,0,0,0,43,47,1,0,0,0,44,46,
        3,6,3,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,
        48,54,1,0,0,0,49,47,1,0,0,0,50,53,3,10,5,0,51,53,3,12,6,0,52,50,
        1,0,0,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,
        55,58,1,0,0,0,56,54,1,0,0,0,57,59,3,8,4,0,58,57,1,0,0,0,59,60,1,
        0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,3,1,0,0,0,62,63,5,38,0,0,63,
        64,5,71,0,0,64,5,1,0,0,0,65,66,5,39,0,0,66,67,5,71,0,0,67,68,5,26,
        0,0,68,69,5,71,0,0,69,7,1,0,0,0,70,71,5,71,0,0,71,73,5,65,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,3,26,13,0,75,9,1,0,
        0,0,76,79,3,16,8,0,77,79,3,18,9,0,78,76,1,0,0,0,78,77,1,0,0,0,79,
        11,1,0,0,0,80,81,5,15,0,0,81,82,3,14,7,0,82,13,1,0,0,0,83,84,5,25,
        0,0,84,85,5,5,0,0,85,86,5,71,0,0,86,87,5,13,0,0,87,88,5,71,0,0,88,
        89,5,6,0,0,89,15,1,0,0,0,90,92,3,24,12,0,91,90,1,0,0,0,91,92,1,0,
        0,0,92,93,1,0,0,0,93,94,3,22,11,0,94,96,5,71,0,0,95,97,3,20,10,0,
        96,95,1,0,0,0,96,97,1,0,0,0,97,17,1,0,0,0,98,99,5,30,0,0,99,100,
        3,22,11,0,100,101,5,71,0,0,101,102,5,65,0,0,102,103,3,32,16,0,103,
        19,1,0,0,0,104,105,5,65,0,0,105,109,3,32,16,0,106,107,5,65,0,0,107,
        109,3,26,13,0,108,104,1,0,0,0,108,106,1,0,0,0,109,21,1,0,0,0,110,
        111,7,0,0,0,111,23,1,0,0,0,112,113,7,1,0,0,113,25,1,0,0,0,114,115,
        6,13,-1,0,115,153,3,28,14,0,116,117,3,28,14,0,117,118,3,30,15,0,
        118,119,3,28,14,0,119,153,1,0,0,0,120,121,5,5,0,0,121,122,3,26,13,
        0,122,123,5,6,0,0,123,153,1,0,0,0,124,125,5,40,0,0,125,153,3,26,
        13,19,126,127,5,48,0,0,127,153,3,26,13,13,128,129,5,49,0,0,129,153,
        3,26,13,12,130,131,5,52,0,0,131,153,3,26,13,9,132,133,5,53,0,0,133,
        153,3,26,13,8,134,135,5,46,0,0,135,136,5,5,0,0,136,137,3,26,13,0,
        137,138,5,6,0,0,138,153,1,0,0,0,139,140,5,47,0,0,140,141,5,5,0,0,
        141,142,3,26,13,0,142,143,5,6,0,0,143,153,1,0,0,0,144,145,5,56,0,
        0,145,153,3,26,13,4,146,147,5,55,0,0,147,153,3,26,13,3,148,149,5,
        58,0,0,149,153,3,26,13,2,150,151,5,57,0,0,151,153,3,26,13,1,152,
        114,1,0,0,0,152,116,1,0,0,0,152,120,1,0,0,0,152,124,1,0,0,0,152,
        126,1,0,0,0,152,128,1,0,0,0,152,130,1,0,0,0,152,132,1,0,0,0,152,
        134,1,0,0,0,152,139,1,0,0,0,152,144,1,0,0,0,152,146,1,0,0,0,152,
        148,1,0,0,0,152,150,1,0,0,0,153,180,1,0,0,0,154,155,10,18,0,0,155,
        156,5,41,0,0,156,179,3,26,13,19,157,158,10,17,0,0,158,159,5,42,0,
        0,159,179,3,26,13,18,160,161,10,16,0,0,161,162,5,44,0,0,162,179,
        3,26,13,17,163,164,10,15,0,0,164,165,5,43,0,0,165,179,3,26,13,16,
        166,167,10,14,0,0,167,168,5,45,0,0,168,179,3,26,13,15,169,170,10,
        11,0,0,170,171,5,50,0,0,171,179,3,26,13,12,172,173,10,10,0,0,173,
        174,5,51,0,0,174,179,3,26,13,11,175,176,10,7,0,0,176,177,5,54,0,
        0,177,179,3,26,13,8,178,154,1,0,0,0,178,157,1,0,0,0,178,160,1,0,
        0,0,178,163,1,0,0,0,178,166,1,0,0,0,178,169,1,0,0,0,178,172,1,0,
        0,0,178,175,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,
        0,0,181,27,1,0,0,0,182,180,1,0,0,0,183,184,6,14,-1,0,184,215,5,71,
        0,0,185,215,3,32,16,0,186,187,5,5,0,0,187,188,3,28,14,0,188,189,
        5,6,0,0,189,215,1,0,0,0,190,191,5,1,0,0,191,215,3,28,14,9,192,193,
        5,16,0,0,193,194,5,5,0,0,194,195,3,28,14,0,195,196,5,6,0,0,196,215,
        1,0,0,0,197,198,5,17,0,0,198,199,5,5,0,0,199,200,3,28,14,0,200,201,
        5,6,0,0,201,215,1,0,0,0,202,203,5,18,0,0,203,204,5,5,0,0,204,205,
        3,28,14,0,205,206,5,6,0,0,206,215,1,0,0,0,207,208,5,19,0,0,208,209,
        5,5,0,0,209,210,3,28,14,0,210,211,5,13,0,0,211,212,3,28,14,0,212,
        213,5,6,0,0,213,215,1,0,0,0,214,183,1,0,0,0,214,185,1,0,0,0,214,
        186,1,0,0,0,214,190,1,0,0,0,214,192,1,0,0,0,214,197,1,0,0,0,214,
        202,1,0,0,0,214,207,1,0,0,0,215,230,1,0,0,0,216,217,10,8,0,0,217,
        218,5,2,0,0,218,229,3,28,14,9,219,220,10,7,0,0,220,221,5,1,0,0,221,
        229,3,28,14,8,222,223,10,6,0,0,223,224,5,3,0,0,224,229,3,28,14,7,
        225,226,10,5,0,0,226,227,5,4,0,0,227,229,3,28,14,6,228,216,1,0,0,
        0,228,219,1,0,0,0,228,222,1,0,0,0,228,225,1,0,0,0,229,232,1,0,0,
        0,230,228,1,0,0,0,230,231,1,0,0,0,231,29,1,0,0,0,232,230,1,0,0,0,
        233,240,5,62,0,0,234,240,5,61,0,0,235,240,5,64,0,0,236,240,5,63,
        0,0,237,240,5,59,0,0,238,240,5,60,0,0,239,233,1,0,0,0,239,234,1,
        0,0,0,239,235,1,0,0,0,239,236,1,0,0,0,239,237,1,0,0,0,239,238,1,
        0,0,0,240,31,1,0,0,0,241,247,5,69,0,0,242,247,5,70,0,0,243,247,3,
        34,17,0,244,245,5,1,0,0,245,247,3,32,16,0,246,241,1,0,0,0,246,242,
        1,0,0,0,246,243,1,0,0,0,246,244,1,0,0,0,247,33,1,0,0,0,248,249,7,
        2,0,0,249,35,1,0,0,0,250,251,5,71,0,0,251,37,1,0,0,0,18,42,47,52,
        54,60,72,78,91,96,108,152,178,180,214,228,230,239,246
    ]

class LtlParser ( Parser ):

    grammarFileName = "LtlParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'+'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "':'", "','", "'.'", 
                     "'@'", "'abs'", "'sqrt'", "'exp'", "'pow'", "'s'", 
                     "'ms'", "'us'", "'ns'", "'ps'", "'topic'", "'import'", 
                     "'input'", "'output'", "'internal'", "'const'", "'real'", 
                     "'float'", "'long'", "'complex'", "'int'", "'bool'", 
                     "'assertion'", "'specification'", "'from'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'xor'", "'rise'", "'fall'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'=='", "'!=='", "'>='", "'<='", "'>'", 
                     "'<'", "'='" ]

    symbolicNames = [ "<INVALID>", "MINUS", "PLUS", "TIMES", "DIVIDE", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMICOLON", "COLON", "COMMA", "DOT", "AT", "ABS", 
                      "SQRT", "EXP", "POW", "SEC", "MSEC", "USEC", "NSEC", 
                      "PSEC", "ROS_Topic", "Import", "Input", "Output", 
                      "Internal", "Constant", "DomainTypeReal", "DomainTypeFloat", 
                      "DomainTypeLong", "DomainTypeComplex", "DomainTypeInt", 
                      "DomainTypeBool", "Assertion", "Specification", "From", 
                      "NotOperator", "OrOperator", "AndOperator", "IffOperator", 
                      "ImpliesOperator", "XorOperator", "RiseOperator", 
                      "FallOperator", "AlwaysOperator", "EventuallyOperator", 
                      "UntilOperator", "UnlessOperator", "HistoricallyOperator", 
                      "OnceOperator", "SinceOperator", "NextOperator", "PreviousOperator", 
                      "StrongNextOperator", "StrongPreviousOperator", "EqualOperator", 
                      "NotEqualOperator", "GreaterOrEqualOperator", "LesserOrEqualOperator", 
                      "GreaterOperator", "LesserOperator", "EQUAL", "BooleanLiteral", 
                      "TRUE", "FALSE", "IntegerLiteral", "RealLiteral", 
                      "Identifier", "LINE_TERMINATOR", "WHITESPACE", "COMMENT", 
                      "LINE_COMMENT" ]

    RULE_specification_file = 0
    RULE_specification = 1
    RULE_spec = 2
    RULE_modimport = 3
    RULE_assertion = 4
    RULE_declaration = 5
    RULE_annotation = 6
    RULE_annotation_type = 7
    RULE_variableDeclaration = 8
    RULE_constantDeclaration = 9
    RULE_assignment = 10
    RULE_domainType = 11
    RULE_ioType = 12
    RULE_expression = 13
    RULE_real_expression = 14
    RULE_comparisonOp = 15
    RULE_literal = 16
    RULE_boolLiteral = 17
    RULE_identifier = 18

    ruleNames =  [ "specification_file", "specification", "spec", "modimport", 
                   "assertion", "declaration", "annotation", "annotation_type", 
                   "variableDeclaration", "constantDeclaration", "assignment", 
                   "domainType", "ioType", "expression", "real_expression", 
                   "comparisonOp", "literal", "boolLiteral", "identifier" ]

    EOF = Token.EOF
    MINUS=1
    PLUS=2
    TIMES=3
    DIVIDE=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    LBRACK=9
    RBRACK=10
    SEMICOLON=11
    COLON=12
    COMMA=13
    DOT=14
    AT=15
    ABS=16
    SQRT=17
    EXP=18
    POW=19
    SEC=20
    MSEC=21
    USEC=22
    NSEC=23
    PSEC=24
    ROS_Topic=25
    Import=26
    Input=27
    Output=28
    Internal=29
    Constant=30
    DomainTypeReal=31
    DomainTypeFloat=32
    DomainTypeLong=33
    DomainTypeComplex=34
    DomainTypeInt=35
    DomainTypeBool=36
    Assertion=37
    Specification=38
    From=39
    NotOperator=40
    OrOperator=41
    AndOperator=42
    IffOperator=43
    ImpliesOperator=44
    XorOperator=45
    RiseOperator=46
    FallOperator=47
    AlwaysOperator=48
    EventuallyOperator=49
    UntilOperator=50
    UnlessOperator=51
    HistoricallyOperator=52
    OnceOperator=53
    SinceOperator=54
    NextOperator=55
    PreviousOperator=56
    StrongNextOperator=57
    StrongPreviousOperator=58
    EqualOperator=59
    NotEqualOperator=60
    GreaterOrEqualOperator=61
    LesserOrEqualOperator=62
    GreaterOperator=63
    LesserOperator=64
    EQUAL=65
    BooleanLiteral=66
    TRUE=67
    FALSE=68
    IntegerLiteral=69
    RealLiteral=70
    Identifier=71
    LINE_TERMINATOR=72
    WHITESPACE=73
    COMMENT=74
    LINE_COMMENT=75

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Specification_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def specification(self):
            return self.getTypedRuleContext(LtlParser.SpecificationContext,0)


        def EOF(self):
            return self.getToken(LtlParser.EOF, 0)

        def getRuleIndex(self):
            return LtlParser.RULE_specification_file

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification_file" ):
                return visitor.visitSpecification_file(self)
            else:
                return visitor.visitChildren(self)




    def specification_file(self):

        localctx = LtlParser.Specification_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_specification_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.specification()
            self.state = 39
            self.match(LtlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spec(self):
            return self.getTypedRuleContext(LtlParser.SpecContext,0)


        def modimport(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ModimportContext)
            else:
                return self.getTypedRuleContext(LtlParser.ModimportContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(LtlParser.DeclarationContext,i)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(LtlParser.AnnotationContext,i)


        def assertion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.AssertionContext)
            else:
                return self.getTypedRuleContext(LtlParser.AssertionContext,i)


        def getRuleIndex(self):
            return LtlParser.RULE_specification

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification" ):
                return visitor.visitSpecification(self)
            else:
                return visitor.visitChildren(self)




    def specification(self):

        localctx = LtlParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 41
                self.spec()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 44
                self.modimport()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 52
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [27, 28, 30, 32, 33, 34, 35, 36, 71]:
                        self.state = 50
                        self.declaration()
                        pass
                    elif token in [15]:
                        self.state = 51
                        self.annotation()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.assertion()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 554999384841846818) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 31) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_spec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SpecificationIdContext(SpecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.SpecContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Specification(self):
            return self.getToken(LtlParser.Specification, 0)
        def Identifier(self):
            return self.getToken(LtlParser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecificationId" ):
                return visitor.visitSpecificationId(self)
            else:
                return visitor.visitChildren(self)



    def spec(self):

        localctx = LtlParser.SpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_spec)
        try:
            localctx = LtlParser.SpecificationIdContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(LtlParser.Specification)
            self.state = 63
            self.match(LtlParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModimportContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_modimport

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ModImportContext(ModimportContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ModimportContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def From(self):
            return self.getToken(LtlParser.From, 0)
        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(LtlParser.Identifier)
            else:
                return self.getToken(LtlParser.Identifier, i)
        def Import(self):
            return self.getToken(LtlParser.Import, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModImport" ):
                return visitor.visitModImport(self)
            else:
                return visitor.visitChildren(self)



    def modimport(self):

        localctx = LtlParser.ModimportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modimport)
        try:
            localctx = LtlParser.ModImportContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(LtlParser.From)
            self.state = 66
            self.match(LtlParser.Identifier)
            self.state = 67
            self.match(LtlParser.Import)
            self.state = 68
            self.match(LtlParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def Identifier(self):
            return self.getToken(LtlParser.Identifier, 0)

        def EQUAL(self):
            return self.getToken(LtlParser.EQUAL, 0)

        def getRuleIndex(self):
            return LtlParser.RULE_assertion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertion" ):
                return visitor.visitAssertion(self)
            else:
                return visitor.visitChildren(self)




    def assertion(self):

        localctx = LtlParser.AssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 70
                self.match(LtlParser.Identifier)
                self.state = 71
                self.match(LtlParser.EQUAL)


            self.state = 74
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclVariableContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variableDeclaration(self):
            return self.getTypedRuleContext(LtlParser.VariableDeclarationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclVariable" ):
                return visitor.visitDeclVariable(self)
            else:
                return visitor.visitChildren(self)


    class DeclConstantContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constantDeclaration(self):
            return self.getTypedRuleContext(LtlParser.ConstantDeclarationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclConstant" ):
                return visitor.visitDeclConstant(self)
            else:
                return visitor.visitChildren(self)



    def declaration(self):

        localctx = LtlParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27, 28, 32, 33, 34, 35, 36, 71]:
                localctx = LtlParser.DeclVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.variableDeclaration()
                pass
            elif token in [30]:
                localctx = LtlParser.DeclConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.constantDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(LtlParser.AT, 0)

        def annotation_type(self):
            return self.getTypedRuleContext(LtlParser.Annotation_typeContext,0)


        def getRuleIndex(self):
            return LtlParser.RULE_annotation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotation" ):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def annotation(self):

        localctx = LtlParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(LtlParser.AT)
            self.state = 81
            self.annotation_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Annotation_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_annotation_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RosTopicContext(Annotation_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Annotation_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROS_Topic(self):
            return self.getToken(LtlParser.ROS_Topic, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(LtlParser.Identifier)
            else:
                return self.getToken(LtlParser.Identifier, i)
        def COMMA(self):
            return self.getToken(LtlParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRosTopic" ):
                return visitor.visitRosTopic(self)
            else:
                return visitor.visitChildren(self)



    def annotation_type(self):

        localctx = LtlParser.Annotation_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_annotation_type)
        try:
            localctx = LtlParser.RosTopicContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(LtlParser.ROS_Topic)
            self.state = 84
            self.match(LtlParser.LPAREN)
            self.state = 85
            self.match(LtlParser.Identifier)
            self.state = 86
            self.match(LtlParser.COMMA)
            self.state = 87
            self.match(LtlParser.Identifier)
            self.state = 88
            self.match(LtlParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domainType(self):
            return self.getTypedRuleContext(LtlParser.DomainTypeContext,0)


        def Identifier(self):
            return self.getToken(LtlParser.Identifier, 0)

        def ioType(self):
            return self.getTypedRuleContext(LtlParser.IoTypeContext,0)


        def assignment(self):
            return self.getTypedRuleContext(LtlParser.AssignmentContext,0)


        def getRuleIndex(self):
            return LtlParser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = LtlParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27 or _la==28:
                self.state = 90
                self.ioType()


            self.state = 93
            self.domainType()
            self.state = 94
            self.match(LtlParser.Identifier)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 95
                self.assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Constant(self):
            return self.getToken(LtlParser.Constant, 0)

        def domainType(self):
            return self.getTypedRuleContext(LtlParser.DomainTypeContext,0)


        def Identifier(self):
            return self.getToken(LtlParser.Identifier, 0)

        def EQUAL(self):
            return self.getToken(LtlParser.EQUAL, 0)

        def literal(self):
            return self.getTypedRuleContext(LtlParser.LiteralContext,0)


        def getRuleIndex(self):
            return LtlParser.RULE_constantDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantDeclaration" ):
                return visitor.visitConstantDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constantDeclaration(self):

        localctx = LtlParser.ConstantDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constantDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(LtlParser.Constant)
            self.state = 99
            self.domainType()
            self.state = 100
            self.match(LtlParser.Identifier)
            self.state = 101
            self.match(LtlParser.EQUAL)
            self.state = 102
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsgnExprContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EQUAL(self):
            return self.getToken(LtlParser.EQUAL, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsgnExpr" ):
                return visitor.visitAsgnExpr(self)
            else:
                return visitor.visitChildren(self)


    class AsgnLiteralContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EQUAL(self):
            return self.getToken(LtlParser.EQUAL, 0)
        def literal(self):
            return self.getTypedRuleContext(LtlParser.LiteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsgnLiteral" ):
                return visitor.visitAsgnLiteral(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = LtlParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = LtlParser.AsgnLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(LtlParser.EQUAL)
                self.state = 105
                self.literal()
                pass

            elif la_ == 2:
                localctx = LtlParser.AsgnExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(LtlParser.EQUAL)
                self.state = 107
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DomainTypeFloat(self):
            return self.getToken(LtlParser.DomainTypeFloat, 0)

        def DomainTypeInt(self):
            return self.getToken(LtlParser.DomainTypeInt, 0)

        def DomainTypeLong(self):
            return self.getToken(LtlParser.DomainTypeLong, 0)

        def DomainTypeComplex(self):
            return self.getToken(LtlParser.DomainTypeComplex, 0)

        def DomainTypeBool(self):
            return self.getToken(LtlParser.DomainTypeBool, 0)

        def Identifier(self):
            return self.getToken(LtlParser.Identifier, 0)

        def getRuleIndex(self):
            return LtlParser.RULE_domainType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDomainType" ):
                return visitor.visitDomainType(self)
            else:
                return visitor.visitChildren(self)




    def domainType(self):

        localctx = LtlParser.DomainTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_domainType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 549755813919) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Input(self):
            return self.getToken(LtlParser.Input, 0)

        def Output(self):
            return self.getToken(LtlParser.Output, 0)

        def getRuleIndex(self):
            return LtlParser.RULE_ioType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIoType" ):
                return visitor.visitIoType(self)
            else:
                return visitor.visitChildren(self)




    def ioType(self):

        localctx = LtlParser.IoTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ioType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprSinceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def SinceOperator(self):
            return self.getToken(LtlParser.SinceOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSince" ):
                return visitor.visitExprSince(self)
            else:
                return visitor.visitChildren(self)


    class ExprParenContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParen" ):
                return visitor.visitExprParen(self)
            else:
                return visitor.visitChildren(self)


    class ExprIffContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def IffOperator(self):
            return self.getToken(LtlParser.IffOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprIff" ):
                return visitor.visitExprIff(self)
            else:
                return visitor.visitChildren(self)


    class ExpreOnceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OnceOperator(self):
            return self.getToken(LtlParser.OnceOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpreOnce" ):
                return visitor.visitExpreOnce(self)
            else:
                return visitor.visitChildren(self)


    class ExprEvContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EventuallyOperator(self):
            return self.getToken(LtlParser.EventuallyOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprEv" ):
                return visitor.visitExprEv(self)
            else:
                return visitor.visitChildren(self)


    class ExprStrongPreviousContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def StrongPreviousOperator(self):
            return self.getToken(LtlParser.StrongPreviousOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStrongPrevious" ):
                return visitor.visitExprStrongPrevious(self)
            else:
                return visitor.visitChildren(self)


    class ExprImpliesContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def ImpliesOperator(self):
            return self.getToken(LtlParser.ImpliesOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprImplies" ):
                return visitor.visitExprImplies(self)
            else:
                return visitor.visitChildren(self)


    class ExprUntilContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def UntilOperator(self):
            return self.getToken(LtlParser.UntilOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprUntil" ):
                return visitor.visitExprUntil(self)
            else:
                return visitor.visitChildren(self)


    class ExprNotContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NotOperator(self):
            return self.getToken(LtlParser.NotOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNot" ):
                return visitor.visitExprNot(self)
            else:
                return visitor.visitChildren(self)


    class ExprStrongNextContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def StrongNextOperator(self):
            return self.getToken(LtlParser.StrongNextOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStrongNext" ):
                return visitor.visitExprStrongNext(self)
            else:
                return visitor.visitChildren(self)


    class ExprNextContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NextOperator(self):
            return self.getToken(LtlParser.NextOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNext" ):
                return visitor.visitExprNext(self)
            else:
                return visitor.visitChildren(self)


    class ExprAndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def AndOperator(self):
            return self.getToken(LtlParser.AndOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAnd" ):
                return visitor.visitExprAnd(self)
            else:
                return visitor.visitChildren(self)


    class ExprUnlessContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def UnlessOperator(self):
            return self.getToken(LtlParser.UnlessOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprUnless" ):
                return visitor.visitExprUnless(self)
            else:
                return visitor.visitChildren(self)


    class ExprPreviousContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PreviousOperator(self):
            return self.getToken(LtlParser.PreviousOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPrevious" ):
                return visitor.visitExprPrevious(self)
            else:
                return visitor.visitChildren(self)


    class ExprPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.Real_expressionContext,i)

        def comparisonOp(self):
            return self.getTypedRuleContext(LtlParser.ComparisonOpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPredicate" ):
                return visitor.visitExprPredicate(self)
            else:
                return visitor.visitChildren(self)


    class ExprHistContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HistoricallyOperator(self):
            return self.getToken(LtlParser.HistoricallyOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprHist" ):
                return visitor.visitExprHist(self)
            else:
                return visitor.visitChildren(self)


    class ExprFallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FallOperator(self):
            return self.getToken(LtlParser.FallOperator, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFall" ):
                return visitor.visitExprFall(self)
            else:
                return visitor.visitChildren(self)


    class ExprXorContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def XorOperator(self):
            return self.getToken(LtlParser.XorOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprXor" ):
                return visitor.visitExprXor(self)
            else:
                return visitor.visitChildren(self)


    class ExprRiseContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RiseOperator(self):
            return self.getToken(LtlParser.RiseOperator, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRise" ):
                return visitor.visitExprRise(self)
            else:
                return visitor.visitChildren(self)


    class ExprOrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def OrOperator(self):
            return self.getToken(LtlParser.OrOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOr" ):
                return visitor.visitExprOr(self)
            else:
                return visitor.visitChildren(self)


    class ExprAlwaysContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AlwaysOperator(self):
            return self.getToken(LtlParser.AlwaysOperator, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAlways" ):
                return visitor.visitExprAlways(self)
            else:
                return visitor.visitChildren(self)


    class ExprRealContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self):
            return self.getTypedRuleContext(LtlParser.Real_expressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprReal" ):
                return visitor.visitExprReal(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LtlParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = LtlParser.ExprRealContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 115
                self.real_expression(0)
                pass

            elif la_ == 2:
                localctx = LtlParser.ExprPredicateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.real_expression(0)
                self.state = 117
                self.comparisonOp()
                self.state = 118
                self.real_expression(0)
                pass

            elif la_ == 3:
                localctx = LtlParser.ExprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(LtlParser.LPAREN)
                self.state = 121
                self.expression(0)
                self.state = 122
                self.match(LtlParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = LtlParser.ExprNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(LtlParser.NotOperator)
                self.state = 125
                self.expression(19)
                pass

            elif la_ == 5:
                localctx = LtlParser.ExprAlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(LtlParser.AlwaysOperator)
                self.state = 127
                self.expression(13)
                pass

            elif la_ == 6:
                localctx = LtlParser.ExprEvContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(LtlParser.EventuallyOperator)
                self.state = 129
                self.expression(12)
                pass

            elif la_ == 7:
                localctx = LtlParser.ExprHistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(LtlParser.HistoricallyOperator)
                self.state = 131
                self.expression(9)
                pass

            elif la_ == 8:
                localctx = LtlParser.ExpreOnceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 132
                self.match(LtlParser.OnceOperator)
                self.state = 133
                self.expression(8)
                pass

            elif la_ == 9:
                localctx = LtlParser.ExprRiseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.match(LtlParser.RiseOperator)
                self.state = 135
                self.match(LtlParser.LPAREN)
                self.state = 136
                self.expression(0)
                self.state = 137
                self.match(LtlParser.RPAREN)
                pass

            elif la_ == 10:
                localctx = LtlParser.ExprFallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                self.match(LtlParser.FallOperator)
                self.state = 140
                self.match(LtlParser.LPAREN)
                self.state = 141
                self.expression(0)
                self.state = 142
                self.match(LtlParser.RPAREN)
                pass

            elif la_ == 11:
                localctx = LtlParser.ExprPreviousContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(LtlParser.PreviousOperator)
                self.state = 145
                self.expression(4)
                pass

            elif la_ == 12:
                localctx = LtlParser.ExprNextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(LtlParser.NextOperator)
                self.state = 147
                self.expression(3)
                pass

            elif la_ == 13:
                localctx = LtlParser.ExprStrongPreviousContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(LtlParser.StrongPreviousOperator)
                self.state = 149
                self.expression(2)
                pass

            elif la_ == 14:
                localctx = LtlParser.ExprStrongNextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(LtlParser.StrongNextOperator)
                self.state = 151
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 178
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = LtlParser.ExprOrContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 155
                        self.match(LtlParser.OrOperator)
                        self.state = 156
                        self.expression(19)
                        pass

                    elif la_ == 2:
                        localctx = LtlParser.ExprAndContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 158
                        self.match(LtlParser.AndOperator)
                        self.state = 159
                        self.expression(18)
                        pass

                    elif la_ == 3:
                        localctx = LtlParser.ExprImpliesContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 161
                        self.match(LtlParser.ImpliesOperator)
                        self.state = 162
                        self.expression(17)
                        pass

                    elif la_ == 4:
                        localctx = LtlParser.ExprIffContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 164
                        self.match(LtlParser.IffOperator)
                        self.state = 165
                        self.expression(16)
                        pass

                    elif la_ == 5:
                        localctx = LtlParser.ExprXorContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 167
                        self.match(LtlParser.XorOperator)
                        self.state = 168
                        self.expression(15)
                        pass

                    elif la_ == 6:
                        localctx = LtlParser.ExprUntilContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 170
                        self.match(LtlParser.UntilOperator)
                        self.state = 171
                        self.expression(12)
                        pass

                    elif la_ == 7:
                        localctx = LtlParser.ExprUnlessContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 172
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 173
                        self.match(LtlParser.UnlessOperator)
                        self.state = 174
                        self.expression(11)
                        pass

                    elif la_ == 8:
                        localctx = LtlParser.ExprSinceContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 176
                        self.match(LtlParser.SinceOperator)
                        self.state = 177
                        self.expression(8)
                        pass

             
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Real_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_real_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprSubtractionContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.Real_expressionContext,i)

        def MINUS(self):
            return self.getToken(LtlParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSubtraction" ):
                return visitor.visitExprSubtraction(self)
            else:
                return visitor.visitChildren(self)


    class ExprPowContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(LtlParser.POW, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.Real_expressionContext,i)

        def COMMA(self):
            return self.getToken(LtlParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPow" ):
                return visitor.visitExprPow(self)
            else:
                return visitor.visitChildren(self)


    class ExprDivisionContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.Real_expressionContext,i)

        def DIVIDE(self):
            return self.getToken(LtlParser.DIVIDE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprDivision" ):
                return visitor.visitExprDivision(self)
            else:
                return visitor.visitChildren(self)


    class ExprMultiplicationContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.Real_expressionContext,i)

        def TIMES(self):
            return self.getToken(LtlParser.TIMES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultiplication" ):
                return visitor.visitExprMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(LtlParser.LiteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteral" ):
                return visitor.visitExprLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ExprExpContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXP(self):
            return self.getToken(LtlParser.EXP, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def real_expression(self):
            return self.getTypedRuleContext(LtlParser.Real_expressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprExp" ):
                return visitor.visitExprExp(self)
            else:
                return visitor.visitChildren(self)


    class ExprUnaryMinusContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(LtlParser.MINUS, 0)
        def real_expression(self):
            return self.getTypedRuleContext(LtlParser.Real_expressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprUnaryMinus" ):
                return visitor.visitExprUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class ExprParenRealExprContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def real_expression(self):
            return self.getTypedRuleContext(LtlParser.Real_expressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParenRealExpr" ):
                return visitor.visitExprParenRealExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExprSqrtContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SQRT(self):
            return self.getToken(LtlParser.SQRT, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def real_expression(self):
            return self.getTypedRuleContext(LtlParser.Real_expressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSqrt" ):
                return visitor.visitExprSqrt(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LtlParser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprId" ):
                return visitor.visitExprId(self)
            else:
                return visitor.visitChildren(self)


    class ExprAbsContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABS(self):
            return self.getToken(LtlParser.ABS, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def real_expression(self):
            return self.getTypedRuleContext(LtlParser.Real_expressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAbs" ):
                return visitor.visitExprAbs(self)
            else:
                return visitor.visitChildren(self)


    class ExprAdditionContext(Real_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.Real_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.Real_expressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.Real_expressionContext,i)

        def PLUS(self):
            return self.getToken(LtlParser.PLUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddition" ):
                return visitor.visitExprAddition(self)
            else:
                return visitor.visitChildren(self)



    def real_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LtlParser.Real_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_real_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = LtlParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 184
                self.match(LtlParser.Identifier)
                pass

            elif la_ == 2:
                localctx = LtlParser.ExprLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 185
                self.literal()
                pass

            elif la_ == 3:
                localctx = LtlParser.ExprParenRealExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 186
                self.match(LtlParser.LPAREN)
                self.state = 187
                self.real_expression(0)
                self.state = 188
                self.match(LtlParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = LtlParser.ExprUnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 190
                self.match(LtlParser.MINUS)
                self.state = 191
                self.real_expression(9)
                pass

            elif la_ == 5:
                localctx = LtlParser.ExprAbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                self.match(LtlParser.ABS)
                self.state = 193
                self.match(LtlParser.LPAREN)
                self.state = 194
                self.real_expression(0)
                self.state = 195
                self.match(LtlParser.RPAREN)
                pass

            elif la_ == 6:
                localctx = LtlParser.ExprSqrtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 197
                self.match(LtlParser.SQRT)
                self.state = 198
                self.match(LtlParser.LPAREN)
                self.state = 199
                self.real_expression(0)
                self.state = 200
                self.match(LtlParser.RPAREN)
                pass

            elif la_ == 7:
                localctx = LtlParser.ExprExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 202
                self.match(LtlParser.EXP)
                self.state = 203
                self.match(LtlParser.LPAREN)
                self.state = 204
                self.real_expression(0)
                self.state = 205
                self.match(LtlParser.RPAREN)
                pass

            elif la_ == 8:
                localctx = LtlParser.ExprPowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 207
                self.match(LtlParser.POW)
                self.state = 208
                self.match(LtlParser.LPAREN)
                self.state = 209
                self.real_expression(0)
                self.state = 210
                self.match(LtlParser.COMMA)
                self.state = 211
                self.real_expression(0)
                self.state = 212
                self.match(LtlParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 228
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = LtlParser.ExprAdditionContext(self, LtlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 216
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 217
                        self.match(LtlParser.PLUS)
                        self.state = 218
                        self.real_expression(9)
                        pass

                    elif la_ == 2:
                        localctx = LtlParser.ExprSubtractionContext(self, LtlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 219
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 220
                        self.match(LtlParser.MINUS)
                        self.state = 221
                        self.real_expression(8)
                        pass

                    elif la_ == 3:
                        localctx = LtlParser.ExprMultiplicationContext(self, LtlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 222
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 223
                        self.match(LtlParser.TIMES)
                        self.state = 224
                        self.real_expression(7)
                        pass

                    elif la_ == 4:
                        localctx = LtlParser.ExprDivisionContext(self, LtlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 225
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 226
                        self.match(LtlParser.DIVIDE)
                        self.state = 227
                        self.real_expression(6)
                        pass

             
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_comparisonOp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GreaterOrEqualOperator(self):
            return self.getToken(LtlParser.GreaterOrEqualOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeq" ):
                return visitor.visitGeq(self)
            else:
                return visitor.visitChildren(self)


    class LeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LesserOrEqualOperator(self):
            return self.getToken(LtlParser.LesserOrEqualOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeq" ):
                return visitor.visitLeq(self)
            else:
                return visitor.visitChildren(self)


    class GreaterContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GreaterOperator(self):
            return self.getToken(LtlParser.GreaterOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreater" ):
                return visitor.visitGreater(self)
            else:
                return visitor.visitChildren(self)


    class NeqContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NotEqualOperator(self):
            return self.getToken(LtlParser.NotEqualOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeq" ):
                return visitor.visitNeq(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EqualOperator(self):
            return self.getToken(LtlParser.EqualOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LesserOperator(self):
            return self.getToken(LtlParser.LesserOperator, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)



    def comparisonOp(self):

        localctx = LtlParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparisonOp)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                localctx = LtlParser.LeqContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(LtlParser.LesserOrEqualOperator)
                pass
            elif token in [61]:
                localctx = LtlParser.GeqContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(LtlParser.GreaterOrEqualOperator)
                pass
            elif token in [64]:
                localctx = LtlParser.LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.match(LtlParser.LesserOperator)
                pass
            elif token in [63]:
                localctx = LtlParser.GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.match(LtlParser.GreaterOperator)
                pass
            elif token in [59]:
                localctx = LtlParser.EqContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 237
                self.match(LtlParser.EqualOperator)
                pass
            elif token in [60]:
                localctx = LtlParser.NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 238
                self.match(LtlParser.NotEqualOperator)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(LtlParser.IntegerLiteral, 0)

        def RealLiteral(self):
            return self.getToken(LtlParser.RealLiteral, 0)

        def boolLiteral(self):
            return self.getTypedRuleContext(LtlParser.BoolLiteralContext,0)


        def MINUS(self):
            return self.getToken(LtlParser.MINUS, 0)

        def literal(self):
            return self.getTypedRuleContext(LtlParser.LiteralContext,0)


        def getRuleIndex(self):
            return LtlParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = LtlParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(LtlParser.IntegerLiteral)
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(LtlParser.RealLiteral)
                pass
            elif token in [67, 68]:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.boolLiteral()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.match(LtlParser.MINUS)
                self.state = 245
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(LtlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LtlParser.FALSE, 0)

        def getRuleIndex(self):
            return LtlParser.RULE_boolLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLiteral" ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)




    def boolLiteral(self):

        localctx = LtlParser.BoolLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_boolLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==67 or _la==68):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_identifier

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdContext(IdentifierContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.IdentifierContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LtlParser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def identifier(self):

        localctx = LtlParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_identifier)
        try:
            localctx = LtlParser.IdContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(LtlParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        self._predicates[14] = self.real_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

    def real_expression_sempred(self, localctx:Real_expressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 5)
         




