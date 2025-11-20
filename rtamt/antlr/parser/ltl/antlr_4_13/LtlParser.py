# Generated from LtlParser.g4 by ANTLR 4.13.2
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
        4,1,77,246,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,3,1,41,8,
        1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,1,4,1,57,8,1,11,1,12,1,58,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,3,4,71,8,4,1,4,1,4,1,4,1,5,1,5,3,5,78,8,5,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,3,8,91,8,8,1,8,1,8,1,8,3,8,96,8,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,108,8,10,1,11,1,
        11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,185,8,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,223,8,13,10,13,12,
        13,226,9,13,1,14,1,14,3,14,230,8,14,1,15,1,15,3,15,234,8,15,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,242,8,16,1,17,1,17,1,17,0,1,26,18,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,3,2,0,34,37,73,
        73,1,0,29,30,1,0,71,72,275,0,36,1,0,0,0,2,40,1,0,0,0,4,60,1,0,0,
        0,6,63,1,0,0,0,8,70,1,0,0,0,10,77,1,0,0,0,12,79,1,0,0,0,14,82,1,
        0,0,0,16,90,1,0,0,0,18,97,1,0,0,0,20,107,1,0,0,0,22,109,1,0,0,0,
        24,111,1,0,0,0,26,184,1,0,0,0,28,229,1,0,0,0,30,233,1,0,0,0,32,241,
        1,0,0,0,34,243,1,0,0,0,36,37,3,2,1,0,37,38,5,0,0,1,38,1,1,0,0,0,
        39,41,3,4,2,0,40,39,1,0,0,0,40,41,1,0,0,0,41,45,1,0,0,0,42,44,3,
        6,3,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,
        52,1,0,0,0,47,45,1,0,0,0,48,51,3,10,5,0,49,51,3,12,6,0,50,48,1,0,
        0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,56,
        1,0,0,0,54,52,1,0,0,0,55,57,3,8,4,0,56,55,1,0,0,0,57,58,1,0,0,0,
        58,56,1,0,0,0,58,59,1,0,0,0,59,3,1,0,0,0,60,61,5,40,0,0,61,62,5,
        73,0,0,62,5,1,0,0,0,63,64,5,41,0,0,64,65,5,73,0,0,65,66,5,28,0,0,
        66,67,5,73,0,0,67,7,1,0,0,0,68,69,5,73,0,0,69,71,5,67,0,0,70,68,
        1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,3,26,13,0,73,74,5,11,0,
        0,74,9,1,0,0,0,75,78,3,16,8,0,76,78,3,18,9,0,77,75,1,0,0,0,77,76,
        1,0,0,0,78,11,1,0,0,0,79,80,5,15,0,0,80,81,3,14,7,0,81,13,1,0,0,
        0,82,83,5,27,0,0,83,84,5,5,0,0,84,85,5,73,0,0,85,86,5,13,0,0,86,
        87,5,73,0,0,87,88,5,6,0,0,88,15,1,0,0,0,89,91,3,24,12,0,90,89,1,
        0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,3,22,11,0,93,95,5,73,0,0,
        94,96,3,20,10,0,95,94,1,0,0,0,95,96,1,0,0,0,96,17,1,0,0,0,97,98,
        5,32,0,0,98,99,3,22,11,0,99,100,5,73,0,0,100,101,5,67,0,0,101,102,
        3,34,17,0,102,19,1,0,0,0,103,104,5,67,0,0,104,108,3,34,17,0,105,
        106,5,67,0,0,106,108,3,26,13,0,107,103,1,0,0,0,107,105,1,0,0,0,108,
        21,1,0,0,0,109,110,7,0,0,0,110,23,1,0,0,0,111,112,7,1,0,0,112,25,
        1,0,0,0,113,114,6,13,-1,0,114,115,5,5,0,0,115,116,3,26,13,0,116,
        117,5,6,0,0,117,185,1,0,0,0,118,119,5,1,0,0,119,185,3,26,13,31,120,
        121,5,16,0,0,121,122,5,5,0,0,122,123,3,26,13,0,123,124,5,6,0,0,124,
        185,1,0,0,0,125,126,5,17,0,0,126,127,5,5,0,0,127,128,3,26,13,0,128,
        129,5,6,0,0,129,185,1,0,0,0,130,131,5,18,0,0,131,132,5,5,0,0,132,
        133,3,26,13,0,133,134,5,6,0,0,134,185,1,0,0,0,135,136,5,19,0,0,136,
        137,5,5,0,0,137,138,3,26,13,0,138,139,5,13,0,0,139,140,3,26,13,0,
        140,141,5,6,0,0,141,185,1,0,0,0,142,143,5,20,0,0,143,144,5,5,0,0,
        144,145,3,26,13,0,145,146,5,13,0,0,146,147,3,26,13,0,147,148,5,6,
        0,0,148,185,1,0,0,0,149,150,5,21,0,0,150,151,5,5,0,0,151,152,3,26,
        13,0,152,153,5,6,0,0,153,185,1,0,0,0,154,155,5,42,0,0,155,185,3,
        26,13,21,156,157,5,50,0,0,157,185,3,26,13,20,158,159,5,51,0,0,159,
        185,3,26,13,19,160,161,5,54,0,0,161,185,3,26,13,18,162,163,5,55,
        0,0,163,185,3,26,13,17,164,165,5,58,0,0,165,185,3,26,13,16,166,167,
        5,57,0,0,167,185,3,26,13,15,168,169,5,60,0,0,169,185,3,26,13,14,
        170,171,5,59,0,0,171,185,3,26,13,13,172,173,5,48,0,0,173,174,5,5,
        0,0,174,175,3,26,13,0,175,176,5,6,0,0,176,185,1,0,0,0,177,178,5,
        49,0,0,178,179,5,5,0,0,179,180,3,26,13,0,180,181,5,6,0,0,181,185,
        1,0,0,0,182,185,5,73,0,0,183,185,3,34,17,0,184,113,1,0,0,0,184,118,
        1,0,0,0,184,120,1,0,0,0,184,125,1,0,0,0,184,130,1,0,0,0,184,135,
        1,0,0,0,184,142,1,0,0,0,184,149,1,0,0,0,184,154,1,0,0,0,184,156,
        1,0,0,0,184,158,1,0,0,0,184,160,1,0,0,0,184,162,1,0,0,0,184,164,
        1,0,0,0,184,166,1,0,0,0,184,168,1,0,0,0,184,170,1,0,0,0,184,172,
        1,0,0,0,184,177,1,0,0,0,184,182,1,0,0,0,184,183,1,0,0,0,185,224,
        1,0,0,0,186,187,10,24,0,0,187,188,3,28,14,0,188,189,3,26,13,25,189,
        223,1,0,0,0,190,191,10,23,0,0,191,192,3,30,15,0,192,193,3,26,13,
        24,193,223,1,0,0,0,194,195,10,22,0,0,195,196,3,32,16,0,196,197,3,
        26,13,23,197,223,1,0,0,0,198,199,10,12,0,0,199,200,5,52,0,0,200,
        223,3,26,13,13,201,202,10,11,0,0,202,203,5,53,0,0,203,223,3,26,13,
        12,204,205,10,10,0,0,205,206,5,56,0,0,206,223,3,26,13,11,207,208,
        10,9,0,0,208,209,5,44,0,0,209,223,3,26,13,10,210,211,10,8,0,0,211,
        212,5,43,0,0,212,223,3,26,13,9,213,214,10,7,0,0,214,215,5,46,0,0,
        215,223,3,26,13,8,216,217,10,6,0,0,217,218,5,45,0,0,218,223,3,26,
        13,7,219,220,10,5,0,0,220,221,5,47,0,0,221,223,3,26,13,6,222,186,
        1,0,0,0,222,190,1,0,0,0,222,194,1,0,0,0,222,198,1,0,0,0,222,201,
        1,0,0,0,222,204,1,0,0,0,222,207,1,0,0,0,222,210,1,0,0,0,222,213,
        1,0,0,0,222,216,1,0,0,0,222,219,1,0,0,0,223,226,1,0,0,0,224,222,
        1,0,0,0,224,225,1,0,0,0,225,27,1,0,0,0,226,224,1,0,0,0,227,230,5,
        3,0,0,228,230,5,4,0,0,229,227,1,0,0,0,229,228,1,0,0,0,230,29,1,0,
        0,0,231,234,5,2,0,0,232,234,5,1,0,0,233,231,1,0,0,0,233,232,1,0,
        0,0,234,31,1,0,0,0,235,242,5,64,0,0,236,242,5,63,0,0,237,242,5,66,
        0,0,238,242,5,65,0,0,239,242,5,61,0,0,240,242,5,62,0,0,241,235,1,
        0,0,0,241,236,1,0,0,0,241,237,1,0,0,0,241,238,1,0,0,0,241,239,1,
        0,0,0,241,240,1,0,0,0,242,33,1,0,0,0,243,244,7,2,0,0,244,35,1,0,
        0,0,16,40,45,50,52,58,70,77,90,95,107,184,222,224,229,233,241
    ]

