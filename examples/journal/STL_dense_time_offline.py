import rtamt

spec = rtamt.StlDenseTimeOfflineSpecification()
spec.declare_var('req', 'float')
spec.declare_var('gnt', 'float')
spec.spec = 'G((req>=3)->(F[0,5](gnt>=3)))'
spec.parse()

req = [[0.0, 0.0], [2.0, 6.0], [4.0, 0.0], [10.0, 0.0]]
gnt = [[0.0, 0.0], [6.0, 6.0], [8.0, 0.0], [10.0, 0.0]]

rob = spec.evaluate(['req', req], ['gnt', gnt])