#!/usr/bin/env python
import sys
import rtamt

def monitor():
    # data
    dataSet = {
         'a': [(0, 100.0), (1, -1.0), (2, -2.0)],
         'b': [(0, 20.0), (1, 2.0), (2, -10.0)]
    }

    # The default sampling period is 1s
    # The default unit is s
    # We require that the bound is divisible by the sampling period

    # # stl
    spec = rtamt.STLSpecification(1)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('c', 'float')
    # bound = [0s:1s]
    # sampling period = s
    # ok
    spec.spec = 'c = always[0:1](a>=0)'
    try:
        spec.parse()
        robustness = spec.offline(dataSet)
        print('Robustness: {}'.format(robustness))
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
    except rtamt.STLOfflineException as err:
        print('STL Offline Evaluation Exception: {}'.format(err))

    # # stl
    spec = rtamt.STLSpecification(1)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('c', 'float')
    # bound = [0s:100ms]
    # sampling period = 1s
    # not divisible - the parser fails
    spec.spec = 'c = always[0:100ms](a>=0)'
    try:
        spec.parse()
        robustness = spec.offline(dataSet)
        print('Robustness: {}'.format(robustness))

    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
    except rtamt.STLOfflineException as err:
        print('STL Offline Evaluation Exception: {}'.format(err))

    # # stl
    spec = rtamt.STLSpecification(1)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('c', 'float')
    # bound = [0s:100ms]
    # sampling period = 10ms
    # ok
    spec.spec = 'c = always[0:100ms](a>=0)'
    spec.set_sampling_period(10,'ms')
    try:
        spec.parse()
        robustness = spec.offline(dataSet)
        print('Robustness: {}'.format(robustness))

    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
    except rtamt.STLOfflineException as err:
        print('STL Offline Evaluation Exception: {}'.format(err))

    # # stl
    spec = rtamt.STLSpecification(1)
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('c', 'float')
    # bound = [0s:0.02s]
    # sampling period = 10ms
    # ok
    spec.spec = 'c = always[0:0.02s](a>=0)'
    spec.set_sampling_period(10, 'ms')
    try:
        spec.parse()
        robustness = spec.offline(dataSet)
        print('Robustness: {}'.format(robustness))

    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
    except rtamt.STLOfflineException as err:
        print('STL Offline Evaluation Exception: {}'.format(err))

if __name__ == '__main__':
    # Process arguments

    monitor()
