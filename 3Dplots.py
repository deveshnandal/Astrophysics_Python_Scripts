gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-6_Maccr/P300Z0S0_ini_GeorgesTest/P002z0S0.dat',1)
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat',2)
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-4_Maccr/P300Z0S0_ini_vvx3/P002z0S0.dat',3)
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/P300Z0S0_ini_vvx3/P002z0S0.dat',4)
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-2_Maccr/P300Z0S0_ini_GeorgesTest/P002z0S0.dat',5)
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/CH_variable_accretion_law/Z0/P300Z0S0/P002z0S0.dat',6)
logL=gtb.Get_Var('L',4)
logT=gtb.Get_Var('Teff',4)
Xc=gtb.Get_Var('H1c',4)

fig,ax=plt.subplots()
ax.plot(logT,logL,color='tab:blue',linewidth=4.,label='Z0')

ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Teff')
ax.set_ylabel('[L$_{\odot}$]')
ax.invert_xaxis()
plt.show()
ax2=ax1.twinx()
ax2.plot(logT, Xc,color="blue",marker="o")
ax2.set_ticks([0.0,0.50,0.75])
ax2.set_ylabel("H1c",color="blue",fontsize=14)
plt.show()


ax.set_xscale('log')
ax.set_yscale('log')



import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/P300Z0S0_ini_vvx3/P002z0S0.dat',4)
logL=gtb.Get_Var('L',4)
logT=gtb.Get_Var('Teff',4)
Xc=gtb.Get_Var('H1c',4)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(logT, logL, Xc, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(logT, logL, Xc, c='red')
ax.invert_xaxis()
plt.show()


import matplotlib.pyplot as plt

logL=gtb.Get_Var('L',4)
logT=gtb.Get_Var('Teff',4)
Xc=gtb.Get_Var('H1c',4)

plt.plot(logT,logL, c=Xc, cmap=plt.cm.get_cmap("cool",5))
cbar = plt.colorbar(orientation="vertical", extend="both",
                   pad=0.05, shrink=1, aspect=20, format="%.3f")
cbar.set_label(label="H1c", size=15)
cbar.set_ticks([0,0.5,0.75])
cbar.set_ticklabels(["0 H1c","5 H1c","H1c"])
cbar.ax.tick_params(labelsize=15)
plt.clim(0,10)
plt.invert_xaxis()
ax.set_xlabel('Teff')
ax.set_ylabel('[L$_{\odot}$]')
plt.show()


gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/P300Z0S0_ini_vvx3/P002z0S0.dat',4)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

logL=gtb.Get_Var('L',4)
logT=gtb.Get_Var('Teff',4)
Xc=gtb.Get_Var('H1c',4)

points = np.array([logT, logL]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)


cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([0.70, 0.71, 0.72, 0.73], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(Xc)
lc.set_linewidth(2)
line = axs[1].add_collection(lc)
fig.colorbar(line, ax=axs[1])

axs[0].set_xlim(3, 6)
axs[0].set_ylim(0, 7)
plt.show()
