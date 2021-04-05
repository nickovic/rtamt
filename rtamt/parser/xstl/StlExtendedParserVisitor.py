# Generated from StlExtendedParser.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StlExtendedParser import StlExtendedParser
else:
    from StlExtendedParser import StlExtendedParser

# This class defines a complete generic visitor for a parse tree produced by StlExtendedParser.

class StlExtendedParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StlExtendedParser#ExprSince.
    def visitExprSince(self, ctx:StlExtendedParser.ExprSinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprParen.
    def visitExprParen(self, ctx:StlExtendedParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprIff.
    def visitExprIff(self, ctx:StlExtendedParser.ExprIffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExpreOnce.
    def visitExpreOnce(self, ctx:StlExtendedParser.ExpreOnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprEv.
    def visitExprEv(self, ctx:StlExtendedParser.ExprEvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprImplies.
    def visitExprImplies(self, ctx:StlExtendedParser.ExprImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprUntil.
    def visitExprUntil(self, ctx:StlExtendedParser.ExprUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprNot.
    def visitExprNot(self, ctx:StlExtendedParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprNext.
    def visitExprNext(self, ctx:StlExtendedParser.ExprNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprAnd.
    def visitExprAnd(self, ctx:StlExtendedParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprUnless.
    def visitExprUnless(self, ctx:StlExtendedParser.ExprUnlessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprPrevious.
    def visitExprPrevious(self, ctx:StlExtendedParser.ExprPreviousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprHist.
    def visitExprHist(self, ctx:StlExtendedParser.ExprHistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprFall.
    def visitExprFall(self, ctx:StlExtendedParser.ExprFallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprPredicate.
    def visitExprPredicate(self, ctx:StlExtendedParser.ExprPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprXor.
    def visitExprXor(self, ctx:StlExtendedParser.ExprXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprRise.
    def visitExprRise(self, ctx:StlExtendedParser.ExprRiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprOr.
    def visitExprOr(self, ctx:StlExtendedParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprBackto.
    def visitExprBackto(self, ctx:StlExtendedParser.ExprBacktoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprAlways.
    def visitExprAlways(self, ctx:StlExtendedParser.ExprAlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprReal.
    def visitExprReal(self, ctx:StlExtendedParser.ExprRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#interval.
    def visitInterval(self, ctx:StlExtendedParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx:StlExtendedParser.IntervalTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#constantTimeLiteral.
    def visitConstantTimeLiteral(self, ctx:StlExtendedParser.ConstantTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#unit.
    def visitUnit(self, ctx:StlExtendedParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#specification_file.
    def visitSpecification_file(self, ctx:StlExtendedParser.Specification_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#specification.
    def visitSpecification(self, ctx:StlExtendedParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#SpecificationId.
    def visitSpecificationId(self, ctx:StlExtendedParser.SpecificationIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#modImport.
    def visitModImport(self, ctx:StlExtendedParser.ModImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#assertion.
    def visitAssertion(self, ctx:StlExtendedParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#declVariable.
    def visitDeclVariable(self, ctx:StlExtendedParser.DeclVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#declConstant.
    def visitDeclConstant(self, ctx:StlExtendedParser.DeclConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#annotation.
    def visitAnnotation(self, ctx:StlExtendedParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#rosTopic.
    def visitRosTopic(self, ctx:StlExtendedParser.RosTopicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:StlExtendedParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx:StlExtendedParser.ConstantDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx:StlExtendedParser.AsgnLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#AsgnExpr.
    def visitAsgnExpr(self, ctx:StlExtendedParser.AsgnExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#domainType.
    def visitDomainType(self, ctx:StlExtendedParser.DomainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ioType.
    def visitIoType(self, ctx:StlExtendedParser.IoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx:StlExtendedParser.ExprSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprDivision.
    def visitExprDivision(self, ctx:StlExtendedParser.ExprDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx:StlExtendedParser.ExprMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprLiteral.
    def visitExprLiteral(self, ctx:StlExtendedParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprId.
    def visitExprId(self, ctx:StlExtendedParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprAbs.
    def visitExprAbs(self, ctx:StlExtendedParser.ExprAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprAddition.
    def visitExprAddition(self, ctx:StlExtendedParser.ExprAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Leq.
    def visitLeq(self, ctx:StlExtendedParser.LeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Geq.
    def visitGeq(self, ctx:StlExtendedParser.GeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Less.
    def visitLess(self, ctx:StlExtendedParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Greater.
    def visitGreater(self, ctx:StlExtendedParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Eq.
    def visitEq(self, ctx:StlExtendedParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Neq.
    def visitNeq(self, ctx:StlExtendedParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#literal.
    def visitLiteral(self, ctx:StlExtendedParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Id.
    def visitId(self, ctx:StlExtendedParser.IdContext):
        return self.visitChildren(ctx)



del StlExtendedParser