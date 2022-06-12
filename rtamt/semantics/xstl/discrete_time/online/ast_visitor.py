from rtamt.semantics.stl.discrete_time.online.ast_visitor import StlDiscreteTimeOnlineAstVisitor
from rtamt.syntax.ast.visitor.stl.ast_visitor import StlAstVisitor

from rtamt.semantics.arithmetic.discrete_time.online.addition_operation import AdditionOperation
from rtamt.semantics.arithmetic.discrete_time.online.multiplication_operation import MultiplicationOperation
from rtamt.semantics.arithmetic.discrete_time.online.subtraction_operation import SubtractionOperation
from rtamt.semantics.arithmetic.discrete_time.online.division_operation import DivisionOperation
from rtamt.semantics.arithmetic.discrete_time.online.abs_operation import AbsOperation
from rtamt.semantics.arithmetic.discrete_time.online.sqrt_operation import SqrtOperation
from rtamt.semantics.arithmetic.discrete_time.online.exp_operation import ExpOperation
from rtamt.semantics.arithmetic.discrete_time.online.pow_operation import PowOperation

from rtamt.semantics.stl.discrete_time.online.predicate_operation import PredicateOperation
from rtamt.semantics.stl.discrete_time.online.and_operation import AndOperation
from rtamt.semantics.stl.discrete_time.online.or_operation import OrOperation
from rtamt.semantics.stl.discrete_time.online.implies_operation import ImpliesOperation
from rtamt.semantics.stl.discrete_time.online.iff_operation import IffOperation
from rtamt.semantics.stl.discrete_time.online.xor_operation import XorOperation
from rtamt.semantics.stl.discrete_time.online.since_operation import SinceOperation
from rtamt.semantics.stl.discrete_time.online.not_operation import NotOperation
from rtamt.semantics.stl.discrete_time.online.rise_operation import RiseOperation
from rtamt.semantics.stl.discrete_time.online.fall_operation import FallOperation
from rtamt.semantics.stl.discrete_time.online.once_operation import OnceOperation
from rtamt.semantics.stl.discrete_time.online.historically_operation import HistoricallyOperation
from rtamt.semantics.stl.discrete_time.online.previous_operation import PreviousOperation
from rtamt.semantics.stl.discrete_time.online.once_timed_operation import OnceTimedOperation
from rtamt.semantics.stl.discrete_time.online.historically_timed_operation import HistoricallyTimedOperation
from rtamt.semantics.stl.discrete_time.online.since_timed_operation import SinceTimedOperation
from rtamt.semantics.stl.discrete_time.online.precedes_timed_operation import PrecedesTimedOperation

from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.exception.ltl.exception import LTLNotImplementedException
from rtamt.syntax.ast.visitor.xstl.ast_visitor import XStlAstVisitor


class XStlDiscreteTimeOnlineAstVisitor(StlDiscreteTimeOnlineAstVisitor, XStlAstVisitor):

    def visitShift(self, node, *args, **kwargs):
        self.visitChildren(node, *args, **kwargs)
        self.online_operator_dict[node.name] = ShiftOperation(node.operator)
