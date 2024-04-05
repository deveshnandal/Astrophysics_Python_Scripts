################### Making a Grid on plots on one figure ##################


H2_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[93])
Y3_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[31])
Li7_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[95])
X_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[6])
R_1 = 10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[4])
C12_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[8])
O16_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[9])
N15_1 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',skip_header=3))[34])

gtb.loadS('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0039151',1)
E_reac_1=gtb.Get_Var('eps_reac',1)
gtb.Set_Var(E_reac_1,'E_reac',1,label="$eps_reac\ [ergs/g/s]$",category="energy")

################## 47571 ######################
H2_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[93])
Y3_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[31])
Li7_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[95])
X_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[6])
C12_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[8])
O16_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[9])
N15_2 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[34])
R_2 = 10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',skip_header=3))[4])

gtb.loadS('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0047571',2)
E_reac_2=gtb.Get_Var('eps_reac',2)
gtb.Set_Var(E_reac_2,'E_reac',2,label="$eps_reac\ [ergs/g/s]$",category="energy")

################## 50221 ######################
H2_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[93])
Y3_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[31])
Li7_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[95])
X_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[6])
C12_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[8])
O16_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[9])
N15_3 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[34])
R_3 = 10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',skip_header=3))[4])

gtb.loadS('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050221',3)
E_reac_3=gtb.Get_Var('eps_reac',3)
gtb.Set_Var(E_reac_3,'E_reac',3,label="$eps_reac\ [ergs/g/s]$",category="energy")

################## 52071 ######################
H2_4 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[93])
Y3_4 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[31])
Li7_4 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[95])
X_4 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[6])
C12_4 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[8])
O16_4 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[9])
N15_4 = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[34])
R_4 = 10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',skip_header=3))[4])

gtb.loadS('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0052071',4)
E_reac_4=gtb.Get_Var('eps_reac',4)
gtb.Set_Var(E_reac_4,'E_reac',4,label="$eps_reac\ [ergs/g/s]$",category="energy")

