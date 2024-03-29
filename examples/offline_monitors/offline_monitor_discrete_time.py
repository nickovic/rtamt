#!/usr/bin/env python
import sys
import csv
import rtamt
import os

from rtamt.spec.stl.discrete_time.specification import Semantics


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
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req>=3) implies (eventually[0:5](gnt>=3)))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data1[' gnt'])):
        rob = spec.update(i, [('req', data1[' req'][i][1]), ('gnt', data1[' gnt'][i][1])])

    print('Example (a) - standard robustness: {}'.format(rob))

    # # #
    #
    # Example (a) - output robustness
    #
    # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.OUTPUT_ROBUSTNESS)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req>=3) implies (eventually[0:5](gnt>=3)))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data1[' gnt'])):
        rob = spec.update(i, [('req', data1[' req'][i][1]), ('gnt', data1[' gnt'][i][1])])

    print('Example (a) - output robustness: {}'.format(rob))

    # # #
    #
    # Example (a) - input vacuity
    #
    # # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.INPUT_VACUITY)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data1[' gnt'])):
        rob = spec.update(i, [('req', data1[' req'][i][1]), ('gnt', data1[' gnt'][i][1])])

    print('Example (a) - input vacuity: {}'.format(rob))

    # # #
    #
    # Example (b) - standard robustness
    #
    # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data2[' gnt'])):
        rob = spec.update(i, [('req', data2[' req'][i][1]), ('gnt', data2[' gnt'][i][1])])

    print('Example (b) - standard robustness: {}'.format(rob))

    # # #
    #
    # Example (b) - output robustness
    #
    # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.OUTPUT_ROBUSTNESS)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data2[' gnt'])):
        rob = spec.update(i, [('req', data2[' req'][i][1]), ('gnt', data2[' gnt'][i][1])])
    print('Example (b) - output robustness: {}'.format(rob))

    # # #
    #
    # Example (b) - input vacuity
    #
    # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.INPUT_VACUITY)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data2[' gnt'])):
        rob = spec.update(i, [('req', data2[' req'][i][1]), ('gnt', data2[' gnt'][i][1])])

    print('Example (b) - input vacuity: {}'.format(rob))

    # # #
    #
    # Example (c) - standard robustness
    #
    # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data3[' gnt'])):
        rob = spec.update(i, [('req', data3[' req'][i][1]), ('gnt', data3[' gnt'][i][1])])

    print('Example (c) - standard robustness: {}'.format(rob))


    # # #
    #
    # Example (c) - output robustness
    #
    # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.OUTPUT_ROBUSTNESS)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data3[' gnt'])):
        rob = spec.update(i, [('req', data3[' req'][i][1]), ('gnt', data3[' gnt'][i][1])])

    print('Example (c) - output robustness: {}'.format(rob))

    # # #
    #
    # Example (c) - input vacuity
    #
    # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.INPUT_VACUITY)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data3[' gnt'])):
        rob = spec.update(i, [('req', data3[' req'][i][1]), ('gnt', data3[' gnt'][i][1])])

    print('Example (c) - input vacuity: {}'.format(rob))

    # # # #
    # #
    # # Example (d) - standard robustness
    # #
    # # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
    spec.name = 'Example d'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data4[' gnt'])):
        rob = spec.update(i, [('req', data4[' req'][i][1]), ('gnt', data4[' gnt'][i][1])])

    print('Example (d) - standard robustness: {}'.format(rob))
    # # # #
    # #
    # # Example (d) - output robustness
    # #
    # # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.OUTPUT_ROBUSTNESS)
    spec.name = 'Example d'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data4[' gnt'])):
        rob = spec.update(i, [('req', data4[' req'][i][1]), ('gnt', data4[' gnt'][i][1])])

    print('Example (d) - output robustness: {}'.format(rob))

    #
    # # # #
    # #
    # # Example (d) - input vacuity
    # #
    # # # #
    spec = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.INPUT_VACUITY)
    spec.name = 'Example 1'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = ((req >= 3) implies eventually[0:5] (gnt >= 3))'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data1[' gnt'])):
        rob = spec.update(i, [('req', data1[' req'][i][1]), ('gnt', data1[' gnt'][i][1])])

    print('Example (d) - input vacuity: {}'.format(rob))

def read_csv(filename):
    f = open(filename, 'r')
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
    
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    monitor()
