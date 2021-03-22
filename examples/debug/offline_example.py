from rtamt import STLDiscreteTimeSpecification
from rtamt import STLDenseTimeSpecification

def monitor():

    #############
    # Example 1 - No Temporal Operators & No Pastification
    #############

    phi = STLDiscreteTimeSpecification()
    tau = STLDenseTimeSpecification()

    phi.set_sampling_period(1.0, 's', 0.1)
    tau.set_sampling_period(1.0, 's', 0.1)

    phi.declare_var('x', 'float')
    tau.declare_var('x', 'float')

    spec = '(x <= 2)'

    timestamps = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    traces = [0.0, 1.0, 2.0, 1.0, 7.0, 2.0]

    print('DATA: {}\n'.format(list(zip(timestamps, traces))))

    phi.spec = spec;
    phi.parse()

    tau.spec = spec;
    tau.parse()

    # do not pastify since we are using offline monitors
    phi_rob = phi.evaluate({'time': timestamps, 'x': traces})
    tau_rob = tau.evaluate(('x', list(zip(timestamps, traces))))

    print('# Example 1 - No Temporal Operators & No Pastification:')
    print('Specification: \'(x <= 2)\'')
    print('(OFFLINE DISCRETE) Standard Robustness: {}'.format(phi_rob))
    print('(OFFLINE DENSE)    Standard Robustness: {}\n'.format(tau_rob))

    #############
    # Example 2 - With bf-Temporal Operators & Pastification
    #############

    phi = STLDiscreteTimeSpecification()
    tau = STLDenseTimeSpecification()

    phi.set_sampling_period(1.0, 's', 0.1)
    tau.set_sampling_period(1.0, 's', 0.1)

    phi.declare_var('x', 'float')
    tau.declare_var('x', 'float')

    spec = 'eventually[0,4.0](x <= 2)'

    phi.spec = spec;
    phi.parse()
    phi.pastify()

    tau.spec = spec;
    tau.parse()
    tau.pastify()

    phi_rob = phi.evaluate({'time': timestamps, 'x': traces})
    tau_rob = tau.evaluate(('x', list(zip(timestamps, traces))))

    print('# Example 2 - With bf-Temporal Operators & Pastification:')
    print('Specification: \'eventually[0,4.0](x <= 2)\'')
    print('(OFFLINE DISCRETE) Standard Robustness: {}'.format(phi_rob))
    print('(OFFLINE DENSE)    Standard Robustness: {}'.format(tau_rob))

if __name__ == '__main__':
    monitor()
