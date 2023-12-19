import sys
import pandas as pd
import rtamt

def monitor():
    df = pd.read_csv('simulation_data.csv')
    dataSet = df.to_dict(orient='list')

    # # stl
    spec = rtamt.StlDiscreteTimeSpecification()
    spec.spec = spec.get_spec_from_file('ttc.stl')

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
