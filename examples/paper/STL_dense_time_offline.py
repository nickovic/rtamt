import rtamt

spec = rtamt.STLDenseTimeSpecification()
spec.declare_var('req', 'float')
spec.declare_var('gnt', 'float')
spec.spec = '(req >= 3) implies (gnt >= 0)'
spec.parse()

req = [[0, 100], [1, -1], [2, -2], [3, 5], [4, -1]]
gnt = [[0, 20], [1, -2], [2, 10], [3, 4], [4, -1]]

rob = spec.evaluate(['req', req], ['gnt', gnt])