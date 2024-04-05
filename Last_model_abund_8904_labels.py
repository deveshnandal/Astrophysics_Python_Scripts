
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/3.5e-3Msun_yr/P002Z0S0.v0173881', skip_header=310)
X = data[:, 6]
H2 = data[:, 93]
Y = data[:, 7]
Y3 = data[:, 31]
Li7 = data[:, 95]
C12 = data[:, 8]
C13 = data[:, 32]
N14 = data[:, 33]
N15 = data[:, 34]
O16 = data[:, 9]
O17 = data[:, 35]
O18 = data[:, 36]
Ne20 = data[:, 37]
Ne22 = data[:, 38]
Mfrac = data[:, 49]

# Initialize the figure and axis
fig, ax = plt.subplots()

# Plotting the data with labels for the legend
ax.plot(Mfrac, X, linewidth=2, label=r'$H^{1}$')
ax.plot(Mfrac, Y, linewidth=2, label=r'$He^{4}$')
#ax.plot(Mfrac, Li7, linewidth=2, label=r'$Li^{7}$')
ax.plot(Mfrac, C12, linewidth=2, label=r'$C^{12}$')
ax.plot(Mfrac, N14, linewidth=2, label=r'$N^{14}$')
ax.plot(Mfrac, O16, linewidth=2, label=r'$O^{16}$')
ax.plot(Mfrac, Ne20, linewidth=2, label=r'$Ne^{20}$')
#ax.plot(Mfrac, H2, linewidth=2, linestyle='--', label=r'$D^{2}$')
ax.plot(Mfrac, Y3, linewidth=2, linestyle='--', label=r'$He^{3}$')
ax.plot(Mfrac, C13, linewidth=2, linestyle='--', label=r'$C^{13}$')
#ax.plot(Mfrac, N15, linewidth=2, linestyle='--', label=r'$N^{15}$')
#ax.plot(Mfrac, O17, linewidth=2, linestyle='--', label=r'$O^{17}$')
#ax.plot(Mfrac, O18, linewidth=2, linestyle='--', label=r'$O^{18}$')
ax.plot(Mfrac, Ne22, linewidth=2, linestyle='--', label=r'$Ne^{22}$')

# Setting axis labels, legend and other properties
ax.set_xlabel('M$_r$ [M$_{\odot}$]', fontsize=22, fontweight='bold')
ax.set_ylabel('Abundance profile', fontsize=22, fontweight='bold')
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
#ax.legend(loc='upper left', fontsize=12, framealpha=0.7)
ax.set_yscale('log')
plt.ylim([1.e-6,2])
fig.tight_layout()
fig.set_size_inches(8, 8)
plt.show()
