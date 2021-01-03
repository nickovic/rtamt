import sys
import csv
import rtamt
import os

def monitor():
    # Load traces
    data = read_csv('example1.csv')

    spec = rtamt.STLDiscreteTimeSpecification()
    spec.name = 'Example 1'
    spec.declare_const('threshold', 'float', '3')
    spec.declare_const('T', 'float', '5')
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('response', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.add_sub_spec('response = eventually[0:T s](gnt >= threshold)')
    spec.spec = 'out = ((req >= threshold) implies response)'
    try:
        spec.parse()
        spec.pastify()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    for i in range(len(data[' gnt'])):
        out_rob = spec.update(i, [('req', data[' req'][i][1]), ('gnt', data[' gnt'][i][1])])
        response_rob = spec.get_value('response')
        print('time: {0}, response robustness: {1}, out robustness: {2}'.format(i, response_rob, out_rob))


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
