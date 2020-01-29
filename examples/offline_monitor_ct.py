#!/usr/bin/env python
import sys
import csv
import rtamt

def monitor():
    # Load traces
    data1 = read_csv('example1.csv')
    data2 = read_csv('example2.csv')
    data3 = read_csv('example3.csv')
    data4 = read_csv('example4.csv')

    # # #
    #
    # Example (a) - standard robustness
    #
    # # #
    spec = rtamt.STLIOCTSpecification(1)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = always((req>=3) implies (eventually[0:5](gnt>=3)))'
    spec.iosem = 'standard'
    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.update(['req', data1[' req']], ['gnt', data1[' gnt']])

    print('Example (a) - standard robustness: {}'.format(min(rob[1])))



def read_csv(filename):
    f = open(filename, 'rb')
    reader = csv.reader(f)
    headers = next(reader, None)

    column = {}
    for h in headers:
        column[h] = []

    for row in reader:
        for h, v in zip(headers, row):
            column[h].append((float(row[0]), float(v)))

    return column





if __name__ == '__main__':
    # Process arguments

    monitor()
