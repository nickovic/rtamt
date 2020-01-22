from rtamt.spec.stl.visitor import STLVisitor
from rtamt.operation.stl_ct.predicate_operation import PredicateOperation
from rtamt.operation.arithmetic_ct.abs_operation import AbsOperation
from rtamt.operation.arithmetic_ct.addition_operation import AdditionOperation
from rtamt.operation.arithmetic_ct.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic_ct.multiplication_operation import MultiplicationOperation
from rtamt.operation.arithmetic_ct.division_operation import DivisionOperation
from rtamt.operation.stl_ct.not_operation import NotOperation
from rtamt.operation.stl_ct.and_operation import AndOperation
from rtamt.operation.stl_ct.or_operation import OrOperation
from rtamt.operation.stl_ct.implies_operation import ImpliesOperation
from rtamt.operation.stl_ct.xor_operation import XorOperation
from rtamt.operation.stl_ct.iff_operation import IffOperation
from rtamt.operation.stl_ct.historically_operation import HistoricallyOperation
from rtamt.operation.stl_ct.once_operation import OnceOperation

class STLCTNodeInit(STLVisitor):


    def visitVariable(self, element, args):
        pass

    def visitPredicate(self, element, args):
        element.node.node = PredicateOperation(element.node.op, element.node.threshold, element.node.io_type)

    def visitAbs(self, element, args):
        self.visit(element.children[0], args)
        element.node.node = AbsOperation()

    def visitAddition(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = AdditionOperation()

    def visitSubtraction(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = SubtractionOperation()

    def visitMultiplication(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = MultiplicationOperation()

    def visitDivision(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = DivisionOperation()

    def visitNot(self, element, args):
        self.visit(element.children[0], args)
        element.node.node = NotOperation()

    def visitAnd(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = AndOperation()

    def visitOr(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = OrOperation()

    def visitImplies(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = ImpliesOperation()

    def visitIff(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = IffOperation()

    def visitXor(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node.node = XorOperation()

    def visitEventually(self, element, args):
        pass

    def visitAlways(self, element, args):
        self.visit(element.children[0], args)
        element.node.node = HistoricallyOperation()

    def visitUntil(self, element, args):
        pass

    def visitOnce(self, element, args):
        self.visit(element.children[0], args)
        element.node.node = OnceOperation()

    def visitHistorically(self, element, args):
        self.visit(element.children[0], args)
        element.node.node = HistoricallyOperation()

    def visitSince(self, element, args):
        pass

    def visitPrecedes(self, element, args):
        pass

    def visitDefault(self, element, args):
        return None