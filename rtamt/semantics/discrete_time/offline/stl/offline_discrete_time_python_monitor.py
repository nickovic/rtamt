from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.semantics.discrete_time.offline.arithmetic.semantics.addition_semantics import AdditionSemantics
from rtamt.semantics.discrete_time.offline.arithmetic.semantics.multiplication_semantics import MultiplicationSemantics
from rtamt.semantics.discrete_time.offline.arithmetic.semantics.subtraction_semantics import SubtractionSemantics
from rtamt.semantics.discrete_time.offline.arithmetic.semantics.division_semantics import DivisionSemantics
from rtamt.semantics.discrete_time.offline.arithmetic.semantics.abs_semantics import AbsSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.predicate_semantics import PredicateSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.and_semantics import AndSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.or_semantics import OrSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.implies_semantics import ImpliesSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.iff_semantics import IffSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.xor_semantics import XorSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.since_semantics import SinceSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.not_semantics import NotSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.rise_semantics import RiseSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.fall_semantics import FallSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.once_semantics import OnceSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.historically_semantics import HistoricallySemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.always_semantics import AlwaysSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.eventually_semantics import EventuallySemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.previous_semantics import PreviousSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.constant_semantics import ConstantSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.once_bounded_semantics import OnceBoundedSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.historically_bounded_semantics import HistoricallyBoundedSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.since_bounded_semantics import SinceBoundedSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.until_semantics import UntilSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.until_bounded_semantics import UntilBoundedSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.always_bounded_semantics import AlwaysBoundedSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.eventually_bounded_semantics import EventuallyBoundedSemantics
from rtamt.semantics.discrete_time.offline.stl.semantics.next_semantics import NextSemantics

class STLOfflineDiscreteTimePythonMonitor(STLVisitor):
    def __init__(self):
        self.node_monitor_dict = dict()

    def generate(self, node):
        self.visit(node, [])
        return self.node_monitor_dict

    def visitPredicate(self, node, pre_out, *args, **kwargs):
        monitor = PredicateSemantics(node.operator)
        self.node_monitor_dict[node.name] = monitor

    def visitVariable(self, node, pre_out, *args, **kwargs):
        pass

    def visitAbs(self, node, pre_out, *args, **kwargs):
        monitor = AbsSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitAddition(self, node, pre_out, *args, **kwargs):
        monitor = AdditionSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitSubtraction(self, node, pre_out, *args, **kwargs):
        monitor = SubtractionSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitMultiplication(self, node, pre_out, *args, **kwargs):
        monitor = MultiplicationSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitDivision(self, node, pre_out, *args, **kwargs):
        monitor = DivisionSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitNot(self, node, pre_out, *args, **kwargs):
        monitor = NotSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitAnd(self, node, pre_out, *args, **kwargs):
        monitor = AndSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitOr(self, node, pre_out, *args, **kwargs):
        monitor = OrSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitImplies(self, node, pre_out, *args, **kwargs):
        monitor = ImpliesSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitIff(self, node, pre_out, *args, **kwargs):
        monitor = IffSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitXor(self, node, pre_out, *args, **kwargs):
        monitor = XorSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitEventually(self, node, pre_out, *args, **kwargs):
        monitor = EventuallySemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitAlways(self, node, pre_out, *args, **kwargs):
        monitor = AlwaysSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitUntil(self, node, pre_out, *args, **kwargs):
        monitor = UntilSemantics()
        self.node_monitor_dict[node.name] = monitor


    def visitOnce(self, node, pre_out, *args, **kwargs):
        monitor = OnceSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitHistorically(self, node, pre_out, *args, **kwargs):
        monitor = HistoricallySemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitSince(self, node, pre_out, *args, **kwargs):
        monitor = SinceSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitRise(self, node, pre_out, *args, **kwargs):
        monitor = RiseSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitFall(self, node, pre_out, *args, **kwargs):
        monitor = FallSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitConstant(self, node, pre_out, *args, **kwargs):
        monitor = ConstantSemantics(node.val)
        self.node_monitor_dict[node.name] = monitor

    def visitPrevious(self, node, pre_out, *args, **kwargs):
        monitor = PreviousSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitNext(self, node, pre_out, *args, **kwargs):
        monitor = NextSemantics()
        self.node_monitor_dict[node.name] = monitor

    def visitTimedPrecedes(self, node, pre_out, *args, **kwargs):
        raise STLNotImplementedException('Precedes operator not implemented in STL offline monitor.')

    def visitTimedOnce(self, node, pre_out, *args, **kwargs):
        monitor = OnceBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedHistorically(self, node, pre_out, *args, **kwargs):
        monitor = HistoricallyBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedSince(self, node, pre_out, *args, **kwargs):
        monitor = SinceBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedAlways(self, node, pre_out, *args, **kwargs):
        monitor = AlwaysBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedEventually(self, node, pre_out, *args, **kwargs):
        monitor = EventuallyBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitTimedUntil(self, node, pre_out, *args, **kwargs):
        monitor = UntilBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

    def visitDefault(self, node, pre_out, *args, **kwargs):
        pass
