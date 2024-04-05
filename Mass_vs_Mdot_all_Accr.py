import math
import pandas as pd
import matplotlib.pyplot as plt

M_eq = [9,12,15,20,30,40,60,85,120]
Time_H = [1.77097e7,1.78575e7,1.29865e7,9.50960e6,6.16050e6,4.79495e6,3.66825e6,3.07592e6,2.73616e6]
Time_M_H = [17.7097,17.8575,12.9865,9.50960,6.16050,4.79495,3.66825,3.07592,2.73616]
Time_M_KH = [0.11959601031463714e6,0.12028039799771725e6,0.09771535195097131e6,0.07568678015787887e6,0.050245619730054925e6,0.039762161583578634e6,0.031222827442315186e6,0.027247214499731477e6,0.025142008661050923e6]

Time_KH = [2.60524075e+08,3.50767623e+08,4.86414778e+08,7.42381152e+08,1.22162262e+09,1.73796211e+09,2.89591148e+09,4.53339496e+09,7.11521010e+09]
Time_accr_2 = [900,1200,1500,2000,3000,4000,6000,8500,12000]
Time_accr_3 = [9000,12000,15000,20000,30000,40000,60000,85000,120000]
Time_accr_4 = [90000,120000,150000,200000,300000,400000,600000,850000,1200000]
Time_accr_5 = [900000,1200000,1500000,2000000,3000000,4000000,6000000,8500000,12000000]
Time_accr_6 = [9000000,12000000,15000000,20000000,30000000,40000000,60000000,85000000,120000000]
Time_accr_CH = [42857.14,34285.71,35714.28,31746.03,36585.36,42105.26,44776.11,44270.83,51282.05]
plt.plot(M_eq,Time_H, label='MS lifetime')
plt.plot(M_eq,Time_M_KH, label='KH contraction')
plt.plot(M_eq,Time_accr_2, label='10 -2 Accretion Time')
plt.plot(M_eq,Time_accr_3, label='10 -3 Accretion Time')
plt.plot(M_eq,Time_accr_4, label='10 -4 Accretion Time')
plt.plot(M_eq,Time_accr_5, label='10 -5 Accretion Time')
plt.plot(M_eq,Time_accr_6, label='10 -6 Accretion Time')
plt.plot(M_eq,Time_accr_CH, label='CH Accretion Time')
plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Various timescales versus Mass")
plt.xlabel("log(Mass when accretion stops)")
plt.ylabel("Log(Time in years)")
plt.legend(fontsize = 6)
plt.show()

###### The real deal !!!! ########

import math
import pandas as pd
import matplotlib.pyplot as plt
M_max = [22.939,82.131,406.95,2798.4,22155,112053,223591]
Accr_rate = [1.00e-6,1.00e-5,1.00e-4,1.00e-3,1.00e-2,1.00e-1,1.00]
M_max_blue = [22155,112053,223591]
Accr_rate_blue = [1.00e-2,1.00e-1,1.00]
x = [1.00e-5]
y = [82.34]
x1 = [0.01]
y1 = [22155]
x2 = [0.1]
y2 = [112053]
x3 = [1]
y3 = [223591]
a = 150
b = 250
plt.axhspan(a, b, color='y', alpha=0.5, lw=0)
a = 20
b = 150
plt.axhspan(a, b, color='g', alpha=0.5, lw=0)
a = 250
b = 308000
plt.axhspan(a, b, color='c', alpha=0.5, lw=0)
plt.plot(Accr_rate,M_max, color='black', linewidth=2.5)
plt.plot(Accr_rate_blue,M_max_blue, color='blue', linewidth=2.5)

plt.plot(x1, y1, marker="x", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x2, y2, marker="x", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x3, y3, marker="x", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x, y, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")

plt.text(0.0094, 12933, 'X$_c$=0.0', fontsize = 12)
plt.text(0.087, 59563, 'X$_c$=0.214', fontsize = 12)
plt.text(0.0880, 220501, 'X$_c$=0.518', fontsize = 12)

plt.text(0.02685, 160.5737, 'PISN', fontsize = 12)
plt.text(0.02685, 59.5737, 'Black Hole', fontsize = 12)
plt.text(0.02685, 439.5737, 'Black Hole', fontsize = 12)
plt.text(1.3563e-5, 1273, 'Z=0', fontsize = 16)
plt.text(1.3563e-5, 68.506, 'Z=0.014', fontsize = 12)
plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Maximum attainable mass")
plt.xlabel("Accretion rate (M$_{\odot}$/year)")
plt.ylabel("Mass(M$_{\odot}$) ")
#plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()

####################
import math
import pandas as pd
import matplotlib.pyplot as plt
M_max = [22.939,82.131,406.95,2798.4,22155,139177,215267]
t_MS = [22.247e+6,8.2417e+6,4.064e+6,2.7967e+6,2.2140e+6,0.1058e+6,0.2131e+6]
Time_accr_2 = [900,1200,1500,2000,3000,4000,6000,8500,12000]
Time_accr_6 = [9000000,12000000,15000000,20000000,30000000,40000000,60000000,85000000,120000000]
plt.plot(M_max,t_MS)

plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Time versus Mass")
plt.xlabel("Log(Mass)")
plt.ylabel("Timescale")
plt.show()


import math
import pandas as pd
import matplotlib.pyplot as plt
M_max = [22.939,82.131,406.95,2798.4,22155,139177,215267]
t_MS = [22.247e+6,8.2417e+6,4.064e+6,2.7967e+6,2.2140e+6,0.1058e+6,0.2131e+6]
M_max2 = [9,12,15,20,30,40,60,85,120]
t_MS2 = [1.77097e+07,1.78575e+7,1.29865e+07,9.50960e+06,6.16050e+6,4.79495e+06,3.66825e+06,3.07592e+06,2.73616e+06]

t_accr_6 = 1.00e+6*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-6_Maccr/P300Z0S0_ini_GeorgesTest/P002z0S0.dat'))[2])
M_6 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-6_Maccr/P300Z0S0_ini_GeorgesTest/P002z0S0.dat'))[2])
t_accr_5 = 1.00e+5*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3/P002z0S0.dat'))[2])
M_5 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-5_Maccr/P300Z0S0_ini_vvx3/P002z0S0.dat'))[2])
t_accr_4 = 1.00e+4*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-4_Maccr/End_HBurning_ini_GeorgesTest/P002z0S0.dat'))[2])
M_4 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-4_Maccr/End_HBurning_ini_GeorgesTest/P002z0S0.dat'))[2])
t_accr_3 = 1.00e+3*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
M_3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat'))[2])
t_accr_2 = 1.00e+2*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat'))[2])
M_2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat'))[2])
t_accr_1 = 1.00e+1*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])
M_1 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat'))[2])
t_accr_0 = 1.00e+0*(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat'))[2])
M_0 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat'))[2])

plt.plot(M_max2,t_MS2)
plt.plot(M_max,t_MS)
plt.plot(M_6,t_accr_6)
plt.plot(M_5,t_accr_5)
plt.plot(M_4,t_accr_4)
plt.plot(M_3,t_accr_3)
plt.plot(M_2,t_accr_2)
plt.plot(M_1,t_accr_1)
plt.plot(M_0,t_accr_0)
plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Time versus Mass")
plt.xlabel("Log(Mass)")
plt.ylabel("Timescale")
plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()
