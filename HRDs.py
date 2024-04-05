Plotting HRDs

gtb.loadE('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat',5)

gtb.set_lineWidth(2.8)
gtb.CBLimits(min=0.5,max=0.75)
gtb.Limits(xmax=5.2)
gtb.mark_phase('H',colour='0.10')
gtb.HRD_plot()
gtb.isoRadius(fontsize=12)
############################# If you need a third axis in HRD (for instance H1c)
gtb.loadE('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/devesh/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.dat',3)
gtb.loadE('/Users/devesh/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',4)
gtb.loadE('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/1e-3_Maccr/End_Hburning_ini_GeorgesTest/P002z0S0.dat',5)
gtb.set_lineWidth(3)
gtb.CBLimits(min=0,max=0.7512)
gtb.Limits(xmax=5.2)
gtb.mark_phase('H',colour='0.10')
gtb.HRD_plot(zcol='H1c')
gtb.isoRadius(fontsize=12)
x1 = [4.888]
y1 = [7.80]
x2 = [3.772]
y2 = [7.99]
plt.plot(x1, y1, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="black")
plt.plot(x2, y2, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="black")
x3 = [3.795]
y3 = [8.69]
x4 = [4.166]
y4 = [8.99]
plt.plot(x3, y3, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
plt.plot(x4, y4, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green")
x5 = [3.817]
y5 = [9.24]
x6 = [3.936]
y6 = [9.70]
plt.plot(x5, y5, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="blue")
plt.plot(x6, y6, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="blue")
x7 = [3.871]
y7 = [9.30]
x8 = [4.012]
y8 = [9.96]
plt.plot(x7, y7, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="yellow")
plt.plot(x8, y8, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="yellow")
x9 = [3.906]
y9 = [9.89]
x10 = [4.006]
y10 = [10.37]
plt.plot(x9, y9, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="white")
plt.plot(x10, y10, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="white")

gtb.add_label(4.162,7.98,'$10^{-3}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.197,9.00,'$10^{-2}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.303,9.88,'$10^{-1}M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.185,9.46,'$1M_{\odot}/yr$',fontsize=12)
gtb.add_label(4.276,10.28,'$10M_{\odot}/yr$',fontsize=12)
############################
#Z0 ZAMS line:
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


#New place
gtb.add_label(4.1780,1.4194, '2',fontsize=14)
gtb.add_label(4.3560,2.1250, '3',fontsize=14)
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


Z14 ZAMS line:
gtb.dotxy(3.6882,0.5909,'ro')
gtb.dotxy(3.7243,0.3660,'ro')
gtb.dotxy(3.7543,0.1380,'ro')
gtb.dotxy(3.9727,1.2088,'ro')
gtb.dotxy(4.1044,1.8989,'ro')
gtb.dotxy(4.1864,2.3653,'ro')
gtb.dotxy(4.2470,2.7127,'ro')
gtb.dotxy(4.3320,3.2203,'ro')
gtb.dotxy(4.3640,3.4166,'ro')
gtb.dotxy(4.3916,3.5843,'ro')
gtb.dotxy(4.4163,3.7304,'ro')
gtb.dotxy(4.4560,3.9774,'ro')
gtb.dotxy(4.4876,4.1793,'ro')
gtb.dotxy(4.5011,4.2663,'ro')
gtb.dotxy(4.5246,4.4216,'ro')
gtb.dotxy(4.5532,4.6148,'ro')
gtb.dotxy(4.5688,4.7241,'ro')
gtb.dotxy(4.5887,4.8659,'ro')
gtb.dotxy(4.6230,5.1250,'ro')
gtb.dotxy(4.6497,5.3431,'ro')
gtb.dotxy(4.6890,5.7030,'ro')
gtb.dotxy(4.7134,5.9803,'ro')
gtb.dotxy(4.7296,6.2310,'ro')

Label:


gtb.dotxy(4.7296,6.2310,'ro')
gtb.add_label(4.7000,6.2310, '120',fontsize=14)
gtb.dotxy(4.7134,5.9803,'ro')
gtb.add_label(4.6934,5.9603, '85',fontsize=14)
gtb.dotxy(4.6890,5.7030,'ro')
gtb.add_label(4.6890,5.7030, '60',fontsize=14)
gtb.dotxy(4.6497,5.3431,'ro')
gtb.add_label(4.6497,5.3431, '40',fontsize=14)
gtb.dotxy(4.6230,5.1250,'ro')
gtb.add_label(4.6230,5.1250, '32',fontsize=14)
gtb.dotxy(4.5532,4.6148,'ro')
gtb.add_label(4.5532,4.6148, '20',fontsize=14)
gtb.dotxy(4.5011,4.2663,'ro')
gtb.add_label(4.5011,4.2663, '15',fontsize=14)
gtb.dotxy(4.4560,3.9774,'ro')
gtb.add_label(4.4560,3.9774, '12',fontsize=14)
gtb.dotxy(4.3916,3.5843,'ro')
gtb.add_label(4.3916,3.5843, '9',fontsize=14)
gtb.dotxy(4.3320,3.2203,'ro')
gtb.add_label(4.3320,3.2203, '7',fontsize=14)
gtb.dotxy(4.2470,2.7127,'ro')
gtb.add_label(4.2470,2.7127, '5',fontsize=14)
gtb.dotxy(4.1864,2.3653,'ro')
gtb.add_label(4.1864,2.3653, '4',fontsize=14)
gtb.dotxy(4.1044,1.8989,'ro')
gtb.add_label(4.1044,1.8989, '3',fontsize=14)
gtb.dotxy(3.9727,1.2088,'ro')
gtb.add_label(3.9727,1.2088, '2',fontsize=14)
