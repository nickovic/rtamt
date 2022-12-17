import rtamt

spec = rtamt.StlDiscreteTimeOfflineSpecification()
spec.declare_var('phi', 'int')
spec.spec = 'G[2, 4] (phi>0)'
spec.parse()

dataset = {
    'time': [0, 1, 2, 3, 4, 5, 6, 7],
    'phi' : [0, 0, 1, 1, 1, 0, 0, 0]
}

rob = spec.evaluate(dataset)
print(rob)