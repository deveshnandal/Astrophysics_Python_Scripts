import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

H1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', skip_header=3))[6])[:-95][::-1]
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', skip_header=3))[8])[:-95][::-1]
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', skip_header=3))[33])[:-95][::-1]
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', skip_header=3))[9])[:-95][::-1]
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', skip_header=3))[37])[:-95][::-1]
M_sol = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', skip_header=3))[49])[:-95][::-1]

dM = np.diff(M_sol)

logNO_list = []
logCO_list = []
logOH_list = []
logNeO_list = []
C12_list = []
N14_list = []
O16_list = []
for i in range(len(dM)):
    H1_sum = np.sum(H1[i:-1]*dM[i:])
    C12_sum = np.sum(C12[i:-1]*dM[i:])
    N14_sum = np.sum(N14[i:-1]*dM[i:])
    O16_sum = np.sum(O16[i:-1]*dM[i:])
    Ne20_sum = np.sum(Ne20[i:-1]*dM[i:])
    N_O = np.log10(N14_sum/O16_sum)-np.log10(14.0/16)
    C_O = np.log10(C12_sum/O16_sum)-np.log10(12.0/16)
    O_H = np.log10(O16_sum/H1_sum)-np.log10(16.0/1.0)
    Ne_O = np.log10(Ne20_sum/O16_sum)-np.log10(20.0/16.0)
    logNO_list.append(N_O)
    logCO_list.append(C_O)
    logOH_list.append(O_H)
    logNeO_list.append(Ne_O)
    N14_list.append(N14_sum)
    C12_list.append(C12_sum)
    O16_list.append(O16_sum)

fig, ax = plt.subplots()

# ax.plot(M_sol[:-1],logNO_list,linewidth=2.0, color='black',linestyle='solid',label="N/O")
# ax.plot(M_sol[:-1],logCO_list,linewidth=2.0, color='Magenta',linestyle='solid',label="C/O")
# ax.plot(M_sol[:-1],logOH_list,linewidth=2.0, color='Orange',linestyle='solid',label="O/H")
# ax.plot(M_sol[:-1],logNeO_list,linewidth=2.0, color='Cyan',linestyle='solid',label="Ne/O")
ax.plot(M_sol[:-1],N14_list,linewidth=2.0, color='black',linestyle='solid',label="N14 integrated")
ax.plot(M_sol[:-1],C12_list,linewidth=2.0, color='Magenta',linestyle='solid',label="C12 integrated")
ax.plot(M_sol[:-1],O16_list,linewidth=2.0, color='Orange',linestyle='solid',label="O16 integrated")
ax.axvline(x=659, color='grey', linestyle='-.', alpha=0.5)
ax.text(659, -0.4, 'CO core', color='Grey', rotation=270, verticalalignment='center', horizontalalignment='left', fontsize=20)
ax.set_title('$M_{final} = 3000 M_{\odot}$', fontsize=22)

ax.set_xlabel('M$_{\mathrm{r}}[M_{\odot}]$', fontsize=20)
ax.set_ylabel('Abundance ratios [log$_{10}$]', fontsize=20)
leg = plt.legend(loc='upper right', shadow=True, prop={'size': 18})
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)

fig.set_size_inches(8, 8)
fig.tight_layout()
plt.show()
