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
        print("Before pastification: " + spec.spec_print())

        spec.pastify()
        print("After pastification: " + spec.spec_print())
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

if __name__ == '__main__':
    monitor()