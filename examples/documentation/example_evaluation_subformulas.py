import sys
import rtamt

def monitor():
    # data
    dataset = {
         'time': [0, 1, 2],
         'a': [100.0, -1.0, -2.0],
         'b': [20.0, 2.0, 10.0]
    }

    # # stl
    spec = rtamt.StlDiscreteTimeSpecification()
    spec.name = 'HandMadeMonitor'
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.declare_var('c', 'float')
    spec.declare_var('d', 'float')
    spec.add_sub_spec('c = a + b;')
    spec.spec = 'd = c >= - 2;'

    try:
        spec.parse()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    spec.evaluate(dataset)
    a = spec.get_value('a')
    b = spec.get_value('b')
    c = spec.get_value('c')
    d = spec.get_value('d')

    print('a: ' + str(a))
    print('b: ' + str(b))
    print('c: ' + str(c))
    print('d: ' + str(d))

if __name__ == '__main__':
    monitor()