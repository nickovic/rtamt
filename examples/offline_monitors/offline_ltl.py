#!/usr/bin/env python
import sys
sys.path.append('../../')

import rtamt

spec = rtamt.LTLrevSpecification()
spec.name = 'STL test'
spec.declare_var('a', 'float')
spec.spec = 'always(a>=2)'
spec.parse()