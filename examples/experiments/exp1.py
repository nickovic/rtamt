import rtamt
import sys
import random
import time
from cycler import cycler
import matplotlib.pyplot as plt

t1 = list(range(10))
t2 = list(range(100))
t3 = list(range(1000))
t4 = list(range(10000))
t5 = list(range(100000))
t6 = list(range(1000000))

v1 = [random.random() for i in range(10)]
v2 = [random.random() for i in range(100)]
v3 = [random.random() for i in range(1000)]
v4 = [random.random() for i in range(10000)]
v5 = [random.random() for i in range(100000)]
v6 = [random.random() for i in range(1000000)]

w1 = [random.random() for i in range(10)]
w2 = [random.random() for i in range(100)]
w3 = [random.random() for i in range(1000)]
w4 = [random.random() for i in range(10000)]
w5 = [random.random() for i in range(100000)]
w6 = [random.random() for i in range(1000000)]

m1 = [[i, random.random()] for i in range(10)]
m2 = [[i, random.random()] for i in range(100)]
m3 = [[i, random.random()] for i in range(1000)]
m4 = [[i, random.random()] for i in range(10000)]
m5 = [[i, random.random()] for i in range(100000)]
m6 = [[i, random.random()] for i in range(1000000)]

n1 = [[i, random.random()] for i in range(10)]
n2 = [[i, random.random()] for i in range(100)]
n3 = [[i, random.random()] for i in range(1000)]
n4 = [[i, random.random()] for i in range(10000)]
n5 = [[i, random.random()] for i in range(100000)]
n6 = [[i, random.random()] for i in range(1000000)]

s1_times = []
s2_times = []
s3_times = []
s4_times = []


spec1 = rtamt.STLDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
spec1.name = 'Example 1'
spec1.declare_var('req', 'float')
spec1.declare_var('gnt', 'float')
spec1.declare_var('out', 'float')
spec1.set_var_io_type('req', 'input')
spec1.set_var_io_type('gnt', 'output')
spec1.spec = 'out = (req>=3)'
try:
    spec1.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec2 = rtamt.STLDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
spec2.name = 'Example 1'
spec2.declare_var('req', 'float')
spec2.declare_var('gnt', 'float')
spec2.declare_var('out', 'float')
spec2.set_var_io_type('req', 'input')
spec2.set_var_io_type('gnt', 'output')
spec2.spec = 'out = ((req>=3) implies (gnt>=3))'
try:
    spec2.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec3 = rtamt.STLDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
spec3.name = 'Example 1'
spec3.declare_var('req', 'float')
spec3.declare_var('gnt', 'float')
spec3.declare_var('out', 'float')
spec3.set_var_io_type('req', 'input')
spec3.set_var_io_type('gnt', 'output')
spec3.spec = 'out = ((req>=3) implies (eventually[0:5](gnt>=3)))'
try:
    spec3.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec4 = rtamt.STLDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
spec4.name = 'Example 1'
spec4.declare_var('req', 'float')
spec4.declare_var('gnt', 'float')
spec4.declare_var('out', 'float')
spec4.set_var_io_type('req', 'input')
spec4.set_var_io_type('gnt', 'output')
spec4.spec = 'out = ((H(req>=3)) implies ((not (req>=3))until[0:5](gnt>=3)))'
try:
    spec4.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

dataset = {'time': t1, 'req': v1, 'gnt': w1}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
s_t = time.time()
spec2.evaluate(dataset)
e_t = time.time()
s2_times.append(e_t-s_t)
s_t = time.time()
spec3.evaluate(dataset)
e_t = time.time()
s3_times.append(e_t-s_t)
s_t = time.time()
spec4.evaluate(dataset)
e_t = time.time()
s4_times.append(e_t-s_t)

dataset = {'time': t2, 'req': v2, 'gnt': w2}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
s_t = time.time()
spec2.evaluate(dataset)
e_t = time.time()
s2_times.append(e_t-s_t)
s_t = time.time()
spec3.evaluate(dataset)
e_t = time.time()
s3_times.append(e_t-s_t)
s_t = time.time()
spec4.evaluate(dataset)
e_t = time.time()
s4_times.append(e_t-s_t)

dataset = {'time': t3, 'req': v3, 'gnt': w3}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
s_t = time.time()
spec2.evaluate(dataset)
e_t = time.time()
s2_times.append(e_t-s_t)
s_t = time.time()
spec3.evaluate(dataset)
e_t = time.time()
s3_times.append(e_t-s_t)
s_t = time.time()
spec4.evaluate(dataset)
e_t = time.time()
s4_times.append(e_t-s_t)

dataset = {'time': t4, 'req': v4, 'gnt': w4}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
s_t = time.time()
spec2.evaluate(dataset)
e_t = time.time()
s2_times.append(e_t-s_t)
s_t = time.time()
spec3.evaluate(dataset)
e_t = time.time()
s3_times.append(e_t-s_t)
s_t = time.time()
spec4.evaluate(dataset)
e_t = time.time()
s4_times.append(e_t-s_t)

dataset = {'time': t5, 'req': v5, 'gnt': w5}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
s_t = time.time()
spec2.evaluate(dataset)
e_t = time.time()
s2_times.append(e_t-s_t)
s_t = time.time()
spec3.evaluate(dataset)
e_t = time.time()
s3_times.append(e_t-s_t)
s_t = time.time()
spec4.evaluate(dataset)
e_t = time.time()
s4_times.append(e_t-s_t)

dataset = {'time': t6, 'req': v6, 'gnt': w6}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
s_t = time.time()
spec2.evaluate(dataset)
e_t = time.time()
s2_times.append(e_t-s_t)
s_t = time.time()
spec3.evaluate(dataset)
e_t = time.time()
s3_times.append(e_t-s_t)
s_t = time.time()
spec4.evaluate(dataset)
e_t = time.time()
s4_times.append(e_t-s_t)


# plot
fontsize = 16
fig = plt.figure()
# Sience+IEEE plot
# https://github.com/garrettj403/SciencePlots/blob/master/styles/journals/ieee.mplstyle
plt.rcParams['axes.prop_cycle'] = cycler('color', ['k', 'r', 'b', 'g']) + cycler('ls', ['-', '--', ':', '-.'])
plt.rcParams['text.usetex'] = True
#plt.title('Offline monitors - Computation time vs. |Formula| and |Input|')
x      = [10,   100,   1000, 10000, 100000, 1000000]
locs   = [0,   500000, 1000000]
xticks = ['0', '500K', '1M']
plt.xticks(locs, xticks, fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.xlabel('\# of samples per signal', fontsize=fontsize)
plt.ylabel('Time [s]', fontsize=fontsize)
plt.plot(x, s1_times, label=r'$\varphi_1$')
plt.plot(x, s2_times, label=r'$\varphi_2$')
plt.plot(x, s3_times, label=r'$\varphi_3$')
plt.plot(x, s4_times, label=r'$\varphi_4$')
plt.legend(fontsize=fontsize, loc='upper left')
plt.savefig('exp1.pdf', bbox_inches='tight')

plt.show()