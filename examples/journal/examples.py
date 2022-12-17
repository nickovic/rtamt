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

# STL
spec = rtamt.StlDenseTimeOfflineSpecification()
spec.declare_var('req', 'float')
spec.declare_var('gnt', 'float')
spec.spec = 'G((req >=3)->(F[0,5](gnt>= 3)))'
spec.parse()

# (a)
req = [[0.0, 0.0], [2.0, 6.0], [4.0, 0.0], [10.0, 0.0]]
gnt = [[0.0, 0.0], [6.0, 6.0], [8.0, 0.0], [10.0, 0.0]]
rob = spec.evaluate(['req', req], ['gnt', gnt])
print('(a) rob={}'.format(min([i[1] for i in rob])))

plt = init_plt(fontsize)

times, values = traj2timesValues(req)
plt.step(times, values, where='post', linewidth=linewidth, label=r'$req$')

times, values = traj2timesValues(gnt)
plt.step(times, values, where='post', linewidth=linewidth, linestyle='-.', label=r'$gnt$')

#plt.quiver(7, 3, 0, 3, angles='xy', scale_units='xy', scale=1, color='blue')
#plt.text(7.2, 4.3, "+3", fontsize=fontsize, color='blue')
#plt.legend(fontsize=fontsize, loc='upper right')
plt.savefig('example_a.pdf', bbox_inches='tight')


# (b)
req = [[0.0, 0.0], [2.0, 2.0], [4.0, 0.0], [10.0, 0.0]]
gnt = [[0.0, 0.0], [6.0, 2.0], [8.0, 0.0], [10.0, 0.0]]
rob = spec.evaluate(['req', req], ['gnt', gnt])
print('(b) rob={}'.format(min([i[1] for i in rob])))

plt = init_plt(fontsize)

times, values = traj2timesValues(req)
plt.step(times, values, where='post', linewidth=linewidth, label=r'$req$')

times, values = traj2timesValues(gnt)
plt.step(times, values, where='post', linewidth=linewidth, linestyle='-.', label=r'$gnt$')

#plt.quiver(3, 2, 0, 1, angles='xy', scale_units='xy', scale=1, color='blue')
#plt.text(3.2, 2.3, "+1", fontsize=fontsize, color='blue')
plt.legend(fontsize=fontsize, loc='upper right')
plt.savefig('example_b.pdf', bbox_inches='tight')


# (c)
req = [[0.0, 0.0], [2.0, 6.0], [4.0, 0.0], [10.0, 0.0]]
gnt = [[0.0, 0.0], [6.0, 1.0], [8.0, 0.0], [10.0, 0.0]]
rob = spec.evaluate(['req', req], ['gnt', gnt])
print('(c) rob={}'.format(min([i[1] for i in rob])))

plt = init_plt(fontsize)

times, values = traj2timesValues(req)
plt.step(times, values, where='post', linewidth=linewidth, label=r'$req$')

times, values = traj2timesValues(gnt)
plt.step(times, values, where='post', linewidth=linewidth, linestyle='-.', label=r'$gnt$')

#plt.quiver(7, 3, 0, -2, angles='xy', scale_units='xy', scale=1, color='blue')
#plt.text(7.2, 2.3, "-2", fontsize=fontsize, color='blue')
#plt.legend(fontsize=fontsize, loc='upper right')
plt.xlabel(r'$t$', fontsize=fontsize)
plt.savefig('example_c.pdf', bbox_inches='tight')


# (d)
req = [[0.0, 0.0], [2.0, 4.0], [4.0, 0.0], [10.0, 0.0]]
gnt = [[0.0, 0.0], [6.0, 1.0], [8.0, 0.0], [10.0, 0.0]]
rob = spec.evaluate(['req', req], ['gnt', gnt])
print('(d) rob={}'.format(min([i[1] for i in rob])))

plt = init_plt(fontsize)

times, values = traj2timesValues(req)
plt.step(times, values, where='post', linewidth=linewidth, label=r'$req$')

times, values = traj2timesValues(gnt)
plt.step(times, values, where='post', linewidth=linewidth, linestyle='-.', label=r'$gnt$')

#plt.quiver(3, 4, 0, -1, angles='xy', scale_units='xy', scale=1, color='blue')
#plt.text(3.2, 3.3, "-1", fontsize=fontsize, color='blue')
#plt.legend(fontsize=fontsize, loc='upper right')
plt.xlabel(r'$t$', fontsize=fontsize)
plt.savefig('example_d.pdf', bbox_inches='tight')


plt.show()