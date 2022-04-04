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

spec1 = rtamt.STLDiscreteTimeSpecification(semantics=rtamt.Semantics.STANDARD)
spec1.name = 'Example 1'
spec1.declare_var('req', 'float')
spec1.declare_var('gnt', 'float')
spec1.declare_var('out', 'float')
spec1.set_var_io_type('req', 'input')
spec1.set_var_io_type('gnt', 'output')
spec1.spec = 'out = ((req>=3) implies (eventually[0:5](gnt>=3)))'
try:
    spec1.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

spec2 = rtamt.STLDenseTimeSpecification(semantics=rtamt.Semantics.STANDARD)
spec2.name = 'Example 1'
spec2.declare_var('req', 'float')
spec2.declare_var('gnt', 'float')
spec2.declare_var('out', 'float')
spec2.set_var_io_type('req', 'input')
spec2.set_var_io_type('gnt', 'output')
spec2.spec = 'out = ((req>=3) implies (eventually[0:5](gnt>=3)))'
try:
    spec2.parse()
except rtamt.STLParseException as err:
    print('STL Parse Exception: {}'.format(err))
    sys.exit()

req = zip(t1, v1)
gnt = zip(t1, w1)
dataset = {'time': t1, 'req': v1, 'gnt': w1}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
print('10 done discrete')
s_t = time.time()
spec2.evaluate(['req', req], ['gnt', gnt])
e_t = time.time()
s2_times.append(e_t-s_t)
print('10 done dense')

req = zip(t2, v2)
gnt = zip(t2, w2)
dataset = {'time': t2, 'req': v2, 'gnt': w2}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
print('100 done discrete')
s_t = time.time()
spec2.evaluate(['req', req], ['gnt', gnt])
e_t = time.time()
s2_times.append(e_t-s_t)
print('100 done dense')

req = zip(t3, v3)
gnt = zip(t3, w3)
dataset = {'time': t3, 'req': v3, 'gnt': w3}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
print('1000 done discrete')
s_t = time.time()
spec2.evaluate(['req', req], ['gnt', gnt])
e_t = time.time()
s2_times.append(e_t-s_t)
print('1000 done dense')


req = zip(t4, v4)
gnt = zip(t4, w4)
dataset = {'time': t4, 'req': v4, 'gnt': w4}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
print('10000 done discrete')
s_t = time.time()
spec2.evaluate(['req', req], ['gnt', gnt])
e_t = time.time()
s2_times.append(e_t-s_t)
print('10000 done dense')

req = zip(t5, v5)
gnt = zip(t5, w5)
dataset = {'time': t5, 'req': v5, 'gnt': w5}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
print('100000 done discrete')
s_t = time.time()
spec2.evaluate(['req', req], ['gnt', gnt])
e_t = time.time()
s2_times.append(e_t-s_t)
print('100000 done dense')

req = zip(t6, v6)
gnt = zip(t6, w6)
dataset = {'time': t6, 'req': v6, 'gnt': w6}
s_t = time.time()
spec1.evaluate(dataset)
e_t = time.time()
s1_times.append(e_t-s_t)
print('1000000 done discrete')
s_t = time.time()
spec2.evaluate(['req', req], ['gnt', gnt])
e_t = time.time()
s2_times.append(e_t-s_t)
print('1000000 done dense')

# plot
fontsize = 16
fig = plt.figure()
# Sience+IEEE plot
# https://github.com/garrettj403/SciencePlots/blob/master/styles/journals/ieee.mplstyle
plt.rcParams['axes.prop_cycle'] = cycler('color', ['k', 'r']) + cycler('ls', ['-', '--'])
plt.rcParams['text.usetex'] = True
#plt.title('Offline monitors - Computation time vs. |Formula| and |Input|')
x      = [10, 100, 1000, 10000, 100000, 1000000]
locs   = [0,   500000, 1000000]
xticks = ['0', '500K', '1M']
plt.xticks(locs, xticks, fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.xlabel('\# of samples per signal', fontsize=fontsize)
plt.ylabel('Time [sec]', fontsize=fontsize)
plt.plot(x, s1_times, label='Discrete-time')
plt.plot(x, s2_times, label='Dense-time')
plt.legend(fontsize=fontsize, loc='upper left')
plt.savefig('experimentDiscreteVsDenseTime.pdf', bbox_inches='tight')

plt.show()