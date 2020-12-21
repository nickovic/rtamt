from rtamt.spec.ltl.discrete_time.reset import LTLReset
from rtamt.spec.stl.discrete_time.visitor import STLVisitor

class STLReset(LTLReset, STLVisitor):

    def visitTimedPrecedes(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitTimedUntil(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitTimedAlways(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitTimedEventually(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitTimedSince(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitTimedHistorically(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitTimedOnce(self, element, args):
        self.visit(element.children[0], args)
        element.reset()

    def visitDefault(self, element):
        pass