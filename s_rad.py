############# Entropy of radiation ###########
############# 1662 model #####################
############# v file with mass 89 Msol #######

import numpy as np
import matplotlib.pyplot as plt

# Constants
a = 7.56576738e-15

# Load data
data = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0040621.gz', skip_header=275))

# Data extraction
R = 10**data[4]
M = 89.58853*data[1]
T = 10**data[3]
rho = 10**data[14]
Mr = data[1]

# Entropy calculation
s_rad = (4*a*(T**3))/(3*rho)

# Plot
plt.figure(figsize=(10,6))
plt.plot(Mr, s_rad)
plt.xlabel('Lagrangian Mass (Mr)')
plt.ylabel('Entropy of Radius')
plt.title('Entropy of Radius vs Lagrangian Mass')
plt.grid(True)
plt.show()
