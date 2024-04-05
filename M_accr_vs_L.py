Mdot_Yoshida = 0.0450*((np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[2])**(-2/3))
L_accr_y = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.dat'))[3])
x1 = [2.2621]
y1 = [0.03814]
x2 = [2.3994]
y2 = [0.0315]
x3 = [2.3149]
y3 = [0.02313]
x4 = [2.2288]
y4 = [0.0157]
x5 = [2.3324]
y5 = [0.0090]
x6 = [3.4841]
y6 = [0.0084]
x7 = [4.8213]
y7 = [0.0080]
x8 = [5.5500]
y8 = [0.0044]
x9 = [6.2771]
y9 = [0.0022]
x10 = [6.8617]
y10 = [0.0009]
x11 = [7.4797]
y11 = [0.00047]

fig,ax=plt.subplots()
ax.plot(L_accr_y,Mdot_Yoshida,linewidth=2., label="Yoshida Z = 0")
plt.plot(x1, y1, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x2, y2, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x3, y3, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x4, y4, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x5, y5, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x6, y6, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x7, y7, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x8, y8, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x9, y9, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x10, y10, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.plot(x11, y11, marker="o", markersize=4, markeredgecolor="red", markerfacecolor="green")
plt.text(2.451, 0.037, '1.666M$_{\odot}$', fontsize = 8)
plt.text(2.537, 0.031, '1.706M$_{\odot}$', fontsize = 8)
plt.text(2.502, 0.023, '2.719M$_{\odot}$', fontsize = 8)
plt.text(2.412, 0.015, '4.782M$_{\odot}$', fontsize = 8)
plt.text(2.455, 0.010, '11.11M$_{\odot}$', fontsize = 8)
plt.text(3.306, 0.010, '12.38M$_{\odot}$', fontsize = 8)
plt.text(4.703, 0.010, '13.30M$_{\odot}$', fontsize = 8)
plt.text(5.468, 0.006, '32.67M$_{\odot}$', fontsize = 8)
plt.text(6.130, 0.004, '103.1M$_{\odot}$', fontsize = 8)
plt.text(6.749, 0.003, '314.0M$_{\odot}$', fontsize = 8)
plt.text(7.104, 0.0012, '465.8M$_{\odot}$', fontsize = 8)

ax.set_xlabel('log[L/L$_{\odot}$]')
ax.set_ylabel('Maccr [M$_{\odot}$/year]')
#plt.xlim([0, 900])

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

#ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()
