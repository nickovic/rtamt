import rtamt

spec = rtamt.StlDiscreteTimeOfflineSpecification()
spec.declare_var('x', 'float')
spec.spec = 'G[3,5](G[1,2](x>5))'
spec.parse()

dataSet = {
    'time': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'x'   : [0, 0, 0, 0, 0, 0, 6, 6, 6, 6],
}

rob = spec.evaluate(dataSet)
print(rob)