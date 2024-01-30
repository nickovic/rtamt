# Generated from rtamt\antlr\grammar\tl\LtlParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LtlParser import LtlParser
else:
    from LtlParser import LtlParser

# This class defines a complete generic visitor for a parse tree produced by LtlParser.

class LtlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LtlParser#specification_file.
    def visitSpecification_file(self, ctx:LtlParser.Specification_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#specification.
    def visitSpecification(self, ctx:LtlParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#SpecificationId.
    def visitSpecificationId(self, ctx:LtlParser.SpecificationIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#modImport.
    def visitModImport(self, ctx:LtlParser.ModImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#assertion.
    def visitAssertion(self, ctx:LtlParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#declVariable.
    def visitDeclVariable(self, ctx:LtlParser.DeclVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#declConstant.
    def visitDeclConstant(self, ctx:LtlParser.DeclConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#annotation.
    def visitAnnotation(self, ctx:LtlParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#rosTopic.
    def visitRosTopic(self, ctx:LtlParser.RosTopicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:LtlParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:LtlParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx:LtlParser.AsgnLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#AsgnExpr.
    def visitAsgnExpr(self, ctx:LtlParser.AsgnExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#domainType.
    def visitDomainType(self, ctx:LtlParser.DomainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ioType.
    def visitIoType(self, ctx:LtlParser.IoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprNot.
    def visitExprNot(self, ctx:LtlParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprNext.
    def visitExprNext(self, ctx:LtlParser.ExprNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprUnless.
    def visitExprUnless(self, ctx:LtlParser.ExprUnlessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprFall.
    def visitExprFall(self, ctx:LtlParser.ExprFallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprPredicate.
    def visitExprPredicate(self, ctx:LtlParser.ExprPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprRise.
    def visitExprRise(self, ctx:LtlParser.ExprRiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprOr.
    def visitExprOr(self, ctx:LtlParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprId.
    def visitExprId(self, ctx:LtlParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprAddition.
    def visitExprAddition(self, ctx:LtlParser.ExprAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprSince.
    def visitExprSince(self, ctx:LtlParser.ExprSinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprParen.
    def visitExprParen(self, ctx:LtlParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprDivision.
    def visitExprDivision(self, ctx:LtlParser.ExprDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprIff.
    def visitExprIff(self, ctx:LtlParser.ExprIffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExpreOnce.
    def visitExpreOnce(self, ctx:LtlParser.ExpreOnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx:LtlParser.ExprMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprEv.
    def visitExprEv(self, ctx:LtlParser.ExprEvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprStrongPrevious.
    def visitExprStrongPrevious(self, ctx:LtlParser.ExprStrongPreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprImplies.
    def visitExprImplies(self, ctx:LtlParser.ExprImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprUntil.
    def visitExprUntil(self, ctx:LtlParser.ExprUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprStrongNext.
    def visitExprStrongNext(self, ctx:LtlParser.ExprStrongNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprAbs.
    def visitExprAbs(self, ctx:LtlParser.ExprAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx:LtlParser.ExprSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprAnd.
    def visitExprAnd(self, ctx:LtlParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprPow.
    def visitExprPow(self, ctx:LtlParser.ExprPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprPrevious.
    def visitExprPrevious(self, ctx:LtlParser.ExprPreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprHist.
    def visitExprHist(self, ctx:LtlParser.ExprHistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprXor.
    def visitExprXor(self, ctx:LtlParser.ExprXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprExp.
    def visitExprExp(self, ctx:LtlParser.ExprExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprAlways.
    def visitExprAlways(self, ctx:LtlParser.ExprAlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprLiteral.
    def visitExprLiteral(self, ctx:LtlParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#ExprSqrt.
    def visitExprSqrt(self, ctx:LtlParser.ExprSqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#Leq.
    def visitLeq(self, ctx:LtlParser.LeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#Geq.
    def visitGeq(self, ctx:LtlParser.GeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#Less.
    def visitLess(self, ctx:LtlParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#Greater.
    def visitGreater(self, ctx:LtlParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#Eq.
    def visitEq(self, ctx:LtlParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#Neq.
    def visitNeq(self, ctx:LtlParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LtlParser#literal.
    def visitLiteral(self, ctx:LtlParser.LiteralContext):
        return self.visitChildren(ctx)



del LtlParser