fig, axs = plt.subplots(3, 4)
axs[0, 0].plot(R_1, E_reac_1)
axs[0, 0].set_title('3330 Years', fontsize=8)
axs[0, 0].tick_params(axis='y', labelsize=3)
axs[0, 0].tick_params(axis='x', labelsize=3)
axs[0, 0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
axs[0, 0].set_ylabel('Energy $[ergs/g/s]$', fontsize = 6)
#axs[0, 0].set_xticks([0.5e12, 1e12, 1.5e12, 2e12])
axs[0, 0].set_xscale('log')
axs[0, 0].set_yscale('log')
axs[0, 1].plot(R_2, E_reac_2)
axs[0, 1].tick_params(axis='y', labelsize=3)
axs[0, 1].set_title('9890 Years', fontsize=8)
axs[0, 1].tick_params(axis='y', labelsize=3)
axs[0, 1].tick_params(axis='x', labelsize=3)
axs[0, 1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
axs[0, 1].set_xscale('log')
axs[0, 1].set_yscale('log')
axs[0, 2].plot(R_3, E_reac_3)
axs[0, 2].tick_params(axis='y', labelsize=3)
axs[0, 2].set_title('13880 Years', fontsize=8)
axs[0, 2].tick_params(axis='y', labelsize=3)
axs[0, 2].tick_params(axis='x', labelsize=3)
axs[0, 2].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
axs[0, 2].set_xscale('log')
axs[0, 2].set_yscale('log')
axs[0, 3].plot(R_4, E_reac_4)
axs[0, 3].tick_params(axis='y', labelsize=3)
axs[0, 3].set_title('17000 Years', fontsize=8)
axs[0, 3].tick_params(axis='y', labelsize=3)
axs[0, 3].tick_params(axis='x', labelsize=3)
axs[0, 3].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
axs[0, 3].set_xscale('log')
axs[0, 3].set_yscale('log')
axs[1, 0].plot(R_1, H2_1,label="H2")
axs[1, 0].plot(R_1, Y3_1,label="Y3")
axs[1, 0].plot(R_1, Li7_1,label="Li7")
axs[1, 0].plot(R_1, X_1,label="H1")
axs[1, 0].set_xscale('log')
axs[1, 0].set_yscale('log')
#axs[1, 0].set_title('Surface Abundance', fontsize=6)
leg_1 = axs[1, 0].legend(loc='lower left', shadow=True,prop={'size': 4})
axs[1, 0].tick_params(axis='y', labelsize=3)
axs[1, 0].tick_params(axis='x', labelsize=3)
axs[1, 0].set_ylabel('Abundance Profile', fontsize = 6)
axs[1, 0].set_xscale('log')
axs[1, 0].set_yscale('log')
axs[1, 1].plot(R_2, H2_2)
axs[1, 1].plot(R_2, Y3_2)
axs[1, 1].plot(R_2, Li7_2)
axs[1, 1].plot(R_2, X_2)
#axs[1, 1].set_xscale('log')
axs[1, 1].set_yscale('log')
axs[1, 1].tick_params(axis='y', labelsize=3)
axs[1, 1].tick_params(axis='x', labelsize=3)
#axs[1, 1].set_title('Surface Abundance', fontsize=6)
axs[1, 1].set_xscale('log')
axs[1, 1].set_yscale('log')
axs[1, 2].plot(R_3, H2_3)
axs[1, 2].plot(R_3, Y3_3)
axs[1, 2].plot(R_3, Li7_3)
axs[1, 2].plot(R_3, X_3)
#axs[1, 2].set_xscale('log')
axs[1, 2].set_yscale('log')
axs[1, 2].tick_params(axis='y', labelsize=3)
axs[1, 2].tick_params(axis='x', labelsize=3)
#axs[1, 2].set_title('Surface Abundance', fontsize=6)
axs[1, 2].set_xscale('log')
axs[1, 2].set_yscale('log')
axs[1, 3].plot(R_4, H2_4)
axs[1, 3].plot(R_4, Y3_4)
axs[1, 3].plot(R_4, Li7_4)
axs[1, 3].plot(R_4, X_4)
#axs[1, 3].set_xscale('log')
axs[1, 3].set_yscale('log')
axs[1, 3].tick_params(axis='y', labelsize=3)
axs[1, 3].tick_params(axis='x', labelsize=3)
#axs[1, 3].set_title('Surface Abundance', fontsize=6)
axs[1, 3].set_xscale('log')
axs[1, 3].set_yscale('log')
axs[2, 0].plot(R_1, C12_1,label="C12")
axs[2, 0].plot(R_1, N15_1,label="N14")
axs[2, 0].plot(R_1, O16_1,label="O16")
#axs[2, 0].set_xscale('log')
axs[2, 0].set_yscale('log')
axs[2, 0].tick_params(axis='y', labelsize=3)
axs[2, 0].tick_params(axis='x', labelsize=3)
#axs[2, 0].set_title('Surface Abundance', fontsize=6)
leg_3 = axs[2, 0].legend(loc='lower left', shadow=True,prop={'size': 4})
axs[2, 0].set_ylabel('Abundance Profile', fontsize = 6)
axs[2, 0].set_xscale('log')
axs[2, 0].set_yscale('log')
axs[2, 0].set_ylim([1e-32, 1e-24])


axs[2, 1].plot(R_2, C12_2)
axs[2, 1].plot(R_2, N15_2)
axs[2, 1].plot(R_2, O16_2)
#axs[2, 1].set_xscale('log')
axs[2, 1].set_yscale('log')
axs[2, 1].tick_params(axis='y', labelsize=3)
axs[2, 1].tick_params(axis='x', labelsize=3)
#axs[2, 1].set_title('Surface Abundance', fontsize=6)
axs[2, 1].set_xscale('log')
axs[2, 1].set_yscale('log')
axs[2, 1].set_ylim([1e-32, 1e-24])

axs[2, 2].plot(R_3, C12_3)
axs[2, 2].plot(R_3, N15_3)
axs[2, 2].plot(R_3, O16_3)
#axs[2, 2].set_xscale('log')
axs[2, 2].set_yscale('log')
axs[2, 2].tick_params(axis='y', labelsize=3)
axs[2, 2].tick_params(axis='x', labelsize=3)
#axs[2, 2].set_title('Surface Abundance', fontsize=6)
axs[2, 2].set_xscale('log')
axs[2, 2].set_yscale('log')
axs[2, 2].set_ylim([1e-20, 1e-14])

axs[2, 3].plot(R_4, C12_4)
axs[2, 3].plot(R_4, N15_4)
axs[2, 3].plot(R_4, O16_4)
#axs[2, 3].set_xscale('log')
axs[2, 3].set_yscale('log')
axs[2, 3].tick_params(axis='y', labelsize=3)
axs[2, 3].tick_params(axis='x', labelsize=3)
#axs[2, 3].set_title('Surface Abundance', fontsize=6)
axs[2, 3].set_xscale('log')
axs[2, 3].set_yscale('log')
axs[2, 3].set_ylim([1e-16, 1e-10])

axs[2,0].set_xlabel('Radius $[cm]$', fontsize=8)
axs[2,1].set_xlabel('Radius $[cm]$', fontsize=8)
axs[2,2].set_xlabel('Radius $[cm]$', fontsize=8)
axs[2,3].set_xlabel('Radius $[cm]$', fontsize=8)

##############
plt.subplots_adjust(wspace=0,hspace=0)
###############
for ax in axs.flat:
    ax.set(xlabel='Radius $[cm]$', ylabel='y-label')
    ax.set_xlabel('Radius $[cm]$', fontsize=8)

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

axs[0,0].set_ylabel('Radius $[cm]$', fontsize=8)
axs[1,0].set_ylabel('Radius $[cm]$', fontsize=8)
axs[2,0].set_ylabel('Radius $[cm]$', fontsize=8)









fig,ax=plt.subplots()
plt.plot(R,E_reac_1,color='red',linestyle='solid',linewidth=2,label='eps reac')

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
