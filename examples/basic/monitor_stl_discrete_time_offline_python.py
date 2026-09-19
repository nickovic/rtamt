import sys
import rtamt

def monitor():
    # data
    dataSet = {
         'time': [0, 1, 2],
         'a': [100.0, -1.0, -2.0],
         'b': [20.0, 2.0, -10.0]
    }

    # # stl
    spec = rtamt.StlDiscreteTimeSpecification()
    spec.name = 'STL discrete-time online Python monitor'
    spec.declare_var('a', 'float')
    spec.declare_var('b', 'float')
    spec.spec = 'a + b >= - 2;'

    try:
        spec.parse()
    except rtamt.RTAMTException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(dataSet)
    print('Robustness: ' + str(rob))

if __name__ == '__main__':
    # Process arguments

    monitor()
