from rtamt.exception.ltl.exception import LTLPastifyException
from rtamt.ast.visitor.stl.ASTVisitor import STLASTVisitor
from tests.python.ast.LTLPrintNameVisitor import LTLPrintNameVisitor


class STLPrintNameVisitor(STLASTVisitor, LTLPrintNameVisitor):
    def visitConstant(self, element, args):
        return str(element.val)

    def visitPredicate(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' +  op1 + ')' + str(element.operator) + '(' + op2 + ')'

    def visitVariable(self, element, args):
        return element.var

    def visitAddition(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + '+' + '(' + op2 + ')'

    def visitMultiplication(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + '*' + '(' + op2 + ')'

    def visitSubtraction(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + '-' + '(' + op2 + ')'

    def visitDivision(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + '/' + '(' + op2 + ')'

    def visitAbs(self, element, args):
        op = self.visit(element.children[0], args)
        return 'abs(' + op + ')'

    def visitSqrt(self, element, args):
        op = self.visit(element.children[0], args)
        return 'sqrt(' + op + ')'

    def visitExp(self, element, args):
        op = self.visit(element.children[0], args)
        return 'exp(' + op + ')'

    def visitPow(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return 'pow(' + op1 + ',' + op2 + ')'

    def visitRise(self, element, args):
        op = self.visit(element.children[0], args)
        return 'rise(' + op + ')'

    def visitFall(self, element, args):
        op = self.visit(element.children[0], args)
        return 'fall(' + op + ')'

    def visitNot(self, element, args):
        op = self.visit(element.children[0], args)
        return 'not(' + op + ')'

    def visitAnd(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'and' + '(' + op2 + ')'

    def visitOr(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'or' + '(' + op2 + ')'

    def visitImplies(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'implies' + '(' + op2 + ')'

    def visitIff(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'iff' + '(' + op2 + ')'

    def visitXor(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'xor' + '(' + op2 + ')'

    def visitEventually(self, element, args):
        op = self.visit(element.children[0], args)
        return 'eventually(' + op + ')'

    def visitAlways(self, element, args):
        op = self.visit(element.children[0], args)
        return 'always(' + op + ')'

    def visitUntil(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'until' + '(' + op2 + ')'

    def visitOnce(self, element, args):
        op = self.visit(element.children[0], args)
        return 'once(' + op + ')'

    def visitPrevious(self, element, args):
        op = self.visit(element.children[0], args)
        return 'prev(' + op + ')'

    def visitNext(self, element, args):
        op = self.visit(element.children[0], args)
        return 'next(' + op + ')'

    def visitHistorically(self, element, args):
        op = self.visit(element.children[0], args)
        return 'historically(' + op + ')'

    def visitSince(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'since' + '(' + op2 + ')'

    def visitDefault(self, element):
        raise LTLPastifyException('LTL Print Name: encountered unexpected type of object.')

    def visitTimedOnce(self, element, args):
        op = self.visit(element.children[0], args)
        return 'once[' + str(element.begin) + ',' + str(element.end) +'](' + op + ')'

    def visitTimedHistorically(self, element, args):
        op = self.visit(element.children[0], args)
        return 'historically[' + str(element.begin) + ',' + str(element.end) +'](' + op + ')'

    def visitTimedEventually(self, element, args):
        op = self.visit(element.children[0], args)
        return 'eventually[' + str(element.begin) + ',' + str(element.end) +'](' + op + ')'

    def visitTimedAlways(self, element, args):
        op = self.visit(element.children[0], args)
        return 'always[' + str(element.begin) + ',' + str(element.end) +'](' + op + ')'

    def visitTimedSince(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'since[' + str(element.begin) + ',' + str(element.end) +'](' + op2 + ')'

    def visitTimedUntil(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'until[' + str(element.begin) + ',' + str(element.end) +'](' + op2 + ')'

    def visitTimedPrecedes(self, element, args):
        op1 = self.visit(element.children[0], args)
        op2 = self.visit(element.children[1], args)
        return '(' + op1 + ')' + 'precedes[' + str(element.begin) + ',' + str(element.end) +'](' + op2 + ')'