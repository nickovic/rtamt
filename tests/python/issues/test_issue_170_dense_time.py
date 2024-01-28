import unittest
import rtamt


class TestIssue164(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIssue164, self).__init__(*args, **kwargs)

    #def test_issue_online_170(self):
    #    spec = rtamt.StlDenseTimeSpecification()
    #    spec.name = "Bug?"
    #    spec.declare_var("y", "int")
    #    spec.declare_var("x", "int")
    #    spec.set_var_io_type("y", "input")
    #    spec.set_var_io_type("x", "output")
    #    spec.spec = "((historically[0,5] x==1) and (y==1)) -> (eventually[0,1] (x==0))"
    #    spec.spec = "((historically[0,5] x==1) and (y==1)) -> (once[0,1] (x==0))"

    #    spec.parse()
        #spec.pastify()
    #    rob = spec.update(["x", [[0.0, 1]]], ["y", [[0.0, 0]]])
    #    print(f"Robustness @0.0: {rob}")

     #   expected = [[0, float('inf')]]

        # self.assertListEqual(rob, expected, 'offline')

    #    for var, time, val in [
     #       ("x", 1.0, 1),
     #       ("y", 7.0, 1),
     #       ("x", 10.0, 0),
     #       ("y", 11.0, 0),
     #   ]:
     #       print(f"{var} {time} {val}")
     #       rob = spec.update([var, [(time, val)]])
     #       print(f"Robustness @{time}: {rob}")

    def test_issue_offline_170_1(self):
        spec = rtamt.StlDenseTimeSpecification()
        spec.name = "Bug?"
        spec.declare_var("y", "int")
        spec.declare_var("x", "int")
        spec.set_var_io_type("y", "input")
        spec.set_var_io_type("x", "output")
        spec.spec = "(x==1)"

        spec.parse()
        rob = spec.evaluate(["x", [[0.0, 1], [10.0, 0]]], ["y", [[0.0, 0], [7.0, 1], [11.0, 0]]])
        expected = [[0, 0], [10.0, -1.0]]

        self.assertListEqual(rob, expected, 'offline')

    def test_issue_offline_170_2(self):
        spec = rtamt.StlDenseTimeSpecification()
        spec.name = "Bug?"
        spec.declare_var("y", "int")
        spec.declare_var("x", "int")
        spec.set_var_io_type("y", "input")
        spec.set_var_io_type("x", "output")
        spec.spec = "(x==0)"

        spec.parse()
        rob = spec.evaluate(["x", [[0.0, 1], [10.0, 0]]], ["y", [[0.0, 0], [7.0, 1], [11.0, 0]]])
        expected = [[0, -1], [10.0, 0]]

        self.assertListEqual(rob, expected, 'offline')

    def test_issue_offline_170_3(self):
        spec = rtamt.StlDenseTimeSpecification()
        spec.name = "Bug?"
        spec.declare_var("y", "int")
        spec.declare_var("x", "int")
        spec.set_var_io_type("y", "input")
        spec.set_var_io_type("x", "output")
        spec.spec = "(y==1)"

        spec.parse()
        rob = spec.evaluate(["x", [[0.0, 1], [10.0, 0]]], ["y", [[0.0, 0], [7.0, 1], [11.0, 0]]])
        expected = [[0, -1], [7, 0], [11.0, -1]]

        self.assertListEqual(rob, expected, 'offline')

    def test_issue_offline_170_4(self):
        spec = rtamt.StlDenseTimeSpecification()
        spec.name = "Bug?"
        spec.declare_var("y", "int")
        spec.declare_var("x", "int")
        spec.set_var_io_type("y", "input")
        spec.set_var_io_type("x", "output")
        spec.spec = "historically[0:5] x==1"

        spec.parse()
        rob = spec.evaluate(["x", [[0.0, 1], [10.0, 0]]], ["y", [[0.0, 0], [7.0, 1], [11.0, 0]]])
        expected = [[0, 0], [10.0, -1]]

        self.assertListEqual(rob, expected, 'offline')

    def test_issue_offline_170_5(self):
        spec = rtamt.StlDenseTimeSpecification()
        spec.name = "Bug?"
        spec.declare_var("y", "int")
        spec.declare_var("x", "int")
        spec.set_var_io_type("y", "input")
        spec.set_var_io_type("x", "output")
        spec.spec = "(historically[0:5] x==1) and y==1"

        spec.parse()
        rob = spec.evaluate(["x", [[0.0, 1], [10.0, 0]]], ["y", [[0.0, 0], [7.0, 1], [11.0, 0]]])
        expected = [[0, -1], [7, 0], [10, -1]]

        self.assertListEqual(rob, expected, 'offline')

    def test_issue_offline_170_6(self):
        spec = rtamt.StlDenseTimeSpecification()
        spec.name = "Bug?"
        spec.declare_var("y", "int")
        spec.declare_var("x", "int")
        spec.set_var_io_type("y", "input")
        spec.set_var_io_type("x", "output")
        spec.spec = "eventually[0:1] (x==0)"

        spec.parse()
        rob = spec.evaluate(["x", [[0.0, 1], [10.0, 0]]], ["y", [[0.0, 0], [7.0, 1], [11.0, 0]]])
        expected = [[0, -1], [9, 0]]

        self.assertListEqual(rob, expected, 'offline')

    def test_issue_offline_170_7(self):
        spec = rtamt.StlDenseTimeSpecification()
        spec.name = "Bug?"
        spec.declare_var("y", "int")
        spec.declare_var("x", "int")
        spec.set_var_io_type("y", "input")
        spec.set_var_io_type("x", "output")
        spec.spec = "((historically[0:5] x==1) and y==1) -> (eventually[0:1] (x==0))"

        spec.parse()
        rob = spec.evaluate(["x", [[0.0, 1], [10.0, 0]]], ["y", [[0.0, 0], [7.0, 1], [11.0, 0]]])
        expected = [[0, 1], [7, 0], [10, 1]]

        self.assertListEqual(rob, expected, 'offline')

if __name__ == '__main__':
    unittest.main()