class LtlParser ( Parser ):

    grammarFileName = "LtlParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'+'", "'*'", "'/'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "':'", "','", "'.'", 
                     "'@'", "'abs'", "'sqrt'", "'exp'", "'pow'", "'log'", 
                     "'ln'", "'s'", "'ms'", "'us'", "'ns'", "'ps'", "'topic'", 
                     "'import'", "'input'", "'output'", "'internal'", "'const'", 
                     "'real'", "'float'", "'long'", "'complex'", "'int'", 
                     "'bool'", "'assertion'", "'specification'", "'from'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'xor'", "'rise'", "'fall'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'=='", "'!=='", "'>='", 
                     "'<='", "'>'", "'<'", "'='" ]

    symbolicNames = [ "<INVALID>", "MINUS", "PLUS", "TIMES", "DIVIDE", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMICOLON", "COLON", "COMMA", "DOT", "AT", "ABS", 
                      "SQRT", "EXP", "POW", "LOG", "LN", "SEC", "MSEC", 
                      "USEC", "NSEC", "PSEC", "ROS_Topic", "Import", "Input", 
                      "Output", "Internal", "Constant", "DomainTypeReal", 
                      "DomainTypeFloat", "DomainTypeLong", "DomainTypeComplex", 
                      "DomainTypeInt", "DomainTypeBool", "Assertion", "Specification", 
                      "From", "NotOperator", "OrOperator", "AndOperator", 
                      "IffOperator", "ImpliesOperator", "XorOperator", "RiseOperator", 
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
    RULE_multdivOp = 14
    RULE_addsubOp = 15
    RULE_comparisonOp = 16
    RULE_literal = 17

    ruleNames =  [ "specification_file", "specification", "spec", "modimport", 
                   "assertion", "declaration", "annotation", "annotation_type", 
                   "variableDeclaration", "constantDeclaration", "assignment", 
                   "domainType", "ioType", "expression", "multdivOp", "addsubOp", 
                   "comparisonOp", "literal" ]

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
    LOG=20
    LN=21
    SEC=22
    MSEC=23
    USEC=24
    NSEC=25
    PSEC=26
    ROS_Topic=27
    Import=28
    Input=29
    Output=30
    Internal=31
    Constant=32
    DomainTypeReal=33
    DomainTypeFloat=34
    DomainTypeLong=35
    DomainTypeComplex=36
    DomainTypeInt=37
    DomainTypeBool=38
    Assertion=39
    Specification=40
    From=41
    NotOperator=42
    OrOperator=43
    AndOperator=44
    IffOperator=45
    ImpliesOperator=46
    XorOperator=47
    RiseOperator=48
    FallOperator=49
    AlwaysOperator=50
    EventuallyOperator=51
    UntilOperator=52
    UnlessOperator=53
    HistoricallyOperator=54
    OnceOperator=55
    SinceOperator=56
    NextOperator=57
    PreviousOperator=58
    StrongNextOperator=59
    StrongPreviousOperator=60
    EqualOperator=61
    NotEqualOperator=62
    GreaterOrEqualOperator=63
    LesserOrEqualOperator=64
    GreaterOperator=65
    LesserOperator=66
    EQUAL=67
    BooleanLiteral=68
    TRUE=69
    FALSE=70
    IntegerLiteral=71
    RealLiteral=72
    Identifier=73
    LINE_TERMINATOR=74
    WHITESPACE=75
    COMMENT=76
    LINE_COMMENT=77

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
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
            self.state = 36
            self.specification()
            self.state = 37
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
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 39
                self.spec()


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 42
                self.modimport()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [29, 30, 32, 34, 35, 36, 37, 73]:
                        self.state = 48
                        self.declaration()
                        pass
                    elif token in [15]:
                        self.state = 49
                        self.annotation()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.assertion()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2219997539367583778) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 7) != 0)):
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
            self.state = 60
            self.match(LtlParser.Specification)
            self.state = 61
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
            self.state = 63
            self.match(LtlParser.From)
            self.state = 64
            self.match(LtlParser.Identifier)
            self.state = 65
            self.match(LtlParser.Import)
            self.state = 66
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


        def SEMICOLON(self):
            return self.getToken(LtlParser.SEMICOLON, 0)

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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 68
                self.match(LtlParser.Identifier)
                self.state = 69
                self.match(LtlParser.EQUAL)


            self.state = 72
            self.expression(0)
            self.state = 73
            self.match(LtlParser.SEMICOLON)
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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 34, 35, 36, 37, 73]:
                localctx = LtlParser.DeclVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.variableDeclaration()
                pass
            elif token in [32]:
                localctx = LtlParser.DeclConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 76
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
            self.state = 79
            self.match(LtlParser.AT)
            self.state = 80
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
            self.state = 82
            self.match(LtlParser.ROS_Topic)
            self.state = 83
            self.match(LtlParser.LPAREN)
            self.state = 84
            self.match(LtlParser.Identifier)
            self.state = 85
            self.match(LtlParser.COMMA)
            self.state = 86
            self.match(LtlParser.Identifier)
            self.state = 87
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
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 89
                self.ioType()


            self.state = 92
            self.domainType()
            self.state = 93
            self.match(LtlParser.Identifier)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==67:
                self.state = 94
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
            self.state = 97
            self.match(LtlParser.Constant)
            self.state = 98
            self.domainType()
            self.state = 99
            self.match(LtlParser.Identifier)
            self.state = 100
            self.match(LtlParser.EQUAL)
            self.state = 101
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = LtlParser.AsgnLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(LtlParser.EQUAL)
                self.state = 104
                self.literal()
                pass

            elif la_ == 2:
                localctx = LtlParser.AsgnExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(LtlParser.EQUAL)
                self.state = 106
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
            self.state = 109
            _la = self._input.LA(1)
            if not(((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 549755813903) != 0)):
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
            self.state = 111
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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


    class ExprAddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def addsubOp(self):
            return self.getTypedRuleContext(LtlParser.AddsubOpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddSub" ):
                return visitor.visitExprAddSub(self)
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


    class ExprPredicateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def comparisonOp(self):
            return self.getTypedRuleContext(LtlParser.ComparisonOpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPredicate" ):
                return visitor.visitExprPredicate(self)
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


    class ExprLogContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOG(self):
            return self.getToken(LtlParser.LOG, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def COMMA(self):
            return self.getToken(LtlParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLog" ):
                return visitor.visitExprLog(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LtlParser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprId" ):
                return visitor.visitExprId(self)
            else:
                return visitor.visitChildren(self)


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


    class ExprAbsContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABS(self):
            return self.getToken(LtlParser.ABS, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAbs" ):
                return visitor.visitExprAbs(self)
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


    class ExprPowContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(LtlParser.POW, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def COMMA(self):
            return self.getToken(LtlParser.COMMA, 0)
        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPow" ):
                return visitor.visitExprPow(self)
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


    class ExprNegateContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(LtlParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNegate" ):
                return visitor.visitExprNegate(self)
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


    class ExprLnContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LN(self):
            return self.getToken(LtlParser.LN, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLn" ):
                return visitor.visitExprLn(self)
            else:
                return visitor.visitChildren(self)


    class ExprExpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXP(self):
            return self.getToken(LtlParser.EXP, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprExp" ):
                return visitor.visitExprExp(self)
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


    class ExprLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(LtlParser.LiteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteral" ):
                return visitor.visitExprLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ExprMultDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LtlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LtlParser.ExpressionContext,i)

        def multdivOp(self):
            return self.getTypedRuleContext(LtlParser.MultdivOpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultDiv" ):
                return visitor.visitExprMultDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprSqrtContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SQRT(self):
            return self.getToken(LtlParser.SQRT, 0)
        def LPAREN(self):
            return self.getToken(LtlParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(LtlParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(LtlParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSqrt" ):
                return visitor.visitExprSqrt(self)
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
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = LtlParser.ExprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 114
                self.match(LtlParser.LPAREN)
                self.state = 115
                self.expression(0)
                self.state = 116
                self.match(LtlParser.RPAREN)
                pass
            elif token in [1]:
                localctx = LtlParser.ExprNegateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(LtlParser.MINUS)
                self.state = 119
                self.expression(31)
                pass
            elif token in [16]:
                localctx = LtlParser.ExprAbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(LtlParser.ABS)
                self.state = 121
                self.match(LtlParser.LPAREN)
                self.state = 122
                self.expression(0)
                self.state = 123
                self.match(LtlParser.RPAREN)
                pass
            elif token in [17]:
                localctx = LtlParser.ExprSqrtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 125
                self.match(LtlParser.SQRT)
                self.state = 126
                self.match(LtlParser.LPAREN)
                self.state = 127
                self.expression(0)
                self.state = 128
                self.match(LtlParser.RPAREN)
                pass
            elif token in [18]:
                localctx = LtlParser.ExprExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(LtlParser.EXP)
                self.state = 131
                self.match(LtlParser.LPAREN)
                self.state = 132
                self.expression(0)
                self.state = 133
                self.match(LtlParser.RPAREN)
                pass
            elif token in [19]:
                localctx = LtlParser.ExprPowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(LtlParser.POW)
                self.state = 136
                self.match(LtlParser.LPAREN)
                self.state = 137
                self.expression(0)
                self.state = 138
                self.match(LtlParser.COMMA)
                self.state = 139
                self.expression(0)
                self.state = 140
                self.match(LtlParser.RPAREN)
                pass
            elif token in [20]:
                localctx = LtlParser.ExprLogContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(LtlParser.LOG)
                self.state = 143
                self.match(LtlParser.LPAREN)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.match(LtlParser.COMMA)
                self.state = 146
                self.expression(0)
                self.state = 147
                self.match(LtlParser.RPAREN)
                pass
            elif token in [21]:
                localctx = LtlParser.ExprLnContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(LtlParser.LN)
                self.state = 150
                self.match(LtlParser.LPAREN)
                self.state = 151
                self.expression(0)
                self.state = 152
                self.match(LtlParser.RPAREN)
                pass
            elif token in [42]:
                localctx = LtlParser.ExprNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(LtlParser.NotOperator)
                self.state = 155
                self.expression(21)
                pass
            elif token in [50]:
                localctx = LtlParser.ExprAlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(LtlParser.AlwaysOperator)
                self.state = 157
                self.expression(20)
                pass
            elif token in [51]:
                localctx = LtlParser.ExprEvContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(LtlParser.EventuallyOperator)
                self.state = 159
                self.expression(19)
                pass
            elif token in [54]:
                localctx = LtlParser.ExprHistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.match(LtlParser.HistoricallyOperator)
                self.state = 161
                self.expression(18)
                pass
            elif token in [55]:
                localctx = LtlParser.ExpreOnceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(LtlParser.OnceOperator)
                self.state = 163
                self.expression(17)
                pass
            elif token in [58]:
                localctx = LtlParser.ExprPreviousContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                self.match(LtlParser.PreviousOperator)
                self.state = 165
                self.expression(16)
                pass
            elif token in [57]:
                localctx = LtlParser.ExprNextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 166
                self.match(LtlParser.NextOperator)
                self.state = 167
                self.expression(15)
                pass
            elif token in [60]:
                localctx = LtlParser.ExprStrongPreviousContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(LtlParser.StrongPreviousOperator)
                self.state = 169
                self.expression(14)
                pass
            elif token in [59]:
                localctx = LtlParser.ExprStrongNextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                self.match(LtlParser.StrongNextOperator)
                self.state = 171
                self.expression(13)
                pass
            elif token in [48]:
                localctx = LtlParser.ExprRiseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 172
                self.match(LtlParser.RiseOperator)
                self.state = 173
                self.match(LtlParser.LPAREN)
                self.state = 174
                self.expression(0)
                self.state = 175
                self.match(LtlParser.RPAREN)
                pass
            elif token in [49]:
                localctx = LtlParser.ExprFallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.match(LtlParser.FallOperator)
                self.state = 178
                self.match(LtlParser.LPAREN)
                self.state = 179
                self.expression(0)
                self.state = 180
                self.match(LtlParser.RPAREN)
                pass
            elif token in [73]:
                localctx = LtlParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.match(LtlParser.Identifier)
                pass
            elif token in [71, 72]:
                localctx = LtlParser.ExprLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = LtlParser.ExprMultDivContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 187
                        self.multdivOp()
                        self.state = 188
                        self.expression(25)
                        pass

                    elif la_ == 2:
                        localctx = LtlParser.ExprAddSubContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 190
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 191
                        self.addsubOp()
                        self.state = 192
                        self.expression(24)
                        pass

                    elif la_ == 3:
                        localctx = LtlParser.ExprPredicateContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 194
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 195
                        self.comparisonOp()
                        self.state = 196
                        self.expression(23)
                        pass

                    elif la_ == 4:
                        localctx = LtlParser.ExprUntilContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 199
                        self.match(LtlParser.UntilOperator)
                        self.state = 200
                        self.expression(13)
                        pass

                    elif la_ == 5:
                        localctx = LtlParser.ExprUnlessContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 202
                        self.match(LtlParser.UnlessOperator)
                        self.state = 203
                        self.expression(12)
                        pass

                    elif la_ == 6:
                        localctx = LtlParser.ExprSinceContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 204
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 205
                        self.match(LtlParser.SinceOperator)
                        self.state = 206
                        self.expression(11)
                        pass

                    elif la_ == 7:
                        localctx = LtlParser.ExprAndContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 207
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 208
                        self.match(LtlParser.AndOperator)
                        self.state = 209
                        self.expression(10)
                        pass

                    elif la_ == 8:
                        localctx = LtlParser.ExprOrContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 210
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 211
                        self.match(LtlParser.OrOperator)
                        self.state = 212
                        self.expression(9)
                        pass

                    elif la_ == 9:
                        localctx = LtlParser.ExprImpliesContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 213
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 214
                        self.match(LtlParser.ImpliesOperator)
                        self.state = 215
                        self.expression(8)
                        pass

                    elif la_ == 10:
                        localctx = LtlParser.ExprIffContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 216
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 217
                        self.match(LtlParser.IffOperator)
                        self.state = 218
                        self.expression(7)
                        pass

                    elif la_ == 11:
                        localctx = LtlParser.ExprXorContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 219
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 220
                        self.match(LtlParser.XorOperator)
                        self.state = 221
                        self.expression(6)
                        pass

             
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultdivOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_multdivOp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivContext(MultdivOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.MultdivOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIVIDE(self):
            return self.getToken(LtlParser.DIVIDE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(MultdivOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.MultdivOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIMES(self):
            return self.getToken(LtlParser.TIMES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)



    def multdivOp(self):

        localctx = LtlParser.MultdivOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_multdivOp)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = LtlParser.MultContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(LtlParser.TIMES)
                pass
            elif token in [4]:
                localctx = LtlParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(LtlParser.DIVIDE)
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


    class AddsubOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LtlParser.RULE_addsubOp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PlusContext(AddsubOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.AddsubOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(LtlParser.PLUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(AddsubOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LtlParser.AddsubOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(LtlParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)



    def addsubOp(self):

        localctx = LtlParser.AddsubOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_addsubOp)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = LtlParser.PlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(LtlParser.PLUS)
                pass
            elif token in [1]:
                localctx = LtlParser.MinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(LtlParser.MINUS)
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
        self.enterRule(localctx, 32, self.RULE_comparisonOp)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                localctx = LtlParser.LeqContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(LtlParser.LesserOrEqualOperator)
                pass
            elif token in [63]:
                localctx = LtlParser.GeqContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(LtlParser.GreaterOrEqualOperator)
                pass
            elif token in [66]:
                localctx = LtlParser.LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.match(LtlParser.LesserOperator)
                pass
            elif token in [65]:
                localctx = LtlParser.GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.match(LtlParser.GreaterOperator)
                pass
            elif token in [61]:
                localctx = LtlParser.EqContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.match(LtlParser.EqualOperator)
                pass
            elif token in [62]:
                localctx = LtlParser.NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 240
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

        def getRuleIndex(self):
            return LtlParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = LtlParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not(_la==71 or _la==72):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 5)
         




