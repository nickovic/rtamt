import unittest
import rtamt
import sys


class TestIssueBooleanDense(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIssueBooleanDense, self).__init__(*args, **kwargs)

    def test_issue_boolean_dense(self):
        req = [[0.0, 0.0], [3.0, 6.0], [5.0, 0.0], [11.0, 0.0]]
        gnt = [[0.0, 0.0], [7.0, 6.0], [9.0, 0.0], [11.0, 0.0]]
        spec = rtamt.StlDenseTimeSpecification()

        spec.name = 'STL Dense-time offline Monitor'
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.set_var_io_type('req', 'input')
        spec.set_var_io_type('gnt', 'output')
        spec.spec = '(eventually[0,11](req>=3)) or (always[0,0.5](gnt>=5))'
        try:
            spec.parse()
        except rtamt.RTANTEXception as err:
            print('RTAMT Exception: {}'.format(err))
            sys.exit()

        rob = spec.evaluate(['req', req], ['gnt', gnt])
        self.assertListEqual([[0, 3.0], [5.0, -3.0]], rob, "dt")

if __name__ == '__main__':
    unittest.main()