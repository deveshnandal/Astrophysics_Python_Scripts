########## Li6, Li7 evolution versus mass for 0.1accr rate##################

####### The data for deuterium abundance is available in column 94,95; at the end of the .v file#########

H2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[93])
Li6 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[94])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[95])
Y3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[31])
X = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[6])
Y = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[7])
C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[9])
N15 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[34])
M_tot = 139171.11504
Mfrac = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0197311',skip_header=316))[49])



fig,ax=plt.subplots()
ax.plot(Mfrac,H2,linewidth=2., label="H2")
ax.plot(Mfrac,Li6,linewidth=2., label="Li6")
ax.plot(Mfrac,Li7,linewidth=2., label="Li7")
ax.plot(Mfrac,Y3,linewidth=2., label="He3")
ax.plot(Mfrac,X,linewidth=2., label="H1")
ax.plot(Mfrac,Y,linewidth=2., label="He4")
ax.plot(Mfrac,C12,linewidth=2., label="C12")
ax.plot(Mfrac,N15,linewidth=2., label="N15")
ax.plot(Mfrac,O16,linewidth=2., label="O16")
ax.set_xlabel('Mr [M$_{\odot}$]')
ax.set_ylabel('Abundance profile')
plt.xlim([0, 140000])

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

#ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

################## Deuterium, Li7, Helium 3 abundance plot for Yoshida track ##################################
################## Central CNO Abundance ######################################################################
################## This if for the very early evolution: the v files are 39151, 47571, 13881, 17001############
################## 39151 ######################
eps_nuc = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[10])

H2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[93])
Y3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[31])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[95])
X = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[6])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[4])

gtb.loadS('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',1)
E_reac=gtb.Get_Var('eps_reac',1)
gtb.Set_Var(E_reac,'E_reac',1,label="$eps_reac\ [ergs/g/s]$",category="energy")

fig,ax=plt.subplots()
plt.plot(R,E_reac,color='red',linestyle='solid',linewidth=2,label='eps reac')

plt.legend(loc='upper center', shadow=True,prop={'size': 6})

plt.xlabel('$M_r$')
plt.ylabel('Energy(ergs/g/s)')
plt.show()



fig,ax=plt.subplots()
ax.plot(R,H2,linewidth=2., label="H2")
ax.plot(R,Li7,linewidth=2., label="Li7")
ax.plot(R,Y3,linewidth=2., label="He3")
ax.plot(R,X,linewidth=2., label="H1")

ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Abundance profile')

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

#ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

##### CNO ####

C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[9])
N15 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[34])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[4])

fig,ax=plt.subplots()

ax.plot(R,C12,linewidth=2., label="C12")
ax.plot(R,N15,linewidth=2., label="N15")
ax.plot(R,O16,linewidth=2., label="O16")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Abundance profile')

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()



################## 47571 ######################
H2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[93])
Y3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[31])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[95])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[4])

fig,ax=plt.subplots()
ax.plot(R,H2,linewidth=2., label="H2")
ax.plot(R,Li7,linewidth=2., label="Li7")
ax.plot(R,Y3,linewidth=2., label="He3")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Abundance profile')

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

#ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

##### CNO ####

C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[9])
N15 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[34])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[4])

fig,ax=plt.subplots()

ax.plot(R,C12,linewidth=2., label="C12")
ax.plot(R,N15,linewidth=2., label="N15")
ax.plot(R,O16,linewidth=2., label="O16")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Abundance profile')

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

################## 50221 ######################
H2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[93])
Y3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[31])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[95])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[4])

fig,ax=plt.subplots()
ax.plot(R,H2,linewidth=2., label="H2")
ax.plot(R,Li7,linewidth=2., label="Li7")
ax.plot(R,Y3,linewidth=2., label="He3")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Abundance profile')

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

#ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

##### CNO ####

C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[9])
N15 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[34])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[4])

fig,ax=plt.subplots()

ax.plot(R,C12,linewidth=2., label="C12")
ax.plot(R,N15,linewidth=2., label="N15")
ax.plot(R,O16,linewidth=2., label="O16")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Abundance profile')

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

################## 52071 ######################
H2 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[93])
Y3 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[31])
Li7 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[95])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[4])

fig,ax=plt.subplots()
ax.plot(R,H2,linewidth=2., label="H2")
ax.plot(R,Li7,linewidth=2., label="Li7")
ax.plot(R,Y3,linewidth=2., label="He3")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Abundance profile')

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

#ax.set_xscale('log')
ax.set_yscale('log')
plt.show()

##### CNO ####

C12 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[8])
O16 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[9])
N15 = (np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[34])
R = 10**(np.transpose(np.genfromtxt('/Users/hermit/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[4])

fig,ax=plt.subplots()

ax.plot(R,C12,linewidth=2., label="C12")
ax.plot(R,N15,linewidth=2., label="N15")
ax.plot(R,O16,linewidth=2., label="O16")
ax.set_xlabel('Radius [cm]')
ax.set_ylabel('Abundance profile')

leg = plt.legend(loc='lower left', shadow=True,prop={'size': 7})

ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
