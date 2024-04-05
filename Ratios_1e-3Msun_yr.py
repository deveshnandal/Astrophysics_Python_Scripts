############## End H burning
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

H1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132021.gz', skip_header=310))[6])[:-168][::-1]
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132021.gz', skip_header=310))[8])[:-168][::-1]
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132021.gz', skip_header=310))[33])[:-168][::-1]
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132021.gz', skip_header=310))[9])[:-168][::-1]
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132021.gz', skip_header=310))[37])[:-168][::-1]
M_sol = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132021.gz', skip_header=310))[49])[:-168][::-1]

dM = np.diff(M_sol)
m_H1 = np.sum(H1[:-1] * dM)
m_N14 = np.sum(N14[:-1] * dM)
m_C12 = np.sum(C12[:-1] * dM)
m_O16 = np.sum(O16[:-1] * dM)
m_ejecta = 1155
H_1 = m_H1 / m_ejecta
N_14 = m_N14 / m_ejecta
C_12 = m_C12 / m_ejecta
O_16 = m_O16 / m_ejecta
N_O =np.log10(N_14/O_16)-np.log10(14.0/16.0)
# H_1 = 0.4299360272354493
# C_12: 4.469364315317495e-10
# X_14: 3.856766402748824e-08
# O_16: 3.639178455800738e-10






############## End He burning
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

H1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170171.gz', skip_header=303))[6])[:-84][::-1]
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170171.gz', skip_header=303))[8])[:-84][::-1]
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170171.gz', skip_header=303))[33])[:-84][::-1]
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170171.gz', skip_header=303))[9])[:-84][::-1]
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170171.gz', skip_header=303))[37])[:-84][::-1]
M_sol = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170171.gz', skip_header=303))[49])[:-84][::-1]

dM = np.diff(M_sol)
m_H1 = np.sum(H1[:-1] * dM)
m_N14 = np.sum(N14[:-1] * dM)
m_C12 = np.sum(C12[:-1] * dM)
m_O16 = np.sum(O16[:-1] * dM)
m_ejecta = 2389
H_1 = m_H1 / m_ejecta
N_14 = m_N14 / m_ejecta
C_12 = m_C12 / m_ejecta
O_16 = m_O16 / m_ejecta
N_O =np.log10(N_14/O_16)-np.log10(14.0/16.0)

# H_1: 0.15702370621913103
# C_12: 0.0016015797837727955
# X_14: 0.03935998050758991
# O_16: 0.013096728471841576

############## End C burning
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

H1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170821.gz', skip_header=293))[6])[:-93][::-1]
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170821.gz', skip_header=293))[8])[:-93][::-1]
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170821.gz', skip_header=293))[33])[:-93][::-1]
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170821.gz', skip_header=293))[9])[:-93][::-1]
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170821.gz', skip_header=293))[37])[:-93][::-1]
M_sol = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170821.gz', skip_header=293))[49])[:-93][::-1]

dM = np.diff(M_sol)
m_H1 = np.sum(H1[:-1] * dM)
m_N14 = np.sum(N14[:-1] * dM)
m_C12 = np.sum(C12[:-1] * dM)
m_O16 = np.sum(O16[:-1] * dM)
m_ejecta = 2390
H_1 = m_H1 / m_ejecta
N_14 = m_N14 / m_ejecta
C_12 = m_C12 / m_ejecta
O_16 = m_O16 / m_ejecta
N_O =np.log10(N_14/O_16)-np.log10(14.0/16.0)

# H_1: 0.15723355788732593
# C_12: 0.0008876894528087792
# X_14: 0.03335029462729917
# O_16: 0.012219979636523664

############# End Si burning
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
m_H1 = np.sum(H1[:-1] * dM)
m_N14 = np.sum(N14[:-1] * dM)
m_C12 = np.sum(C12[:-1] * dM)
m_O16 = np.sum(O16[:-1] * dM)
m_ejecta = 2390
H_1 = m_H1 / m_ejecta
N_14 = m_N14 / m_ejecta
C_12 = m_C12 / m_ejecta
O_16 = m_O16 / m_ejecta
N_O =np.log10(N_14/O_16)-np.log10(14.0/16.0)

# H_1: 0.157233549029559
# C_12: 0.0008876905469380879
# N_14: 0.033350617239823854
# O_16: 0.01222004183702273

fig, ax = plt.subplots()

ax.plot(M_sol[:-1],logNO_list,linewidth=2.0, color='black',linestyle='solid',label="N/O")
ax.plot(M_sol[:-1],logCO_list,linewidth=2.0, color='Magenta',linestyle='solid',label="C/O")
ax.plot(M_sol[:-1],logOH_list,linewidth=2.0, color='Orange',linestyle='solid',label="O/H")
ax.plot(M_sol[:-1],logNeO_list,linewidth=2.0, color='Cyan',linestyle='solid',label="Ne/O")
ax.axvline(x=659, color='grey', linestyle='-.', alpha=0.5)
ax.text(659, -0.4, 'CO core', color='Grey', rotation=270, verticalalignment='center', horizontalalignment='left', fontsize=20)
ax.set_title('$M_{final} = 3000 M_{\odot}$', fontsize=22)

ax.set_xlabel('M$_{\mathrm{r}}[M_{\odot}]$', fontsize=20)
ax.set_ylabel('Abundance ratios [log$_{10}$]', fontsize=20)
leg = plt.legend(loc='lower left', shadow=True, prop={'size': 18})
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)

fig.set_size_inches(8, 8)
fig.tight_layout()
plt.show()
