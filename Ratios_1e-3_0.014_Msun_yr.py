import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

# Load the data
H1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0114971', skip_header=312))[6])[:-105][::-1]
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0114971', skip_header=312))[8])[:-105][::-1]
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0114971', skip_header=312))[33])[:-105][::-1]
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0114971', skip_header=312))[9])[:-105][::-1]
M_sol = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0114971', skip_header=312))[49])[:-105][::-1]

# Constants
N_ini = 6.587580293386503e-04
O_ini = 5.718475172229120e-03
H_ini = 7.200000000000000e-01
C_ini = 2.283152454926108e-03
m_ejecta = 2385

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
sc = plt.scatter(log_OH_values, log_NO_values, c=f_values, cmap='viridis', label='Dependence on f')
plt.xlabel('log$_{10}$ (O/H) + 12', fontsize=22)
plt.ylabel('log$_{10}$ (N/O)', fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=22)
plt.grid(True)
cbar = plt.colorbar(sc)
cbar.set_label('f', size=22)
cbar.ax.tick_params(labelsize=20)
plt.show()

#############################
