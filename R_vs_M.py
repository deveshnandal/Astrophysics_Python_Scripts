######### Plot of radius versus mass for 5 atomically cooled halo models ##############
import numpy as np
import matplotlib.pyplot as plt
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat',5)
gtb.defX('M')
gtb.set_lineWidth(2.8)
gtb.logScale('x')
gtb.logScale('y')
gtb.Plot('R')
x0 = [1,10483]
y0 = [935,59080]
plt.plot(x0, y0,color='grey',linestyle='dashdot',linewidth=2.)
plt.text(15, 4371, "$R \propto M^{1/2}$",color='grey', fontsize = 18,rotation=33)
x1 = [2008]
y1 = [57.1]
x2 = [2822]
y2 = [9163]
#plt.plot(x1, y1, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="black")
#plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="black")
x3 = [14731]
y3 = [19218]
x4 = [22813]
y4 = [4368]
#plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
#plt.plot(x4, y4, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
x5 = [56516]
y5 = [29902]
x6 = [144622]
y6 = [34926]
#plt.plot(x5, y5, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="blue")
#plt.plot(x6, y6, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="blue")
x7 = [90408]
y7 = [26853]
x8 = [309673]
y8 = [30993]
#plt.plot(x7, y7, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="yellow")
#plt.plot(x8, y8, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="yellow")
x9 = [93385]
y9 = [41781]
x10 = [631632]
y10 = [49387]
#plt.plot(x9, y9, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="white")
#plt.plot(x10, y10, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="white")
gtb.put_legend(4,label=['$10M_{\odot}/yr$','$1M_{\odot}/yr$','$10^{-1}M_{\odot}/yr$','$10^{-2}M_{\odot}/yr$','$10^{-3}M_{\odot}/yr$'],fontsize=12)



############### Test for inline prints

import numpy as np
from matplotlib import pyplot as plt
from labellines import labelLines

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

X = np.linspace(0, 1, 500)
A = ["Hello"]

for a in A:
   plt.plot(X, np.arctan(a*X), label=str(a))

labelLines(plt.gca().get_lines(), zorder=2.5)

plt.show()
