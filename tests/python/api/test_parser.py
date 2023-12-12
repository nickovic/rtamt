import unittest

from rtamt.spec.stl.discrete_time.specification import StlDiscreteTimeOfflineSpecification
from rtamt.spec.stl.dense_time.specification import StlDenseTimeOfflineSpecification
from rtamt.spec.stl.discrete_time.specification import StlDiscreteTimeOnlineSpecification
from rtamt.spec.stl.dense_time.specification import StlDenseTimeOnlineSpecification


class TestSemantics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSemantics, self).__init__(*args, **kwargs)


    def test_stl_spec_with_constant(self):
        spec = StlDiscreteTimeOfflineSpecification()
        spec.declare_var('a', 'float')
        spec.declare_const('b', 'float', 5)
        spec.spec = 'always(a>=b)'
        spec.parse()


if __name__ == '__main__':
    unittest.main()