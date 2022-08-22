import unittest
import rtamt


class TestIssue157(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIssue157, self).__init__(*args, **kwargs)

    def test_issue_157_1(self):
        spec = rtamt.StlDiscreteTimeSpecification()
        spec.name = 'Example'
        spec.declare_var('p1', 'float')
        spec.declare_var('p2', 'float')
        spec.declare_var('out', 'float')
        spec.set_var_io_type('p1', 'input')
        spec.set_var_io_type('p2', 'input')
        spec.set_var_io_type('out', 'output')
        spec.spec = "out = eventually[0, 50] (p1 or p2)"
        spec.parse()
        data = {'time': range(2), 'p1': [1.0] * 2, 'p2': [1.0] * 2}
        rob = spec.evaluate(data)

        self.assertEqual(rob, [[0, 1.0], [1, 1.0]], 'test issue 157 1')

    def test_issue_158_2(self):
        spec = rtamt.StlDiscreteTimeSpecification()
        spec.name = 'Example'
        spec.declare_var('p1', 'float')
        spec.declare_var('p2', 'float')
        spec.declare_var('out', 'float')
        spec.set_var_io_type('p1', 'input')
        spec.set_var_io_type('p2', 'input')
        spec.set_var_io_type('out', 'output')
        spec.spec = "out = eventually[0, 500] (p1 or p2)"
        spec.parse()
        data = {
            'time': [0.0, 100.0, 200.0, 300.00000000000006, 400.0, 500.0, 600.0000000000001, 700.0000000000001, 800.0,
                     900.0, 1000.0, 1100.0, 1200.0000000000002, 1300.0, 1400.0000000000002, 1500.0, 1600.0,
                     1700.0000000000002, 1800.0, 1900.0000000000002, 2000.0], 'p1': [1.0] * 21, 'p2': [1.0] * 21}
        rob = spec.evaluate(data)
        print(rob)


if __name__ == '__main__':
    unittest.main()