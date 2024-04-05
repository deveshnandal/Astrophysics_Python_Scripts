import numpy as np
import matplotlib.pyplot as plt

data_files = [
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_491M_SS71.txt', '491M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_771M_SS40.txt', '771M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_778M_SS39.txt', '778M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_932M_SS27.txt', '932M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1135M_SS20.txt', '1135M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1331M_SS14.txt', '1331M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1662M_SS10.txt', '1662M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_1923M_SS6.txt', '1923M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_4477M_SS1.txt', '4477M$_{\odot}$'),
    ('/Users/hermit/Observatory/GENEC_SMS_final/inputs/HaloA/HaloA_AccretionRates_6127M_SS0.txt', '6127M$_{\odot}$')
]

fig, ax = plt.subplots()

for data_file, label in data_files:
    data = np.genfromtxt(data_file, skip_header=3).T
    accretion_rate = data[0]
    time = (10**3) * data[1]
    ax.plot(time, accretion_rate, label=label, linewidth=2)

# Add labels, title, and legend
ax.set_xlabel('Time [yr]', fontsize=22)
ax.set_ylabel('Mass Accretion Rate $[M_{\odot}/yr]$', fontsize=22)
#ax.set_title('Halo A Mass Accretion Rates', fontsize=22)
ax.legend(loc='lower left', fontsize=14)
ax.tick_params(axis='both', labelsize=20)
ax.set_ylim(1e-6, 1)


# Adjust plot limits
ax.set_xscale('log')
ax.set_yscale('log')
fig.set_size_inches(8, 8)
# Show the plot
plt.show()
