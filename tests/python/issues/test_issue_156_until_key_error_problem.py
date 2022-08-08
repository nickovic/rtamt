import unittest
import rtamt


class TestIssue156(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIssue156, self).__init__(*args, **kwargs)

    def test_issue_156(self):
        spec = rtamt.StlDenseTimeSpecification();
        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')
        spec.spec = 'out = (req) until (gnt and req)'

        spec.parse();
        left = [[0, 1.3], [0.7, 3], [1.3, 0.1], [2.1, -2.2]]
        right = [[0, 2.5], [0.7, 4], [1.3, -1.2], [2.1, 1.7]]

        out = spec.evaluate(['req', left], ['gnt', right])


if __name__ == '__main__':
    unittest.main()
