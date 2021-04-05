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
    spec = rtamt.LTLSpecification(language=rtamt.Language.PYTHON)
    spec.name = 'LTL discrete-time online Python monitor'
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.spec = 'prev(next(a + b)) >= - 2'

    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    # # # eval
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
