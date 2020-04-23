import rtamt

# Assumes piece wise constant interpolation.
data = {
    'a': [(0, 1), (11, -1), (13, 1), (14,1)],
}

spec = rtamt.STLIOCTSpecification(1)
spec.name = 'spec'
spec.declare_var('a', 'float')
spec.declare_var('out', 'float')
spec.set_var_io_type('a', 'input')
spec.set_var_io_type('out', 'output')
#spec.spec = 'out = always((a>=3) implies (eventually[0:5](a>=3)))'
spec.spec = 'out = always[0:1.5](a<0.0)'
spec.iosem = 'standard'
spec.parse()

rob = spec.offline(['a', data['a']])
print('output robustness: {}'.format(rob))
