import math
import pandas as pd
import matplotlib.pyplot as plt

T = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0_StrucData_0197311.dat',skip_header=12))[3])
R = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0_StrucData_0197311.dat',skip_header=12))[1])
x1 = [9.6358]
y1 = [8.3896]
x2 = [11.1505]
y2 = [8.3878]
x3 = [12.5112]
y3 = [7.9825]
x4 = [13.3660]
y4 = [6.9590]
x5 = [14.7620]
y5 = [5.4070]
x6 = [15.2800]
y6 = [3.8914]


a = 6.96
b = 14.50
plt.axvspan(a, b, color='c', alpha=0.2, lw=0)
a = 14.50
b = 14.56
plt.axvspan(a, b, color='y', alpha=0.2, lw=0)
a = 14.56
b = 15.280
plt.axvspan(a, b, color='c', alpha=0.2, lw=0)
fig,ax=plt.subplots()
ax.plot(R,T,linewidth=2., label="Temperature vs Radius")
plt.plot(x1, y1, marker="o", markersize=6, markeredgecolor="red", markerfacecolor="green")
plt.plot(x2, y2, marker="o", markersize=6, markeredgecolor="red", markerfacecolor="green")
plt.plot(x3, y3, marker="o", markersize=6, markeredgecolor="red", markerfacecolor="green")
plt.plot(x4, y4, marker="o", markersize=6, markeredgecolor="red", markerfacecolor="green")
plt.plot(x5, y5, marker="o", markersize=6, markeredgecolor="red", markerfacecolor="green")
plt.plot(x6, y6, marker="o", markersize=6, markeredgecolor="red", markerfacecolor="green")
plt.text(9.472, 8.104, '0.0002M$_{\odot}$', fontsize = 8)
plt.text(10.926, 8.104, '43.60M$_{\odot}$', fontsize = 8)
plt.text(12.798, 8.017, '82036M$_{\odot}$', fontsize = 8)
plt.text(13.601, 6.866, '126834M$_{\odot}$', fontsize = 8)
plt.text(13.585, 5.369, '137892M$_{\odot}$', fontsize = 8)
plt.text(14.084, 3.889, '139160M$_{\odot}$', fontsize = 8)

ax.set_xlabel('log R')
ax.set_ylabel('log T')
#plt.xlim([0, 900])

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

#ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()

a = 0
b = 14.50
plt.axhspan(a, b, color='c', alpha=0.5, lw=0)
a = 14.50
b = 14.56
plt.axhspan(a, b, color='g', alpha=0.5, lw=0)
a = 14.56
b = 15.280
plt.axhspan(a, b, color='c', alpha=0.5, lw=0)
plt.plot(Accr_rate,M_max, color='black', linewidth=2.5)
plt.plot(x, y, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")

plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Maximum attainable mass")
plt.xlabel("Accretion rate (M$_{\odot}$/year)")
plt.ylabel("Mass(M$_{\odot}$) ")
plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()

135430
3.341e4*.9551e10
3.531e4*.9551e10
137219
