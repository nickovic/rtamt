import rtamt
import sys
import random
import time
from cycler import cycler
import matplotlib.pyplot as plt


t = list(range(10000))

v = [random.random() for i in range(10000)]
w = [random.random() for i in range(10000)]


s1_times = []
s2_times = []


spec1 = rtamt.StlDiscreteTimeOnlineSpecification()
spec1.name = 'Example 1'
spec1.declare_var('req', 'float')
spec1.declare_var('gnt', 'float')
spec1.declare_var('out', 'float')
spec1.set_var_io_type('req', 'input')
spec1.set_var_io_type('gnt', 'output')
spec1.spec = 'out = ((req>=3) implies (once[0:10](gnt>=3)))'
try:
    spec1.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec2 = rtamt.StlDiscreteTimeOnlineSpecification()
spec2.name = 'Example 1'
spec2.declare_var('req', 'float')
spec2.declare_var('gnt', 'float')
spec2.declare_var('out', 'float')
spec2.set_var_io_type('req', 'input')
spec2.set_var_io_type('gnt', 'output')
spec2.spec = 'out = ((req>=3) implies (once[0:100](gnt>=3)))'
try:
    spec2.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec3 = rtamt.StlDiscreteTimeOnlineSpecification()
spec3.name = 'Example 1'
spec3.declare_var('req', 'float')
spec3.declare_var('gnt', 'float')
spec3.declare_var('out', 'float')
spec3.set_var_io_type('req', 'input')
spec3.set_var_io_type('gnt', 'output')
spec3.spec = 'out = ((req>=3) implies (once[0:1000](gnt>=3)))'
try:
    spec3.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec4 = rtamt.StlDiscreteTimeOnlineSpecification()
spec4.name = 'Example 1'
spec4.declare_var('req', 'float')
spec4.declare_var('gnt', 'float')
spec4.declare_var('out', 'float')
spec4.set_var_io_type('req', 'input')
spec4.set_var_io_type('gnt', 'output')
spec4.spec = 'out = ((req>=3) implies (once[0:10000](gnt>=3)))'
try:
    spec4.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

s_t = time.time()
[spec1.update(i, [['req', v[i]], ['gnt', w[i]]]) for i in t]
e_t = time.time()
s1_times.append(e_t-s_t)

s_t = time.time()
[spec2.update(i, [['req', v[i]], ['gnt', w[i]]]) for i in t]
e_t = time.time()
s1_times.append(e_t-s_t)

s_t = time.time()
[spec3.update(i, [['req', v[i]], ['gnt', w[i]]]) for i in t]
e_t = time.time()
s1_times.append(e_t-s_t)

s_t = time.time()
[spec4.update(i, [['req', v[i]], ['gnt', w[i]]]) for i in t]
e_t = time.time()
s1_times.append(e_t-s_t)

spec1 = rtamt.StlDiscreteTimeOnlineSpecificationCpp()
spec1.name = 'Example 1'
spec1.declare_var('req', 'float')
spec1.declare_var('gnt', 'float')
spec1.declare_var('out', 'float')
spec1.set_var_io_type('req', 'input')
spec1.set_var_io_type('gnt', 'output')
spec1.spec = 'out = ((req>=3) implies (once[0:10](gnt>=3)))'
try:
    spec1.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec2 = rtamt.StlDiscreteTimeOnlineSpecificationCpp()
spec2.name = 'Example 1'
spec2.declare_var('req', 'float')
spec2.declare_var('gnt', 'float')
spec2.declare_var('out', 'float')
spec2.set_var_io_type('req', 'input')
spec2.set_var_io_type('gnt', 'output')
spec2.spec = 'out = ((req>=3) implies (once[0:100](gnt>=3)))'
try:
    spec2.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec3 = rtamt.StlDiscreteTimeOnlineSpecificationCpp()
spec3.name = 'Example 1'
spec3.declare_var('req', 'float')
spec3.declare_var('gnt', 'float')
spec3.declare_var('out', 'float')
spec3.set_var_io_type('req', 'input')
spec3.set_var_io_type('gnt', 'output')
spec3.spec = 'out = ((req>=3) implies (once[0:1000](gnt>=3)))'
try:
    spec3.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec4 = rtamt.StlDiscreteTimeOnlineSpecificationCpp()
spec4.name = 'Example 1'
spec4.declare_var('req', 'float')
spec4.declare_var('gnt', 'float')
spec4.declare_var('out', 'float')
spec4.set_var_io_type('req', 'input')
spec4.set_var_io_type('gnt', 'output')
spec4.spec = 'out = ((req>=3) implies (once[0:10000](gnt>=3)))'
try:
    spec4.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

s_t = time.time()
[spec1.update(i, [['req', v[i]], ['gnt', w[i]]]) for i in t]
e_t = time.time()
s2_times.append(e_t-s_t)

s_t = time.time()
[spec2.update(i, [['req', v[i]], ['gnt', w[i]]]) for i in t]
e_t = time.time()
s2_times.append(e_t-s_t)

s_t = time.time()
[spec3.update(i, [['req', v[i]], ['gnt', w[i]]]) for i in t]
e_t = time.time()
s2_times.append(e_t-s_t)

s_t = time.time()
[spec4.update(i, [['req', v[i]], ['gnt', w[i]]]) for i in t]
e_t = time.time()
s2_times.append(e_t-s_t)


# plot
fontsize = 16
fig = plt.figure()
# Sience+IEEE plot
# https://github.com/garrettj403/SciencePlots/blob/master/styles/journals/ieee.mplstyle
plt.rcParams['axes.prop_cycle'] = cycler('color', ['k', 'r', 'b', 'g']) + cycler('ls', ['-', '--', ':', '-.'])
plt.rcParams['text.usetex'] = True
#plt.title('Online monitors - Python vs. C++')
x      = [10, 100, 1000, 10000]
locs   = [0,   5000, 10000]
xticks = ['0', '5K', '10K']
plt.xticks(locs, xticks, fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.xlabel('Upper bound in the temporal modality', fontsize=fontsize)
plt.ylabel('Time [sec]', fontsize=fontsize)
plt.plot(x, s1_times, label='Python')
plt.plot(x, s2_times, label='C++')
plt.legend(fontsize=fontsize, loc='upper left')
plt.savefig('experimentPythonCpp.pdf', bbox_inches='tight')

plt.show()