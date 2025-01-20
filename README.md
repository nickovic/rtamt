<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**

- [About](#about)
- [Installation](#installation)
  - [Install prerequisites for RTAMT installation](#install-prerequisites-for-rtamt-installation)
  - [Option 1: Install Python package version](#option-1-install-python-package-version)
  - [Option 2: Build the tool](#option-2-build-the-tool)
    - [Clone the repository](#clone-the-repository)
    - [Build CPP libraries](#build-cpp-libraries)
    - [Install RTAMT](#install-rtamt)
    - [uninstall RTAMT](#uninstall-rtamt)
  - [test RTAMT](#test-rtamt)
- [Theory](#theory)
  - [Specification Language](#specification-language)
- [Usage](#usage)
  - [Example Usage](#example-usage)
    - [Discrete-time online monitor](#discrete-time-online-monitor)
    - [Dense-time online monitor](#dense-time-online-monitor)
  - [Dense-time Offline Monitor](#dense-time-offline-monitor)
  - [Discrete-time Specifics](#discrete-time-specifics)
    - [Working with time units and timing assumptions](#working-with-time-units-and-timing-assumptions)
- [References](#references)

<!-- markdown-toc end -->

# About

RTAMT is a Python (2- and 3-compatible) library for monitoring of Signal Temporal Logic (STL). 
The library implements algorithms offline and online monitoring of discrete-time and dense-time STL.
The online monitors support the bounded future fragment of STL.
The online discrete-time part of the library has an optimized C++ back-end.

# Installation

## Install prerequisites for RTAMT installation

```bash
sudo apt install libboost-all-dev
sudo apt install python-dev
sudo apt install python-pip
```

If your want to extend the specification language, you may need the ANTLR4 parser generator.

```bash
sudo apt install antlr4
```

You will also need CMake version 3.12 or higher if you need to build the CPP backend.

```bash
sudo apt install cmake
```

In our experience, Ubuntu 16.04, 18.04 don't support the versions in default. You can check [our manual installation of cmake](README_cmake.md).

## Option 1: Install Python package version

We provide Python package version of RTAMT.

for Python 2

```bash
sudo pip2 install rtamt
```

for Python 3

```bash
sudo pip3 install rtamt
```

## Option 2: Build the tool

### Clone the repository

```bash
git clone https://github.com/nickovic/rtamt
```

### Build CPP libraries

This step is needed only if you want to use the CPP backend and
can be skipped if you want to use pure Python monitors.

for Python 2

```bash
cd rtamt/rtamt
mkdir build
cd build
cmake -DPythonVersion=2 ../
make
```

for Python 3

```bash
cd rtamt/rtamt
mkdir build
cd build
cmake -DPythonVersion=3 ../
make
```

### Install RTAMT

for Python 2

```bash
cd rtamt/
sudo pip2 install .
```

for Python 3

```bash
cd rtamt/
sudo pip3 install .
```

### uninstall RTAMT

for Python 2

```bash
sudo pip2 uninstall rtamt
```

for Python 3

```bash
sudo pip3 uninstall rtamt
```

## test RTAMT

for Python 2

```bash
cd rtamt/
python2 -m unittest discover tests/
```

for Python 3

```bash
cd rtamt/
python3 -m unittest discover tests/
```

# Theory

RTAMT is a Python library for offline and online monitoring of (bounded-future)  
Signal Temporal Logic (STL). The library is inspired by several theoretical and practical  
works:

- The bounded-future fragment of STL is inspired by [3]
- The interface-aware interpretation of STL quantitative semantics is inspired by [4]
- The periodic-sampling interpretation of specifications (even in presence of timestamps that are not perfectly periodic) is inspired by [5]
- The translation of bounded-future STL to "equirobust" past STL prior to the online monitoring phase is inspired by [3]

## Specification Language

RTAMT supports Signal Temporal Logic (STL) and interface-aware STL (IA-STL).

The library supports a variant of STL with past and future temporal operators as well as basic arithmetic and absolute value operators.  
Semantics of STL is defined in terms of a robustness degree `rho(phi,w,t)`, a function defined over real numbers extended with `+inf` and `-inf` that takes as input an STL specification `phi`, an input signal `w` and time index `t`, and computes how far is the signal `w` at time `t` from satisfying/violating `phi`. The robustness degree function is defined inductively as follows (`c` is a real constant, `x` is a variable, `w_x(t)` denotes the value of `w` projected to `x` at time `t`, `a,b` are rational constants such that `0 <= a <= b` and `|w|` is the length of `w`):

```txt
% Constant
rho(c,w,t) = c

% Variable
rho(x,w,t) = w_x(t)

% Absolute value, exponentials
rho(abs(phi),w,t) = |rho(phi,w,t)|
rho(exp(phi),w,t) = e**rho(phi,w,t)
rho(pow(phi1, phi2),w,t) = rho(phi1,w,t)**rho(phi2,w,t)

% Arithmetic operators
rho(phi + psi,w,t) = rho(phi,w,t) + rho(psi,w,t)
rho(phi - psi,w,t) = rho(phi,w,t) - rho(psi,w,t)
rho(phi * psi,w,t) = rho(phi,w,t) * rho(psi,w,t)
rho(phi / psi,w,t) = rho(phi,w,t) / rho(psi,w,t)

% Numeric predicates
rho(phi <= psi,w,t) = rho(psi,w,t) - rho(phi,w,t) 
rho(phi < psi,w,t) = rho(psi,w,t) - rho(phi,w,t)
rho(phi >= psi,w,t) = rho(phi,w,t) - rho(psi,w,t)
rho(phi > psi,w,t) = rho(phi,w,t) - rho(psi,w,t)
rho(phi == psi,w,t) = -|rho(phi,w,t) - rho(psi,w,t)|
rho(phi !== psi,w,t) = |rho(phi,w,t) - rho(psi,w,t)|

% Boolean operators
rho(not(phi),w,t) = -rho(phi,w,t)
rho(phi or psi,w,t) = max(rho(phi,w,t),rho(psi,w,t))
rho(phi and psi,w,t) = min(rho(phi,w,t),rho(psi,w,t))
rho(phi -> psi,w,t) = max(-rho(phi,w,t),rho(psi,w,t))
rho(phi <-> psi,w,t) = -|rho(phi,w,t) - rho(psi,w,t)|
rho(phi xor psi,w,t) = |rho(phi,w,t) - rho(psi,w,t)|

% Events
rho(rise(phi),w,t) = rho(phi,w,t)                     if t=0
                     min(-rho(phi,w,t-1),rho(phi,w,t) otherwise
rho(fall(phi),w,t) = -rho(phi,w,t)                    if t=0
                     min(rho(phi,w,t-1),-rho(phi,w,t) otherwise

% Past untimed temporal operators
rho(prev phi,w,t) = -inf            if t<=0
                    rho(phi,w,t-1) otherwise
rho(once phi,w,t) = max_{t' in [0,t]} rho(phi,w,t')
rho(historically phi,w,t) = min_{t' in [0,t]} rho(phi,w,t')
rho(phi since psi,w,t) = max_{t' in [0,t]}(min(rho(psi,w,t'), min_{t'' in (t',t]} rho(phi,w,t'')))

% Past timed temporal operators
rho(once[a,b] phi,w,t) = -inf                                                            if t-a < 0
                         max_{t' in ([0,t] intersect [t-a,t-b])} rho(phi,w,t')           otherwise
rho(historically[a,b] phi,w,t) = inf                                                     if t-a < 0
                                 min_{t' in ([0,t] intersect [t-a,t-b])} rho(phi,w,t')   otherwise
rho(phi since[a,b] psi,w,t) = -inf                                                       if t-a < 0 
                              max_{t' in ([0,t] intersect [t-a,t-b]} (min(rho(psi,w,t'), 
                              min_{t'' in (t',t]} rho(phi,w,t'')))          otherwise

% Future untimed temporal operators
rho(next phi,w,t) = rho(phi,w,t+1)
rho(eventually phi,w,t) = max_{t' in [t,|w|]} rho(phi,w,t')
rho(always phi,w,t) = min_{t' in [t, |w|]} rho(phi,w,t')
rho(phi until psi,w,t) = max_{t' in [t,|w|] min(rho(psi,w,t'), 
                              min_{t'' in [t,t')}rho(psi,w,t') rho(phi,w,t'')))         otherwise


% Future timed temporal operators
rho(eventually[a,b] phi,w,t) = -inf                                                     if t+a >= |w|
                               max_{t' in ([0,t] intersect [t+a,t+b])} rho(phi,w,t')    otherwise
rho(always[a,b] phi,w,t) = inf                                                          if t+a >= |w|
                           min_{t' in ([0,t] intersect [t+a,t+b])} rho(phi,w,t')        otherwise
rho(phi until[a,b] psi,w,t) = -inf                                                      if t+a >= |w|
                              max_{t' in ([0,t] intersect [t+a,t+b]}(min(rho(psi,w,t'), 
                              min_{t'' in [t,t')}rho(psi,w,t') rho(phi,w,t'')))         otherwise   
```

We define the robustness degree `rho(phi,w)` as `rho(phi,w,0)`.

There are several important points to note about the above syntax and semantics:

- In the online monitoring mode, the library allows only bounded-future STL specifications, meaning that _unbounded_ future operators `always` `eventually` and `until` cannot appear in the specification.  
- The `prev` and `next` operators are valid only under the discrete-time interpretation of STL
- The `unless` operator is added as syntactic sugar - `phi unless[a,b] psi = always[0,b] phi or phi until[a,b] psi

We can see from the semantics of bounded-future STL that the direct evaluation of a formula `phi` at time `t` may depend on inputs at `t'>t` that have not arrived yet.
The library monitors bounded-future STL formulas with a fixed _delay_. In order to compute `rho(phi,w,t)`, the monitor waits for all inputs required to evaluate `phi` to become available before computing the robustness degree. This delay is fixed and depends on the specification. For instance, the specification `always((req >= 3) -> eventually[0:2]always[0:3](gnt >= 3)`is evaluated with delay `5` - the time needed to capture all inputs required for evaluating bounded `eventually` and `always` operators. We refer the reader to [3] for algorithmic details regarding monitoring with delay.

# Usage

The API provides two monitoring classes:

- `StlDiscreteTimeSpecification` for discrete-time monitors
- `StlDenseTimeSpecification` for dense-time monitors

Both classes implement online and offline monitors:

- `update` method is used for online evaluation
. `evaluate` method is used for offline evaluation

## Example Usage

### Discrete-time online monitor

```python
import sys
import rtamt

def monitor():
    # # stl
    spec = rtamt.StlDiscreteTimeSpecification()
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
```

### Dense-time online monitor

```python
import sys
import rtamt

def monitor():
    a1 = [(0, 3), (3, 2)]
    b1 = [(0, 2), (2, 5), (4, 1), (7, -7)]

    a2 = [(5, 6), (6, -2), (8, 7), (11, -1)]
    b2 = [(10, 4)]

    a3 = [(13, -6), (15, 0)]
    b3 = [(15, 0)]

    # # stl
    spec = rtamt.StlDenseTimeSpecification()
    spec.name = 'STL dense-time specification'
    spec.declare_var('a', 'float')
    spec.spec = 'a>=2'
    try:
        spec.parse()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    rob = spec.update(['a', a1], ['b', b1])
    print('rob: ' + str(rob))

    rob = spec.update(['a', a2], ['b', b2])
    print('rob: ' + str(rob))

    rob = spec.update(['a', a3], ['b', b3])
    print('rob: ' + str(rob))

if __name__ == '__main__':
    monitor()
```

## Dense-time Offline Monitor

```python
import sys
import rtamt

def monitor():

    req = [[0.0, 0.0], [3.0, 6.0], [5.0, 0.0], [11.0, 0.0]]
    gnt = [[0.0, 0.0], [7.0, 6.0], [9.0, 0.0], [11.0, 0.0]]
    
    spec = rtamt.StlDenseTimeSpecification()
    spec.name = 'STL Dense-time Offline Monitor'
    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')
    spec.set_var_io_type('req', 'input')
    spec.set_var_io_type('gnt', 'output')
    spec.spec = 'out = always((req>=3) implies (eventually[0:5](gnt>=3)))'
    try:
        spec.parse()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(['req', req], ['gnt', gnt])

    print('Robustness: {}'.format(rob))

if __name__ == '__main__':
    # Process arguments
    monitor()
```

## Discrete-time Specifics

### Working with time units and timing assumptions

The default unit in RTAMT is seconds, and the default expected period between two consecutive input samples is `1s` with `10%` tolerance.  
The following program uses these default values to implicitly set up the monitor.  
The specification intuitively states that whenever the `req` is above `3`, eventually within `5s` `gnt` also goes above `3`.  
The user feeds the monitor with values timestamped _exactly_ `1s` apart from each other. It follows that the periodic sampling assumption holds.

RTAMT counts how many times the periodic sampling assumption has been violated up to the moment of being invoked via the `sampling_violation_counter` member.  
In this example, this violation obviously occurs `0` times.

```python
# examples/documentation/time_units_1.py
import sys
import rtamt

def monitor():
    spec = rtamt.StlDiscreteTimeSpecification()
    spec.name = 'Bounded-response Request-Grant'

    spec.declare_var('req', 'float')
    spec.declare_var('gnt', 'float')
    spec.declare_var('out', 'float')

    spec.spec = 'out = (req>=3) implies (eventually[0:5](gnt>=3))'

    try:
        spec.parse()
        spec.update(0, [('req', 0.1), ('gnt', 0.3)])
        spec.update(1, [('req', 0.45), ('gnt', 0.12)])
        spec.update(2, [('req', 0.78), ('gnt', 0.18)])
        nb_violations = spec.sampling_violation_counter // nb_violations = 0
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

if __name__ == '__main__':
    # Process arguments
    monitor()
}
```

The same program, but with slightly different timestamps still reports `0` number of periodic sampling assumption violations. This is because the difference between all consecutive sampling timestamps remains within the (implicitly) specified `10%` tolerance.

```python
# examples/documentation/time_units_2.py
    ...
    spec.update(0, [('req', 0.1), ('gnt', 0.3)])
    spec.update(1.02, [('req', 0.45), ('gnt', 0.12)])
    spec.update(1.98, [('req', 0.78), ('gnt', 0.18)])
    nb_violations = spec.sampling_violation_counter // nb_violations = 0
    ....
```

On the other hand, the following sequence of inputs results in `1` reported violation of periodic sampling assumption.
This is because the third input is `1.12s` away from the second sample, which is `12%` above the assumed `1s` period.

```python
# examples/documentation/time_units_3.py
    ...
    spec.update(0, [('req', 0.1), ('gnt', 0.3)])
    spec.update(1.02, [('req', 0.45), ('gnt', 0.12)])
    spec.update(2.14, [('req', 0.78), ('gnt', 0.18)])
    nb_violations = spec.sampling_violation_counter // nb_violations = 1
```

This same sequence of inputs results in `0` reported violation of periodic sampling assumption if we explicitly set the sampling period tolerance value to `20%`.  

```python
# examples/documentation/time_units_4.py
    ...
    spec.set_sampling_period(1, 's', 0.2)
    ...
    spec.update(0, [('req', 0.1), ('gnt', 0.3)])
    spec.update(1.02, [('req', 0.45), ('gnt', 0.12)])
    spec.update(2.14, [('req', 0.78), ('gnt', 0.18)])
    nb_violations = spec.sampling_violation_counter // nb_violations = 0
```

The user can also explicitly set the default unit, as well as the expected period and tolerance. In that case, the user must ensure that the timing bounds declared in the specification are divisible by the sampling period. The following specification is correct, since the sampling period is set to `500ms`, the default unit is set to seconds, and the specification implicitly defines the bound from `0.5s = 500ms` and `1.5s = 1500ms`, i.e. between `1` amd `3` sampling periods.

```python
# examples/documentation/time_units_5.py
    ...
    spec.unit = 's'
    spec.set_sampling_period(500, 'ms', 0.1)
    ...
    spec.spec = 'out = (req>=3) implies (eventually[0.5:1.5](gnt>=3))'
    ...
    spec.update(0, [('req', 0.1), ('gnt', 0.3)])
    spec.update(0.5, [('req', 0.45), ('gnt', 0.12)])
    spec.update(1, [('req', 0.78), ('gnt', 0.18)])
    nb_violations = spec.sampling_violation_counter // nb_violations = 0
}
```

The following defines the same program, but now with `ms` as the default unit.

```python
 # examples/documentation/time_units_6.py
    ...
    spec.unit = 'ms'
    spec.set_sampling_period(500, 'ms', 0.1)
    ...
    spec.spec = 'out = (req>=3) implies (eventually[500:1500](gnt>=3))'
    ...
    spec.update(0, [('req', 0.1), ('gnt', 0.3)])
    spec.update(500, [('req', 0.45), ('gnt', 0.12)])
    spec.update(1000, [('req', 0.78), ('gnt', 0.18)])
    nb_violations = spec.sampling_violation_counter // nb_violations = 0
}
```

The following program throws an exception - the temporal bound is defined between `500ms` and `1500ms`, while the sampling period equals to `1s = 1000ms`.

```python
# examples/documentation/time_units_7.py
    ...
    spec.unit = 'ms'
    spec.set_sampling_period(1, 's', 0.1)
    ...
    spec.spec = 'out = always((req>=3) implies (eventually[500:1500](gnt>=3)))'
    ...
    spec.parse()
    ...
    
}
```

Finally, the following program is correct, because the temporal bound is explicitly defined between `500s` and `1500s`, while the sampling period equals to `1s`.

```python
# examples/documentation/time_units_8.py
    ...
    spec.unit = 'ms'
    spec.set_sampling_period(1, 's', 0.1)
    ...
    spec.spec = 'out = always((req>=3) implies (eventually[500s:1500s](gnt>=3)))'
    ...
    spec.parse()
    ...
```

# References

- [1] Tomoya Yamaguchi, Bardh Hoxha, Dejan Nickovic: RTAMT - Runtime Robustness Monitors with Application to CPS and Robotics. International Journal on Software Tools for Technology Transfer, 1-21 (2023)
- [2] Dejan Nickovic, Tomoya Yamaguchi: RTAMT: Online Robustness Monitors from STL. CoRR abs/2005.11827 (2020)
- [3] Stefan Jaksic, Ezio Bartocci, Radu Grosu, Reinhard Kloibhofer, Thang Nguyen, Dejan Nickovic: From signal temporal logic to FPGA monitors. MEMOCODE 2015: 218-227
- [4] Thomas Ferrère, Dejan Nickovic, Alexandre Donzé, Hisahiro Ito, James Kapinski: Interface-aware signal temporal logic. HSCC 2019: 57-66
- [5] Thomas A. Henzinger, Zohar Manna, Amir Pnueli: What Good Are Digital Clocks? ICALP 1992: 545-558
