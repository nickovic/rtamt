import pytest
import rtamt

import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))


# TODO Fake a file containing the stl formulation
def get_specification(spec_file):
    spec = rtamt.StlDiscreteTimeSpecification()
    spec.spec = spec.get_spec_from_file(spec_file)
    spec.parse()
    return spec


@pytest.fixture
def tcc_runtime_monitor():
    # TODO Where are the specs?
    return get_specification(join(root_dir, 'specs', 'ttc.stl'))
