
import math
import pandas as pd
import matplotlib.pyplot as plt


xd2_rel = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.wg'))[113])/2.5e-5
Li7_rel = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.wg'))[115])/1.0e-8

M = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.wg'))[2])


fig,ax=plt.subplots()
ax.plot(M,xd2_rel,color='tab:blue',linewidth=3., label="Deuterium")
ax.plot(M,Li7_rel,color='tab:red',linewidth=3., label="Lithium")
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M/M$_{\odot}$]')
ax.set_ylabel('Relative Abundance')

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()


C12m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.wg'))[24])
N14m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.wg'))[26])
O16m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.wg'))[27])

M = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.wg'))[2])
fig,ax=plt.subplots()
ax.plot(M,C12m,linewidth=3., label="Carbon")
ax.plot(M,N14m,linewidth=3., label="Nitrogen")
ax.plot(M,O16m,linewidth=3., label="Oxygen")
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M/M$_{\odot}$]')
ax.set_ylabel('Abundance')

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

########### for Yoshida accretion law ##############
########### central CNO vs Mass ###########

import math
import pandas as pd
import matplotlib.pyplot as plt


C12m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[24])
N14m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[26])
O16m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[27])

M = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[2])
fig,ax=plt.subplots()
ax.plot(M,C12m,linewidth=3., label="Carbon")
ax.plot(M,N14m,linewidth=3., label="Nitrogen")
ax.plot(M,O16m,linewidth=3., label="Oxygen")
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M/M$_{\odot}$]')
ax.set_ylabel('Abundance')

leg = plt.legend(loc='upper left', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

######### Deuterium and Lithium 7 ############
import math
import pandas as pd
import matplotlib.pyplot as plt


xd2_rel = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[113])/2.5e-5
Li7_rel = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[115])/1.0e-8

M = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[2])


fig,ax=plt.subplots()
ax.plot(M,xd2_rel,color='tab:blue',linewidth=3., label="Deuterium")
ax.plot(M,Li7_rel,color='tab:red',linewidth=3., label="Lithium")
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M/M$_{\odot}$]')
ax.set_ylabel('Relative Abundance')

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

########### for 1e-5 ##############
########### central CNO vs Mass ###########

import math
import pandas as pd
import matplotlib.pyplot as plt


C12m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[24])
N14m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[26])
O16m = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[27])

M = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[2])
fig,ax=plt.subplots()
ax.plot(M,C12m,linewidth=3., label="Carbon")
ax.plot(M,N14m,linewidth=3., label="Nitrogen")
ax.plot(M,O16m,linewidth=3., label="Oxygen")
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M/M$_{\odot}$]')
ax.set_ylabel('Abundance')

leg = plt.legend(loc='upper left', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

######### Deuterium and Lithium 7 ############
import math
import pandas as pd
import matplotlib.pyplot as plt


xd2_rel = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[113])/2.5e-5
Li7_rel = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[115])/1.0e-8

M = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3//P002z0S0.dat'))[2])


fig,ax=plt.subplots()
ax.plot(M,xd2_rel,color='tab:blue',linewidth=3., label="Deuterium")
ax.plot(M,Li7_rel,color='tab:red',linewidth=3., label="Lithium")
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M/M$_{\odot}$]')
ax.set_ylabel('Relative Abundance')

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
