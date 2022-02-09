from rtamt.exception.ltl.exception import LTLPastifyException
from rtamt.ast.visitor.stl.ast_visitor import StlAstVisitor
from tests.python.ast.ltl_print_name_ast_visitor import LtlPrintNameAstVisitor


class StlPrintNameAstVisitor(StlAstVisitor, LtlPrintNameAstVisitor):
    def visitConstant(self, node, *args, **kwargs):
        return str(node.val)

    def visitPredicate(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' +  op1 + ')' + str(node.operator) + '(' + op2 + ')'

    def visitVariable(self, node, *args, **kwargs):
        return node.var

    def visitAddition(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + '+' + '(' + op2 + ')'

    def visitMultiplication(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + '*' + '(' + op2 + ')'

    def visitSubtraction(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + '-' + '(' + op2 + ')'

    def visitDivision(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + '/' + '(' + op2 + ')'

    def visitAbs(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'abs(' + op + ')'

    def visitSqrt(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'sqrt(' + op + ')'

    def visitExp(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'exp(' + op + ')'

    def visitPow(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return 'pow(' + op1 + ',' + op2 + ')'

    def visitRise(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'rise(' + op + ')'

    def visitFall(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'fall(' + op + ')'

    def visitNot(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'not(' + op + ')'

    def visitAnd(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'and' + '(' + op2 + ')'

    def visitOr(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'or' + '(' + op2 + ')'

    def visitImplies(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'implies' + '(' + op2 + ')'

    def visitIff(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'iff' + '(' + op2 + ')'

    def visitXor(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'xor' + '(' + op2 + ')'

    def visitEventually(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'eventually(' + op + ')'

    def visitAlways(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'always(' + op + ')'

    def visitUntil(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'until' + '(' + op2 + ')'

    def visitOnce(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'once(' + op + ')'

    def visitPrevious(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'prev(' + op + ')'

    def visitNext(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'next(' + op + ')'

    def visitHistorically(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'historically(' + op + ')'

    def visitSince(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'since' + '(' + op2 + ')'

    def visitDefault(self, node):
        raise LTLPastifyException('LTL Print Name: encountered unexpected type of object.')

    def visitTimedOnce(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'once[' + str(node.begin) + ',' + str(node.end) +'](' + op + ')'

    def visitTimedHistorically(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'historically[' + str(node.begin) + ',' + str(node.end) +'](' + op + ')'

    def visitTimedEventually(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'eventually[' + str(node.begin) + ',' + str(node.end) +'](' + op + ')'

    def visitTimedAlways(self, node, *args, **kwargs):
        op = self.visit(node.children[0], *args, **kwargs)
        return 'always[' + str(node.begin) + ',' + str(node.end) +'](' + op + ')'

    def visitTimedSince(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'since[' + str(node.begin) + ',' + str(node.end) +'](' + op2 + ')'

    def visitTimedUntil(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'until[' + str(node.begin) + ',' + str(node.end) +'](' + op2 + ')'

    def visitTimedPrecedes(self, node, *args, **kwargs):
        op1 = self.visit(node.children[0], *args, **kwargs)
        op2 = self.visit(node.children[1], *args, **kwargs)
        return '(' + op1 + ')' + 'precedes[' + str(node.begin) + ',' + str(node.end) +'](' + op2 + ')'