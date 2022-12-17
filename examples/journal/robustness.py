import rtamt

from cycler import cycler
import control as ctrl
import matplotlib.pyplot as plt

def init_plt(fontsize=12):

    # Sience+IEEE plot
    # https://github.com/garrettj403/SciencePlots/blob/master/styles/journals/ieee.mplstyle
    plt.rcParams['axes.prop_cycle'] = cycler('color', ['k', 'r', 'b', 'g']) + cycler('ls', ['-', '--', ':', '-.'])
    plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.subplot.bottom"] = 0.15
    plt.rcParams["figure.subplot.left"] = 0.15

    fig = plt.figure(figsize=(6, 4))

    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.xlim([0.0, 0.8])
    plt.ylim([0.8, 1.4])
    #plt.grid(which = 'major', axis = 'y', color = 'gray', linestyle = "--", linewidth = 1)
    plt.axhline(y=0.8, color = 'black', linestyle = 'dotted', linewidth = 1)
    plt.axhline(y=0.9, color = 'black', linestyle = 'dotted', linewidth = 1)
    plt.axhline(y=1.0, color = 'black', linestyle = 'dotted', linewidth = 1)
    plt.axhline(y=1.1, color = 'black', linestyle = 'dashed', linewidth = 3)
    plt.axhline(y=1.2, color = 'black', linestyle = 'dotted', linewidth = 1)
    plt.axhline(y=1.3, color = 'black', linestyle = 'dotted', linewidth = 1)
    #plt.xlabel('Time', fontsize=fontsize)
    #plt.ylabel('Robustness', fontsize=fontsize)

    return plt

# params
fontsize = 20
linewidth = 3

# STL
spec = rtamt.StlDenseTimeOfflineSpecification()
spec.declare_var('f', 'float')
spec.spec = 'G(f <=1.1)'
spec.parse()


# true case
transferFunction = ctrl.tf([1.3, 42.0, 774.4, 5797, 7515],[1.629,45.74,788.4,5809,7515])
time, out = ctrl.step_response(transferFunction)
f = [[i,j] for i, j in zip(time, out)]
rob = spec.evaluate(['f', f])
print('true rob={}'.format(min([i[1] for i in rob])))

plt = init_plt(fontsize)
plt.plot(time, out)

plt.quiver(0.14, 1.1, 0, -0.048, angles='xy', scale_units='xy', scale=1, color='blue')
plt.text(0.2, 1.05, '+0.048', fontsize=fontsize, color='blue')
plt.xlabel(r'$t$', fontsize=fontsize)
plt.ylabel(r'$f(t)$', fontsize=fontsize)
plt.savefig('robustness_true.pdf', bbox_inches='tight')


# false case
transferFunction = ctrl.tf([0.05, 37.74, 774.4, 5797, 7515],[1.629,45.74,788.4,5809,7515])
time, out = ctrl.step_response(transferFunction)
f = [[i,j] for i, j in zip(time, out)]
rob = spec.evaluate(['f', f])
print('false rob={}'.format(min([i[1] for i in rob])))

plt = init_plt(fontsize)
plt.plot(time, out)

plt.quiver(0.125, 1.1, 0, 0.198, angles='xy', scale_units='xy', scale=1, color='blue')
plt.text(0.2, 1.15, '-0.198', fontsize=fontsize, color='blue')
plt.xlabel(r'$t$', fontsize=fontsize)
plt.savefig('robustness_false.pdf', bbox_inches='tight')


plt.show()