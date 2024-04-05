### Figure 1 HRD ###

gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',1)
gtb.set_lineWidth(3.5)
gtb.CBLimits(min=0,max=0.7516)
gtb.Limits(xmax=5.2)
gtb.set_colourMap('jet')
gtb.HRD_plot(zcol='H1c')
gtb.mark_phase('H',colour='k')
gtb.isoRadius(fontsize=11,line='dashdot',colour='.60')

gtb.dotxy(4.1293,1.4694,'ko')
gtb.dotxy(4.2790,2.1333,'ko')
gtb.dotxy(4.3790,2.5751,'ko')
gtb.dotxy(4.4521,2.9016,'ko')
gtb.dotxy(4.5563,3.3746,'ko')
gtb.dotxy(4.6303,3.7150,'ko')
gtb.dotxy(4.6788,4.0754,'ko')
gtb.dotxy(4.7306,4.3346,'ko')
gtb.dotxy(4.7942,4.6600,'ko')
gtb.dotxy(4.8633,5.0928,'ko')
gtb.dotxy(4.8983,5.3706,'ko')
gtb.dotxy(4.9361,5.7251,'ko')
gtb.dotxy(4.9604,5.9992,'ko')
gtb.dotxy(4.9773,6.2475,'ko')

gtb.line(4.1293,4.2790,1.4694,2.1333,colour='k')
gtb.line(4.2790,4.3790,2.1333,2.5751,colour='k')
gtb.line(4.3790,4.4521,2.5751,2.9016,colour='k')
gtb.line(4.4521,4.5563,2.9016,3.3746,colour='k')
gtb.line(4.5563,4.6303,3.3746,3.7150,colour='k')
gtb.line(4.6303,4.6788,3.7150,4.0754,colour='k')
gtb.line(4.6788,4.7306,4.0754,4.3346,colour='k')
gtb.line(4.7306,4.7942,4.3346,4.6600,colour='k')
gtb.line(4.7942,4.8633,4.6600,5.0928,colour='k')
gtb.line(4.8633,4.8983,5.0928,5.3706,colour='k')
gtb.line(4.8983,4.9361,5.3706,5.7251,colour='k')
gtb.line(4.9361,4.9604,5.7251,5.9992,colour='k')
gtb.line(4.9604,4.9773,5.9992,6.2475,colour='k')

gtb.add_label(4.1780,1.4194, '2',fontsize=14)
gtb.add_label(4.3300,1.9300, '3',fontsize=14)
gtb.add_label(4.4280,2.3451, '4',fontsize=14)
gtb.add_label(4.5000,2.6556, '5',fontsize=14)
gtb.add_label(4.6000,3.0646, '7',fontsize=14)
gtb.add_label(4.6850,3.4950, '9',fontsize=14)
gtb.add_label(4.7700,3.8504, '12',fontsize=14)
gtb.add_label(4.82000,4.1500, '15',fontsize=14)
gtb.add_label(4.8800,4.4800, '20',fontsize=14)
gtb.add_label(4.9350,4.8600, '30',fontsize=14)
gtb.add_label(4.9780,5.1706, '40',fontsize=14)
gtb.add_label(5.0100,5.4900, '60',fontsize=14)
gtb.add_label(5.0380,5.7492, '85',fontsize=14)
gtb.add_label(5.0790,6.0375, '120',fontsize=14)

### Figure 2 left panel R_vs_M Kipp ###
import sys
sys.path.append('/Users/hermit/Observatory/UtilsEvol/')
import UltimateKippenhahn as kpn
mykip = kpn.m2d()
mykip.loadfiles('Observatory/StarCalc/SMS/1e-3Msun_yr/',vpattern=['1'])
mykip.Kippenplot(ymin=0,xmin=0.282,xmax=3.60,yvar='Rsol',xvar='Mtot',makefig=True,burn=True,cmap='gist_earth_r',alpha=0.6,mylevels=[1,10,100,1000,10000,100000])

