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
        4,1,75,242,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,3,1,41,8,
        1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,1,4,1,57,8,1,11,1,12,1,58,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,3,4,71,8,4,1,4,1,4,1,5,1,5,3,5,77,8,5,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,3,8,90,8,8,1,8,1,8,1,8,3,8,95,8,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,107,8,10,1,11,1,11,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,147,8,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,177,8,13,10,13,12,13,180,9,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,207,8,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,221,8,14,
        10,14,12,14,224,9,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,232,8,15,
        1,16,1,16,1,16,1,16,3,16,238,8,16,1,17,1,17,1,17,0,2,26,28,18,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,2,2,0,32,35,71,
        71,1,0,27,28,270,0,36,1,0,0,0,2,40,1,0,0,0,4,60,1,0,0,0,6,63,1,0,
        0,0,8,70,1,0,0,0,10,76,1,0,0,0,12,78,1,0,0,0,14,81,1,0,0,0,16,89,
        1,0,0,0,18,96,1,0,0,0,20,106,1,0,0,0,22,108,1,0,0,0,24,110,1,0,0,
        0,26,146,1,0,0,0,28,206,1,0,0,0,30,231,1,0,0,0,32,237,1,0,0,0,34,
        239,1,0,0,0,36,37,3,2,1,0,37,38,5,0,0,1,38,1,1,0,0,0,39,41,3,4,2,
        0,40,39,1,0,0,0,40,41,1,0,0,0,41,45,1,0,0,0,42,44,3,6,3,0,43,42,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,52,1,0,0,0,
        47,45,1,0,0,0,48,51,3,10,5,0,49,51,3,12,6,0,50,48,1,0,0,0,50,49,
        1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,56,1,0,0,0,
        54,52,1,0,0,0,55,57,3,8,4,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,
        0,0,0,58,59,1,0,0,0,59,3,1,0,0,0,60,61,5,38,0,0,61,62,5,71,0,0,62,
        5,1,0,0,0,63,64,5,39,0,0,64,65,5,71,0,0,65,66,5,26,0,0,66,67,5,71,
        0,0,67,7,1,0,0,0,68,69,5,71,0,0,69,71,5,65,0,0,70,68,1,0,0,0,70,
        71,1,0,0,0,71,72,1,0,0,0,72,73,3,26,13,0,73,9,1,0,0,0,74,77,3,16,
        8,0,75,77,3,18,9,0,76,74,1,0,0,0,76,75,1,0,0,0,77,11,1,0,0,0,78,
        79,5,15,0,0,79,80,3,14,7,0,80,13,1,0,0,0,81,82,5,25,0,0,82,83,5,
        5,0,0,83,84,5,71,0,0,84,85,5,13,0,0,85,86,5,71,0,0,86,87,5,6,0,0,
        87,15,1,0,0,0,88,90,3,24,12,0,89,88,1,0,0,0,89,90,1,0,0,0,90,91,
        1,0,0,0,91,92,3,22,11,0,92,94,5,71,0,0,93,95,3,20,10,0,94,93,1,0,
        0,0,94,95,1,0,0,0,95,17,1,0,0,0,96,97,5,30,0,0,97,98,3,22,11,0,98,
        99,5,71,0,0,99,100,5,65,0,0,100,101,3,32,16,0,101,19,1,0,0,0,102,
        103,5,65,0,0,103,107,3,32,16,0,104,105,5,65,0,0,105,107,3,26,13,
        0,106,102,1,0,0,0,106,104,1,0,0,0,107,21,1,0,0,0,108,109,7,0,0,0,
        109,23,1,0,0,0,110,111,7,1,0,0,111,25,1,0,0,0,112,113,6,13,-1,0,
        113,147,3,28,14,0,114,115,5,5,0,0,115,116,3,26,13,0,116,117,5,6,
        0,0,117,147,1,0,0,0,118,119,5,40,0,0,119,147,3,26,13,19,120,121,
        5,48,0,0,121,147,3,26,13,13,122,123,5,49,0,0,123,147,3,26,13,12,
        124,125,5,52,0,0,125,147,3,26,13,9,126,127,5,53,0,0,127,147,3,26,
        13,8,128,129,5,46,0,0,129,130,5,5,0,0,130,131,3,26,13,0,131,132,
        5,6,0,0,132,147,1,0,0,0,133,134,5,47,0,0,134,135,5,5,0,0,135,136,
        3,26,13,0,136,137,5,6,0,0,137,147,1,0,0,0,138,139,5,56,0,0,139,147,
        3,26,13,4,140,141,5,55,0,0,141,147,3,26,13,3,142,143,5,58,0,0,143,
        147,3,26,13,2,144,145,5,57,0,0,145,147,3,26,13,1,146,112,1,0,0,0,
        146,114,1,0,0,0,146,118,1,0,0,0,146,120,1,0,0,0,146,122,1,0,0,0,
        146,124,1,0,0,0,146,126,1,0,0,0,146,128,1,0,0,0,146,133,1,0,0,0,
        146,138,1,0,0,0,146,140,1,0,0,0,146,142,1,0,0,0,146,144,1,0,0,0,
        147,178,1,0,0,0,148,149,10,21,0,0,149,150,3,30,15,0,150,151,3,26,
        13,22,151,177,1,0,0,0,152,153,10,18,0,0,153,154,5,41,0,0,154,177,
        3,26,13,19,155,156,10,17,0,0,156,157,5,42,0,0,157,177,3,26,13,18,
        158,159,10,16,0,0,159,160,5,44,0,0,160,177,3,26,13,17,161,162,10,
        15,0,0,162,163,5,43,0,0,163,177,3,26,13,16,164,165,10,14,0,0,165,
        166,5,45,0,0,166,177,3,26,13,15,167,168,10,11,0,0,168,169,5,50,0,
        0,169,177,3,26,13,12,170,171,10,10,0,0,171,172,5,51,0,0,172,177,
        3,26,13,11,173,174,10,7,0,0,174,175,5,54,0,0,175,177,3,26,13,8,176,
        148,1,0,0,0,176,152,1,0,0,0,176,155,1,0,0,0,176,158,1,0,0,0,176,
        161,1,0,0,0,176,164,1,0,0,0,176,167,1,0,0,0,176,170,1,0,0,0,176,
        173,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,
        27,1,0,0,0,180,178,1,0,0,0,181,182,6,14,-1,0,182,207,5,71,0,0,183,
        207,3,32,16,0,184,185,5,16,0,0,185,186,5,5,0,0,186,187,3,28,14,0,
        187,188,5,6,0,0,188,207,1,0,0,0,189,190,5,17,0,0,190,191,5,5,0,0,
        191,192,3,28,14,0,192,193,5,6,0,0,193,207,1,0,0,0,194,195,5,18,0,
        0,195,196,5,5,0,0,196,197,3,28,14,0,197,198,5,6,0,0,198,207,1,0,
        0,0,199,200,5,19,0,0,200,201,5,5,0,0,201,202,3,28,14,0,202,203,5,
        13,0,0,203,204,3,28,14,0,204,205,5,6,0,0,205,207,1,0,0,0,206,181,
        1,0,0,0,206,183,1,0,0,0,206,184,1,0,0,0,206,189,1,0,0,0,206,194,
        1,0,0,0,206,199,1,0,0,0,207,222,1,0,0,0,208,209,10,8,0,0,209,210,
        5,2,0,0,210,221,3,28,14,9,211,212,10,7,0,0,212,213,5,1,0,0,213,221,
        3,28,14,8,214,215,10,6,0,0,215,216,5,3,0,0,216,221,3,28,14,7,217,
        218,10,5,0,0,218,219,5,4,0,0,219,221,3,28,14,6,220,208,1,0,0,0,220,
        211,1,0,0,0,220,214,1,0,0,0,220,217,1,0,0,0,221,224,1,0,0,0,222,
        220,1,0,0,0,222,223,1,0,0,0,223,29,1,0,0,0,224,222,1,0,0,0,225,232,
        5,62,0,0,226,232,5,61,0,0,227,232,5,64,0,0,228,232,5,63,0,0,229,
        232,5,59,0,0,230,232,5,60,0,0,231,225,1,0,0,0,231,226,1,0,0,0,231,
        227,1,0,0,0,231,228,1,0,0,0,231,229,1,0,0,0,231,230,1,0,0,0,232,
        31,1,0,0,0,233,238,5,69,0,0,234,238,5,70,0,0,235,236,5,1,0,0,236,
        238,3,32,16,0,237,233,1,0,0,0,237,234,1,0,0,0,237,235,1,0,0,0,238,
        33,1,0,0,0,239,240,5,71,0,0,240,35,1,0,0,0,18,40,45,50,52,58,70,
        76,89,94,106,146,176,178,206,220,222,231,237
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
    RULE_identifier = 17

    ruleNames =  [ "specification_file", "specification", "spec", "modimport", 
                   "assertion", "declaration", "annotation", "annotation_type", 
                   "variableDeclaration", "constantDeclaration", "assignment", 
                   "domainType", "ioType", "expression", "real_expression", 
                   "comparisonOp", "literal", "identifier" ]

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
            if _la==38:
                self.state = 39
                self.spec()


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
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
                    if token in [27, 28, 30, 32, 33, 34, 35, 71]:
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 554999384841846818) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & 7) != 0)):
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
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27, 28, 32, 33, 34, 35, 71]:
                localctx = LtlParser.DeclVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.variableDeclaration()
                pass
            elif token in [30]:
                localctx = LtlParser.DeclConstantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
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
            self.state = 78
            self.match(LtlParser.AT)
            self.state = 79
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
            self.state = 81
            self.match(LtlParser.ROS_Topic)
            self.state = 82
            self.match(LtlParser.LPAREN)
            self.state = 83
            self.match(LtlParser.Identifier)
            self.state = 84
            self.match(LtlParser.COMMA)
            self.state = 85
            self.match(LtlParser.Identifier)
            self.state = 86
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
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27 or _la==28:
                self.state = 88
                self.ioType()


            self.state = 91
            self.domainType()
            self.state = 92
            self.match(LtlParser.Identifier)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 93
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
            self.state = 96
            self.match(LtlParser.Constant)
            self.state = 97
            self.domainType()
            self.state = 98
            self.match(LtlParser.Identifier)
            self.state = 99
            self.match(LtlParser.EQUAL)
            self.state = 100
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
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = LtlParser.AsgnLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(LtlParser.EQUAL)
                self.state = 103
                self.literal()
                pass

            elif la_ == 2:
                localctx = LtlParser.AsgnExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(LtlParser.EQUAL)
                self.state = 105
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
            self.state = 108
            _la = self._input.LA(1)
            if not(((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 549755813903) != 0)):
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
            self.state = 110
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
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 16, 17, 18, 19, 69, 70, 71]:
                localctx = LtlParser.ExprRealContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 113
                self.real_expression(0)
                pass
            elif token in [5]:
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
            elif token in [40]:
                localctx = LtlParser.ExprNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(LtlParser.NotOperator)
                self.state = 119
                self.expression(19)
                pass
            elif token in [48]:
                localctx = LtlParser.ExprAlwaysContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(LtlParser.AlwaysOperator)
                self.state = 121
                self.expression(13)
                pass
            elif token in [49]:
                localctx = LtlParser.ExprEvContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(LtlParser.EventuallyOperator)
                self.state = 123
                self.expression(12)
                pass
            elif token in [52]:
                localctx = LtlParser.ExprHistContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(LtlParser.HistoricallyOperator)
                self.state = 125
                self.expression(9)
                pass
            elif token in [53]:
                localctx = LtlParser.ExpreOnceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(LtlParser.OnceOperator)
                self.state = 127
                self.expression(8)
                pass
            elif token in [46]:
                localctx = LtlParser.ExprRiseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(LtlParser.RiseOperator)
                self.state = 129
                self.match(LtlParser.LPAREN)
                self.state = 130
                self.expression(0)
                self.state = 131
                self.match(LtlParser.RPAREN)
                pass
            elif token in [47]:
                localctx = LtlParser.ExprFallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(LtlParser.FallOperator)
                self.state = 134
                self.match(LtlParser.LPAREN)
                self.state = 135
                self.expression(0)
                self.state = 136
                self.match(LtlParser.RPAREN)
                pass
            elif token in [56]:
                localctx = LtlParser.ExprPreviousContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(LtlParser.PreviousOperator)
                self.state = 139
                self.expression(4)
                pass
            elif token in [55]:
                localctx = LtlParser.ExprNextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(LtlParser.NextOperator)
                self.state = 141
                self.expression(3)
                pass
            elif token in [58]:
                localctx = LtlParser.ExprStrongPreviousContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(LtlParser.StrongPreviousOperator)
                self.state = 143
                self.expression(2)
                pass
            elif token in [57]:
                localctx = LtlParser.ExprStrongNextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(LtlParser.StrongNextOperator)
                self.state = 145
                self.expression(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 176
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = LtlParser.ExprPredicateContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 149
                        self.comparisonOp()
                        self.state = 150
                        self.expression(22)
                        pass

                    elif la_ == 2:
                        localctx = LtlParser.ExprOrContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 152
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 153
                        self.match(LtlParser.OrOperator)
                        self.state = 154
                        self.expression(19)
                        pass

                    elif la_ == 3:
                        localctx = LtlParser.ExprAndContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 155
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 156
                        self.match(LtlParser.AndOperator)
                        self.state = 157
                        self.expression(18)
                        pass

                    elif la_ == 4:
                        localctx = LtlParser.ExprImpliesContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 158
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 159
                        self.match(LtlParser.ImpliesOperator)
                        self.state = 160
                        self.expression(17)
                        pass

                    elif la_ == 5:
                        localctx = LtlParser.ExprIffContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 161
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 162
                        self.match(LtlParser.IffOperator)
                        self.state = 163
                        self.expression(16)
                        pass

                    elif la_ == 6:
                        localctx = LtlParser.ExprXorContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 165
                        self.match(LtlParser.XorOperator)
                        self.state = 166
                        self.expression(15)
                        pass

                    elif la_ == 7:
                        localctx = LtlParser.ExprUntilContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 167
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 168
                        self.match(LtlParser.UntilOperator)
                        self.state = 169
                        self.expression(12)
                        pass

                    elif la_ == 8:
                        localctx = LtlParser.ExprUnlessContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 171
                        self.match(LtlParser.UnlessOperator)
                        self.state = 172
                        self.expression(11)
                        pass

                    elif la_ == 9:
                        localctx = LtlParser.ExprSinceContext(self, LtlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 174
                        self.match(LtlParser.SinceOperator)
                        self.state = 175
                        self.expression(8)
                        pass

             
                self.state = 180
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
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [71]:
                localctx = LtlParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 182
                self.match(LtlParser.Identifier)
                pass
            elif token in [1, 69, 70]:
                localctx = LtlParser.ExprLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.literal()
                pass
            elif token in [16]:
                localctx = LtlParser.ExprAbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 184
                self.match(LtlParser.ABS)
                self.state = 185
                self.match(LtlParser.LPAREN)
                self.state = 186
                self.real_expression(0)
                self.state = 187
                self.match(LtlParser.RPAREN)
                pass
            elif token in [17]:
                localctx = LtlParser.ExprSqrtContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.match(LtlParser.SQRT)
                self.state = 190
                self.match(LtlParser.LPAREN)
                self.state = 191
                self.real_expression(0)
                self.state = 192
                self.match(LtlParser.RPAREN)
                pass
            elif token in [18]:
                localctx = LtlParser.ExprExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 194
                self.match(LtlParser.EXP)
                self.state = 195
                self.match(LtlParser.LPAREN)
                self.state = 196
                self.real_expression(0)
                self.state = 197
                self.match(LtlParser.RPAREN)
                pass
            elif token in [19]:
                localctx = LtlParser.ExprPowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 199
                self.match(LtlParser.POW)
                self.state = 200
                self.match(LtlParser.LPAREN)
                self.state = 201
                self.real_expression(0)
                self.state = 202
                self.match(LtlParser.COMMA)
                self.state = 203
                self.real_expression(0)
                self.state = 204
                self.match(LtlParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 220
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = LtlParser.ExprAdditionContext(self, LtlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 208
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 209
                        self.match(LtlParser.PLUS)
                        self.state = 210
                        self.real_expression(9)
                        pass

                    elif la_ == 2:
                        localctx = LtlParser.ExprSubtractionContext(self, LtlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 211
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 212
                        self.match(LtlParser.MINUS)
                        self.state = 213
                        self.real_expression(8)
                        pass

                    elif la_ == 3:
                        localctx = LtlParser.ExprMultiplicationContext(self, LtlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 214
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 215
                        self.match(LtlParser.TIMES)
                        self.state = 216
                        self.real_expression(7)
                        pass

                    elif la_ == 4:
                        localctx = LtlParser.ExprDivisionContext(self, LtlParser.Real_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_real_expression)
                        self.state = 217
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 218
                        self.match(LtlParser.DIVIDE)
                        self.state = 219
                        self.real_expression(6)
                        pass

             
                self.state = 224
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
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                localctx = LtlParser.LeqContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(LtlParser.LesserOrEqualOperator)
                pass
            elif token in [61]:
                localctx = LtlParser.GeqContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(LtlParser.GreaterOrEqualOperator)
                pass
            elif token in [64]:
                localctx = LtlParser.LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(LtlParser.LesserOperator)
                pass
            elif token in [63]:
                localctx = LtlParser.GreaterContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.match(LtlParser.GreaterOperator)
                pass
            elif token in [59]:
                localctx = LtlParser.EqContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.match(LtlParser.EqualOperator)
                pass
            elif token in [60]:
                localctx = LtlParser.NeqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 230
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(LtlParser.IntegerLiteral)
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(LtlParser.RealLiteral)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.match(LtlParser.MINUS)
                self.state = 236
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
        self.enterRule(localctx, 34, self.RULE_identifier)
        try:
            localctx = LtlParser.IdContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 239
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
                return self.precpred(self._ctx, 21)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

    def real_expression_sempred(self, localctx:Real_expressionContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 5)
         




