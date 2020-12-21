from rtamt.spec.stl.discrete_time.visitor import STLVisitor
from rtamt.operation.stl.dense_time.predicate_operation import PredicateOperation
from rtamt.operation.arithmetic.dense_time import AbsOperation
from rtamt.operation.arithmetic.dense_time.addition_operation import AdditionOperation
from rtamt.operation.arithmetic.dense_time.subtraction_operation import SubtractionOperation
from rtamt.operation.arithmetic.dense_time import MultiplicationOperation
from rtamt.operation.arithmetic.dense_time.division_operation import DivisionOperation
from rtamt.operation.stl.dense_time.not_operation import NotOperation
from rtamt.operation.stl.dense_time import AndOperation
from rtamt.operation.stl.dense_time import OrOperation
from rtamt.operation.stl.dense_time import ImpliesOperation
from rtamt.operation.stl.dense_time import XorOperation
from rtamt.operation.stl.dense_time.iff_operation import IffOperation
from rtamt.operation.stl.dense_time import HistoricallyOperation
from rtamt.operation.stl.dense_time import OnceOperation
from rtamt.operation.stl.dense_time import OnceBoundedOperation
from rtamt.operation.stl.dense_time import HistoricallyBoundedOperation
from rtamt.operation.stl.dense_time import ConstantOperation

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

    def visitTimedEventually(self, element, args):
        pass

    def visitAlways(self, element, args):
        self.visit(element.children[0], args)
        element.node = HistoricallyOperation()

    def visitTimedAlways(self, element, args):
        pass

    def visitUntil(self, element, args):
        pass

    def visitTimedUntil(self, element, args):
        pass

    def visitPrevious(self, element, args):
        pass

    def visitNext(self, element, args):
        pass

    def visitOnce(self, element, args):
        self.visit(element.children[0], args)
        element.node = OnceOperation()

    def visitTimedOnce(self, element, args):
        self.visit(element.children[0], args)
        element.node = OnceBoundedOperation(element.begin, element.end)

    def visitRise(self, element, args):
        self.visit(element.children[0], args)
        #element.node = RiseOperation()

    def visitFall(self, element, args):
        self.visit(element.children[0], args)
        #element.node = FallOperation()

    def visitHistorically(self, element, args):
        self.visit(element.children[0], args)
        element.node = HistoricallyOperation()

    def visitTimedHistorically(self, element, args):
        self.visit(element.children[0], args)
        element.node = HistoricallyBoundedOperation(element.begin, element.end)

    def visitSince(self, element, args):
        pass

    def visitTimedSince(self, element, args):
        pass

    def visitTimedPrecedes(self, element, args):
        pass

    def visitDefault(self, element, args):
        return None