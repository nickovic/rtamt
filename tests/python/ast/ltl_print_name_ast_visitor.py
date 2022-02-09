from rtamt.exception.ltl.exception import LTLPastifyException

from rtamt.ast.visitor.ltl.ast_visitor import LtlAstVisitor

class LtlPrintNameAstVisitor(LtlAstVisitor):
    def visitConstant(self, element, *args, **kwargs):
        return str(element.val)

    def visitPredicate(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' +  op1 + ')' + str(element.operator) + '(' + op2 + ')'

    def visitVariable(self, element, *args, **kwargs):
        return element.var

    def visitAddition(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + '+' + '(' + op2 + ')'

    def visitMultiplication(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + '*' + '(' + op2 + ')'

    def visitSubtraction(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + '-' + '(' + op2 + ')'

    def visitDivision(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + '/' + '(' + op2 + ')'

    def visitAbs(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'abs(' + op + ')'

    def visitSqrt(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'sqrt(' + op + ')'

    def visitExp(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'exp(' + op + ')'

    def visitPow(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return 'pow(' + op1 + ',' + op2 + ')'

    def visitRise(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'rise(' + op + ')'

    def visitFall(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'fall(' + op + ')'

    def visitNot(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'not(' + op + ')'

    def visitAnd(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'and' + '(' + op2 + ')'

    def visitOr(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'or' + '(' + op2 + ')'

    def visitImplies(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'implies' + '(' + op2 + ')'

    def visitIff(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'iff' + '(' + op2 + ')'

    def visitXor(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'xor' + '(' + op2 + ')'

    def visitEventually(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'eventually(' + op + ')'

    def visitAlways(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'always(' + op + ')'

    def visitUntil(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'until' + '(' + op2 + ')'

    def visitOnce(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'once(' + op + ')'

    def visitPrevious(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'prev(' + op + ')'

    def visitNext(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'next(' + op + ')'

    def visitHistorically(self, element, *args, **kwargs):
        op = self.visit(element.children[0], *args, **kwargs)
        return 'historically(' + op + ')'

    def visitSince(self, element, *args, **kwargs):
        op1 = self.visit(element.children[0], *args, **kwargs)
        op2 = self.visit(element.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'since' + '(' + op2 + ')'

    def visitDefault(self, element):
        raise LTLPastifyException('LTL Print Name: encountered unexpected type of object.')
