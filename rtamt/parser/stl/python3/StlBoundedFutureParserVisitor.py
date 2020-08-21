# Generated from StlBoundedFutureParser.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StlBoundedFutureParser import StlBoundedFutureParser
else:
    from StlBoundedFutureParser import StlBoundedFutureParser

# This class defines a complete generic visitor for a parse tree produced by StlBoundedFutureParser.

class StlBoundedFutureParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StlBoundedFutureParser#stlfile.
    def visitStlfile(self, ctx:StlBoundedFutureParser.StlfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#stlSpecification.
    def visitStlSpecification(self, ctx:StlBoundedFutureParser.StlSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#Specification.
    def visitSpecification(self, ctx:StlBoundedFutureParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#modImport.
    def visitModImport(self, ctx:StlBoundedFutureParser.ModImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#assertion.
    def visitAssertion(self, ctx:StlBoundedFutureParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#declVariable.
    def visitDeclVariable(self, ctx:StlBoundedFutureParser.DeclVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#annotation.
    def visitAnnotation(self, ctx:StlBoundedFutureParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#rosTopic.
    def visitRosTopic(self, ctx:StlBoundedFutureParser.RosTopicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:StlBoundedFutureParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx:StlBoundedFutureParser.AsgnLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#AsgnExpr.
    def visitAsgnExpr(self, ctx:StlBoundedFutureParser.AsgnExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#domainType.
    def visitDomainType(self, ctx:StlBoundedFutureParser.DomainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ioType.
    def visitIoType(self, ctx:StlBoundedFutureParser.IoTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#interval.
    def visitInterval(self, ctx:StlBoundedFutureParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx:StlBoundedFutureParser.IntervalTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#unit.
    def visitUnit(self, ctx:StlBoundedFutureParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprUntimedAlwaysExpr.
    def visitExprUntimedAlwaysExpr(self, ctx:StlBoundedFutureParser.ExprUntimedAlwaysExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprUntimedEvExpr.
    def visitExprUntimedEvExpr(self, ctx:StlBoundedFutureParser.ExprUntimedEvExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#Expr.
    def visitExpr(self, ctx:StlBoundedFutureParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprParen.
    def visitExprParen(self, ctx:StlBoundedFutureParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprAndExpr.
    def visitExprAndExpr(self, ctx:StlBoundedFutureParser.ExprAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExpreOnceExpr.
    def visitExpreOnceExpr(self, ctx:StlBoundedFutureParser.ExpreOnceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprAlwaysExpr.
    def visitExprAlwaysExpr(self, ctx:StlBoundedFutureParser.ExprAlwaysExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprImpliesExpr.
    def visitExprImpliesExpr(self, ctx:StlBoundedFutureParser.ExprImpliesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprXorExpr.
    def visitExprXorExpr(self, ctx:StlBoundedFutureParser.ExprXorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprSinceExpr.
    def visitExprSinceExpr(self, ctx:StlBoundedFutureParser.ExprSinceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprNot.
    def visitExprNot(self, ctx:StlBoundedFutureParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprOrExpr.
    def visitExprOrExpr(self, ctx:StlBoundedFutureParser.ExprOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprIffExpr.
    def visitExprIffExpr(self, ctx:StlBoundedFutureParser.ExprIffExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprFall.
    def visitExprFall(self, ctx:StlBoundedFutureParser.ExprFallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprRise.
    def visitExprRise(self, ctx:StlBoundedFutureParser.ExprRiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprHistExpr.
    def visitExprHistExpr(self, ctx:StlBoundedFutureParser.ExprHistExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprReal.
    def visitExprReal(self, ctx:StlBoundedFutureParser.ExprRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprUntilExpr.
    def visitExprUntilExpr(self, ctx:StlBoundedFutureParser.ExprUntilExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprEvExpr.
    def visitExprEvExpr(self, ctx:StlBoundedFutureParser.ExprEvExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#IdCompInt.
    def visitIdCompInt(self, ctx:StlBoundedFutureParser.IdCompIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx:StlBoundedFutureParser.ExprSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprDivision.
    def visitExprDivision(self, ctx:StlBoundedFutureParser.ExprDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx:StlBoundedFutureParser.ExprMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprLiteral.
    def visitExprLiteral(self, ctx:StlBoundedFutureParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprId.
    def visitExprId(self, ctx:StlBoundedFutureParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprAbs.
    def visitExprAbs(self, ctx:StlBoundedFutureParser.ExprAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprAddition.
    def visitExprAddition(self, ctx:StlBoundedFutureParser.ExprAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpLs.
    def visitCmpOpLs(self, ctx:StlBoundedFutureParser.CmpOpLsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpGte.
    def visitCmpOpGte(self, ctx:StlBoundedFutureParser.CmpOpGteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpLse.
    def visitCmpOpLse(self, ctx:StlBoundedFutureParser.CmpOpLseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpGt.
    def visitCmpOpGt(self, ctx:StlBoundedFutureParser.CmpOpGtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpEq.
    def visitCmpOpEq(self, ctx:StlBoundedFutureParser.CmpOpEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ComOpNeq.
    def visitComOpNeq(self, ctx:StlBoundedFutureParser.ComOpNeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#literal.
    def visitLiteral(self, ctx:StlBoundedFutureParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#Id.
    def visitId(self, ctx:StlBoundedFutureParser.IdContext):
        return self.visitChildren(ctx)



del StlBoundedFutureParser