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
    spec = rtamt.STLSpecification(1)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.declare_var('c', 'float')
    spec.spec = 'c = always(a<=2 and b>=1)'
    try:
        spec.parse()
        robustness = spec.offline(dataSet)
        print('Robustness: {}'.format(robustness))

    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()
    except rtamt.STLOfflineException as err:
        print('STL Offline Evaluation Exception: {}'.format(err))
        sys.exit()

if __name__ == '__main__':
    # Process arguments

    monitor()
