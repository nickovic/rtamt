import rtamt

spec = rtamt.StlDiscreteTimeOfflineSpecification()
spec.declare_var('phi1', 'int')
spec.declare_var('phi2', 'int')
spec.spec = '(phi1>0) S[2, 4] (phi2>0)'
spec.parse()

dataset = {
    'time': [0, 1, 2, 3, 4, 5, 6, 7],
    'phi1': [0, 0, 0, 0, 1, 1, 0, 0],
    'phi2': [0, 0, 1, 1, 0, 0, 0, 0]
}

rob = spec.evaluate(dataset)
print(rob)