#!/usr/bin/env python
import sys
import csv
import rtamt

def monitor():
    # Load traces
    data1 = read_csv('example.csv')


    spec = rtamt.STLDenseTimeSpecification(semantics=rtamt.Semantics.STANDARD)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req>=3) implies (eventually[0:5.1s](gnt>=3)))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()


    rob = spec.evaluate(['req', data1[' req']], ['gnt', data1[' gnt']])

    print('Example (a) - standard robustness: {}'.format(rob))

    spec = rtamt.STLDenseTimeSpecification(semantics=rtamt.Semantics.STANDARD)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req>=3) implies (eventually[0:5100ms](gnt>=3)))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()


    rob = spec.evaluate(['req', data1[' req']], ['gnt', data1[' gnt']])

    # print('Example (a) - standard robustness: {}'.format(rob[len(rob)-1][1]))
    print('Example (a) - standard robustness: {}'.format(rob))



def read_csv(filename):
    f = open(filename, 'r')
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