### Figure 2 right panel R_vs_time Kipp ###
import sys
sys.path.append('/Users/hermit/Observatory/UtilsEvol/')
import UltimateKippenhahn as kpn
mykip = kpn.m2d()
mykip.loadfiles('Observatory/StarCalc/SMS/1e-3Msun_yr/',vpattern=['1'])
mykip.Kippenplot(ymin=0,xmin=0,yvar='Rsol',xvar='age',makefig=True,burn=True,cmap='gist_earth_r',alpha=0.6,mylevels=[1,10,100,1000,10000])

### Figure 3 Tc vs rhoc ###
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',1)
gtb.set_lineWidth(2)
gtb.rhoT()

#### Fig 3 with marked phases ##########
import numpy as np
from matplotlib import pyplot as plt

Tc_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[20])
rhoc_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[19])
Tc_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/P120z00S0.wg',skip_header=0))[20])
rhoc_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/P120z00S0.wg',skip_header=0))[19])

x1=[1.7975]
y1=[8.0975]
x2=[1.0651]
y2=[8.1895]
x3=[1.5460]
y3=[8.3408]
x4=[2.5703]
y4=[8.6097]
x5=[2.1190]
y5=[8.4603]
x6=[5.0660]
y6=[9.2414]
x7=[5.0829]
y7=[9.2458]
x8=[5.0898]
y8=[9.2478]
x9=[5.1130]
y9=[9.2535]
x10=[5.7690]
y10=[9.4442]
fig,ax=plt.subplots()
ax.plot(rhoc_1,Tc_1,linewidth=2., label="$3053 M_{\odot}$")
ax.plot(rhoc_2,Tc_2,linewidth=2., label="$120 M_{\odot}$")
plt.plot(x1, y1, marker="o", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x2, y2, marker="o", markersize=7, markeredgecolor="red", markerfacecolor="red")
plt.plot(x3, y3, marker="s", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x4, y4, marker="s", markersize=7, markeredgecolor="red", markerfacecolor="red")
plt.plot(x5, y5, marker="d", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x6, y6, marker="d", markersize=7, markeredgecolor="red", markerfacecolor="red")
plt.plot(x7, y7, marker="1", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x8, y8, marker="2", markersize=7, markeredgecolor="red", markerfacecolor="red")
plt.plot(x9, y9, marker="h", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x10, y10, marker="H", markersize=7, markeredgecolor="red", markerfacecolor="red")

ax.set_xlabel('log$(T_{c})$',fontsize=24, fontweight='bold')
ax.set_ylabel('log$(\\rho_{c})$',fontsize=24, fontweight='bold')

leg = plt.legend(loc='lower right', shadow=True,prop={'size': 9})
#fig.tight_layout()
plt.show()




### Figure 4 Abundance profile at end of computation, currently for model 171981 ###
import numpy as np
from matplotlib import pyplot as plt

X = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[6])
Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[7])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[95])
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[8])
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[33])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[9])
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[37])
M_tot = 139171.11504
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[49])



fig,ax=plt.subplots()
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.plot(Mfrac,X,linewidth=2., label="$H^{1}$")
ax.plot(Mfrac,Y,linewidth=2., label="$He^{4}$")
ax.plot(Mfrac,Li7,linewidth=2., label="$Li^{7}$")
ax.plot(Mfrac,C12,linewidth=2., label="$C^{12}$")
ax.plot(Mfrac,N14,linewidth=2., label="$N^{14}$")
ax.plot(Mfrac,O16,linewidth=2., label="$O^{16}$")
ax.plot(Mfrac,Ne20,linewidth=2., label="$Ne^{20}$")
ax.set_xlabel('Mr [M$_{\odot}$]',fontsize=18, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=18, fontweight='bold')


leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
fig.set_size_inches(8, 8)

plt.show()

### Figure 4 Abundance profile at end of computation, currently for model 171981 Without LABELS###
import numpy as np
from matplotlib import pyplot as plt

X = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[6])
Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[7])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[95])
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[8])
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[33])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[9])
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[37])
M_tot = 139171.11504
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[49])



fig,ax=plt.subplots()
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.plot(Mfrac,X,linewidth=2.)
ax.plot(Mfrac,Y,linewidth=2.)
ax.plot(Mfrac,Li7,linewidth=2.)
ax.plot(Mfrac,C12,linewidth=2.)
ax.plot(Mfrac,N14,linewidth=2.)
ax.plot(Mfrac,O16,linewidth=2.)
ax.plot(Mfrac,Ne20,linewidth=2.)
ax.set_xlabel('M$_r$ [M$_{\odot}$]',fontsize=22, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=22, fontweight='bold')


#leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
fig.set_size_inches(8, 8)
#plt.savefig('/Users/hermit/Observatory/abund_3000.pdf', facecolor='none', dpi=300, transparent=True)
plt.show()

### Figure 4 Abundance profile at end of computation, currently for model 171941 ###

###### 171941
import numpy as np
from matplotlib import pyplot as plt

X = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[6])
Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[7])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[95])
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[8])
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[33])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[9])
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[37])
M_tot = 139171.11504
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[49])



fig,ax=plt.subplots()
ax.plot(Mfrac,X,linewidth=2., label="$H^{1}$")
ax.plot(Mfrac,Y,linewidth=2., label="$He^{4}$")
ax.plot(Mfrac,Li7,linewidth=2., label="$Li^{7}$")
ax.plot(Mfrac,C12,linewidth=2., label="$C^{12}$")
ax.plot(Mfrac,N14,linewidth=2., label="$N^{14}$")
ax.plot(Mfrac,O16,linewidth=2., label="$O^{16}$")
ax.plot(Mfrac,Ne20,linewidth=2., label="$Ne^{20}$")
ax.set_xlabel('Mr [M$_{\odot}$]',fontsize=18, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=18, fontweight='bold')


leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
fig.set_size_inches(8, 8)

plt.show()


###### 171941
import numpy as np
from matplotlib import pyplot as plt

X = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[6])
Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[7])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[95])
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[8])
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[33])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[9])
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[37])
M_tot = 139171.11504
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[49])
R = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0133021',skip_header=309))[4])



fig,ax=plt.subplots()
ax.plot(R,X,linewidth=2., label="$H^{1}$")
ax.plot(R,Y,linewidth=2., label="$He^{4}$")
ax.plot(R,Li7,linewidth=2., label="$Li^{7}$")
ax.plot(R,C12,linewidth=2., label="$C^{12}$")
ax.plot(R,N14,linewidth=2., label="$N^{14}$")
ax.plot(R,O16,linewidth=2., label="$O^{16}$")
ax.plot(R,Ne20,linewidth=2., label="$Ne^{20}$")
ax.set_xlabel('Rr [R$_{\odot}$]',fontsize=18, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=18, fontweight='bold')


leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
plt.show()

##### Calculate CO core mass
# End O and Si
import numpy as np
from matplotlib import pyplot as plt
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[9])
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171941',skip_header=294))[49])



fig,ax=plt.subplots()
ax.plot(Mfrac,C12,linewidth=2., label="$C^{12}$")
ax.plot(Mfrac,O16,linewidth=2., label="$O^{16}$")
ax.set_xlabel('Mr [M$_{\odot}$]',fontsize=18, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=18, fontweight='bold')


leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
plt.show()

#### End # NOTE: gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170781',8)
import numpy as np
from matplotlib import pyplot as plt
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170781',skip_header=293))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170781',skip_header=293))[9])
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170781',skip_header=293))[49])



fig,ax=plt.subplots()
ax.plot(Mfrac,C12,linewidth=2., label="$C^{12}$")
ax.plot(Mfrac,O16,linewidth=2., label="$O^{16}$")
ax.set_xlabel('Mr [M$_{\odot}$]',fontsize=18, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=18, fontweight='bold')


leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
plt.show()

