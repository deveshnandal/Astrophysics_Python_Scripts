

############## 1e-3Msun_yr both end Si burning
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.dat',3)

gtb.set_lineWidth(2.6)
gtb.HRD_plot()
gtb.isoRadius(fontsize=11,line='dashdot',colour='0.4')
# Mass versus H1c
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.dat',2)
gtb.set_lineWidth(2.6)
gtb.defX('H1c')
gtb.Plot('M')

############## 1e-2Msun_yr
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-2Msun_yr_1e-6/P002z0S0.dat',2)
gtb.set_lineWidth(2.6)
gtb.HRD_plot()
gtb.isoRadius(fontsize=11,line='dashdot',colour='0.4')
# Mass versus H1c
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Test_Z0_1e-2_0.999_iover1/P002z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-2Msun_yr_1e-6/P002z0S0.dat',2)
gtb.set_lineWidth(2.6)
gtb.defX('H1c')
gtb.Plot('M')

############## 1Msun HRD comparison of different Z
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1Msun_yr_1e-6/P010Z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1Msun_yr_0.014/P010Z0S0.dat',4)
gtb.set_lineWidth(2.6)
gtb.HRD_plot()
gtb.isoRadius(fontsize=11,line='dashdot',colour='0.4')
# Mass versus H1c
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e0fromstart_iover0/P010Z0S0.dat',2)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1Msun_yr_1e-6/P010Z0S0.dat',3)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1Msun_yr_0.014/P010Z0S0.dat',4)
gtb.set_lineWidth(2.6)
gtb.defX('H1c')
gtb.Plot('M')

############## 10 Msun HRD
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/10Msun_yr_1e-6/P010Z0S0.dat',2)
gtb.set_lineWidth(2.6)
gtb.HRD_plot()
gtb.isoRadius(fontsize=11,line='dashdot',colour='0.4')
# Mass versus H1c
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/10Msun_yr_1e-6/P010Z0S0.dat',2)
gtb.set_lineWidth(2.6)
gtb.defX('H1c')
gtb.Plot('M')

############## 100 Msun_yr
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/100Msun_yr/P010z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/100Msun_yr_1e-6/P010Z0S0.dat',5)
gtb.set_lineWidth(2.6)
gtb.HRD_plot()
gtb.isoRadius(fontsize=11,line='dashdot',colour='0.4')
# Mass versus H1c
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/100Msun_yr/P010z0S0.dat',1)
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/100Msun_yr_1e-6/P010Z0S0.dat',5)
gtb.set_lineWidth(2.6)
gtb.defX('H1c')
gtb.Plot('M')
