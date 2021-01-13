#!/usr/bin/env python
import sys
import rtamt

def monitor():
    # data
    dataSet = {
         'a': [(0, 100.0), (1, -1.0), (2, -2.0)],
         'b': [(0, 20.0), (1, 2.0), (2, -10.0)]
    }

    # # stl
    spec = rtamt.STLDiscreteTimeSpecification(language=rtamt.Language.PYTHON)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.declare_const('c', 'float', '5.2')
    spec.spec = 'a + b >= c'

    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    # # eval
    aTraj = dataSet['a']
    bTraj = dataSet['b']
    for i in range(len(dataSet['a'])):
        aData = aTraj[i]
        bData = bTraj[i]
        rob = spec.update(aData[0], [('a', aData[1]), ('b', bData[1])])
        print('time='+str(aData[0])+' rob='+str(rob))

if __name__ == '__main__':
    # Process arguments

    monitor()
