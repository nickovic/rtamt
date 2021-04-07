# Generated from StlExtendedParser.g4 by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by StlExtendedParser.

class StlExtendedParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StlExtendedParser#ExprSince.
    def visitExprSince(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprParen.
    def visitExprParen(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprIff.
    def visitExprIff(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExpreOnce.
    def visitExpreOnce(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprEv.
    def visitExprEv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprImplies.
    def visitExprImplies(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprUntil.
    def visitExprUntil(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprNot.
    def visitExprNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprNext.
    def visitExprNext(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprAnd.
    def visitExprAnd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprUnless.
    def visitExprUnless(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprPrevious.
    def visitExprPrevious(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprHist.
    def visitExprHist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprFall.
    def visitExprFall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprPredicate.
    def visitExprPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprXor.
    def visitExprXor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprRise.
    def visitExprRise(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprOr.
    def visitExprOr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprBackto.
    def visitExprBackto(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprAlways.
    def visitExprAlways(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprReal.
    def visitExprReal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#interval.
    def visitInterval(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#intervalTimeLiteral.
    def visitIntervalTimeLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#constantTimeLiteral.
    def visitConstantTimeLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#unit.
    def visitUnit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#specification_file.
    def visitSpecification_file(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#specification.
    def visitSpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#SpecificationId.
    def visitSpecificationId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#modImport.
    def visitModImport(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#assertion.
    def visitAssertion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#declVariable.
    def visitDeclVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#declConstant.
    def visitDeclConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#annotation.
    def visitAnnotation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#rosTopic.
    def visitRosTopic(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#constantDeclaration.
    def visitConstantDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#AsgnLiteral.
    def visitAsgnLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#AsgnExpr.
    def visitAsgnExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#domainType.
    def visitDomainType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ioType.
    def visitIoType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprSubtraction.
    def visitExprSubtraction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprDivision.
    def visitExprDivision(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprMultiplication.
    def visitExprMultiplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprLiteral.
    def visitExprLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprId.
    def visitExprId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprAbs.
    def visitExprAbs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#ExprAddition.
    def visitExprAddition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Leq.
    def visitLeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Geq.
    def visitGeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Less.
    def visitLess(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Greater.
    def visitGreater(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Eq.
    def visitEq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Neq.
    def visitNeq(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StlExtendedParser#Id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


