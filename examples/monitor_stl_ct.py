#!/usr/bin/env python
import sys
import rtamt

def monitor():
    a1 = [(0, 3), (3, 2)]
    b1 = [(0, 2), (2, 5), (4, 1), (7, -7)]

    a2 = [(5, 6), (6, -2), (8, 7), (11, -1)]
    b2 = [(10, 4)]

    a3 = [(13, -6), (15, 0)]
    b3 = [(15, 0)]

    # # stl
    spec = rtamt.STLCTSpecification(1)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.declare_var('c', 'float')
    spec.spec = 'c=a>=2'
    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.update(['a', a1], ['b', b1])
    print('rob: ' + str(rob))

    rob = spec.update(['a', a2], ['b', b2])
    print('rob: ' + str(rob))

    rob = spec.update(['a', a3], ['b', b3])
    print('rob: ' + str(rob))

    # # eval
    # aTraj = dataSet['a']
    # bTraj = dataSet['b']
    # for i in range(len(dataSet['a'])):
    #     aData = aTraj[i]
    #     bData = bTraj[i]
    #     rob = spec.update(aData[0], [('a', aData[1]), ('b', bData[1])])
    #     print('time='+str(aData[0])+' rob='+str(rob))

if __name__ == '__main__':
    # Process arguments

    monitor()
