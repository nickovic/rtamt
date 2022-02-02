from rtamt.ast.visitor.ltl.ast_visitor import LtlAstVisitor


class PrintNameLtlAstVisitor(LtlAstVisitor):

    def visitPredicate(self, node, *args, **kwargs):
        print(node.name)

    def visitVariable(self, node, *args, **kwargs):
        print(node.name)

    def visitAbs(self, node, *args, **kwargs):
        print(node.name)

    def visitAddition(self, node, *args, **kwargs):
        print(node.name)

    def visitSubtraction(self, node, *args, **kwargs):
        print(node.name)

    def visitMultiplication(self, node, *args, **kwargs):
        print(node.name)

    def visitDivision(self, node, *args, **kwargs):
        print(node.name)

    def visitNot(self, node, *args, **kwargs):
        print(node.name)

    def visitAnd(self, node, *args, **kwargs):
        print(node.name)

    def visitOr(self, node, *args, **kwargs):
        print(node.name)

    def visitImplies(self, node, *args, **kwargs):
        print(node.name)

    def visitIff(self, node, *args, **kwargs):
        print(node.name)

    def visitXor(self, node, *args, **kwargs):
        print(node.name)

    def visitEventually(self, node, *args, **kwargs):
        print(node.name)

    def visitAlways(self, node, *args, **kwargs):
        print(node.name)

    def visitUntil(self, node, *args, **kwargs):
        print(node.name)

    def visitOnce(self, node, *args, **kwargs):
        print(node.name)

    def visitHistorically(self, node, *args, **kwargs):
        print(node.name)

    def visitSince(self, node, *args, **kwargs):
        print(node.name)

    def visitRise(self, node, *args, **kwargs):
        print(node.name)

    def visitFall(self, node, *args, **kwargs):
        print(node.name)

    def visitConstant(self, node, *args, **kwargs):
        print(node.name)

    def visitPrevious(self, node, *args, **kwargs):
        print(node.name)

    def visitNext(self, node, *args, **kwargs):
        print(node.name)

    def visitTimedPrecedes(self, node, *args, **kwargs):
        print(node.name)

    def visitTimedOnce(self, node, *args, **kwargs):
        print(node.name)

    def visitTimedHistorically(self, node, *args, **kwargs):
        print(node.name)

    def visitTimedSince(self, node, *args, **kwargs):
        print(node.name)

    def visitTimedAlways(self, node, *args, **kwargs):
        print(node.name)

    def visitTimedEventually(self, node, *args, **kwargs):
        print(node.name)

    def visitTimedUntil(self, node, *args, **kwargs):
        print(node.name)

    def visitDefault(self, node, *args, **kwargs):
        pass