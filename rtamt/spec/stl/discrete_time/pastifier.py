from rtamt.spec.stl.discrete_time.visitor import STLVisitor
from rtamt.spec.ltl.discrete_time.pastifier import LTLPastifier

from rtamt.node.ltl.predicate import Predicate
from rtamt.node.ltl.variable import Variable
from rtamt.node.ltl.neg import Neg
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.implies import Implies
from rtamt.node.ltl.iff import Iff
from rtamt.node.ltl.xor import Xor
from rtamt.node.ltl.eventually import Eventually
from rtamt.node.ltl.always import Always
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.historically import Historically
from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.ltl.since import Since
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.arithmetic.abs import Abs
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.previous import Previous
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince


class STLPastifier(LTLPastifier, STLVisitor):

    def __init__(self, is_pure_python=True):
        self.is_pure_python = is_pure_python
        
    @property
    def is_pure_python(self):
        return self.__is_pure_python

    @is_pure_python.setter
    def is_pure_python(self, is_pure_python):
        self.__is_pure_python = is_pure_python

    def visitVariable(self, element, args):
        horizon = args[0]
        node = Variable(element.var, element.field, element.io_type)
        if horizon > 0:
            node = TimedOnce(node, horizon, horizon, self.is_pure_python)
        return node

    def visitTimedEventually(self, element, args):
        horizon = args[0] - element.end
        node = self.visit(element.children[0], [horizon])
        begin = 0
        end = element.end - element.begin
        if end > 0:
            node = TimedOnce(node, begin, end, self.is_pure_python)
        return node

    def visitTimedAlways(self, element, args):
        horizon = args[0] - element.end
        node = self.visit(element.children[0], [horizon])
        begin = 0
        end = element.end - element.begin
        if end > 0:
            node = TimedHistorically(node, begin, end, self.is_pure_python)
        return node

    def visitTimedUntil(self, element, args):
        horizon = args[0] - element.end
        begin = element.begin
        end = element.end
        child1_node = self.visit(element.children[0], [horizon])
        child2_node = self.visit(element.children[1], [horizon])
        node = TimedPrecedes(child1_node, child2_node, begin, end, self.is_pure_python)
        return node

    def visitTimedOnce(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = TimedOnce(child_node, element.begin, element.end, self.is_pure_python)
        return node

    def visitTimedHistorically(self, element, args):
        child_node = self.visit(element.children[0], args)
        node = TimedHistorically(child_node, element.begin, element.end, self.is_pure_python)
        return node

    def visitTimedSince(self, element, args):
        child_node_1 = self.visit(element.children[0], args)
        child_node_2 = self.visit(element.children[1], args)
        node = TimedSince(child_node_1, child_node_2, element.begin, element.end, self.is_pure_python)
        return node

    def visitTimedPrecedes(self, element, args):
        end = element.end
        begin = element.begin
        child1_node = self.visit(element.children[0], args)
        child2_node = self.visit(element.children[1], args)
        node = TimedPrecedes(child1_node, child2_node, begin, end, self.is_pure_python)
        return node

    def visitDefault(self, element):
        return None