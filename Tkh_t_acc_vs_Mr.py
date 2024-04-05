import math
import pandas as pd
import matplotlib.pyplot as plt
G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
t_accr_3 = 1.00e+3*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
M_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
M_accr_3 = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
L_accr_3 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat')))[3])
Teff_accr_3 = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat')))[4])**4
R_accr_3 = (L_accr_3/(4*pi*sigma*(Teff_accr_3)))**0.5 # Correct
t_top_3 = 0.5*G*(M_accr_3**2) # Correct
t_bot_3 = R_accr_3*L_accr_3 # Correct
t_KH_3 = (t_top_3/t_bot_3)*year # Correct
Time_3 = t_KH_3/t_accr_3 # Correct

################### Same for 10^-2 at Z=0#####################

t_accr_2 = 1.00e+2*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat'))[2])
M_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat'))[2])
M_accr_2 = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat'))[2])
L_accr_2 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat')))[3])
Teff_accr_2 = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat')))[4])**4
R_accr_2 = (L_accr_2/(4*pi*sigma*(Teff_accr_2)))**0.5 # Correct
t_top_2 = 0.5*G*(M_accr_2**2) # Correct
t_bot_2 = R_accr_2*L_accr_2 # Correct
t_KH_2 = (t_top_2/t_bot_2)*year  # Correct
Time_2 = t_KH_2/t_accr_2 # Correct

################### Same for 10^-1 at Z=0#####################

t_accr_1 = 1.00e+1*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])
M_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])
M_accr_1 = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])
L_accr_1 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat')))[3])
Teff_accr_1 = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat')))[4])**4
R_accr_1 = (L_accr_1/(4*pi*sigma*(Teff_accr_1)))**0.5 # Correct
t_top_1 = 0.5*G*(M_accr_1**2) # Correct
t_bot_1 = R_accr_1*L_accr_1 # Correct
t_KH_1 = (t_top_1/t_bot_1)*year  # Correct
Time_1 = t_KH_1/t_accr_1 # Correct

################### Same for 10^0 at Z=0#####################

t_accr_0 = 1.00e+0*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat'))[2])
M_0 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat'))[2])
M_accr_0 = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat'))[2])
L_accr_0 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat')))[3])
Teff_accr_0 = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat')))[4])**4
R_accr_0 = (L_accr_0/(4*pi*sigma*(Teff_accr_0)))**0.5 # Correct
t_top_0 = 0.5*G*(M_accr_0**2) # Correct
t_bot_0 = R_accr_0*L_accr_0 # Correct
t_KH_0 = (t_top_0/t_bot_0)*year  # Correct
Time_0 = t_KH_0/t_accr_0 # Correct

################### Same for 10^1 at Z=0#####################

t_accr_ten = 1.00e-1*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat'))[2])
M_ten = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat'))[2])
M_accr_ten = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat'))[2])
L_accr_ten = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat')))[3])
Teff_accr_ten = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat')))[4])**4
R_accr_ten = (L_accr_ten/(4*pi*sigma*(Teff_accr_ten)))**0.5 # Correct
t_top_ten = 0.5*G*(M_accr_ten**2) # Correct
t_bot_ten = R_accr_ten*L_accr_ten # Correct
t_KH_ten = (t_top_ten/t_bot_ten)*year  # Correct
Time_ten = t_KH_ten/t_accr_ten # Correct
#### Now the same for yoshida #######


fig,ax=plt.subplots()
plt.hlines(1, 0, 1.e6, color='grey',linestyle='dashdot')
ax.plot(M_ten,Time_ten,color='k',linewidth=2.5, label="$10M_{\odot}/yr$")
ax.plot(M_0,Time_0,color='tab:red',linewidth=2.5, label="$1M_{\odot}/yr$")
ax.plot(M_1,Time_1,color='tab:green',linewidth=2.5, label="$0.1M_{\odot}/yr$")
ax.plot(M_2,Time_2,color='tab:blue',linewidth=2.5, label="$0.01M_{\odot}/yr$")
ax.plot(M_3,Time_3,color='tab:cyan',linewidth=2.5, label="$0.001M_{\odot}/yr$")



#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('$t_{KH}$/$t_{accr}$')
#plt.xlim([0, 80])

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

############# Only t_KH versus Mass for all models

