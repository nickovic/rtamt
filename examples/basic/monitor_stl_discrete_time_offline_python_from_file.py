import sys
import rtamt

def monitor():
    # data
    dataSet = {
         'time': [0, 1, 2],
         'velocity': [12.0, 11.0, 9.3],
    }

    # # stl
    spec = rtamt.StlDiscreteTimeOfflineSpecification()
    spec.name = 'STL discrete-time online Python monitor'
    spec.spec = spec.get_spec_from_file('./spec.stl')

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
