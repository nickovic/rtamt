from rtamt.spec.stl.visitor import STLVisitor

from rtamt.interval.interval import Interval
from rtamt.node.stl.predicate import Predicate
from rtamt.node.stl.variable import Variable
from rtamt.node.stl.neg import Neg
from rtamt.node.stl.conjunction import Conjunction
from rtamt.node.stl.disjunction import Disjunction
from rtamt.node.stl.implies import Implies
from rtamt.node.stl.iff import Iff
from rtamt.node.stl.xor import Xor
from rtamt.node.stl.eventually import Eventually
from rtamt.node.stl.always import Always
from rtamt.node.stl.once import Once
from rtamt.node.stl.historically import Historically
from rtamt.node.stl.precedes import Precedes
from rtamt.node.stl.since import Since
from rtamt.node.stl.addition import Addition
from rtamt.node.stl.subtraction import Subtraction
from rtamt.node.stl.multiplication import Multiplication
from rtamt.node.stl.division import Division
from rtamt.node.stl.abs import Abs
from rtamt.node.stl.fall import Fall
from rtamt.node.stl.rise import Rise
from rtamt.node.stl.constant import Constant

class STLReset(STLVisitor):

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

    def visitPrecedes(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.reset()

    def visitDefault(self, element):
        pass