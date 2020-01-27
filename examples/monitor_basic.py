#!/usr/bin/env python
import sys
import rtamt

def monitor():
    # data
    dataSet = {
         'a1': [(0, 100.0), (1, -1.0), (2, -2.0)],
         'b2': [(0, 20.0), (1, 2.0), (2, -10.0)]
    }

    # # stl
    spec = rtamt.STLSpecification(1)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a1', 'float')
    spec.declare_var('b2', 'float')
    spec.declare_var('c', 'float')
<<<<<<< HEAD
    spec.spec = 'c = a + b'
=======
    spec.spec = 'c = always(a1<=2 and b2>=1)'
>>>>>>> master
    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    # # eval
    aTraj = dataSet['a1']
    bTraj = dataSet['b2']
    for i in range(len(dataSet['a1'])):
        aData = aTraj[i]
        bData = bTraj[i]
        rob = spec.update(aData[0], [('a1', aData[1]), ('b2', bData[1])])
        print('time='+str(aData[0])+' rob='+str(rob))

if __name__ == '__main__':
    # Process arguments

    monitor()
