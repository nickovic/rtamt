import sys
import rtamt

def monitor():
    # # stl
    spec = rtamt.StlDiscreteTimeSpecification()
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.spec = 'eventually[0,1] (a >= b);'

    try:
        spec.parse()
        spec.pastify()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    t = 0
    rob = spec.update(t, [('a', 100.0), ('b', 20.0)])
    print('time=' + str(t) + ' rob=' + str(rob))

    t = 1
    rob = spec.update(t, [('a', -1.0), ('b', 2.0)])
    print('time=' + str(t) + ' rob=' + str(rob))

    t = 2
    rob = spec.update(t, [('a', -2.0), ('b', -10.0)])
    print('time=' + str(t) + ' rob=' + str(rob))

if __name__ == '__main__':
    monitor()