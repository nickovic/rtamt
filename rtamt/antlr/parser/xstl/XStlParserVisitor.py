# Generated from XStlParser.g4 by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by XStlParser.

class XStlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XStlParser#ExprSince.
    def visitExprSince(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprParen.
    def visitExprParen(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprIff.
    def visitExprIff(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExpreOnce.
    def visitExpreOnce(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprEv.
    def visitExprEv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprImplies.
    def visitExprImplies(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprUntil.
    def visitExprUntil(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprNot.
    def visitExprNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprShift.
    def visitExprShift(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprNext.
    def visitExprNext(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprAnd.
    def visitExprAnd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprUnless.
    def visitExprUnless(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprPrevious.
    def visitExprPrevious(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprHist.
    def visitExprHist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprFall.
    def visitExprFall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprPredicate.
    def visitExprPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprXor.
    def visitExprXor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprRise.
    def visitExprRise(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprOr.
    def visitExprOr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprAlways.
    def visitExprAlways(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprReal.
    def visitExprReal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#interval.
    def visitInterval(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#constantTimeLiteral.
    def visitConstantTimeLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#unit.
    def visitUnit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#specification_file.
    def visitSpecification_file(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#specification.
    def visitSpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#SpecificationId.
    def visitSpecificationId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#modImport.
    def visitModImport(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#assertion.
    def visitAssertion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#declVariable.
    def visitDeclVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#declConstant.
    def visitDeclConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#annotation.
    def visitAnnotation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#rosTopic.
    def visitRosTopic(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#AsgnExpr.
    def visitAsgnExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#domainType.
    def visitDomainType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ioType.
    def visitIoType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprPow.
    def visitExprPow(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprDivision.
    def visitExprDivision(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprLiteral.
    def visitExprLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprExp.
    def visitExprExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprSqrt.
    def visitExprSqrt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprId.
    def visitExprId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprAbs.
    def visitExprAbs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#ExprAddition.
    def visitExprAddition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Leq.
    def visitLeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Geq.
    def visitGeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Less.
    def visitLess(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Greater.
    def visitGreater(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Eq.
    def visitEq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Neq.
    def visitNeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XStlParser#Id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


