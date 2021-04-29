from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent.parent))

import rtamt

a = [(0, 2), (2, 5), (4, 1), (7, -7)]


spec = rtamt.STLabDenseTimeSpecification()
spec.name = 'STLab dense-time specification'
spec.declare_var('a', 'float')
spec.spec = 'always(a>=2)'
spec.parse()

rob = spec.evaluate(['a', a])
print(rob)