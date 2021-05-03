#!/usr/bin/env python
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

import rtamt

time = [0, 1, 2, 3]
a =    [2, 5, 1, 7]

spec = rtamt.STLrevDiscreteTimeSpecification()
spec.name = 'STL test'
spec.declare_var('a', 'float')
spec.spec = 'always(a>=2)'
spec.parse()

rob = spec.evaluate({'time': time, 'a': a})
#TODO: the dictionary type input must be old.

print(rob)