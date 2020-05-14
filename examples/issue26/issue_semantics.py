import numpy as np
import matplotlib.pyplot as plt
import sys
import mtl
import rtamt
import pickle

from webotPyLib import *
import scenarioParams


dataPHF = []
with open('dataProhibitHardFail.binaryfile', 'rb') as web:
    dataPHF = pickle.load(web)


fig = plt.figure(figsize=(6.4, 6.4))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.set_ylabel('input')
ax1.set_xlabel('Time [sec]')
ax1.hlines(y=0, xmin=0, xmax=35, color="green", linestyles='dotted', label='Threshold')
ax2.set_ylabel('always(input>0.0)')
ax2.set_xlabel('Time [sec]')
ax2.hlines(y=0, xmin=0, xmax=35, color="green", linestyles='dotted', label='Threshold')

#data
disttegopa1 = distTraj2Po(scenarioParams.prohibitArea1, dataPHF["tegoodox"], dataPHF["tegoodoy"])
tdata = {'disttegopa1': disttegopa1}
time,x = dicTraj2tx(tdata, 'disttegopa1')
ax1.plot(time, x, linestyle='solid', color='black', label='input')
ax1.legend()

#rtamt
spec = rtamt.STLIOCTSpecification(1)
spec.name = 'Prohibit Area'
spec.declare_var('disttegopa1', 'float')
spec.declare_var('out', 'float')
spec.set_var_io_type('disttegopa1', 'input')
spec.set_var_io_type('out', 'output')
#spec.spec = 'out=always((disttegopa1<0.0) implies eventually[0:5](disttegopa1>0.0))'
spec.spec = 'out=always(disttegopa1>0.0)'
spec.iosem = 'standard'
spec.parse()

rob = spec.offline(['disttegopa1', tdata['disttegopa1']])
#print('output robustness: {}'.format(rob))
time = np.asarray([i[0] for i in rob])
x = np.asarray([i[1] for i in rob])
ax2.plot(time, x, linestyle='solid', color='blue', label='rtamt offline')

#mtl
#spec = mtl.parse('(G(disttegopa1)->F[0,5](~disttegopa1))')
spec = mtl.parse('G(disttegopa1)')
rob = spec(tdata,time=None)
time = np.asarray([i[0] for i in rob])
x = np.asarray([i[1] for i in rob])
ax2.plot(time, x, linestyle='solid', color='red', label='stl')
ax2.legend()

plt.show()
