import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
M_max = [22.939,82.131,406.95,2798.4,22155,82006,100181,108053,223591]
M_max_2 = [3283,26157,118621,259564,467300,718212]
M_max_3 = []

Accr_rate = [1.00e-6,1.00e-5,1.00e-4,1.00e-3,1.00e-2,5.00e-2,7.5e-2,1.00e-1,1.00]
Accr_rate_2 = [1.00e-3,1.00e-2,1.00e-1,1.00,10.00,100.00]

M_max_blue = [22155,82006,100181,108053,223591,449661,697384, 1027570]
Accr_rate_blue = [1.00e-2,5.00e-2,7.5e-2,1.00e-1,1.00,10.00,100.00,1000.00]

x = [1.00e-5]
y = [82.34]
x1 = [0.01]
y1 = [22155]
x2 = [5.00e-2]
y2 = [82006]
x3 = [7.50e-2]
y3 = [100181]
x4 = [0.01]
y4 = [22155]
x5 = [0.1]
y5 = [108053]
x6 = [1]
y6 = [223591]
x7 = [10]
y7 = [449661]
x8 = [100]
y8 = [697384]
x9 = [1000]
y9 = [1027570]

p1 = [1.00e-3]
q1 = [3283]
p2 = [1.00e-2]
q2 = [26157]
p3 = [1.00e-1]
q3 = [53590]
p4 = [1.00]
q4 = [153264]
p5 = [10.00]
q5 = [467300]
p6 = [100.00]
q6 = [718212]

s1 = [1.00]
t1 = [467800]
a = 150
b = 250
plt.axhspan(a, b, color='grey', alpha=0.5, lw=0)
a = 20
b = 150
plt.axhspan(a, b, color='g', alpha=0.5, lw=0)
a = 250
b = 22155
plt.axhspan(a, b, color='c', alpha=0.5, lw=0)
a = 22155
b = 112053
plt.axhspan(a, b, color='y', alpha=0.5, lw=0)
a = 112053
b = 697384
plt.axhspan(a, b, color='r', alpha=0.4, lw=0)
a = 697384
b = 1360000
plt.axhspan(a, b, color='m', alpha=0.5, lw=0)

plt.plot(Accr_rate,M_max, color='black', linewidth=2.5)
plt.plot(Accr_rate_2,M_max_2, color='grey', linewidth=2.5)

plt.plot(Accr_rate_blue,M_max_blue, color='blue', linewidth=2.5)

plt.plot(x1, y1, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x2, y2, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x3, y3, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x4, y4, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x5, y5, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x6, y6, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x7, y7, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x8, y8, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x9, y9, marker="^", markersize=6, markeredgecolor="black", markerfacecolor="green")

