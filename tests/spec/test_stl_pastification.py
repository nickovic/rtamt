import unittest
from rtamt.spec.stl.pastifier import STLPastifier
from rtamt.node.stl.constant import Constant
from rtamt.node.stl.variable import Variable


class TestSTLPastification(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSTLPastification, self).__init__(*args, **kwargs)

    def test_constant(self):
        old_node = Constant(2)
        pastifier = STLPastifier()
        old_node.accept(pastifier)
        new_node = pastifier.pastify(old_node)

        self.assertEqual(str(2), new_node.name, 'Constant pastification assertion')

    def test_variable_1(self):
        old_node = Variable('req', '', 'output')
        pastifier = STLPastifier()
        old_node.accept(pastifier)
        new_node = pastifier.pastify(old_node)

        self.assertEqual('req', new_node.name, 'Constant pastification assertion')

    def test_variable_2(self):
        old_node = Variable('req', '', 'output')
        old_node.horizon = int(5)
        pastifier = STLPastifier()
        old_node.accept(pastifier)
        new_node = pastifier.pastify(old_node)

        self.assertEqual('once[5,5](req)', new_node.name, 'Constant pastification assertion')

if __name__ == '__main__':
    unittest.main()
