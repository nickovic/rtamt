from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException

class PrintNameVisitor(STLVisitor):

    def visitPredicate(self, node, args):
        print(node.name)

    def visitVariable(self, node, args):
        print(node.name)

    def visitAbs(self, node, args):
        print(node.name)

    def visitAddition(self, node, args):
        print(node.name)

    def visitSubtraction(self, node, args):
        print(node.name)

    def visitMultiplication(self, node, args):
        print(node.name)

    def visitDivision(self, node, args):
        print(node.name)

    def visitNot(self, node, args):
        print(node.name)

    def visitAnd(self, node, args):
        print(node.name)

    def visitOr(self, node, args):
        print(node.name)

    def visitImplies(self, node, args):
        print(node.name)

    def visitIff(self, node, args):
        print(node.name)

    def visitXor(self, node, args):
        print(node.name)

    def visitEventually(self, node, args):
        print(node.name)

    def visitAlways(self, node, args):
        print(node.name)

    def visitUntil(self, node, args):
        print(node.name)

    def visitOnce(self, node, args):
        print(node.name)

    def visitHistorically(self, node, args):
        print(node.name)

    def visitSince(self, node, args):
        print(node.name)

    def visitRise(self, node, args):
        print(node.name)

    def visitFall(self, node, args):
        print(node.name)

    def visitConstant(self, node, args):
        print(node.name)

    def visitPrevious(self, node, args):
        print(node.name)

    def visitNext(self, node, args):
        print(node.name)

    def visitTimedPrecedes(self, node, args):
        print(node.name)

    def visitTimedOnce(self, node, args):
        print(node.name)

    def visitTimedHistorically(self, node, args):
        print(node.name)

    def visitTimedSince(self, node, args):
        print(node.name)

    def visitTimedAlways(self, node, args):
        print(node.name)

    def visitTimedEventually(self, node, args):
        print(node.name)

    def visitTimedUntil(self, node, args):
        print(node.name)

    def visitDefault(self, node, args):
        pass
