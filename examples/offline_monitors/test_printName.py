#!/usr/bin/env python
import sys
sys.path.append('../../')

import rtamt
from rtamt.spec_rev.stl.discrete_time.printName_specification import PrintNameSpecification

time = [0, 1, 2, 3]
a =    [2, 5, 1, 7]

spec = PrintNameSpecification()
spec.name = 'STL test'
spec.declare_var('a', 'float')
spec.spec = 'always(a>=2)'
spec.parse()

out = spec.printName()
print('Inclusion relationship = '+out)
