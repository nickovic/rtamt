from rtamt.ast.parser_visitor.stl.rtamtASTvisitor import STLVisitor
from rtamt.exception.stl.exception import STLNotImplementedException
from rtamt.semantics.arithmetic.discrete_time.offline.addition_semantics import AdditionSemantics
from rtamt.semantics.arithmetic.discrete_time.offline.multiplication_semantics import MultiplicationSemantics
from rtamt.semantics.arithmetic.discrete_time.offline.subtraction_semantics import SubtractionSemantics
from rtamt.semantics.arithmetic.discrete_time.offline.division_semantics import DivisionSemantics
from rtamt.semantics.arithmetic.discrete_time.offline.abs_semantics import AbsSemantics
from rtamt.semantics.stl.discrete_time.offline.predicate_semantics import PredicateSemantics
from rtamt.semantics.stl.discrete_time.offline.and_semantics import AndSemantics
from rtamt.semantics.stl.discrete_time.offline.or_semantics import OrSemantics
from rtamt.semantics.stl.discrete_time.offline.implies_semantics import ImpliesSemantics
from rtamt.semantics.stl.discrete_time.offline.iff_semantics import IffSemantics
from rtamt.semantics.stl.discrete_time.offline.xor_semantics import XorSemantics
from rtamt.semantics.stl.discrete_time.offline.since_semantics import SinceSemantics
from rtamt.semantics.stl.discrete_time.offline.not_semantics import NotSemantics
from rtamt.semantics.stl.discrete_time.offline.rise_semantics import RiseSemantics
from rtamt.semantics.stl.discrete_time.offline.fall_semantics import FallSemantics
from rtamt.semantics.stl.discrete_time.offline.once_semantics import OnceSemantics
from rtamt.semantics.stl.discrete_time.offline.historically_semantics import HistoricallySemantics
from rtamt.semantics.stl.discrete_time.offline.always_semantics import AlwaysSemantics
from rtamt.semantics.stl.discrete_time.offline.eventually_semantics import EventuallySemantics
from rtamt.semantics.stl.discrete_time.offline.previous_semantics import PreviousSemantics
from rtamt.semantics.stl.discrete_time.offline.constant_semantics import ConstantSemantics
from rtamt.semantics.stl.discrete_time.offline.once_bounded_semantics import OnceBoundedSemantics
from rtamt.semantics.stl.discrete_time.offline.historically_bounded_semantics import HistoricallyBoundedSemantics
from rtamt.semantics.stl.discrete_time.offline.since_bounded_semantics import SinceBoundedSemantics
from rtamt.semantics.stl.discrete_time.offline.until_semantics import UntilSemantics
from rtamt.semantics.stl.discrete_time.offline.until_bounded_semantics import UntilBoundedSemantics
from rtamt.semantics.stl.discrete_time.offline.always_bounded_semantics import AlwaysBoundedSemantics
from rtamt.semantics.stl.discrete_time.offline.eventually_bounded_semantics import EventuallyBoundedSemantics
from rtamt.semantics.stl.discrete_time.offline.next_semantics import NextSemantics

class STLOfflineDiscreteTimePythonMonitor(STLVisitor):
    def __init__(self):
        self.node_monitor_dict = dict()

    def generate(self, node):
        self.visit(node, [])
        return self.node_monitor_dict

    def visitPredicate(self, node, args):
        monitor = PredicateSemantics(node.operator)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitVariable(self, node, args):
        pass

    def visitAbs(self, node, args):
        monitor = AbsSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitAddition(self, node, args):
        monitor = AdditionSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitSubtraction(self, node, args):
        monitor = SubtractionSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitMultiplication(self, node, args):
        monitor = MultiplicationSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitDivision(self, node, args):
        monitor = DivisionSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitNot(self, node, args):
        monitor = NotSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitAnd(self, node, args):
        monitor = AndSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitOr(self, node, args):
        monitor = OrSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitImplies(self, node, args):
        monitor = ImpliesSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitIff(self, node, args):
        monitor = IffSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitXor(self, node, args):
        monitor = XorSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitEventually(self, node, args):
        monitor = EventuallySemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitAlways(self, node, args):
        monitor = AlwaysSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitUntil(self, node, args):
        monitor = UntilSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitOnce(self, node, args):
        monitor = OnceSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitHistorically(self, node, args):
        monitor = HistoricallySemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitSince(self, node, args):
        monitor = SinceSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitRise(self, node, args):
        monitor = RiseSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitFall(self, node, args):
        monitor = FallSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitConstant(self, node, args):
        monitor = ConstantSemantics(node.val)
        self.node_monitor_dict[node.name] = monitor

    def visitPrevious(self, node, args):
        monitor = PreviousSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitNext(self, node, args):
        monitor = NextSemantics()
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedPrecedes(self, node, args):
        raise STLNotImplementedException('Precedes operator not implemented in STL offline monitor.')

    def visitTimedOnce(self, node, args):
        monitor = OnceBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedHistorically(self, node, args):
        monitor = HistoricallyBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedSince(self, node, args):
        monitor = SinceBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitTimedAlways(self, node, args):
        monitor = AlwaysBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedEventually(self, node, args):
        monitor = EventuallyBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)

    def visitTimedUntil(self, node, args):
        monitor = UntilBoundedSemantics(node.begin, node.end)
        self.node_monitor_dict[node.name] = monitor

        self.visit(node.children[0], args)
        self.visit(node.children[1], args)

    def visitDefault(self, node, args):
        pass
