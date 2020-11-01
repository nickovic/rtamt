import unittest
from rtamt.spec.stl.pastifier import STLPastifier
from rtamt.node.stl.constant import Constant
from rtamt.node.stl.variable import Variable
from rtamt.node.stl.abs import Abs
from rtamt.node.stl.addition import Addition
from rtamt.node.stl.subtraction import Subtraction
from rtamt.node.stl.multiplication import Multiplication
from rtamt.node.stl.division import Division
from rtamt.node.stl.predicate import Predicate
from rtamt.node.stl.neg import Neg
from rtamt.node.stl.conjunction import Conjunction
from rtamt.node.stl.disjunction import Disjunction
from rtamt.node.stl.implies import Implies
from rtamt.node.stl.iff import Iff
from rtamt.node.stl.xor import Xor
from rtamt.node.stl.rise import Rise
from rtamt.node.stl.fall import Fall
from rtamt.node.stl.once import Once
from rtamt.node.stl.historically import Historically
from rtamt.node.stl.eventually import Eventually
from rtamt.node.stl.always import Always
from rtamt.node.stl.since import Since
from rtamt.node.stl.until import Until
from rtamt.node.stl.precedes import Precedes
from rtamt.interval.interval import Interval
from rtamt.spec.stl.comp_op import StlComparisonOperator


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

    def test_variable_2(self):
        old_node = Variable('req', '', 'output')
        old_node.horizon = int(5)
        pastifier = STLPastifier()
        old_node.accept(pastifier)
        new_node = pastifier.pastify(old_node)

        self.assertEqual('once[5,5](req)', new_node.name, 'Variable pastification assertion')

    def test_abs_1(self):
        var_node = Variable('req', '', 'output')
        abs_node = Abs(var_node)

        pastifier = STLPastifier()
        abs_node.accept(pastifier)
        new_node = pastifier.pastify(abs_node)

        self.assertEqual('abs(req)', new_node.name, 'Absolute Value pastification assertion')

    def test_abs_2(self):
        var_node = Variable('req', '', 'output')
        var_node.horizon = 5
        abs_node = Abs(var_node)
        abs_node.horizon = 5

        pastifier = STLPastifier()
        abs_node.accept(pastifier)
        new_node = pastifier.pastify(abs_node)

        self.assertEqual('abs(once[5,5](req))', new_node.name, 'Absolute Value pastification assertion')

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

    def test_predicate_leq_2(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        node = Predicate(var_node_1, var_node_2, StlComparisonOperator.LEQ)
        node.horizon = 5

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('(once[5,5](req))<=(once[5,5](gnt))', new_node.name, 'Predicate LEQ pastification assertion')

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

        node.horizon = 5

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('once(once[5,5](req))', new_node.name, 'Once pastification assertion')


    def test_historically(self):
        var_node = Variable('req', '', 'output')
        node = Historically(var_node)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('historically(req)', new_node.name, 'Historically pastification assertion')

    def test_eventually(self):
        var_node = Variable('req', '', 'output')
        node = Eventually(var_node)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('eventually(req)', new_node.name, 'Eventually pastification assertion')

        node.horizon = 5

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('eventually(once[5,5](req))', new_node.name, 'Eventually pastification assertion')

    def test_always(self):
        var_node = Variable('req', '', 'output')
        node = Always(var_node)

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('always(req)', new_node.name, 'Always pastification assertion')

        node.horizon = 5

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('always(once[5,5](req))', new_node.name, 'Always pastification assertion')

    def test_since(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Since(var_node_1, var_node_2)

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)since(gnt)', new_node.name, 'Since pastification assertion')

        add_node.horizon = 5
        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(once[5,5](req))since(once[5,5](gnt))', new_node.name, 'Since pastification assertion')


    def test_once_0_1(self):
        var_node = Variable('req', '', 'output')
        node = Once(var_node, Interval(0, 1))

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('once[0,1](req)', new_node.name, 'Once pastification assertion')

        node.horizon = 5

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('once[0,1](once[5,5](req))', new_node.name, 'Once pastification assertion')

    def test_historically_0_1(self):
        var_node = Variable('req', '', 'output')
        node = Historically(var_node, Interval(0, 1))

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('historically[0,1](req)', new_node.name, 'Historically pastification assertion')

        node.horizon = 5

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('historically[0,1](once[5,5](req))', new_node.name, 'Historically pastification assertion')

    def test_eventually_0_1(self):
        var_node = Variable('req', '', 'output')
        node = Eventually(var_node, Interval(0, 1))

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('once[0,1](req)', new_node.name, 'Eventually pastification assertion')

        node.horizon = 5

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('once[0,1](once[4,4](req))', new_node.name, 'Eventually pastification assertion')

    def test_always_0_1(self):
        var_node = Variable('req', '', 'output')
        node = Always(var_node, Interval(0, 1))

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('historically[0,1](req)', new_node.name, 'Always pastification assertion')

        node.horizon = 5

        pastifier = STLPastifier()
        node.accept(pastifier)
        new_node = pastifier.pastify(node)

        self.assertEqual('historically[0,1](once[4,4](req))', new_node.name, 'Always pastification assertion')

    def test_until_0_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Until(var_node_1, var_node_2, Interval(0,1))

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)precedes[0,1](gnt)', new_node.name, 'Until pastification assertion')

        add_node.horizon = 5
        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(once[4,4](req))precedes[0,1](once[4,4](gnt))', new_node.name, 'Until pastification assertion')

    def test_since_0_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Since(var_node_1, var_node_2, Interval(0,1))

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)since[0,1](gnt)', new_node.name, 'Since pastification assertion')

        add_node.horizon = 5
        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(once[5,5](req))since[0,1](once[5,5](gnt))', new_node.name, 'Since pastification assertion')

    def test_precedes_0_1(self):
        var_node_1 = Variable('req', '', 'output')
        var_node_2 = Variable('gnt', '', 'output')
        add_node = Precedes(var_node_1, var_node_2, Interval(0,1))

        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(req)precedes[0,1](gnt)', new_node.name, 'Precedes pastification assertion')

        add_node.horizon = 5
        pastifier = STLPastifier()
        add_node.accept(pastifier)
        new_node = pastifier.pastify(add_node)

        self.assertEqual('(once[5,5](req))precedes[0,1](once[5,5](gnt))', new_node.name, 'Precedes pastification assertion')





if __name__ == '__main__':
    unittest.main()
