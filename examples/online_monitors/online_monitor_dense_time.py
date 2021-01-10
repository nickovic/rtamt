#!/usr/bin/env python
import sys
import csv
import rtamt

def monitor():
    # Load traces
    req = [[0, 0], [1.5, 2], [2.3, 4.3], [3, 0], [7, 3.1], [8, 1], [9.2, 2.8], [10, 2.8]]
    gnt = [[0, 0], [2.5, 2.9], [5.6, 1], [7.9, 6], [10, 6]]

    req_1 = [[0, 0], [1.5, 2], [2.3, 4.3]]
    gnt_1 = [[0, 0], [2.5, 2.9]]

    req_2 = [[3, 0], [7, 3.1], [8, 1]]
    gnt_2 = [[5.6, 1], [7.9, 6]]

    req_3 = [[9.2, 2.8], [10, 2.8]]
    gnt_3 = [[10, 6]]

    # # #
    #
    # Example - offline robustness
    #
    # # #
    spec = rtamt.STLDenseTimeSpecification()
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req>=3) implies (eventually[1:2](gnt>=3)))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()


    rob = spec.evaluate(['req', req], ['gnt', gnt])
    print('Robustness offline: {}'.format(rob))

    # # #
    #
    # Example - online robustness
    #
    # # #
    spec = rtamt.STLDenseTimeSpecification()
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req>=3) implies (eventually[1:2](gnt>=3)))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.update(['req', req_1], ['gnt', gnt_1])
    print('Robustness online - step 1: {}'.format(rob))

    rob = spec.update(['req', req_2], ['gnt', gnt_2])
    print('Robustness online - step 2: {}'.format(rob))

    rob = spec.update(['req', req_3], ['gnt', gnt_3])
    print('Robustness online - step 3: {}'.format(rob))

    #rob = spec.update_final(['req', []], ['gnt', []])
    #print('Robustness online - step final: {}'.format(rob))


def read_csv(filename):
    f = open(filename, 'rb')
    reader = csv.reader(f)
    headers = next(reader, None)

    column = {}
    for h in headers:
        column[h] = []

    for row in reader:
        for h, v in zip(headers, row):
            column[h].append([float(row[0]), float(v)])

    return column





if __name__ == '__main__':
    # Process arguments

    monitor()
