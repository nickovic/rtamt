import unittest
import rtamt


class TestIssue85(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIssue85, self).__init__(*args, **kwargs)

    def test_issue_85(self):
        specification = rtamt.STLDiscreteTimeSpecification()

        specification.declare_var('zzz', 'float')
        specification.spec = '!( (eventually[2,3]( zzz) ) )'

        specification.parse()

        signal1 = {'time': [0, 1, 2, 3], 'zzz': [-5., -4., -0.3, 0.1]}

        rob = specification.evaluate(signal1)

        expected = [[0, -0.1], [1, -0.1], [2, float('inf')], [3, float('inf')]]

        self.assertEqual(rob, expected, "issue 85 - 1st run")

        rob = specification.evaluate(signal1)

        self.assertEqual(rob, expected, "issue 85 - 2nd run")


if __name__ == '__main__':
    unittest.main()
