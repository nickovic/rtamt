import unittest
from rtamt import StlDenseTimeSpecification


class TestIssue173(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIssue173, self).__init__(*args, **kwargs)

    def test_issue_173_1(self):
        spec1 = StlDenseTimeSpecification()
        spec1.spec = "signal > (50 + 0)"
        spec1.declare_var("signal", "float")
        spec1.parse()

        spec2 = StlDenseTimeSpecification()
        spec2.spec = "signal > 50"
        spec2.declare_var("signal", "float")
        spec2.parse()

        rob1 = spec1.update(['signal', [(0, 25), (10, 75), (20, 100)]])
        print('spec1: ' + str(rob1))

        rob2 = spec2.update(['signal', [(0, 25), (10, 75), (20, 100)]])
        print('spec2: ' + str(rob2))

        self.assertListEqual(rob1, rob2)

if __name__ == '__main__':
    unittest.main()