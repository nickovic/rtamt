import rtamt

spec = rtamt.StlDenseTimeOfflineSpecification()
spec.declare_var('req', 'float')
spec.declare_var('event', 'float')
spec.spec = 'G((req >= 3) -> (F[0, 2] (event >= 0)))'
spec.parse()

req   = [[0, 100], [1, -1], [2, -2], [3, 5], [4, -1]]
event = [[0,  20], [1, -2], [2, 10], [3, 4], [4, -1]]

rob = spec.evaluate(['req', req], ['event', event])