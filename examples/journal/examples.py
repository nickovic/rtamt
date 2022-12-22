import rtamt

from cycler import cycler
import matplotlib.pyplot as plt

def init_plt(fontsize=12):
    # Sience+IEEE plot
    # https://github.com/garrettj403/SciencePlots/blob/master/styles/journals/ieee.mplstyle
    plt.rcParams['axes.prop_cycle'] = cycler('color', ['k', 'r', 'b', 'g']) + cycler('ls', ['-', '--', ':', '-.'])
    plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.subplot.bottom"] = 0.15

    fig = plt.figure(figsize=(6, 4))

    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.xlim([0.0, 10.0])
    plt.ylim([0.0, 7.0])
    #plt.grid(which = 'major', axis = 'y', color = 'gray', linestyle = "--", linewidth = 1)
    plt.axhline(y=1, color = 'black', linestyle = 'dotted', linewidth = 1)
    plt.axhline(y=2, color = 'black', linestyle = 'dotted', linewidth = 1)
    plt.axhline(y=3, color = 'black', linestyle = 'dashed', linewidth = 3)
    plt.axhline(y=4, color = 'black', linestyle = 'dotted', linewidth = 1)
    plt.axhline(y=5, color = 'black', linestyle = 'dotted', linewidth = 1)
    plt.axhline(y=6, color = 'black', linestyle = 'dotted', linewidth = 1)
    #plt.xlabel('Time', fontsize=fontsize)
    #plt.ylabel('Robustness', fontsize=fontsize)

    return plt

def traj2timesValues(traj):
    times  = [i[0] for i in traj]
    values = [i[1] for i in traj]
    return times, values

# params
fontsize = 20
linewidth = 3

specStr = 'G((req >=3)->(F[0,5](gnt>= 3)))'

# STL
specStl = rtamt.StlDiscreteTimeSpecification()
specStl.declare_var('req', 'float')
specStl.declare_var('gnt', 'float')
specStl.spec = specStr
specStl.parse()

# IA-STL
specIaStlIn = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.INPUT_VACUITY)
specIaStlIn.declare_var('req', 'float')
specIaStlIn.declare_var('gnt', 'float')
specIaStlIn.set_var_io_type('req', 'input')
specIaStlIn.set_var_io_type('gnt', 'output')
specIaStlIn.spec = specStr
specIaStlIn.parse()

specIaStlOut = rtamt.StlDiscreteTimeSpecification(semantics=rtamt.Semantics.OUTPUT_ROBUSTNESS)
specIaStlOut.declare_var('req', 'float')
specIaStlOut.declare_var('gnt', 'float')
specIaStlOut.set_var_io_type('req', 'input')
specIaStlOut.set_var_io_type('gnt', 'output')
specIaStlOut.spec = specStr
specIaStlOut.parse()

# (a)
dataset = {
    'time': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'req' : [0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0],
    'gnt' : [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0]
}
rob = specStl.evaluate(dataset)
robIn = specIaStlIn.evaluate(dataset)
robOut = specIaStlOut.evaluate(dataset)
print('(a) rob={}, robIn={}, robOut={}'.format(min([i[1] for i in rob]), min([i[1] for i in robIn]), min([i[1] for i in robOut])))

plt = init_plt(fontsize)
plt.step(dataset['time'], dataset['req'], where='post', linewidth=linewidth, label=r'$req$')
plt.step(dataset['time'], dataset['gnt'], where='post', linewidth=linewidth, linestyle='-.', label=r'$gnt$')

#plt.quiver(7, 3, 0, 3, angles='xy', scale_units='xy', scale=1, color='blue')
#plt.text(7.2, 4.3, "+3", fontsize=fontsize, color='blue')
#plt.legend(fontsize=fontsize, loc='upper right')
plt.savefig('example_a.pdf', bbox_inches='tight')


# (b)
dataset = {
    'time': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'req' : [0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    'gnt' : [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0]
}
rob = specStl.evaluate(dataset)
print('(b) rob={}, robIn={}, robOut={}'.format(min([i[1] for i in rob]), min([i[1] for i in robIn]), min([i[1] for i in robOut])))

plt = init_plt(fontsize)
plt.step(dataset['time'], dataset['req'], where='post', linewidth=linewidth, label=r'$req$')
plt.step(dataset['time'], dataset['gnt'], where='post', linewidth=linewidth, linestyle='-.', label=r'$gnt$')

#plt.quiver(3, 2, 0, 1, angles='xy', scale_units='xy', scale=1, color='blue')
#plt.text(3.2, 2.3, "+1", fontsize=fontsize, color='blue')
plt.legend(fontsize=fontsize, loc='upper right')
plt.savefig('example_b.pdf', bbox_inches='tight')


# (c)
dataset = {
    'time': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'req' : [0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0],
    'gnt' : [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
}
rob = specStl.evaluate(dataset)
print('(c) rob={}, robIn={}, robOut={}'.format(min([i[1] for i in rob]), min([i[1] for i in robIn]), min([i[1] for i in robOut])))

plt = init_plt(fontsize)
plt.step(dataset['time'], dataset['req'], where='post', linewidth=linewidth, label=r'$req$')
plt.step(dataset['time'], dataset['gnt'], where='post', linewidth=linewidth, linestyle='-.', label=r'$gnt$')

#plt.quiver(7, 3, 0, -2, angles='xy', scale_units='xy', scale=1, color='blue')
#plt.text(7.2, 2.3, "-2", fontsize=fontsize, color='blue')
#plt.legend(fontsize=fontsize, loc='upper right')
plt.xlabel(r'$t$', fontsize=fontsize)
plt.savefig('example_c.pdf', bbox_inches='tight')


# (d)
dataset = {
    'time': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'req' : [0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0],
    'gnt' : [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
}
rob = specStl.evaluate(dataset)
print('(d) rob={}, robIn={}, robOut={}'.format(min([i[1] for i in rob]), min([i[1] for i in robIn]), min([i[1] for i in robOut])))

plt = init_plt(fontsize)
plt.step(dataset['time'], dataset['req'], where='post', linewidth=linewidth, label=r'$req$')
plt.step(dataset['time'], dataset['gnt'], where='post', linewidth=linewidth, linestyle='-.', label=r'$gnt$')

#plt.quiver(3, 4, 0, -1, angles='xy', scale_units='xy', scale=1, color='blue')
#plt.text(3.2, 3.3, "-1", fontsize=fontsize, color='blue')
#plt.legend(fontsize=fontsize, loc='upper right')
plt.xlabel(r'$t$', fontsize=fontsize)
plt.savefig('example_d.pdf', bbox_inches='tight')


plt.show()