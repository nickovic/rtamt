import unittest

import rtamt
from rtamt.spec.stl.discrete_time.specification import StlDiscreteTimeOfflineSpecification
from rtamt.spec.stl.dense_time.specification import StlDenseTimeOfflineSpecification
from rtamt.spec.stl.discrete_time.specification import StlDiscreteTimeOnlineSpecification
from rtamt.spec.stl.dense_time.specification import StlDenseTimeOnlineSpecification

import os.path


class TestSemantics(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSemantics, self).__init__(*args, **kwargs)


    def test_stl_spec_with_constant(self):
        spec = StlDiscreteTimeOfflineSpecification()
        spec.declare_var('a', 'float')
        spec.declare_const('b', 'float', 5)
        spec.spec = 'always(a>=b)'

        try:
            spec.parse()
        except Exception:
            self.fail("parse() raised Exception unexpectedly!")

    def test_stl_spec_with_constant_from_file(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "specs/req.stl")
        spec = StlDiscreteTimeOfflineSpecification()
        spec.spec = spec.get_spec_from_file(path)

        try:
            spec.parse()
        except Exception:
            self.fail("parse() raised Exception unexpectedly!")

    def test_stl_ttc_spec_from_file(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "specs/ttc.stl")
        spec = StlDiscreteTimeOfflineSpecification()
        spec.spec = spec.get_spec_from_file(path)

        try:
            spec.parse()
        except Exception:
            self.fail("parse() raised Exception unexpectedly!")

    def test_stl_mttc_spec_from_file(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "specs/mttc.stl")
        spec = StlDiscreteTimeOfflineSpecification()
        spec.spec = spec.get_spec_from_file(path)

        try:
            spec.parse()
        except Exception:
            self.fail("parse() raised Exception unexpectedly!")

    def test_stl_ioreq_spec_from_file(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "specs/ioreq.stl")
        spec = rtamt.StlDiscreteTimeSpecification(rtamt.Semantics.OUTPUT_ROBUSTNESS)
        spec.spec = spec.get_spec_from_file(path)

        spec.parse()

        out = spec.update(0, [('a', 5), ('b', 4)])
        self.assertEqual(out, float('inf'), "input 1")

        out = spec.update(0, [('a', 4), ('b', 5)])
        self.assertEqual(out, -1, "input 1")


if __name__ == '__main__':
    unittest.main()