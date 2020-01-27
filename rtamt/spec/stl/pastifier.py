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

class STLPastifier(STLVisitor):

    def __init__(self, spec):
        self.spec = spec

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, spec):
        self.__spec = spec

    def pastify(self, element):
        return self.visit(element, [element.horizon])

    def visitPredicate(self, element, args):
        horizon = args[0]
        if horizon == 0:
            node = Predicate(element.child, element.io_type, element.operator, element.threshold, self.spec.is_pure_python)
        else:
            child = Predicate(element.child, element.io_type, element.operator, element.threshold, self.spec.is_pure_python)
            bound = Interval(horizon, horizon)
            node = Once(child, bound, self.spec.is_pure_python)
        return node

    def visitVariable(self, element, args):
        horizon = args[0]
        var_type = self.spec.var_type_dict[element.var]
        if horizon == 0:
            node = Variable(element.var, element.field, var_type)
        else:
            child = Variable(element.var, element.field, var_type)
            bound = Interval(horizon, horizon)
            node = Once(child, bound, self.spec.is_pure_python)
        return node

    def visitAddition(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Addition(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitMultiplication(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Multiplication(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitSubtraction(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Subtraction(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitDivision(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Division(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitAbs(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Abs(child_node, self.spec.is_pure_python)
        return node

    def visitRise(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Rise(child_node, self.spec.is_pure_python)
        return node

    def visitFall(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Fall(child_node, self.spec.is_pure_python)
        return node

    def visitNot(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = Neg(child_node, self.spec.is_pure_python)
        return node

    def visitAnd(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Conjunction(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitOr(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Disjunction(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitImplies(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Implies(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitIff(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Iff(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitXor(self, element, args):
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = Xor(child1_node, child2_node, self.spec.is_pure_python)
        return node

    def visitEventually(self, element, args):
        horizon = args[0]
        if element.bound == None:
            child_node = self.visit(element.children[0], [horizon])
            node = Eventually(child_node, element.bound)
        else:
            child_node = self.visit(element.children[0], [horizon - element.bound.end])
            bound = Interval(horizon - element.bound.end, horizon - element.bound.begin)
            node = Once(child_node, bound, self.spec.is_pure_python)
        return node

    def visitAlways(self, element, args):
        horizon = args[0]
        if element.bound == None:
            child_node = self.visit(element.children[0], [horizon])
            node = Always(child_node, element.bound, self.spec.is_pure_python)
        else:
            child_node = self.visit(element.children[0], [horizon - element.bound.end])
            bound = Interval(horizon - element.bound.end, horizon - element.bound.begin)
            node = Historically(child_node, bound, self.spec.is_pure_python)
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
        node = Precedes(child1_node, child2_node, bound, self.spec.is_pure_python)
        return node

    def visitOnce(self, element, args):
        horizon = args[0]
        child_node = self.visit(element.children[0], [horizon])

        if element.bound == None:
            if horizon == 0:
                node = Once(child_node, None, self.spec.is_pure_python)
            else:
                bound = Interval(horizon, float("inf"))
                node = Once(child_node, bound, self.spec.is_pure_python)
        else:
            begin = element.bound.begin
            end = element.bound.end
            bound = Interval(begin + horizon, end + horizon)
            node = Once(child_node, bound, self.spec.is_pure_python)

        return node

    def visitHistorically(self, element, args):
        horizon = args[0]
        child_node = self.visit(element.children[0], [horizon])

        if element.bound == None:
            if horizon == 0:
                node = Historically(child_node, None, self.spec.is_pure_python)
            else:
                bound = Interval(horizon, float("inf"))
                node = Historically(child_node, bound, self.spec.is_pure_python)
        else:
            begin = element.bound.begin
            end = element.bound.end
            bound = Interval(begin + horizon, end + horizon)
            node = Historically(child_node, bound, self.spec.is_pure_python)

        return node

    def visitSince(self, element, args):
        horizon = args[0]
        child_node_1 = self.visit(element.children[0], [horizon])
        child_node_2 = self.visit(element.children[1], [horizon])

        if element.bound == None:
            if horizon == 0:
                node = Since(child_node_1, child_node_2, None, self.spec.is_pure_python)
            else:
                bound = Interval(horizon, float("inf"))
                node = Since(child_node_1, child_node_2, bound, self.spec.is_pure_python)
        else:
            begin = element.bound.begin
            end = element.bound.end
            bound = Interval(begin + horizon, end + horizon)
            node = Since(child_node_1, child_node_2, bound, self.spec.is_pure_python)

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
        node = Precedes(child1_node, child2_node, bound, self.spec.is_pure_python)
        return node



    def visitDefault(self, element):
        return None