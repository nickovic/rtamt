import rtamt

spec = rtamt.StlDenseTimeOnlineSpecification()
spec.declare_var('req', 'float')
spec.declare_var('gnt', 'float')
spec.spec = 'H[0, 10]((req >= 3) -> (O[0, 5] (gnt >= 3)))'
spec.parse()

req_0 = [[0.0, 0.0], [2.0, 6.0]]
gnt_0 = [[0.0, 0.0]]
req_1 = [[4.0, 0.0], [10.0, 0.0]]
gnt_1 = [[5.0, 6.0], [8.0, 0.0], [10.0, 0.0]]

rob = spec.update(['req', req_0], ['gnt', gnt_0])
rob = spec.update(['req', req_1], ['gnt', gnt_1])