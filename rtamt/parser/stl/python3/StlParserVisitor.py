# Generated from StlParser.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StlParser import StlParser
else:
    from StlParser import StlParser

# This class defines a complete generic visitor for a parse tree produced by StlParser.

class StlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StlParser#stlfile.
    def visitStlfile(self, ctx:StlParser.StlfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#stlSpecification.
    def visitStlSpecification(self, ctx:StlParser.StlSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Specification.
    def visitSpecification(self, ctx:StlParser.SpecificationContext):
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


    # Visit a parse tree produced by StlParser#annotation.
    def visitAnnotation(self, ctx:StlParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#rosTopic.
    def visitRosTopic(self, ctx:StlParser.RosTopicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:StlParser.VariableDeclarationContext):
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


    # Visit a parse tree produced by StlParser#interval.
    def visitInterval(self, ctx:StlParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx:StlParser.IntervalTimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#unit.
    def visitUnit(self, ctx:StlParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUntimedAlwaysExpr.
    def visitExprUntimedAlwaysExpr(self, ctx:StlParser.ExprUntimedAlwaysExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUntimedEvExpr.
    def visitExprUntimedEvExpr(self, ctx:StlParser.ExprUntimedEvExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Expr.
    def visitExpr(self, ctx:StlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprParen.
    def visitExprParen(self, ctx:StlParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAndExpr.
    def visitExprAndExpr(self, ctx:StlParser.ExprAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExpreOnceExpr.
    def visitExpreOnceExpr(self, ctx:StlParser.ExpreOnceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAlwaysExpr.
    def visitExprAlwaysExpr(self, ctx:StlParser.ExprAlwaysExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprImpliesExpr.
    def visitExprImpliesExpr(self, ctx:StlParser.ExprImpliesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprXorExpr.
    def visitExprXorExpr(self, ctx:StlParser.ExprXorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprSinceExpr.
    def visitExprSinceExpr(self, ctx:StlParser.ExprSinceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprNot.
    def visitExprNot(self, ctx:StlParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprOrExpr.
    def visitExprOrExpr(self, ctx:StlParser.ExprOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprIffExpr.
    def visitExprIffExpr(self, ctx:StlParser.ExprIffExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprFall.
    def visitExprFall(self, ctx:StlParser.ExprFallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprRise.
    def visitExprRise(self, ctx:StlParser.ExprRiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprHistExpr.
    def visitExprHistExpr(self, ctx:StlParser.ExprHistExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprReal.
    def visitExprReal(self, ctx:StlParser.ExprRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUntilExpr.
    def visitExprUntilExpr(self, ctx:StlParser.ExprUntilExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprEvExpr.
    def visitExprEvExpr(self, ctx:StlParser.ExprEvExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#IdCompInt.
    def visitIdCompInt(self, ctx:StlParser.IdCompIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx:StlParser.ExprSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprDivision.
    def visitExprDivision(self, ctx:StlParser.ExprDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx:StlParser.ExprMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprId.
    def visitExprId(self, ctx:StlParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAbs.
    def visitExprAbs(self, ctx:StlParser.ExprAbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAddition.
    def visitExprAddition(self, ctx:StlParser.ExprAdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpLs.
    def visitCmpOpLs(self, ctx:StlParser.CmpOpLsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpGte.
    def visitCmpOpGte(self, ctx:StlParser.CmpOpGteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpLse.
    def visitCmpOpLse(self, ctx:StlParser.CmpOpLseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpGt.
    def visitCmpOpGt(self, ctx:StlParser.CmpOpGtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpEq.
    def visitCmpOpEq(self, ctx:StlParser.CmpOpEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ComOpNeq.
    def visitComOpNeq(self, ctx:StlParser.ComOpNeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#literal.
    def visitLiteral(self, ctx:StlParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Id.
    def visitId(self, ctx:StlParser.IdContext):
        return self.visitChildren(ctx)



del StlParser