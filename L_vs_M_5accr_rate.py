
import numpy as np
import matplotlib.pyplot as plt
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat',5)
gtb.defX('M')
gtb.logScale('x')
gtb.set_lineWidth(2.8)
gtb.Plot('L')

x9 = [8915]
y9 = [8.46]
x10 = [537167]
y10 = [10.25]
#plt.plot(x9, y9, marker="o", markersize=10, markeredgecolor="grey", markerfacecolor="yellow")
#plt.plot(x10, y10, marker="o", markersize=10, markeredgecolor="grey", markerfacecolor="yellow")
gtb.put_legend(4,label=['$10M_{\odot}/yr$','$1M_{\odot}/yr$','$10^{-1}M_{\odot}/yr$','$10^{-2}M_{\odot}/yr$','$10^{-3}M_{\odot}/yr$'],fontsize=14)
gtb.add_label(185,9.35, '$M \propto L$',fontsize=18)
