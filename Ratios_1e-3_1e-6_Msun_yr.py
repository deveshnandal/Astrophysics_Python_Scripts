# log N/O versus log (O/H)+12 plot for 1e-3Msun_yr_1e-6 model at the end of core Helium burning.


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

H1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[6])[:-95][::-1]
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[8])[:-95][::-1]
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[33])[:-95][::-1]
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[9])[:-95][::-1]
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[37])[:-95][::-1]
M_sol = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[49])[:-95][::-1]
N_ini = 4.705414495276072e-08
O_ini = 4.084625123020800e-07
C_ini = 1.630823182090076e-07
H_ini = 7.515977428571429e-01
m_ejecta = 2640
f = 1.0

dM = np.diff(M_sol)
X_H1 = np.sum(H1[:-1] * dM)/ m_ejecta
X_N14 = np.sum(N14[:-1] * dM) / m_ejecta
X_C12 = np.sum(C12[:-1] * dM) / m_ejecta
X_O16 = np.sum(O16[:-1] * dM) / m_ejecta

log_NO_num = ((X_N14 + (N_ini*f))*16.0)
log_NO_den = ((X_O16 + (O_ini*f))*14.0)
log_NO = np.log10(log_NO_num/log_NO_den)

log_OH_num = ((X_O16 + (O_ini*f))*1.0)
log_OH_den = ((X_H1 + (H_ini*f))*16.0)
log_OH = np.log10(log_OH_num/log_OH_den) + 12.0


################## Script with varying values of f
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

# Load the data
H1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[6])[:-95][::-1]
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[8])[:-95][::-1]
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[33])[:-95][::-1]
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[9])[:-95][::-1]
M_sol = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', skip_header=295))[49])[:-95][::-1]

# Constants
N_ini = 4.705414495276072e-08
O_ini = 4.084625123020800e-07
H_ini = 7.515977428571429e-01
m_ejecta = 2640

# Variables to store results
log_NO_values = []
log_OH_values = []

# Loop through values of f
f_values = np.logspace(-1, 3, 200)  # logarithmic space from 0.1 to 1000 with 200 steps
dM = np.diff(M_sol)

for f in f_values:
    X_H1 = np.sum(H1[:-1] * dM)/ m_ejecta
    X_N14 = np.sum(N14[:-1] * dM) / m_ejecta
    X_O16 = np.sum(O16[:-1] * dM) / m_ejecta

    log_NO_num = ((X_N14 + (N_ini*f))*16.0)
    log_NO_den = ((X_O16 + (O_ini*f))*14.0)
    log_NO = np.log10(log_NO_num/log_NO_den)
    log_NO_values.append(log_NO)

    log_OH_num = ((X_O16 + (O_ini*f))*1.0)
    log_OH_den = ((X_H1 + (H_ini*f))*16.0)
    log_OH = np.log10(log_OH_num/log_OH_den) + 12.0
    log_OH_values.append(log_OH)

# Plotting
plt.figure(figsize=(8, 8))
sc = plt.scatter(log_OH_values, log_NO_values, c=f_values, cmap='viridis')
plt.xlabel('log$_{10}$ (O/H) + 12', fontsize=22)
plt.ylabel('log$_{10}$ (N/O)', fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=22)
plt.grid(True)
cbar = plt.colorbar(sc)
cbar.set_label('Dilution factor (f)', size=22)
cbar.ax.tick_params(labelsize=20)
plt.show()
