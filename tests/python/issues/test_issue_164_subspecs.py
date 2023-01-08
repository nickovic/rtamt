import unittest
import rtamt


class TestIssue164(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIssue164, self).__init__(*args, **kwargs)

    def test_issue_157_1(self):
        # define data and variables types
        data = {
            "time": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "req": [0.0, 0.0, 0.0, 6.0, 6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "gnt": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0, 6.0, 0.0, 0.0, 0.0],
        }

        var_types = {
            "req": "float",
            "gnt": "float",
            "premise": "float",
            "response": "float",
        }

        # example 1: unique stl formula
        unique_formula = 'always((req>=3) implies (eventually[0:5]((gnt>=3) and (gnt<=10))))'

        spec1 = rtamt.StlDiscreteTimeSpecification()
        for var, type in var_types.items():
            spec1.declare_var(var, type)
        spec1.spec = unique_formula
        spec1.parse()

        # example 2: equivalent stl formula with 2 subformulas
        premise_formula = 'premise = (req >= 3)'
        response_formula = 'response = (eventually[0:5]((gnt>=3) and (gnt<=10)))'
        premise_response_formula = 'always(premise implies response)'

        spec2 = rtamt.StlDiscreteTimeSpecification()
        for var, type in var_types.items():
            spec2.declare_var(var, type)
        spec2.add_sub_spec(premise_formula)
        spec2.add_sub_spec(response_formula)
        spec2.spec = premise_response_formula
        spec2.parse()

        spec2.evaluate(data)

        # evaluate robustness
        robustnesses = []
        for spec in [spec1, spec2]:
            robustness_trace = spec.evaluate(data)
            robustnesses.append(robustness_trace[0][1])
            print(robustness_trace)

        self.assertEqual(robustnesses[0], robustnesses[1], 'test issue 164')


if __name__ == '__main__':
    unittest.main()