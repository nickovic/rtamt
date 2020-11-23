# Generated from StlParser.g4 by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by StlParser.

class StlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StlParser#stlfile.
    def visitStlfile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#stlSpecification.
    def visitStlSpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Specification.
    def visitSpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#modImport.
    def visitModImport(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#assertion.
    def visitAssertion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#declVariable.
    def visitDeclVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#annotation.
    def visitAnnotation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#rosTopic.
    def visitRosTopic(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#AsgnExpr.
    def visitAsgnExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#domainType.
    def visitDomainType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ioType.
    def visitIoType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#interval.
    def visitInterval(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#unit.
    def visitUnit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUntimedAlwaysExpr.
    def visitExprUntimedAlwaysExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUntimedEvExpr.
    def visitExprUntimedEvExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprParen.
    def visitExprParen(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAndExpr.
    def visitExprAndExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExpreOnceExpr.
    def visitExpreOnceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAlwaysExpr.
    def visitExprAlwaysExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprImpliesExpr.
    def visitExprImpliesExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprXorExpr.
    def visitExprXorExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprSinceExpr.
    def visitExprSinceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprNot.
    def visitExprNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprOrExpr.
    def visitExprOrExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprNext.
    def visitExprNext(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUnless.
    def visitExprUnless(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprPrevious.
    def visitExprPrevious(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprIffExpr.
    def visitExprIffExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprFall.
    def visitExprFall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprRise.
    def visitExprRise(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprHistExpr.
    def visitExprHistExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprReal.
    def visitExprReal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprUntilExpr.
    def visitExprUntilExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprEvExpr.
    def visitExprEvExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#IdCompInt.
    def visitIdCompInt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprDivision.
    def visitExprDivision(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprLiteral.
    def visitExprLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprId.
    def visitExprId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAbs.
    def visitExprAbs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ExprAddition.
    def visitExprAddition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpLs.
    def visitCmpOpLs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpGte.
    def visitCmpOpGte(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpLse.
    def visitCmpOpLse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpGt.
    def visitCmpOpGt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#CmpOpEq.
    def visitCmpOpEq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#ComOpNeq.
    def visitComOpNeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlParser#Id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


