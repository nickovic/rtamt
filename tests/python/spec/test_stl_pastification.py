import unittest
from rtamt.pastifier.stl.pastifier import STLPastifier
from rtamt.node.ltl.constant import Constant
from rtamt.node.ltl.variable import Variable
from rtamt.node.arithmetic.abs import Abs
from rtamt.node.arithmetic.sqrt import Sqrt
from rtamt.node.arithmetic.exp import Exp
from rtamt.node.arithmetic.pow import Pow
from rtamt.node.arithmetic.addition import Addition
from rtamt.node.arithmetic.subtraction import Subtraction
from rtamt.node.arithmetic.multiplication import Multiplication
from rtamt.node.arithmetic.division import Division
from rtamt.node.ltl.predicate import Predicate
from rtamt.node.ltl.neg import Neg
from rtamt.node.ltl.conjunction import Conjunction
from rtamt.node.ltl.disjunction import Disjunction
from rtamt.node.ltl.implies import Implies
from rtamt.node.ltl.iff import Iff
from rtamt.node.ltl.xor import Xor
from rtamt.node.ltl.rise import Rise
from rtamt.node.ltl.fall import Fall
from rtamt.node.ltl.once import Once
from rtamt.node.ltl.historically import Historically
from rtamt.node.ltl.since import Since
from rtamt.node.stl.timed_precedes import TimedPrecedes
from rtamt.node.ltl.previous import Previous
from rtamt.node.ltl.next import Next
from rtamt.enumerations.comp_op import StlComparisonOperator
from rtamt.node.stl.timed_always import TimedAlways
from rtamt.node.stl.timed_eventually import TimedEventually
from rtamt.node.stl.timed_historically import TimedHistorically
from rtamt.node.stl.timed_once import TimedOnce
from rtamt.node.stl.timed_since import TimedSince
from rtamt.node.stl.timed_until import TimedUntil


