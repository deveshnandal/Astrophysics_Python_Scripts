###### R vs M plot for Y1 Model in Ohkubo 2009 made using Dexter############
# https://ui.adsabs.harvard.edu/abs/2009ApJ...706.1184O/abstract ###########

from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt

# define Stefan-Boltzmann constant in cgs units
sigma = 5.670374419e-5  # erg⋅cm⁻²⋅s⁻¹⋅K⁻⁴

# define solar radius in cm
R_sun = 6.96e10  # cm

# define solar luminosity in erg/s
L_sun = 3.828e33  # erg/s

M_Y_in_range = M_Y[(M_Y>=15000) & (M_Y<=18900)]
R_Y_in_range = R_Y[(M_Y>=15000) & (M_Y<=18900)]

M_Y1_in_range = M_Y1[(M_Y1>=15000) & (M_Y1<=18900)]
R_Y1_in_range = R_Y1[(M_Y1>=15000) & (M_Y1<=18900)]

L_Y = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[3]) * L_sun  # convert solar luminosity to erg/s
T_Y = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[4])  # transform from log base 10
M_Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[2])

# calculate R_Y using Stefan-Boltzmann Law and convert it to solar radius
R_Y = np.sqrt(L_Y / (4 * np.pi * sigma * T_Y**4)) / R_sun  # the radius is in cm, convert it to solar radius
R_Y = np.log10(R_Y)  # transform it to log base 10

M_Y1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/Dexter_Data/R_Vs_M_Ohkubo_Y1.txt',skip_header=0))[0])
R_Y1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/Dexter_Data/R_Vs_M_Ohkubo_Y1.txt',skip_header=0))[1])

fig,ax=plt.subplots()
# the shaded area in the selected range
ax.fill_between(M_Y_in_range, R_Y_in_range-0.2, R_Y_in_range+0.2, color='red', alpha=0.3, zorder=3)
ax.fill_between(M_Y1_in_range, R_Y1_in_range-0.2, R_Y1_in_range+0.2, color='blue', alpha=0.3, zorder=4)

ax.plot(M_Y,R_Y,linewidth=2.6, color='red',linestyle='solid',label="Our Model", zorder=1)  # lower zorder, this will be drawn first
ax.plot(M_Y1,R_Y1,linewidth=2.6, color='blue',linestyle='dotted',label="Ohkubo 2009", zorder=2)  # higher zorder, this will be drawn on top
ax.tick_params(axis='x', labelsize=26)
ax.tick_params(axis='y', labelsize=26)

ax.set_xlabel('M $[M_{\odot}]$',fontsize=26)
ax.set_ylabel('log R $[R_{\odot}]$',fontsize=26)

#leg = plt.legend(loc='lower left', shadow=True, prop={'size': 18})

ax.set_xscale('log')
fig.set_size_inches(8, 8)
plt.show()



####################
from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt

# define Stefan-Boltzmann constant in cgs units
sigma = 5.670374419e-5  # erg⋅cm⁻²⋅s⁻¹⋅K⁻⁴

# define solar radius in cm
R_sun = 6.96e10  # cm

# define solar luminosity in erg/s
L_sun = 3.828e33  # erg/s

L_Y = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[3]) * L_sun
T_Y = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[4])
M_Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Yoshida_case4/P002z0S0.dat',skip_header=0))[2])

# calculate R_Y using Stefan-Boltzmann Law and convert it to solar radius
R_Y = np.sqrt(L_Y / (4 * np.pi * sigma * T_Y**4)) / R_sun
R_Y = np.log10(R_Y)

M_Y1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/Dexter_Data/R_Vs_M_Ohkubo_Y1.txt',skip_header=0))[0])
R_Y1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/Dexter_Data/R_Vs_M_Ohkubo_Y1.txt',skip_header=0))[1])

M_Y_in_range = M_Y[(M_Y>=15.0) & (M_Y<=18.9)]
R_Y_in_range = R_Y[(M_Y>=15.0) & (M_Y<=18.9)]

M_Y1_in_range = M_Y1[(M_Y1>=15.0) & (M_Y1<=18.9)]
R_Y1_in_range = R_Y1[(M_Y1>=15.0) & (M_Y1<=18.9)]

# Add additional ranges
M_Y_in_range2 = M_Y[(M_Y>=97.2) & (M_Y<=132.8)]
R_Y_in_range2 = R_Y[(M_Y>=97.2) & (M_Y<=132.8)]

M_Y1_in_range2 = M_Y1[(M_Y1>=97.2) & (M_Y1<=132.8)]
R_Y1_in_range2 = R_Y1[(M_Y1>=97.2) & (M_Y1<=132.8)]

M_Y_in_range3 = M_Y[(M_Y>=849) & (M_Y<=1007)]
R_Y_in_range3 = R_Y[(M_Y>=849) & (M_Y<=1007)]

#M_Y1_in_range3 = M_Y1[(M_Y1>=849) & (M_Y1<=1007)]
#R_Y1_in_range3 = R_Y1[(M_Y1>=849) & (M_Y1<=1007)]

fig,ax=plt.subplots()

ax.fill_between(M_Y_in_range, R_Y_in_range-0.1, R_Y_in_range+0.1, color='red', alpha=0.3, zorder=3)
ax.fill_between(M_Y1_in_range, R_Y1_in_range-0.1, R_Y1_in_range+0.1, color='blue', alpha=0.3, zorder=4)

# Plot additional regions
ax.fill_between(M_Y_in_range2, R_Y_in_range2-0.1, R_Y_in_range2+0.1, color='green', alpha=0.3, zorder=5)
ax.fill_between(M_Y1_in_range2, R_Y1_in_range2-0.1, R_Y1_in_range2+0.1, color='purple', alpha=0.3, zorder=6)

#ax.fill_between(M_Y_in_range3, R_Y_in_range3-0.1, R_Y_in_range3+0.1, color='orange', alpha=0.3, zorder=7)
#ax.fill_between(M_Y1_in_range3, R_Y1_in_range3-0.1, R_Y1_in_range3+0.1, color='cyan', alpha=0.3, zorder=8)

ax.plot(M_Y,R_Y,linewidth=2.6, color='red',linestyle='solid',label="Our Model", zorder=1)
ax.plot(M_Y1,R_Y1,linewidth=2.6, color='blue',linestyle='dotted',label="Ohkubo 2009", zorder=2)

# Plot filled circles
ax.scatter(912.7, 2.629, color='blue', s=100)
ax.scatter(952, 3.87, color='red', s=100)

ax.tick_params(axis='x', labelsize=26)
ax.tick_params(axis='y', labelsize=26)

ax.set_xlabel('M $[M_{\odot}]$',fontsize=26)
ax.set_ylabel('log R $[R_{\odot}]$',fontsize=26)

ax.set_xscale('log')
fig.set_size_inches(8, 8)
plt.show()