#### End He
import numpy as np
from matplotlib import pyplot as plt
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170201',skip_header=889))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170201',skip_header=889))[9])
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170201',skip_header=889))[49])



fig,ax=plt.subplots()
ax.plot(Mfrac,C12,linewidth=2., label="$C^{12}$")
ax.plot(Mfrac,O16,linewidth=2., label="$O^{16}$")
ax.set_xlabel('Mr [M$_{\odot}$]',fontsize=18, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=18, fontweight='bold')


leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
plt.show()

#### End H
import numpy as np
from matplotlib import pyplot as plt
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132131',skip_header=310))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132131',skip_header=310))[9])
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132131',skip_header=310))[49])



fig,ax=plt.subplots()
ax.plot(Mfrac,C12,linewidth=2., label="$C^{12}$")
ax.plot(Mfrac,O16,linewidth=2., label="$O^{16}$")
ax.set_xlabel('Mr [M$_{\odot}$]',fontsize=18, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=18, fontweight='bold')


leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
plt.show()

####### Test Tc rhoc
import numpy as np
from matplotlib import pyplot as plt

Tc_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[20])
rhoc_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.wg',skip_header=0))[19])
Tc_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/P120z00S0.wg',skip_header=0))[20])
rhoc_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/P120z00S0.wg',skip_header=0))[19])
T1= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[3]))
rho1= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981',skip_header=294))[14]))
T2= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170781',skip_header=293))[3]))
rho2= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170781',skip_header=293))[14]))
T3= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170201',skip_header=889))[3]))
rho3= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170201',skip_header=889))[14]))
T4= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132131',skip_header=310))[3]))
rho4= ((np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0132131',skip_header=310))[14]))

x1=[1.7975]
y1=[8.0975]
x2=[1.0651]
y2=[8.1895]
x3=[1.5460]
y3=[8.3408]
x4=[2.5703]
y4=[8.6097]
x5=[2.1190]
y5=[8.4603]
x6=[5.0660]
y6=[9.2414]
x7=[5.0829]
y7=[9.2458]
x8=[5.0898]
y8=[9.2478]
x9=[5.1130]
y9=[9.2535]
x10=[5.7690]
y10=[9.4442]
fig,ax=plt.subplots()
ax.plot(rhoc_1,Tc_1,linewidth=2., label="$3053 M_{\odot}$")
ax.plot(rhoc_2,Tc_2,linewidth=2., label="$120 M_{\odot}$")
ax.plot(rho1,T1,linewidth=2., label="$Last model$")
#ax.plot(rho2,T2,linewidth=2., label="$End Ne$")
#ax.plot(rho3,T3,linewidth=2., label="$End He$")
#ax.plot(rho4,T4,linewidth=2., label="$End H$")

plt.plot(x1, y1, marker="o", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x2, y2, marker="o", markersize=7, markeredgecolor="red", markerfacecolor="red")
plt.plot(x3, y3, marker="s", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x4, y4, marker="s", markersize=7, markeredgecolor="red", markerfacecolor="red")
plt.plot(x5, y5, marker="d", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x6, y6, marker="d", markersize=7, markeredgecolor="red", markerfacecolor="red")
plt.plot(x7, y7, marker="1", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x8, y8, marker="2", markersize=7, markeredgecolor="red", markerfacecolor="red")
plt.plot(x9, y9, marker="h", markersize=7, markeredgecolor="green", markerfacecolor="green")
plt.plot(x10, y10, marker="H", markersize=7, markeredgecolor="red", markerfacecolor="red")

ax.set_xlabel('log$(T_{c})$',fontsize=24, fontweight='bold')
ax.set_ylabel('log$(\\rho_{c})$',fontsize=24, fontweight='bold')

leg = plt.legend(loc='lower right', shadow=True,prop={'size': 9})
#fig.tight_layout()
plt.show()

### Figure 4 Abundance profile at end of Si BURNING, currently for model 177201 Without LABELS###
import numpy as np
from matplotlib import pyplot as plt

X = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[6])
Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[7])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[95])
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[8])
N14 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[33])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[9])
Ne20 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[37])
M_tot = 139171.11504
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201',skip_header=3))[49])