plt.plot(p1, q1, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p2, q2, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p3, q3, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p4, q4, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p5, q5, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p6, q6, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")

plt.plot(s1, t1, marker="o", markersize=6, markeredgecolor="indigo", markerfacecolor="orange")

plt.text(0.0094, 12933, 'X$_c$=0.0', fontsize = 9, fontweight="bold")
plt.text(0.087, 59563, 'X$_c$=0.214', fontsize = 9, fontweight="bold")
plt.text(0.0780, 220501, 'X$_c$=0.525', fontsize = 9, fontweight="bold")
plt.text(0.8314, 519484, 'X$_c$=0.619', fontsize = 9, fontweight="bold")
plt.text(53, 388919, 'X$_c$=0.723', fontsize = 9, fontweight="bold")
plt.text(221.53, 596697, 'X$_c$=0.751', fontsize = 9, fontweight="bold")

plt.text(7.86e-5, 160.5737, 'PISN', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 59.5737, 'CCSBH', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 3239, 'CCMBH', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 37928, 'GRBH', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 248749, 'GRSMBH', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 815926, 'GRDCBH', fontsize = 11, fontweight="bold")

plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Maximum attainable mass", fontsize = 16, fontweight="bold")
plt.xlabel("Accretion rate (M$_{\odot}$/year)", fontsize = 16, fontweight="bold")
plt.ylabel("Mass(M$_{\odot}$) ", fontsize = 16, fontweight="bold")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
#plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()





################### Alternate cube helix colour


import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
M_max = [22.939,82.131,406.95,2798.4,22155,82006,100181,108053,223591]
M_max_2 = [3283,26157,118621,259564,467300,718212]
M_max_3 = []

Accr_rate = [1.00e-6,1.00e-5,1.00e-4,1.00e-3,1.00e-2,5.00e-2,7.5e-2,1.00e-1,1.00]
Accr_rate_2 = [1.00e-3,1.00e-2,1.00e-1,1.00,10.00,100.00]

M_max_blue = [22155,82006,100181,108053,223591,449661,697384, 1027570]
Accr_rate_blue = [1.00e-2,5.00e-2,7.5e-2,1.00e-1,1.00,10.00,100.00,1000.00]

x = [1.00e-5]
y = [82.34]
x1 = [0.01]
y1 = [22155]
x2 = [5.00e-2]
y2 = [82006]
x3 = [7.50e-2]
y3 = [100181]
x4 = [0.01]
y4 = [22155]
x5 = [0.1]
y5 = [108053]
x6 = [1]
y6 = [223591]
x7 = [10]
y7 = [449661]
x8 = [100]
y8 = [697384]
x9 = [1000]
y9 = [1027570]

p1 = [1.00e-3]
q1 = [3283]
p2 = [1.00e-2]
q2 = [26157]
p3 = [1.00e-1]
q3 = [53590]
p4 = [1.00]
q4 = [153264]
p5 = [10.00]
q5 = [467300]
p6 = [100.00]
q6 = [718212]

s1 = [1.00]
t1 = [467800]
a = 150
b = 250
plt.axhspan(a, b, color='#000000', alpha=0.5, lw=0)
a = 20
b = 150
plt.axhspan(a, b, color='#1b1e3b', alpha=0.5, lw=0)
a = 250
b = 22155
plt.axhspan(a, b, color='#16534c', alpha=0.5, lw=0)
a = 22155
b = 112053
plt.axhspan(a, b, color='#447731', alpha=0.5, lw=0)
a = 112053
b = 697384
plt.axhspan(a, b, color='#a1794a', alpha=0.5, lw=0)
a = 697384
b = 1360000
plt.axhspan(a, b, color='#d484a9', alpha=0.5, lw=0)

plt.plot(Accr_rate,M_max, color='black', linewidth=2.5)
plt.plot(Accr_rate_2,M_max_2, color='grey', linewidth=2.5)

plt.plot(Accr_rate_blue,M_max_blue, color='blue', linewidth=2.5)

plt.plot(x1, y1, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x2, y2, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x3, y3, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x4, y4, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x5, y5, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x6, y6, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x7, y7, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x8, y8, marker="o", markersize=6, markeredgecolor="black", markerfacecolor="green")
plt.plot(x9, y9, marker="^", markersize=6, markeredgecolor="black", markerfacecolor="green")

plt.plot(p1, q1, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p2, q2, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p3, q3, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p4, q4, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p5, q5, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")
plt.plot(p6, q6, marker="o", markersize=6, markeredgecolor="white", markerfacecolor="red")

plt.plot(s1, t1, marker="o", markersize=6, markeredgecolor="indigo", markerfacecolor="orange")

plt.text(0.0094, 12933, 'X$_c$=0.0', fontsize = 9, fontweight="bold")
plt.text(0.087, 59563, 'X$_c$=0.214', fontsize = 9, fontweight="bold")
plt.text(0.0780, 220501, 'X$_c$=0.525', fontsize = 9, fontweight="bold")
plt.text(0.8314, 519484, 'X$_c$=0.619', fontsize = 9, fontweight="bold")
plt.text(53, 388919, 'X$_c$=0.723', fontsize = 9, fontweight="bold")
plt.text(221.53, 596697, 'X$_c$=0.751', fontsize = 9, fontweight="bold")

plt.text(7.86e-5, 160.5737, 'PISN', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 59.5737, 'CCSBH', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 3239, 'CCMBH', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 37928, 'GRBH', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 248749, 'GRSMBH', fontsize = 11, fontweight="bold")
plt.text(7.86e-5, 815926, 'GRDCBH', fontsize = 11, fontweight="bold")

plt.yscale('log',base=10)
plt.xscale('log',base=10)
plt.title("Maximum attainable mass", fontsize = 16, fontweight="bold")
plt.xlabel("Accretion rate (M$_{\\odot}$/year)", fontsize = 16, fontweight="bold")
plt.ylabel("Mass(M$_{\\odot}$) ", fontsize = 16, fontweight="bold")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
#plt.subplots_adjust(top=0.992,bottom=0.088,left=0.083,right=0.99,hspace=0.2,wspace=0.2)
plt.show()
