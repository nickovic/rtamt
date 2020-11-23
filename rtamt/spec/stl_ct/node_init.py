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
from rtamt.operation.stl_ct.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl_ct.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl_ct.constant_operation import ConstantOperation

class STLCTNodeInit(STLVisitor):


    def visitVariable(self, element, args):
        pass

    def visitConstant(self, element, args):
        element.node = ConstantOperation(element.node.val)

    def visitPredicate(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = PredicateOperation(element.node.op)

    def visitAbs(self, element, args):
        self.visit(element.children[0], args)
        element.node = AbsOperation()

    def visitAddition(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = AdditionOperation()

    def visitSubtraction(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = SubtractionOperation()

    def visitMultiplication(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = MultiplicationOperation()

    def visitDivision(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = DivisionOperation()

    def visitNot(self, element, args):
        self.visit(element.children[0], args)
        element.node = NotOperation()

    def visitAnd(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = AndOperation()

    def visitOr(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = OrOperation()

    def visitImplies(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = ImpliesOperation()

    def visitIff(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = IffOperation()

    def visitXor(self, element, args):
        self.visit(element.children[0], args)
        self.visit(element.children[1], args)
        element.node = XorOperation()

    def visitEventually(self, element, args):
        pass

    def visitAlways(self, element, args):
        self.visit(element.children[0], args)
        element.node = HistoricallyOperation()

    def visitUntil(self, element, args):
        pass

    def visitOnce(self, element, args):
        self.visit(element.children[0], args)
        if element.bound is None:
            element.node = OnceOperation()
        else:
            element.node = OnceBoundedOperation(element.bound.begin, element.bound.end)


    def visitRise(self, element, args):
        self.visit(element.children[0], args)
        #element.node = RiseOperation()

    def visitFall(self, element, args):
        self.visit(element.children[0], args)
        #element.node = FallOperation()

    def visitHistorically(self, element, args):
        self.visit(element.children[0], args)
        if element.bound is None:
            element.node = HistoricallyOperation()
        else:
            element.node = HistoricallyBoundedOperation(element.bound.begin, element.bound.end)

    def visitSince(self, element, args):
        pass

    def visitPrecedes(self, element, args):
        pass

    def visitDefault(self, element, args):
        return None