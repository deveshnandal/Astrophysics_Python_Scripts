import numpy as np
import matplotlib.pyplot as plt
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat',5)
gtb.set_lineWidth(2.8)
gtb.defX('M')
gtb.logScale('x')
gtb.Plot('Teff')
x1 = [532.06]
y1 = [5.00]
x2 = [2645]
y2 = [3.768]
#plt.plot(x1, y1, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="black")
#plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="black")
x3 = [9060]
y3 = [3.772]
x4 = [22416]
y4 = [4.168]
#plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
#plt.plot(x4, y4, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
x5 = [87525]
y5 = [3.868]
x6 = [142298]
y6 = [3.902]
#plt.plot(x5, y5, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="blue")
#plt.plot(x6, y6, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="blue")
x7 = [121017]
y7 = [3.929]
x8 = [285579]
y8 = [4.011]
#plt.plot(x7, y7, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="yellow")
#plt.plot(x8, y8, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="yellow")
x9 = [111621]
y9 = [3.829]
x10 = [611495]
y10 = [3.995]
#plt.plot(x9, y9, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="white")
#plt.plot(x10, y10, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="white")
gtb.put_legend(1,label=['$10M_{\odot}/yr$','$1M_{\odot}/yr$','$10^{-1}M_{\odot}/yr$','$10^{-2}M_{\odot}/yr$','$10^{-3}M_{\odot}/yr$'],fontsize=14)
