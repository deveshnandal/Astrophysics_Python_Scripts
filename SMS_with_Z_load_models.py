####### SMS models with metallicity
# 1e-3Msun_yr_1e-6 End of Silicon burning, Mfin = 3.2k ish
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.dat',1)

# 1e-2Msun_yr_1e-6 End H burning, phase = 2, Mfin = 26005
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-2Msun_yr_1e-6/P002z0S0.dat',2)

# 1e-1 Msun_yr_1e-6, Mass 53k GR instability not reached
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1e-1Msun_yr_1e-6/P002z0S0.dat',3)

# 1 Msun_yr_1e-6 Xc=0.57, Mass 259226 GR instability reached
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1Msun_yr_1e-6/P010Z0S0.dat',3)
# Model at GR Inst
gtb.loadS('/Users/hermit/Observatory/StarCalc/SMS/1Msun_yr_1e-6/P010z0S0.v0146931',3)


# 10 Msun_yr_1e-6 Xc=0.696, Mass 467k-GR instability reached
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/10Msun_yr_1e-6/P010Z0S0.dat',5)

# 100 Msun_yr_1e-6 Xc=0.7078, Mass 718212-GR instability reached
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/100Msun_yr_1e-6/P010Z0S0.dat',6)


######### Z = 0.014 ##########

# 1 Msun_yr_0.014 Xc=0.5543, Mass 417k-GR instability reached
gtb.loadE('/Users/hermit/Observatory/StarCalc/SMS/1Msun_yr_0.014/P010Z0S0.dat',4)
