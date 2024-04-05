##### t_KH versus Mr for a structure file ###########

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
Lsol=3.8427*10**33
Ltot1= (10**(5.304989))
Ltot2= (10**(5.6121))
Ltot3= (10**(5.6843))
Msol=1.9884*10**33


#### model 25921, redward transition for 0.1Msun/yr model ####
#### Mass 21.68, Teff 4.2718
R1 = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0025921.gz',skip_header=3, skip_footer=2))[4])
Mr1 = Msol*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0025921.gz',skip_header=3, skip_footer=2))[49])
Lr1 = Lsol*Ltot1*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0025921.gz',skip_header=3, skip_footer=2))[5])
T_KH1 = (G*(Mr1)**2)/(2*(R1*Lr1))
#### model 26011, redward transition for 0.1Msun/yr model ####
#### Mass 21.84, L = 5.6121
R2 = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0026011.gz',skip_header=3, skip_footer=2))[4])
Mr2 = Msol*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0026011.gz',skip_header=3, skip_footer=2))[49])
Lr2 = Lsol*Ltot2*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0026011.gz',skip_header=3, skip_footer=2))[5])
T_KH2 = (G*(Mr2)**2)/(2*(R2*Lr2))
#### model 26141, redward transition for 0.1Msun/yr model ####
#### Mass 21.924, L = 5.6843
R3 = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0026141.gz',skip_header=3, skip_footer=2))[4])
Mr3 = Msol*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0026141.gz',skip_header=3, skip_footer=2))[49])
Lr3 = Lsol*Ltot3*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0026141.gz',skip_header=3, skip_footer=2))[5])
T_KH3 = (G*(Mr3)**2)/(2*(R3*Lr3))
fig,ax=plt.subplots()
ax.plot(Mr1,T_KH1,color='tab:blue',linewidth=2.2, label="0.1 M$_{\odot}/yr$ model at M = 21.68 $M_{\odot}$ and $logL = 5.30$")
ax.plot(Mr2,T_KH2,color='tab:red',linewidth=2.2, label="0.1 M$_{\odot}/yr$ model at M = 21.84 $M_{\odot}$ and $logL = 5.61$")
ax.plot(Mr3,T_KH3,color='k',linewidth=2.2, label="0.1 M$_{\odot}/yr$ model at M = 21.92 $M_{\odot}$ and $logL = 5.68$")

ax.set_xlabel('Mass [grams]')
ax.set_ylabel('$t_{KH}[seconds]$')
#plt.xlim([0, 80])
leg = plt.legend(loc='upper center', shadow=True,prop={'size': 9})
#ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
