# Generated from XStlParser.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XStlParser import XStlParser
else:
    from XStlParser import XStlParser

# This class defines a complete generic visitor for a parse tree produced by XStlParser.

class XStlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XStlParser#ExprSince.
    def visitExprSince(self, ctx:XStlParser.ExprSinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprParen.
    def visitExprParen(self, ctx:XStlParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprIff.
    def visitExprIff(self, ctx:XStlParser.ExprIffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExpreOnce.
    def visitExpreOnce(self, ctx:XStlParser.ExpreOnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprEv.
    def visitExprEv(self, ctx:XStlParser.ExprEvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprImplies.
    def visitExprImplies(self, ctx:XStlParser.ExprImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprUntil.
    def visitExprUntil(self, ctx:XStlParser.ExprUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprNot.
    def visitExprNot(self, ctx:XStlParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprShift.
    def visitExprShift(self, ctx:XStlParser.ExprShiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprNext.
    def visitExprNext(self, ctx:XStlParser.ExprNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprAnd.
    def visitExprAnd(self, ctx:XStlParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprUnless.
    def visitExprUnless(self, ctx:XStlParser.ExprUnlessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprPrevious.
    def visitExprPrevious(self, ctx:XStlParser.ExprPreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprHist.
    def visitExprHist(self, ctx:XStlParser.ExprHistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprFall.
    def visitExprFall(self, ctx:XStlParser.ExprFallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprPredicate.
    def visitExprPredicate(self, ctx:XStlParser.ExprPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprXor.
    def visitExprXor(self, ctx:XStlParser.ExprXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprRise.
    def visitExprRise(self, ctx:XStlParser.ExprRiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprOr.
    def visitExprOr(self, ctx:XStlParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprAlways.
    def visitExprAlways(self, ctx:XStlParser.ExprAlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprReal.
    def visitExprReal(self, ctx:XStlParser.ExprRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#interval.
    def visitInterval(self, ctx:XStlParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx:XStlParser.IntervalTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#constantTimeLiteral.
    def visitConstantTimeLiteral(self, ctx:XStlParser.ConstantTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#unit.
    def visitUnit(self, ctx:XStlParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#specification_file.
    def visitSpecification_file(self, ctx:XStlParser.Specification_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#specification.
    def visitSpecification(self, ctx:XStlParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#SpecificationId.
    def visitSpecificationId(self, ctx:XStlParser.SpecificationIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#modImport.
    def visitModImport(self, ctx:XStlParser.ModImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#assertion.
    def visitAssertion(self, ctx:XStlParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#declVariable.
    def visitDeclVariable(self, ctx:XStlParser.DeclVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#declConstant.
    def visitDeclConstant(self, ctx:XStlParser.DeclConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#annotation.
    def visitAnnotation(self, ctx:XStlParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#rosTopic.
    def visitRosTopic(self, ctx:XStlParser.RosTopicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:XStlParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:XStlParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx:XStlParser.AsgnLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#AsgnExpr.
    def visitAsgnExpr(self, ctx:XStlParser.AsgnExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#domainType.
    def visitDomainType(self, ctx:XStlParser.DomainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ioType.
    def visitIoType(self, ctx:XStlParser.IoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx:XStlParser.ExprSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprPow.
    def visitExprPow(self, ctx:XStlParser.ExprPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprDivision.
    def visitExprDivision(self, ctx:XStlParser.ExprDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx:XStlParser.ExprMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprLiteral.
    def visitExprLiteral(self, ctx:XStlParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprExp.
    def visitExprExp(self, ctx:XStlParser.ExprExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprSqrt.
    def visitExprSqrt(self, ctx:XStlParser.ExprSqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprId.
    def visitExprId(self, ctx:XStlParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprAbs.
    def visitExprAbs(self, ctx:XStlParser.ExprAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprAddition.
    def visitExprAddition(self, ctx:XStlParser.ExprAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Leq.
    def visitLeq(self, ctx:XStlParser.LeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Geq.
    def visitGeq(self, ctx:XStlParser.GeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Less.
    def visitLess(self, ctx:XStlParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Greater.
    def visitGreater(self, ctx:XStlParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Eq.
    def visitEq(self, ctx:XStlParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Neq.
    def visitNeq(self, ctx:XStlParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#literal.
    def visitLiteral(self, ctx:XStlParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Id.
    def visitId(self, ctx:XStlParser.IdContext):
        return self.visitChildren(ctx)



del XStlParser