class TestSTLPastification(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSTLPastification, self).__init__(*args, **kwargs)

    def test_constant(self):
        old_node = Constant(2)
        pastifier = STLPastifier()
        old_node.accept(pastifier)
        new_node = pastifier.pastify(old_node)

        self.assertEqual(str(2), new_node.name, 'Constant pastification assertion')

    def test_variable_1(self):
        old_node = Variable('req', '', 'output')
        pastifier = STLPastifier()
        old_node.accept(pastifier)
        new_node = pastifier.pastify(old_node)

        self.assertEqual('req', new_node.name, 'Variable pastification assertion')

        old_node = Variable('myvar.req', 'val', 'output')
        pastifier = STLPastifier()
        old_node.accept(pastifier)
        new_node = pastifier.pastify(old_node)

        self.assertEqual('myvar.req.val', new_node.name, 'Variable pastification assertion')


    def test_previous_1(self):
        var_node = Variable('req', '', 'output')
        abs_node = Previous(var_node)

        pastifier = STLPastifier()
        abs_node.accept(pastifier)
        new_node = pastifier.pastify(abs_node)

        self.assertEqual('previous(req)', new_node.name, 'Previous pastification assertion')


    def test_next_1(self):
        var_node = Variable('req', '', 'output')
        abs_node = Next(var_node)

        pastifier = STLPastifier()
        abs_node.accept(pastifier)
        new_node = pastifier.pastify(abs_node)

        self.assertEqual('req', new_node.name, 'Next pastification assertion')

    def test_abs_1(self):
        var_node = Variable('req', '', 'output')
        abs_node = Abs(var_node)

        pastifier = STLPastifier()
        abs_node.accept(pastifier)
        new_node = pastifier.pastify(abs_node)

        self.assertEqual('abs(req)', new_node.name, 'Absolute Value pastification assertion')

    def test_sqrt_1(self):
        var_node = Variable('req', '', 'output')
        sqrt_node = Sqrt(var_node)

        pastifier = STLPastifier()
        sqrt_node.accept(pastifier)
        new_node = pastifier.pastify(sqrt_node)

        self.assertEqual('sqrt(req)', new_node.name, 'Square Root pastification assertion')


    def test_exp(self):
        var_node = Variable('req', '', 'output')
        sqrt_node = Exp(var_node)

        pastifier = STLPastifier()
        sqrt_node.accept(pastifier)
        new_node = pastifier.pastify(sqrt_node)

        self.assertEqual('exp(req)', new_node.name, 'Exp pastification assertion')

    def test_pow(self):
        var_node = Variable('req', '', 'output')
        cnt_node = Constant(2)
        sqrt_node = Pow(cnt_node, var_node)

        pastifier = STLPastifier()
        sqrt_node.accept(pastifier)
        new_node = pastifier.pastify(sqrt_node)

        self.assertEqual('pow(2,req)', new_node.name, 'Pow pastification assertion')

    def test_addition(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Addition(var_node_1, var_node_2)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)+(gnt)', new_node.name, 'Addition pastification assertion')

    def test_subtraction(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        sub_node = Subtraction(var_node_1, var_node_2)

        pastifier = STLPastifier()
        sub_node.accept(pastifier)
        new_node = pastifier.pastify(sub_node)

        self.assertEqual('(req)-(gnt)', new_node.name, 'Subtraction pastification assertion')

    def test_multiplication(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Multiplication(var_node_1, var_node_2)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(req)*(gnt)', new_node.name, 'Multiplication pastification assertion')

    def test_division(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Division(var_node_1, var_node_2)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(req)/(gnt)', new_node.name, 'Division pastification assertion')

    def test_predicate_leq_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Predicate(var_node_1, var_node_2, StlComparisonOperator.LEQ)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(req)<=(gnt)', new_node.name, 'Predicate LEQ pastification assertion')

    def test_predicate_less(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Predicate(var_node_1, var_node_2, StlComparisonOperator.LESS)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(req)<(gnt)', new_node.name, 'Predicate LESS pastification assertion')

    def test_predicate_geq(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Predicate(var_node_1, var_node_2, StlComparisonOperator.GEQ)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(req)>=(gnt)', new_node.name, 'Predicate GEQ pastification assertion')

    def test_predicate_greater(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Predicate(var_node_1, var_node_2, StlComparisonOperator.GREATER)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(req)>(gnt)', new_node.name, 'Predicate GREATER pastification assertion')

    def test_predicate_eq(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Predicate(var_node_1, var_node_2, StlComparisonOperator.EQUAL)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(req)==(gnt)', new_node.name, 'Predicate EQ pastification assertion')

    def test_predicate_neq(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Predicate(var_node_1, var_node_2, StlComparisonOperator.NEQ)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(req)!=(gnt)', new_node.name, 'Predicate NEQ pastification assertion')


    def test_not(self):
        var_node = Variable('req', '', 'output')
        node = Neg(var_node)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('not(req)', new_node.name, 'Negation pastification assertion')


    def test_conjunction(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Conjunction(var_node_1, var_node_2)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)and(gnt)', new_node.name, 'Conjunction pastification assertion')

    def test_disjunction(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Disjunction(var_node_1, var_node_2)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)or(gnt)', new_node.name, 'Disjunction pastification assertion')

    def test_implication(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Implies(var_node_1, var_node_2)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)->(gnt)', new_node.name, 'Implication pastification assertion')

    def test_iff(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Iff(var_node_1, var_node_2)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)<->(gnt)', new_node.name, 'Iff pastification assertion')

    def test_xor(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Xor(var_node_1, var_node_2)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)xor(gnt)', new_node.name, 'Xor pastification assertion')

    def test_rise(self):
        var_node = Variable('req', '', 'output')
        node = Rise(var_node)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('rise(req)', new_node.name, 'Rise pastification assertion')

    def test_fall(self):
        var_node = Variable('req', '', 'output')
        node = Fall(var_node)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('fall(req)', new_node.name, 'Fall pastification assertion')

    def test_once(self):
        var_node = Variable('req', '', 'output')
        node = Once(var_node)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('once(req)', new_node.name, 'Once pastification assertion')


    def test_historically(self):
        var_node = Variable('req', '', 'output')
        node = Historically(var_node)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('historically(req)', new_node.name, 'Historically pastification assertion')

    def test_since(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Since(var_node_1, var_node_2)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)since(gnt)', new_node.name, 'Since pastification assertion')

    def test_once_0_1(self):
        var_node = Variable('req', '', 'output')
        node = TimedOnce(var_node, 0, 1)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('once[0,1](req)', new_node.name, 'Once pastification assertion')

    def test_historically_0_1(self):
        var_node = Variable('req', '', 'output')
        node = TimedHistorically(var_node, 0, 1)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('historically[0,1](req)', new_node.name, 'Historically pastification assertion')

    def test_eventually_0_1(self):
        var_node = Variable('req', '', 'output')
        node = TimedEventually(var_node, 0, 1)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('once[0,1](req)', new_node.name, 'Eventually pastification assertion')

    def test_always_0_1(self):
        var_node = Variable('req', '', 'output')
        node = TimedAlways(var_node, 0, 1)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('historically[0,1](req)', new_node.name, 'Always pastification assertion')

    def test_until_0_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = TimedUntil(var_node_1, var_node_2, 0, 1)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)precedes[0,1](gnt)', new_node.name, 'Until pastification assertion')

    def test_since_0_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = TimedSince(var_node_1, var_node_2, 0, 1)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)since[0,1](gnt)', new_node.name, 'Since pastification assertion')

    def test_precedes_0_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = TimedPrecedes(var_node_1, var_node_2, 0, 1)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)precedes[0,1](gnt)', new_node.name, 'Precedes pastification assertion')

    def test_complex_past_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        rise_node = Rise(var_node_1)
        hist_node = Historically(var_node_2)
        once_node = TimedOnce(hist_node, 1, 2)
        add_node = TimedSince(rise_node, once_node, 2, 6)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(rise(req))since[2,6](once[1,2](historically(gnt)))', new_node.name, 'Complex pastification assertion')

    def test_complex_past_2(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        rise_node = Rise(var_node_1)
        hist_node = Historically(var_node_2)
        once_node = TimedOnce(hist_node, 1, 2)
        add_node = TimedSince(rise_node, once_node, 2, 6)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(rise(req))since[2,6](once[1,2](historically(gnt)))', new_node.name, 'Complex pastification assertion')

    def test_complex_bounded_future_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        cnt_node_1 = Constant(3)
        cnt_node_2 = Constant(3)
        pd_node_1 = Predicate(var_node_1, cnt_node_1, StlComparisonOperator.GEQ)
        pd_node_2 = Predicate(var_node_2, cnt_node_2, StlComparisonOperator.GEQ)
        rise_node = Rise(pd_node_1)
        hist_node = TimedAlways(pd_node_2, 3, 4)
        once_node = TimedEventually(hist_node, 1, 2)
        add_node = Implies(rise_node, once_node)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(rise((once[6,6](req))>=(3)))->(once[0,1](historically[0,1]((gnt)>=(3))))', new_node.name, 'Complex pastification assertion')

    def test_complex_bounded_future_2(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        var_node_3 = Variable('ack', '', 'output')

        until_node = TimedUntil(var_node_1, var_node_2, 1, 2)
        ev_node = TimedEventually(var_node_3, 0, 6)
        add_node = Implies(until_node, ev_node)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('((once[4,4](req))precedes[1,2](once[4,4](gnt)))->(once[0,6](ack))', new_node.name, 'Complex pastification assertion')

    def test_complex_mixed_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')

        ev_node = TimedEventually(var_node_1, 5, 6)
        once_node = TimedOnce(var_node_2, 1, 2)
        ev_once_node = TimedEventually(once_node, 3, 3)
        add_node = Implies(ev_node, ev_once_node)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(once[0,1](req))->(once[1,2](once[3,3](gnt)))', new_node.name, 'Complex pastification assertion')

    def test_complex_mixed_2(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')

        ev_node = TimedEventually(var_node_1, 5, 6)
        once_node = TimedOnce(var_node_2, 1, 2)
        alw_node = TimedAlways(once_node, 3, 3)
        add_node = Implies(ev_node, alw_node)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(once[0,1](req))->(once[1,2](once[3,3](gnt)))', new_node.name, 'Complex pastification assertion')


    if __name__ == '__main__':
        unittest.main()