fig,ax=plt.subplots()
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.plot(Mfrac,X,linewidth=2.,color='k', label="$H^{1}$")
ax.plot(Mfrac,Y,linewidth=2.,color='tab:green', label="$He^{4}$")
#ax.plot(Mfrac,Li7,linewidth=2.)
ax.plot(Mfrac,C12,linewidth=2.,color='tab:red', label="$C^{12}$")
ax.plot(Mfrac,N14,linewidth=2.,color='tab:brown', label="$N^{14}$")
ax.plot(Mfrac,O16,linewidth=2.,color='tab:blue', label="$O^{16}$")
ax.plot(Mfrac,Ne20,linewidth=2.,color='tab:grey', label="$Ne^{20}$")
ax.set_xlabel('Mr [M$_{\odot}$]',fontsize=18, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=18, fontweight='bold')


#leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
plt.show()

########################## Abundance model numbers #################
###### 1e-3Msun/yr - end of C burning - 170611,
###### 1e-3_1e-6 - 182521
###### 1e-3_0.014 - 115241
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170611',1)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0182521.gz',2)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0115241',3)
###### 1e-3Msun/yr - halfway He4c - 152081,
###### 1e-3_1e-6 - 163701
###### 1e-3_0.014 - 84031
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0152081',1)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0163701.gz',2)
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0084031',3)


gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0092151',1)

gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0066051',3)


################ abund final model, use this one
import numpy as np
import matplotlib
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 14})
matplotlib.rcParams['text.latex.preamble'] = r"\usepackage{amsmath}"
matplotlib.rcParams['xtick.top'] = True
matplotlib.rcParams['ytick.right'] = True
matplotlib.rcParams['ytick.minor.visible'] = True
matplotlib.rcParams['xtick.minor.visible'] = True
from matplotlib import pyplot as plt

pagewidth = 513

def get_figsize(width, wf=1, hf=(5.**0.5-1.0)/2.0):
    fig_width_pt = width * wf
    inches_per_pt = 1.0 / 72.27
    fig_width = fig_width_pt * inches_per_pt
    fig_height = fig_width * hf
    return [fig_width, fig_height]

X = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[6]
H2 = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[93]
Y = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[7]
Li7 = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[95]
C12 = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[8]
N14 = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[33]
O16 = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[9]
Ne20 = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[37]
Mfrac = np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0171981', skip_header=294))[49]

fig, ax = plt.subplots(figsize=get_figsize(pagewidth, wf=1.0, hf=1))
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.plot(Mfrac, X, linewidth=2.)
ax.plot(Mfrac, Y, linewidth=2.)
ax.plot(Mfrac, H2, linewidth=2.)
ax.plot(Mfrac, Li7, linewidth=2.)
ax.plot(Mfrac, C12, linewidth=2.)
ax.plot(Mfrac, N14, linewidth=2.)
ax.plot(Mfrac, O16, linewidth=2.)
ax.plot(Mfrac, Ne20, linewidth=2.)
ax.set_xlabel('M$_r$ [M$_{\odot}$]',fontsize=22, fontweight='bold')
ax.set_ylabel('Abundance profile',fontsize=22, fontweight='bold')


#leg = plt.legend(loc='lower center', shadow=True,prop={'size': 9})
plt.ylim([1.e-6,2])

#ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
fig.set_size_inches(8, 8)
#ax.legend(['X', 'Y', 'Li7', 'C12', 'N14', 'O16', 'Ne20'], loc='upper right', fontsize=14)
#plt.grid()
#plt.title('Abundance Profiles', fontsize=22)
plt.tight_layout()

# Save the figure
#plt.savefig("abundance_profiles.png", dpi=300)
#plt.savefig('/Users/hermit/Observatory/abund_3000_new.png', facecolor='none', dpi=300, transparent=True)

# Show the figure
plt.show()
