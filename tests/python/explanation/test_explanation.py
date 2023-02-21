import unittest
import rtamt


class TestSemantics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSemantics, self).__init__(*args, **kwargs)
        self.dataset = {
            'time': [0, 1, 2, 3, 4],
            'req': [-1, -1, -2, 5, -1],
            'gnt': [20, -2, 10, 4, -1]
        }

    def test_eventually_0_1(self):
        spec = rtamt.StlDiscreteTimeOfflineSpecification()
        spec.declare_var('req', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = eventually[0,1] req'

        spec.parse()
        out = spec.evaluate(self.dataset)
        expected = [[0, -1], [1, -1], [2, 5], [3, 5], [4, -1]]

        spec.explain()
        explanation = spec.explainer.explanations
        print(explanation)

        self.assertListEqual(out, expected, "eventually[0,1]")


if __name__ == '__main__':
    unittest.main()