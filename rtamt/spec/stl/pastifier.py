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

class STLPastifier(STLVisitor):

    def pastify(self, element):
        return self.visit(element, [element.horizon])

    def visitPredicate(self, element, args):
        horizon = args[0]
        if horizon == 0:
            node = Predicate(element.var, element.field, element.io_type, element.operator, element.threshold)
        else:
            child = Predicate(element.var, element.field, element.io_type, element.operator, element.threshold)
            bound = Interval(horizon, horizon)
            node = Once(child, bound)
        return node

    def visitVariable(self, element, args):
        horizon = args[0]
        if horizon == 0:
            node = Variable(element.var, element.field)
        else:
            child = Variable(element.var, element.field)
            bound = Interval(horizon, horizon)
            node = Once(child, bound)
        return node

    def visitNot(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Neg(child_node)
        return node

    def visitAnd(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Conjunction(child1_node, child2_node)
        return node

    def visitOr(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Disjunction(child1_node, child2_node)
        return node

    def visitImplies(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Implies(child1_node, child2_node)
        return node

    def visitIff(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Iff(child1_node, child2_node)
        return node

    def visitXor(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Xor(child1_node, child2_node)
        return node

    def visitEventually(self, element, args):
        horizon = args[0]
        if element.bound == None:
            child_node = self.visit(element.children[0], [horizon])
            node = Eventually(child_node, element.bound)
        else:
            child_node = self.visit(element.children[0], [horizon - element.bound.end])
            bound = Interval(horizon - element.bound.end, horizon - element.bound.begin)
            node = Once(child_node, bound)
        return node

    def visitAlways(self, element, args):
        horizon = args[0]
        if element.bound == None:
            child_node = self.visit(element.children[0], [horizon])
            node = Always(child_node, element.bound)
        else:
            child_node = self.visit(element.children[0], [horizon - element.bound.end])
            bound = Interval(horizon - element.bound.end, horizon - element.bound.begin)
            node = Historically(child_node, bound)
        return node

    def visitUntil(self, element, args):
        horizon = args[0]
        end = 0
        begin = 0
        if element.bound != None:
            end = element.bound.end
            begin = element.bound.begin
        child1_node = self.visit(element.children[0], [horizon - end])
        child2_node = self.visit(element.children[1], [horizon - end])
        bound = Interval(horizon - begin, horizon - begin)
        node = Precedes(child1_node, child2_node, bound)
        return node

    def visitOnce(self, element, args):
        horizon = args[0]
        end = 0
        begin = 0
        if element.bound != None:
            end = element.bound.end
            begin = element.bound.begin
        child_node = self.visit(element.children[0], [horizon - end])
        bound = Interval(begin + horizon, begin + horizon)
        node = Once(child_node, bound)
        return node

    def visitHistorically(self, element, args):
        horizon = args[0]
        end = 0
        begin = 0
        if element.bound != None:
            end = element.bound.end
            begin = element.bound.begin
        child_node = self.visit(element.children[0], [horizon - end])
        bound = Interval(begin + horizon, begin + horizon)
        node = Historically(child_node, bound)
        return node

    def visitSince(self, element, args):
        horizon = args[0]
        end = 0
        begin = 0
        if element.bound != None:
            end = element.bound.end
            begin = element.bound.begin
        child1_node = self.visit(element.children[0], [horizon - end])
        child2_node = self.visit(element.children[1], [horizon - end])
        bound = Interval(begin + horizon, begin + horizon)
        node = Since(child1_node, child2_node, bound)
        return node

    def visitPrecedes(self, element, args):
        horizon = args[0]
        end = 0
        begin = 0
        if element.bound != None:
            end = element.bound.end
            begin = element.bound.begin
        child1_node = self.visit(element.children[0], [horizon - end])
        child2_node = self.visit(element.children[1], [horizon - end])
        bound = Interval(begin + horizon, begin + horizon)
        node = Precedes(child1_node, child2_node, bound)
        return node



    def visitDefault(self, element):
        return None