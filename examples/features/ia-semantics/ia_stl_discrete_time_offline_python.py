import sys
import rtamt

def monitor():
    # data

    dataSet = {
        'time': [0, 1, 2, 3, 4, 5],
        'x': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
        'y': [1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
    }

    # # STANDARD ROBUSTNESS
    spec = rtamt.STLSpecification(language=rtamt.Language.PYTHON, semantics=rtamt.Semantics.STANDARD)
    spec.name = 'IA-STL discrete-time online Python monitor with STANDARD semantics'
    spec.declare_var('x', 'float')
    spec.declare_var('y', 'float')
    spec.set_var_io_type('x', 'input')
    spec.set_var_io_type('y', 'output')
    spec.spec = '(x>=0.25) and (y>=1.25)'

    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(dataSet)
    print('Standard robustness: ' + str(rob))

    # # OUTPUT ROBUSTNESS
    spec = rtamt.STLSpecification(language=rtamt.Language.PYTHON, semantics=rtamt.Semantics.OUTPUT_ROBUSTNESS)
    spec.name = 'IA-STL discrete-time online Python monitor with OUTPUT ROBUSTNESS semantics'
    spec.declare_var('x', 'float')
    spec.declare_var('y', 'float')
    spec.set_var_io_type('x', 'input')
    spec.set_var_io_type('y', 'output')
    spec.spec = '(x>=0.25) or (y>=1.25)'

    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(dataSet)
    print('Output robustness: ' + str(rob))

    # # INPUT VACUITY
    spec = rtamt.STLSpecification(language=rtamt.Language.PYTHON, semantics=rtamt.Semantics.INPUT_VACUITY)
    spec.name = 'IA-STL discrete-time online Python monitor with INPUT VACUITY semantics'
    spec.declare_var('x', 'float')
    spec.declare_var('y', 'float')
    spec.set_var_io_type('x', 'input')
    spec.set_var_io_type('y', 'output')
    spec.spec = '(x>=0.25) or (y>=1.25)'

    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(dataSet)
    print('Input vacuity: ' + str(rob))

if __name__ == '__main__':
    # Process arguments

    monitor()
