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
        print(rob)


if __name__ == '__main__':
    unittest.main()