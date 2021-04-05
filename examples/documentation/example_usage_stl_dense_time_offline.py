import sys
import rtamt

def monitor():

    req = [[0.0, 0.0], [3.0, 6.0], [5.0, 0.0], [11.0, 0.0]]
    gnt = [[0.0, 0.0], [7.0, 6.0], [9.0, 0.0], [11.0, 0.0]]

    spec = rtamt.STLDenseTimeSpecification()
    spec.name = 'STL Dense-time Offline Monitor'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = (req>=3) implies (eventually[0:5](gnt>=3))'
    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(['req', req], ['gnt', gnt])

    print('Robustness: {}'.format(rob))

if __name__ == '__main__':
    # Process arguments
    monitor()