import math
import pandas as pd
import matplotlib.pyplot as plt
G=6.67428e-8
pi=3.141592653589793e0
M_sun=1.9885e33
sigma = 5.670374e-05
year = 3.17098e-8
t_accr_3 = 1.00e+3*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
M_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
M_accr_3 = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
L_accr_3 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat')))[3])
Teff_accr_3 = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat')))[4])**4
R_accr_3 = (L_accr_3/(4*pi*sigma*(Teff_accr_3)))**0.5 # Correct
t_top_3 = 0.5*G*(M_accr_3**2) # Correct
t_bot_3 = R_accr_3*L_accr_3 # Correct
t_KH_3 = (t_top_3/t_bot_3)*year # Correct
Time_3 = t_KH_3/t_accr_3 # Correct

################### Same for 10^-2 at Z=0#####################

t_accr_2 = 1.00e+2*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat'))[2])
M_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat'))[2])
M_accr_2 = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat'))[2])
L_accr_2 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat')))[3])
Teff_accr_2 = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat')))[4])**4
R_accr_2 = (L_accr_2/(4*pi*sigma*(Teff_accr_2)))**0.5 # Correct
t_top_2 = 0.5*G*(M_accr_2**2) # Correct
t_bot_2 = R_accr_2*L_accr_2 # Correct
t_KH_2 = (t_top_2/t_bot_2)*year  # Correct
Time_2 = t_KH_2/t_accr_2 # Correct

################### Same for 10^-1 at Z=0#####################

t_accr_1 = 1.00e+1*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])
M_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])
M_accr_1 = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])
L_accr_1 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat')))[3])
Teff_accr_1 = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat')))[4])**4
R_accr_1 = (L_accr_1/(4*pi*sigma*(Teff_accr_1)))**0.5 # Correct
t_top_1 = 0.5*G*(M_accr_1**2) # Correct
t_bot_1 = R_accr_1*L_accr_1 # Correct
t_KH_1 = (t_top_1/t_bot_1)*year  # Correct
Time_1 = t_KH_1/t_accr_1 # Correct

################### Same for 10^0 at Z=0#####################

t_accr_0 = 1.00e+0*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat'))[2])
M_0 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat'))[2])
M_accr_0 = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat'))[2])
L_accr_0 = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat')))[3])
Teff_accr_0 = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat')))[4])**4
R_accr_0 = (L_accr_0/(4*pi*sigma*(Teff_accr_0)))**0.5 # Correct
t_top_0 = 0.5*G*(M_accr_0**2) # Correct
t_bot_0 = R_accr_0*L_accr_0 # Correct
t_KH_0 = (t_top_0/t_bot_0)*year  # Correct
Time_0 = t_KH_0/t_accr_0 # Correct

################### Same for 10^1 at Z=0#####################

t_accr_ten = 1.00e-1*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat'))[2])
M_ten = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat'))[2])
M_accr_ten = M_sun*(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat'))[2])
L_accr_ten = 3.846e+33*(10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat')))[3])
Teff_accr_ten = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat')))[4])**4
R_accr_ten = (L_accr_ten/(4*pi*sigma*(Teff_accr_ten)))**0.5 # Correct
t_top_ten = 0.5*G*(M_accr_ten**2) # Correct
t_bot_ten = R_accr_ten*L_accr_ten # Correct
t_KH_ten = (t_top_ten/t_bot_ten)*year  # Correct
Time_ten = t_KH_ten/t_accr_ten # Correct
#### Now the same for yoshida #######


fig,ax=plt.subplots()
plt.hlines(1, 0, 1.e6, color='grey',linestyle='dashdot')
ax.plot(M_ten,Time_ten,color='k',linewidth=2.5, label="$10M_{\odot}/yr$")
ax.plot(M_0,Time_0,color='tab:red',linewidth=2.5, label="$1M_{\odot}/yr$")
ax.plot(M_1,Time_1,color='tab:green',linewidth=2.5, label="$0.1M_{\odot}/yr$")
ax.plot(M_2,Time_2,color='tab:blue',linewidth=2.5, label="$0.01M_{\odot}/yr$")
ax.plot(M_3,Time_3,color='tab:cyan',linewidth=2.5, label="$0.001M_{\odot}/yr$")



#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('$t_{KH}$/$t_{accr}$')
#plt.xlim([0, 80])

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
