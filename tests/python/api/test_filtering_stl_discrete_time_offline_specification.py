import unittest
import math
import rtamt

class TestFilteringStlDiscreteTimeOfflineSpecification(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFilteringStlDiscreteTimeOfflineSpecification, self).__init__(*args, **kwargs)
        self.dataset = {
            'time': [0, 1, 2, 3, 4],
            'req': [0, 1, 1, 1, 1],
            'gnt': [0, 1, 0, 0, 1]
        }

    def test_constant_1(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('out', 'float')
        spec.spec = 'out = 5'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]

        self.assertListEqual(out, expected, "constant")

    def test_constant_2(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_const('c', 'int', 5)
        spec.declare_var('out', 'float')
        spec.spec = 'out = c'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]

        self.assertListEqual(out, expected, "constant")

    def test_addition(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req + gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0+0], [1, 1+1], [2, 1+0], [3, 1+0], [4, 1+1]]

        self.assertListEqual(out, expected, "addition")

    def test_subtraction(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req - gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0-0], [1, 1-1], [2, 1-0], [3, 1-0], [4, 1-1]]

        self.assertListEqual(out, expected, "subtraction")

    def test_multiplication(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req * gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0*0], [1, 1*1], [2, 1*0], [3, 1*0], [4, 1*1]]

        self.assertListEqual(out, expected, "multiplication")


    def test_abs(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = abs(req)'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "abs")

    def test_sqrt(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = sqrt(abs(req))'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, math.sqrt(0)], [1, math.sqrt(1)], [2, math.sqrt(1)], [3, math.sqrt(1)], [4, math.sqrt(1)]]

        self.assertListEqual(out, expected, "abs")

    def test_exp(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = exp(req)'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, math.exp(0)], [1, math.exp(1)], [2, math.exp(1)], [3, math.exp(1)], [4, math.exp(1)]]

        self.assertListEqual(out, expected, "exp")

    def test_pow(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = pow(2.2,req)'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, math.pow(2.2, 0)], [1, math.pow(2.2, 1)], [2, math.pow(2.2, 1)], [3, math.pow(2.2, 1)], [4, math.pow(2.2, 1)]]

        self.assertListEqual(out, expected, "pow")

    def test_previous(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = prev req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 0], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "previous")

    def test_next(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = next req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "next")

    def test_and(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req and gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1], [2, 0], [3, 0], [4, 1]]

        self.assertListEqual(out, expected, "and")

    def test_or(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req or gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "or")

    def test_iff(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req iff gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 1], [2, 0], [3, 0], [4, 1]]

        self.assertListEqual(out, expected, "iff")

    def test_xor(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req xor gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 0], [2, 1], [3, 1], [4, 0]]

        self.assertListEqual(out, expected, "xor")


    def test_implies(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req -> gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 1], [2, 0], [3, 0], [4, 1]]

        self.assertListEqual(out, expected, "implies")

    def test_always(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = always req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "always")

    def test_always_0_1(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = always[0,1] req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "always[0,1]")

    def test_historically(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = historically req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]

        self.assertListEqual(out, expected, "historically")

    def test_once(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = once req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1/2], [2, 2/3], [3, 3/4], [4, 4/5]]

        self.assertListEqual(out, expected, "once")

    def test_eventually(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = eventually req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 4/5], [1, 1], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "eventually")

    def test_eventually_0_1(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = eventually[0,1] req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1/2], [1, 1], [2, 1], [3, 1], [4, 1/2]]

        self.assertListEqual(out, expected, "eventually[0,1]")

    def test_since(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req since gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1/2], [2, 1/3], [3, 1/4], [4, 2/5]]

        self.assertListEqual(out, expected, "since")

    def test_until(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req until gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 2/4], [2, 1/3], [3, 1/2], [4, 1]]

        self.assertListEqual(out, expected, "until")

    def test_until_0_1(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req until[0,1] gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1/2], [2, 0], [3, 1/2], [4, 1/2]]

        self.assertListEqual(out, expected, "until")

    def test_once_0_1(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = once[0,1] req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1/2], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "once[0,1]")

    def test_once_1_2(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = once[1,2] req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 0], [2, 1/2], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "once[1,2]")

    def test_historically_0_1(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = historically[0,1] req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 0], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "historically[0,1]")

    def test_historically_1_2(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = historically[1,2] req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 0], [2, 0], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "historically[1,2]")

    def test_since_0_1(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req since[0,1] gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1/2], [2, 1/2], [3, 0], [4, 1/2]]

        self.assertListEqual(out, expected, "since[0,1]")

    def test_not(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = not req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 0], [2, 0], [3, 0], [4, 0]]

        self.assertListEqual(out, expected, "not")

    def test_rise(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = rise(req)'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 1], [2, 0], [3, 0], [4, 0]]

        self.assertListEqual(out, expected, "rise")

    def test_fall(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = fall(req)'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]

        self.assertListEqual(out, expected, "fall")

    def test_predicate_leq(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req <= gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 1], [2, 0], [3, 0], [4, 1]]

        self.assertListEqual(out, expected, "leq")

    def test_predicate_less(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req < gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]

        self.assertListEqual(out, expected, "less")

    def test_predicate_geq(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req >= gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]

        self.assertListEqual(out, expected, "geq")

    def test_predicate_greater(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req > gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 0], [2, 1], [3, 1], [4, 0]]

        self.assertListEqual(out, expected, "greater")

    def test_predicate_eq(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req == gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 1], [1, 1], [2, 0], [3, 0], [4, 1]]

        self.assertListEqual(out, expected, "eq")

    def test_predicate_neq(self):
        spec = rtamt.FilteringStlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = req !== gnt'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, 0], [1, 0], [2, 1], [3, 1], [4, 0]]

        self.assertListEqual(out, expected, "neq")

if __name__ == '__main__':
    unittest.main()