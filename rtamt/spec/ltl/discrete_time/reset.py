from rtamt.spec.ltl.discrete_time.visitor import LTLVisitor

class LTLReset(LTLVisitor):

    def reset(self, element):
        return self.visit(element, [])

    def visitConstant(self, element, args):
        element.reset()

    def visitPredicate(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitVariable(self, element, args):
        element.reset()

    def visitAddition(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitMultiplication(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitSubtraction(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitDivision(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitAbs(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitRise(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitFall(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitNot(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitAnd(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitOr(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitImplies(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitIff(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitXor(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitEventually(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitAlways(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitUntil(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitOnce(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitPrevious(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitNext(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitHistorically(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitSince(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitDefault(self, element):
        pass