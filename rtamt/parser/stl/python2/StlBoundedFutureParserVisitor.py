# Generated from StlBoundedFutureParser.g4 by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by StlBoundedFutureParser.

class StlBoundedFutureParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StlBoundedFutureParser#stlfile.
    def visitStlfile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#stlSpecification.
    def visitStlSpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#Specification.
    def visitSpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#modImport.
    def visitModImport(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#assertion.
    def visitAssertion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#declVariable.
    def visitDeclVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#annotation.
    def visitAnnotation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#rosTopic.
    def visitRosTopic(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#AsgnExpr.
    def visitAsgnExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#domainType.
    def visitDomainType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ioType.
    def visitIoType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#interval.
    def visitInterval(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#unit.
    def visitUnit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprUntimedAlwaysExpr.
    def visitExprUntimedAlwaysExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprUntimedEvExpr.
    def visitExprUntimedEvExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#Expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprParen.
    def visitExprParen(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprAndExpr.
    def visitExprAndExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExpreOnceExpr.
    def visitExpreOnceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprAlwaysExpr.
    def visitExprAlwaysExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprImpliesExpr.
    def visitExprImpliesExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprXorExpr.
    def visitExprXorExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprSinceExpr.
    def visitExprSinceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprNot.
    def visitExprNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprOrExpr.
    def visitExprOrExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprIffExpr.
    def visitExprIffExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprFall.
    def visitExprFall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprRise.
    def visitExprRise(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprHistExpr.
    def visitExprHistExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprReal.
    def visitExprReal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprUntilExpr.
    def visitExprUntilExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprEvExpr.
    def visitExprEvExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#IdCompInt.
    def visitIdCompInt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprDivision.
    def visitExprDivision(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprLiteral.
    def visitExprLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprId.
    def visitExprId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprAbs.
    def visitExprAbs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ExprAddition.
    def visitExprAddition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpLs.
    def visitCmpOpLs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpGte.
    def visitCmpOpGte(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpLse.
    def visitCmpOpLse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpGt.
    def visitCmpOpGt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#CmpOpEq.
    def visitCmpOpEq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#ComOpNeq.
    def visitComOpNeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlBoundedFutureParser#Id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


