import unittest
import rtamt
from rtamt.operation.sample import Sample


class TestSTLSamplingTimeUnits(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSTLSamplingTimeUnits, self).__init__(*args, **kwargs)
        self.left1 = Sample()
        self.right1 = Sample()
        self.left1.value = 100
        self.right1.value = 20

        self.left2 = Sample()
        self.right2 = Sample()
        self.left2.value = -1
        self.right2.value = 2

        self.left3 = Sample()
        self.right3 = Sample()
        self.left3.value = -2
        self.right3.value = -10

        self.left4 = Sample()
        self.right4 = Sample()
        self.left4.value = 5
        self.right4.value = 4

        self.left5 = Sample()
        self.right5 = Sample()
        self.left5.value = -1
        self.right5.value = -1

    def test_example(self):
        spec = rtamt.STLSpecification()
        spec.name = 'STL Example specification'

        self.assertEqual(spec.name, 'STL Example specification', 'Spec name assertion')

        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')

        spec.spec = 'out = req<=2 and gnt>=3'

        self.assertEqual(spec.spec, 'out = req<=2 and gnt>=3', 'Spec assertion')
        self.assertEqual(spec.sampling_tolerance, 0.1, 'Spec sampling tolerance assertion')

        try:
            spec.parse();
            computed = spec.update(0, [['req', 2.2], ['gnt', 1]])
            self.assertEqual(-2.0, computed, 'First computation')

            computed = spec.update(1.2, [['req', 4.2], ['gnt', -3.7]])
            self.assertEqual(-6.7, computed, 'First computation')
            self.assertEqual(1, spec.sampling_violation_counter, 'Violation counter')
        except rtamt.STLParseException as err:
            print('STL Parse Exception: {}'.format(err))

    def test_wrong_tolerance(self):
        spec = rtamt.STLSpecification()
        with self.assertRaises(rtamt.STLSpecificationException):
            spec.set_sampling_period(1, 's', 1.5)

    def test_default_unit_default_sampling_unit_greater_tolerance_ok_samples(self):
        spec = rtamt.STLSpecification()
        spec.name = 'STL Example specification'

        self.assertEqual(spec.name, 'STL Example specification', 'Spec name assertion')

        spec.declare_var('req', 'float')
        spec.declare_var('gnt', 'float')
        spec.declare_var('out', 'float')

        spec.set_sampling_period(1, 's', 0.5)

        spec.spec = 'out = rise(req)'

        try:
            spec.parse();
            spec.update(0, [['req', 2.2], ['gnt', 1]])
            spec.update(1.11, [['req', 2.2], ['gnt', 1]])
            spec.update(1.99, [['req', 2.2], ['gnt', 1]])
            spec.update(3.38, [['req', 2.2], ['gnt', 1]])
            spec.update(4.39, [['req', 2.2], ['gnt', 1]])

            self.assertEqual(0, spec.sampling_violation_counter, 'Violation counter')
        except rtamt.STLParseException as err:
            print('STL Parse Exception: {}'.format(err))


if __name__ == '__main__':
    unittest.main()
