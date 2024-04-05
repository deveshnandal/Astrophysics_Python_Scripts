# Load models for Betelgeuse

gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/Betelgeuse_files/P016Z0.02S0/P016Z0.02S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/Betelgeuse_files/P016Z0.02S0.4/P016Z0.02S0.4.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/Betelgeuse_files/P017Z0.02S0/P017Z0.02S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/Betelgeuse_files/P017Z0.02S0.4/P017Z0.02S0.4.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/Betelgeuse_files/P017Z0.02S0.4_elph1.5/P017Z0.02S0.4_elph1.5.dat',5)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P018Z0.02S0_over0.3_xmloss/P018Z0.02S0_over0.3_xmloss.dat',6)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/Betelgeuse_files/P018Z0.02S0.4_over0.3_xmloss/P018Z0.02S0.4_over0.3_xmloss.dat',7)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/Betelgeuse_files/P020Z0.02S0_dovhp0.3/P020Z0.02S0_dovhp0.3.dat',8)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/Betelgeuse_files/P020Z0.02S0_hp0.3_xmloss_215/P020Z0.02S0_hp0.3_xmloss.dat',9)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0_xmloss/P020Z0.02S0_xmloss.dat',10)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0_over0.3_xmloss_96fitm/P020Z0.02S0_over0.3_xmloss_96fitm.dat',11)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.2_over0.3_xmloss_96fitm/P020Z0.02S0.2_over0.3_xmloss_96fitm.dat',12)
gtb.loadE('/Users/hermit/Observatory/Starcalc/Betelgeuse/P018Z0.02S0.2_over0.3_xmloss_96fitm/P018Z0.02S0.2_over0.3_xmloss_96fitm.dat',13)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0_over0.3_xmloss3_96fitm/P020Z0.02S0_over0.3_xmloss3_96fitm.dat',14)
gtb.loadE('/Users/hermit/Observatory/Starcalc/Betelgeuse/P020Z0.02S0.2_over0.1_xmloss3_90fitm/P020Z0.02S0.2_over0.1_xmloss3_90fitm.dat',15)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.4_over0.1_xmloss3_90fitm/P020Z0.02S0.4_over0.1_xmloss3_90fitm.dat',16)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P018Z0.02S0.4_over1_fitm0.90/P018Z0.02S0.4_over0.1_fitm0.90.dat',17)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P019Z0.02S0.4_over0.1_fitm0.92/P019Z0.02S0.4_over0.1_fitm0.92.dat',18)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P017Z0.02S0.4_over0.1_fitm0.92/P017Z0.02S0.4_over0.1_fitm0.92.dat',19)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P019Z0.02S0.4_over0.1_fitm0.92_Ledoux/P019Z0.02S0.4_over0.1_fitm0.92_Ledoux.dat',20)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.2_fitm0.92_Ledoux/P020Z0.02S0.2_fitm0.92_Ledoux.dat',21)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.4_fitm0.92_Ledoux/P020Z0.02S0.4_fitm0.92_Ledoux.dat',22)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P019Z0.02S0.2_fitm0.92/P019Z0.02S0.2_fitm0.92.dat',23)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Betelgeuse/P019Z0.02S0.1_fitm0.92/P019Z0.02S0.1_fitm0.92.dat',24)



from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

Nsurf = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.2_fitm0.92_Ledoux/P020Z0.02S0.2_fitm0.92_Ledoux.dat',skip_header=0))[10])
Csurf = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.2_fitm0.92_Ledoux/P020Z0.02S0.2_fitm0.92_Ledoux.dat',skip_header=0))[8])
NC = Nsurf/Csurf
Osurf = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.2_fitm0.92_Ledoux/P020Z0.02S0.2_fitm0.92_Ledoux.dat',skip_header=0))[11])
time = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.2_fitm0.92_Ledoux/P020Z0.02S0.2_fitm0.92_Ledoux.dat',skip_header=0))[1])

NO = Nsurf/Osurf
fig,ax=plt.subplots()
ax.plot(time,NC,linewidth=1.5, color='red',linestyle='solid',label="N/C")
ax.plot(time,NO,linewidth=1.5, color='blue',linestyle='dashed',label="N/O")

#ax.plot(T_Cstar,L_Cstar,linewidth=1.5, color='magenta',linestyle='dashdot',label="C*")
#ax.plot(T_E,L_E,linewidth=1.5, color='red',linestyle='solid')
#ax.plot(T_F,L_F,linewidth=1.5, color='blue',linestyle='solid')
#plt.text(4.401, 4.52, 'F', fontsize = 13)
#plt.text(4.373, 4.60, 'D', fontsize = 13)
#plt.text(4.402, 4.67, 'E', fontsize = 13)
#plt.text(4.409, 4.71, 'C', fontsize = 13)
#plt.text(4.410, 4.40, '15M$_{\odot}, Z=0.014$', fontsize = 14)
#plt.text(4.400, 4.37, 'V/V$_{crit}=0.4$', fontsize = 14)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
#ax.set_xlim(4.35, 4.500)
#ax.set_ylim(4.2, 4.84)
ax.set_xlabel('Time (years)',fontsize=20)
ax.set_ylabel('Mass fraction ratio',fontsize=20)
#ax.invert_xaxis()
leg = plt.legend(loc='upper left', shadow=True,prop={'size': 14})

#plt.xticks(np.arange(4.35, 4.500, 0.05))
plt.show()




from numpy import *
from matplotlib import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

Nsurf = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.4_fitm0.92_Ledoux/P020Z0.02S0.4_fitm0.92_Ledoux.dat',skip_header=0))[10])
Csurf = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.4_fitm0.92_Ledoux/P020Z0.02S0.4_fitm0.92_Ledoux.dat',skip_header=0))[8])
NC = Nsurf/Csurf
Osurf = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.4_fitm0.92_Ledoux/P020Z0.02S0.4_fitm0.92_Ledoux.dat',skip_header=0))[11])
time = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Betelgeuse/P020Z0.02S0.4_fitm0.92_Ledoux/P020Z0.02S0.4_fitm0.92_Ledoux.dat',skip_header=0))[1])

NO = Nsurf/Osurf
fig,ax=plt.subplots()
ax.plot(time,NC,linewidth=1.5, color='red',linestyle='solid',label="N/C")
ax.plot(time,NO,linewidth=1.5, color='blue',linestyle='dashed',label="N/O")

#ax.plot(T_Cstar,L_Cstar,linewidth=1.5, color='magenta',linestyle='dashdot',label="C*")
#ax.plot(T_E,L_E,linewidth=1.5, color='red',linestyle='solid')
#ax.plot(T_F,L_F,linewidth=1.5, color='blue',linestyle='solid')
#plt.text(4.401, 4.52, 'F', fontsize = 13)
#plt.text(4.373, 4.60, 'D', fontsize = 13)
#plt.text(4.402, 4.67, 'E', fontsize = 13)
#plt.text(4.409, 4.71, 'C', fontsize = 13)
#plt.text(4.410, 4.40, '15M$_{\odot}, Z=0.014$', fontsize = 14)
#plt.text(4.400, 4.37, 'V/V$_{crit}=0.4$', fontsize = 14)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
#ax.set_xlim(4.35, 4.500)
#ax.set_ylim(4.2, 4.84)
ax.set_xlabel('Time (years)',fontsize=20)
ax.set_ylabel('Mass fraction ratio',fontsize=20)
#ax.invert_xaxis()
leg = plt.legend(loc='upper left', shadow=True,prop={'size': 14})

#plt.xticks(np.arange(4.35, 4.500, 0.05))
plt.show()
