import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

H1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201', skip_header=3))[6])[:-95][::-1]
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201', skip_header=3))[8])[:-95][::-1]
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201', skip_header=3))[33])[:-95][::-1]
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201', skip_header=3))[9])[:-95][::-1]
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201', skip_header=3))[37])[:-95][::-1]
M_sol = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201', skip_header=3))[49])[:-95][::-1]

dM = np.diff(M_sol)

H1 = H1[:-1]
C12 = C12[:-1]
N14 = N14[:-1]
O16 = O16[:-1]
Ne20 = Ne20[:-1]

H1_sum = np.sum(H1*dM)
C12_sum = np.sum(C12*dM)
N14_sum = np.sum(N14*dM)
O16_sum = np.sum(O16*dM)
Ne20_sum = np.sum(Ne20*dM)
N_O = np.log10(N14_sum/O16_sum)-np.log10(14.0/16)
C_O = np.log10(C12_sum/O16_sum)-np.log10(12.0/16)
O_H = np.log10(O16_sum/H1_sum)-np.log10(16.0/1.0)
Ne_O = np.log10(Ne20_sum/O16_sum)-np.log10(20.0/16.0)

fig, ax = plt.subplots()

ax.scatter(O_H+12.0, N_O, color='black', label="N/O")
ax.scatter(O_H+12.0, C_O, color='Magenta', label="C/O")
ax.scatter(O_H+12.0, Ne_O, color='Cyan', label="Ne/O")

ax.set_xlabel('log (O/H) + 12', fontsize=20)
ax.set_ylabel('Abundance ratios [log$_{10}$]', fontsize=20)
leg = plt.legend(loc='lower left', shadow=True, prop={'size': 18})
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)

fig.set_size_inches(8, 8)
fig.tight_layout()
plt.show()
