gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat',5)
gtb.defX('M')
gtb.set_lineWidth(2.8)
gtb.logScale('x')
gtb.Plot('Tc')
x1 = [908]
y1 = [8.102]
x2 = [2822]
y2 = [8.122]
plt.plot(x1, y1, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="black")
plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="black")
x3 = [12950]
y3 = [8.134]
x4 = [22813]
y4 = [8.462]
plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x4, y4, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
x5 = [56516]
y5 = [8.148]
x6 = [144622]
y6 = [8.401]
plt.plot(x5, y5, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="blue")
plt.plot(x6, y6, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="blue")
x7 = [90408]
y7 = [8.195]
x8 = [309673]
y8 = [8.209]
plt.plot(x7, y7, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="yellow")
plt.plot(x8, y8, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="yellow")
x9 = [93385]
y9 = [8.216]
x10 = [631632]
y10 = [8.234]
plt.plot(x9, y9, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="white")
plt.plot(x10, y10, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="white")
gtb.put_legend(4,label=['$10M_{\odot}/yr$','$1M_{\odot}/yr$','$10^{-1}M_{\odot}/yr$','$10^{-2}M_{\odot}/yr$','$10^{-3}M_{\odot}/yr$'],fontsize=14)
