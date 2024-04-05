########## CNO and C12 abundance prfile for 1Msun/yr when 5% of Hydrogen is burnt in the center#############
import sys
sys.path.append('/Users/hermit/Observatory/GENEC_toolBox/')
import GENEC_toolBox as gtb
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.v0083231',2)
gtb.defX('Mr')
gtb.set_lineWidth(2.5)
CNO = gtb.Get_Var('C12',2)+gtb.Get_Var('N14',2)+gtb.Get_Var('O16',2)
gtb.Set_Var(CNO,'CNO',2,label="$CNO$",category="energy")
gtb.Plot('CNO')
gtb.keep_plot(True)
gtb.set_lineStyle('--')
C_12 = gtb.Get_Var('C12',2)
gtb.Set_Var(C_12,'C_12',2,label="$X(mass fraction)$",category="energy")
gtb.Plot('C_12')
gtb.add_label(2.65e+3,3.70e-9, '$CNO$',fontsize=14)
gtb.add_label(-4.1e+2,4.55e-10, '$C^{12}$',fontsize=14)
#################################################
################ SMS models #####################
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat',5)
############# Creating a CNO variable ##################
CNO = gtb.Get_Var('C12c',1)+gtb.Get_Var('N14c',1)+gtb.Get_Var('O16c',1)
gtb.Set_Var(CNO,'CNO',1,label="$CNO$",category="energy")
CNO = gtb.Get_Var('C12c',2)+gtb.Get_Var('N14c',2)+gtb.Get_Var('O16c',2)
gtb.Set_Var(CNO,'CNO',2,label="$CNO$",category="energy")
CNO = gtb.Get_Var('C12c',3)+gtb.Get_Var('N14c',3)+gtb.Get_Var('O16c',3)
gtb.Set_Var(CNO,'CNO',3,label="$CNO$",category="energy")
CNO = gtb.Get_Var('C12c',4)+gtb.Get_Var('N14c',4)+gtb.Get_Var('O16c',4)
gtb.Set_Var(CNO,'CNO',4,label="$CNO$",category="energy")
CNO = gtb.Get_Var('C12c',5)+gtb.Get_Var('N14c',5)+gtb.Get_Var('O16c',5)
gtb.Set_Var(CNO,'CNO',5,label="$CNO$",category="energy")
#######################################################
#################Central CNO abundance profile for all  SMS models ######################
import numpy as np
import matplotlib.pyplot as plt
M_10 = [1, 10, 100, 1000, 10000, 100000, 200000]
M_1 = [1, 10, 100, 1000, 10000, 100000, 200000]
M_01 = [1, 10, 100, 1000, 10000, 100000]
M_001 = [1, 10, 100, 1000, 10000]
M_0001 = [1, 10, 100, 1000]

C12_10Msun = [9e-15, 9e-15, 9e-15, 9e-15, 9e-15, 2.190e-9, 3.715e-9]
C12_10Msun_array = np.asarray(C12_10Msun) * 1.e9
C12_1Msun = [9e-15, 9e-15, 9e-15, 9e-15, 3.59e-10, 1.155e-9, 1.963e-9]
C12_01Msun = [9e-15, 9e-15, 9e-15, 8.91e-11, 1.766e-10, 1.268e-9]
C12_001Msun = [9e-15, 9e-15, 9e-15, 6.98e-11, 3.00e-10]
C12_0001Msun = [9e-15, 9e-15, 9e-15, 6.98e-11]

CNO_10Msun = [9e-15, 9e-15, 9e-15, 9e-15, 9e-15, 9.140e-9, 1.477e-8]
CN0_10Msun_array = np.asarray(CNO_10Msun) * 1.e9
CNO_1Msun = [9e-15, 9e-15, 9e-15, 9e-15, 3.083e-9, 9.966e-9, 1.470e-8]
CNO_01Msun = [9e-15, 9e-15, 1.99e-9, 3.900e-9, 4.293e-9, 3.563e-8]
CNO_001Msun = [9e-15, 9e-15, 9e-15, 2.000e-9, 1.311e-8]
CNO_0001Msun = [9e-15, 9e-15, 1.421e-11, 1.425e-10]

fig,ax=plt.subplots()
ax.plot(M_10,CNO_10Msun,color='k',linewidth=2.,label='CNO 10M$_{\odot}/yr$')
ax.plot(M_10,C12_10Msun,color='k',linestyle='dashdot',linewidth=2.,label='$C^{12}$10M$_{\odot}/yr$')
ax.plot(M_1,CNO_1Msun,color='tab:red',linewidth=2.,label='CNO 1M$_{\odot}/yr$')
ax.plot(M_1,C12_1Msun,color='tab:red',linestyle='dashdot',linewidth=2.,label='$C^{12}$1M$_{\odot}/yr$')
ax.plot(M_01,CNO_01Msun,color='tab:green',linewidth=2.,label='CNO 0.1M$_{\odot}/yr$')
ax.plot(M_01,C12_01Msun,color='tab:green',linestyle='dashdot',linewidth=2.,label='$C^{12}$0.1M$_{\odot}/yr$')
ax.plot(M_001,CNO_001Msun,color='tab:blue',linewidth=2.,label='CNO 0.01M$_{\odot}/yr$')
ax.plot(M_001,C12_001Msun,color='tab:blue',linestyle='dashdot',linewidth=2.,label='$C^{12}$0.01M$_{\odot}/yr$')
ax.plot(M_0001,CNO_0001Msun,color='tab:cyan',linewidth=2.,label='CNO 0.001M$_{\odot}/yr$')
ax.plot(M_0001,C12_0001Msun,color='tab:cyan',linestyle='dashdot',linewidth=2.,label='$C^{12}$0.001M$_{\odot}/yr$')

ax.legend(loc='upper left', shadow=True,prop={'size': 6})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('Xc Central Abundance')
#plt.ylim([1e-14, 1e-7])
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
