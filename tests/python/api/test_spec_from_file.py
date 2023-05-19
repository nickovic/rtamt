import unittest

from rtamt.spec.stl.discrete_time.specification import StlDiscreteTimeOfflineSpecification
from rtamt.spec.stl.dense_time.specification import StlDenseTimeOfflineSpecification
from rtamt.spec.stl.discrete_time.specification import StlDiscreteTimeOnlineSpecification
from rtamt.spec.stl.dense_time.specification import StlDenseTimeOnlineSpecification


class TestSpecFromFile(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSpecFromFile, self).__init__(*args, **kwargs)


    def test_spec_from_file(self):
        spec = StlDiscreteTimeOfflineSpecification()
        spec.spec = spec.get_spec_from_file('req.stl')
        spec.parse()

        dataset = {
            'time': [0, 1, 2, 3, 4],
            'a': [2, 4, 5, 8, 1]
        }
        rob = spec.evaluate(dataset)

        expected = [[0, 3.0], [1, 1.0], [2, 0.0], [3, -3.0], [4, 4.0]]

        self.assertEqual(rob, expected, "spec from file")


if __name__ == '__main__':
    unittest.main()