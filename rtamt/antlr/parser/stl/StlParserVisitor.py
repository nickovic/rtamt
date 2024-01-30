# Generated from rtamt\antlr\grammar\tl\StlParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StlParser import StlParser
else:
    from StlParser import StlParser

# This class defines a complete generic visitor for a parse tree produced by StlParser.

class StlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StlParser#interval.
    def visitInterval(self, ctx:StlParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx:StlParser.IntervalTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#constantTimeLiteral.
    def visitConstantTimeLiteral(self, ctx:StlParser.ConstantTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#unit.
    def visitUnit(self, ctx:StlParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprNot.
    def visitExprNot(self, ctx:StlParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprNext.
    def visitExprNext(self, ctx:StlParser.ExprNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUnless.
    def visitExprUnless(self, ctx:StlParser.ExprUnlessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprFall.
    def visitExprFall(self, ctx:StlParser.ExprFallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprPredicate.
    def visitExprPredicate(self, ctx:StlParser.ExprPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprRise.
    def visitExprRise(self, ctx:StlParser.ExprRiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprOr.
    def visitExprOr(self, ctx:StlParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprId.
    def visitExprId(self, ctx:StlParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAddition.
    def visitExprAddition(self, ctx:StlParser.ExprAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprSince.
    def visitExprSince(self, ctx:StlParser.ExprSinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprParen.
    def visitExprParen(self, ctx:StlParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprDivision.
    def visitExprDivision(self, ctx:StlParser.ExprDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprIff.
    def visitExprIff(self, ctx:StlParser.ExprIffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExpreOnce.
    def visitExpreOnce(self, ctx:StlParser.ExpreOnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx:StlParser.ExprMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprEv.
    def visitExprEv(self, ctx:StlParser.ExprEvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprStrongPrevious.
    def visitExprStrongPrevious(self, ctx:StlParser.ExprStrongPreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprImplies.
    def visitExprImplies(self, ctx:StlParser.ExprImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUntil.
    def visitExprUntil(self, ctx:StlParser.ExprUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprStrongNext.
    def visitExprStrongNext(self, ctx:StlParser.ExprStrongNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAbs.
    def visitExprAbs(self, ctx:StlParser.ExprAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx:StlParser.ExprSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAnd.
    def visitExprAnd(self, ctx:StlParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprPow.
    def visitExprPow(self, ctx:StlParser.ExprPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprPrevious.
    def visitExprPrevious(self, ctx:StlParser.ExprPreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprHist.
    def visitExprHist(self, ctx:StlParser.ExprHistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprXor.
    def visitExprXor(self, ctx:StlParser.ExprXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprExp.
    def visitExprExp(self, ctx:StlParser.ExprExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAlways.
    def visitExprAlways(self, ctx:StlParser.ExprAlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprLiteral.
    def visitExprLiteral(self, ctx:StlParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprSqrt.
    def visitExprSqrt(self, ctx:StlParser.ExprSqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#specification_file.
    def visitSpecification_file(self, ctx:StlParser.Specification_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#specification.
    def visitSpecification(self, ctx:StlParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#SpecificationId.
    def visitSpecificationId(self, ctx:StlParser.SpecificationIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#modImport.
    def visitModImport(self, ctx:StlParser.ModImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#assertion.
    def visitAssertion(self, ctx:StlParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#declVariable.
    def visitDeclVariable(self, ctx:StlParser.DeclVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#declConstant.
    def visitDeclConstant(self, ctx:StlParser.DeclConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#annotation.
    def visitAnnotation(self, ctx:StlParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#rosTopic.
    def visitRosTopic(self, ctx:StlParser.RosTopicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:StlParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:StlParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx:StlParser.AsgnLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#AsgnExpr.
    def visitAsgnExpr(self, ctx:StlParser.AsgnExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#domainType.
    def visitDomainType(self, ctx:StlParser.DomainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ioType.
    def visitIoType(self, ctx:StlParser.IoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Leq.
    def visitLeq(self, ctx:StlParser.LeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Geq.
    def visitGeq(self, ctx:StlParser.GeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Less.
    def visitLess(self, ctx:StlParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Greater.
    def visitGreater(self, ctx:StlParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Eq.
    def visitEq(self, ctx:StlParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Neq.
    def visitNeq(self, ctx:StlParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#literal.
    def visitLiteral(self, ctx:StlParser.LiteralContext):
        return self.visitChildren(ctx)



del StlParser