import unittest
import rtamt


class TestIssue164(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIssue164, self).__init__(*args, **kwargs)

    def test_issue_170(self):
        spec = rtamt.StlDenseTimeSpecification()
        spec.name = "Bug?"
        spec.declare_var("y", "int")
        spec.declare_var("x", "int")
        spec.set_var_io_type("y", "input")
        spec.set_var_io_type("x", "output")
        #spec.spec = "(once[1,1](historically[0,5] x==1) and y) implies (historically[0, 1] x==0)"
        #spec.spec = "historically[0,1] x==0"
        spec.spec = "x==0 and y==1"

        spec.parse()
        spec.pastify()
        rob = spec.update(["x", [[0.0, 1]]], ["y", [[0.0, 0]]])
        for var, time, val in [
            ("x", 1.0, 1),
            ("y", 7.0, 1),
            ("x", 10.0, 0),
            ("y", 11.0, 0),
        ]:
            print(f"{var} {time} {val}")
            rob = spec.update([var, [(time, val)]])
            print(f"Robustness @{time}: {rob}")


if __name__ == '__main__':
    unittest.main()