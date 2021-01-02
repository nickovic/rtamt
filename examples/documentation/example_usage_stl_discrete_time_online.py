import sys
import rtamt

def monitor():
    # # stl
    spec = rtamt.STLSpecification()
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.spec = 'eventually[0,1] (a >= b)'

    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    rob = spec.update(0, [('a', 100.0), ('b', 20.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

    rob = spec.update(1, [('a', -1.0), ('b', 2.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

    rob = spec.update(2, [('a', -2.0), ('b', -10.0)])
    print('time=' + str(0) + ' rob=' + str(rob))

if __name__ == '__main__':
    monitor()