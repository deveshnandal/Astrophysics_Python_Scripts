##################### Kelvin Helmholtz timescale versus Mass during the evolution (.wg file)###########################

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
t_accr_3 = 1.00e+3*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
M_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
M_accr_3 = M_sun*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
L_accr_3 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat')))[3])
Teff_accr_3 = (10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat')))[4])**4
R_accr_3 = (L_accr_3/(4*pi*sigma*(Teff_accr_3)))**0.5 # Correct
t_top_3 = 0.5*G*(M_accr_3**2) # Correct
t_bot_3 = R_accr_3*L_accr_3 # Correct
t_KH_3 = (t_top_3/t_bot_3)*year # Correct
Time_3 = t_KH_3/t_accr_3 # Correct

################### Same for 10^-5 at Z=0#####################

t_accr_5 = 1.00e+5*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[2])
M_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[2])
M_accr_5 = M_sun*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[2])
L_accr_5 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat')))[3])
Teff_accr_5 = (10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat')))[4])**4
R_accr_5 = (L_accr_5/(4*pi*sigma*(Teff_accr_5)))**0.5 # Correct
t_top_5 = 0.5*G*(M_accr_5**2) # Correct
t_bot_5 = R_accr_5*L_accr_5 # Correct
t_KH_5 = (t_top_5/t_bot_5)*year  # Correct
Time_5 = t_KH_5/t_accr_5 # Correct

#### Now the same for yoshida #######

Mdot_Yoshida = 0.0450*((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[2])**(-2/3))
M_Yoshida = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[2])
t_accr_Yoshida = M_Yoshida/Mdot_Yoshida
M_y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[2])
M_accr_y = M_sun*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[2])
L_accr_y = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat')))[3])
Teff_accr_y = (10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat')))[4])**4
R_accr_y = (L_accr_y/(4*pi*sigma*(Teff_accr_y)))**0.5 # Correct
t_top_y = 0.5*G*(M_accr_y**2) # Correct
t_bot_y = R_accr_y*L_accr_y # Correct
t_KH_y = (t_top_y/t_bot_y)*year
Time_y = t_KH_y/t_accr_Yoshida

fig,ax=plt.subplots()
ax.plot(M_3,Time_3,color='tab:blue',linewidth=4., label="Yoshida")
ax.plot(M_5,Time_5,color='tab:green',linewidth=4., label="10-5")
ax.plot(M_y,Time_y,color='tab:red',linewidth=4.,label="10-3")

#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('$t_{KH}$/$t_{accr}$')
plt.xlim([0, 80])

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

#ax.set_xscale('log')
ax.set_yscale('log')
plt.show()





plt.plot(M_accr_3,t_KH_3)
plt.plot(M_accr_3,t_accr_3)

plt.title("Time versus Mass")
plt.xlabel("Log(Mass)")
plt.ylabel("Timescale")
