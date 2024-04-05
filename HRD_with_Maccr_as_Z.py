from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

L = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',skip_header=0))[3])
T = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',skip_header=0))[4])
M_dot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',skip_header=0))[116])

fig,ax=plt.subplots()
ax.plot(T,L,linewidth=2., label="H2")
ax.set_xlabel('$log(Teff)$',fontsize=12)
ax.set_ylabel('$log(L/L_{\odot}$)',fontsize=12)


leg = plt.legend(loc='lower left', shadow=True,prop={'size': 9})

ax.set_xscale('log')
ax.set_yscale('log')
ax.invert_xaxis()
plt.show()


##########################



from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

L = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',skip_header=0))[3])
T = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',skip_header=0))[4])
M_dot = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.dat',skip_header=0))[116])
# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points = np.array([T, L]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
#norm = plt.Normalize(M_dot.min(), M_dot.max())
#lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
#lc.set_array(M_dot)
#lc.set_linewidth(2.)
#line = axs[0].add_collection(lc)
#fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
cmap = ListedColormap(['r', 'g', 'b', 'y', "cyan", "gold", 'm', 'w', 'k'])
norm = BoundaryNorm([0, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1.e-1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(M_dot)
lc.set_linewidth(2)
line = axs.add_collection(lc)
fig.colorbar(line, ax=axs)

axs.set_xlim(3.6, 5.2)
axs.set_ylim(2, 7.8)
axs.set_xlabel('$log(Teff)$',fontsize=12)
axs.set_ylabel('$log(L/L_{\odot}$)',fontsize=12)
axs.invert_xaxis()
plt.show()






cp ~/Observatory/Starcalc/TutorialCalc/M015Z14V0.4/M015Z14V0.4.v0002341 ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
cp ~/Observatory/Starcalc/Rotation_prescription/M015Z14V0.4Im0Cod12/M015Z14V0.4Im0Cod12.v0002011 ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
cp ~/Observatory/Starcalc/Rotation_prescription/M015Z14V0.4Im0Cod12/M015Z14V0.4Im0Cod12.v0002011.gz ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
cp ~/Observatory/Starcalc/Rotation_prescription/M015Z14V0.4Im0Cod21/M015Z14V0.4Im0Cod21.v0002341.gz ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
cp ~/Observatory/Starcalc/Rotation_prescription/M015Z14V0.4Im0Cod22/M015Z14V0.4Im0Cod22.v0002011.gz ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
cp ~/Observatory/Starcalc/MS_Mag/P015Z14S0.4/P015Z14S0.4.v0002211 ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
cp ~/Observatory/Starcalc/Rotation_prescription/Maeder_Prescriptions/M015Z14V0.4Coef13/M015Z14V0.4Coef13.v0001941.gz ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
cp ~/Observatory/Starcalc/Rotation_prescription/Maeder_Prescriptions/M015Z14V0.4Coef23/M015Z14V0.4Coef23.v0001941.gz ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
cp ~/Observatory/Starcalc/Rotation_prescription/Maeder_Prescriptions/M015Z14V0.4Coef23/M015Z14V0.4Coef23.v0001941 ~/Observatory/Starcalc/Rotation_prescription/ABCDEF_vfiles_halfHburning/
