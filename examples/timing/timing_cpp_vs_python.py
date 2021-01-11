import sys
import time
import rtamt

def monitor():
    # data
    dataSet = {
         'a': [(0, 100.0), (1, -1.0), (2, -2.0)],
         'b': [(0, 20.0), (1, 2.0), (2, -10.0)]
    }

    for i in range(0,7):

        bound = 10**i
        bound_str = str(bound)

        spec_python = rtamt.STLDiscreteTimeSpecification(language=rtamt.Language.PYTHON)
        spec_python.name = 'PythonMonitor'
        spec_python.declare_var('a', 'float')
        spec_python.declare_var('b', 'float')
        spec_python.declare_var('c', 'float')
        spec_python.spec = 'c = always[0:' + bound_str + '](a + b >= - 2)'

        spec_cpp = rtamt.STLDiscreteTimeSpecification(language=rtamt.Language.CPP)
        spec_cpp.name = 'CPPMonitor'
        spec_cpp.declare_var('a', 'float')
        spec_cpp.declare_var('b', 'float')
        spec_cpp.declare_var('c', 'float')
        spec_cpp.spec = 'c = always[0:' + bound_str + '](a + b >= - 2)'

        try:
            spec_python.parse()
            spec_cpp.parse()
        except rtamt.STLParseException as err:
            print('STL Parse Exception: {}'.format(err))
            sys.exit()

        # # eval
        aTraj = dataSet['a']
        bTraj = dataSet['b']
        for i in range(len(dataSet['a'])):
            aData = aTraj[i]
            bData = bTraj[i]
            start_python = time.time()
            spec_python.update(aData[0], [('a', aData[1]), ('b', bData[1])])
            end_python = time.time()
            start_cpp = time.time()
            spec_cpp.update(aData[0], [('a', aData[1]), ('b', bData[1])])
            end_cpp = time.time()

            time_python = end_python - start_python
            time_cpp = end_cpp - start_cpp

            print('Bound {0} - Python time {1} - CPP time {2}'.format(bound, time_python, time_cpp))


if __name__ == '__main__':
    # Process arguments

    monitor()