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
    spec = rtamt.STLDiscreteTimeSpecification(1)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.declare_var('c', 'float')
    spec.add_sub_spec('c = a + b')
    spec.spec = 'c >= - 2'

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
        print('time='+str(aData[0])+' rob='+str(rob) + ' c=' + str(spec.get_value('c')))

if __name__ == '__main__':
    # Process arguments

    monitor()
