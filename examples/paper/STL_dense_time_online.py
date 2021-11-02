import rtamt

spec = rtamt.STLDenseTimeSpecification()
spec.declare_var('req', 'float')
spec.declare_var('event', 'float')
spec.spec = 'historically[0, 4]((req >= 3) implies (once[0, 2] (event >= 0)))'
spec.parse()

req_0   = [[0, 100], [1, -1], [2, -2]]
event_0 = [[0,  20], [1, -2], [2, 10]]
req_1   = [[3, 5], [4, -1]]
event_1 = [[3, 4], [4, -1]]

rob = spec.update(['req', req_0], ['event', event_0])
rob = spec.update(['req', req_1], ['event', event_1])