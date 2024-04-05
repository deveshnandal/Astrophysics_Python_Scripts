########## Deuterium evolution versus mass ##################

####### The data for deuterium abundance is available in column 93; at the end of the .v file#########


Deut_A = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0028861',skip_header=3))[93])
Mr_A = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0028861',skip_header=3))[49])


Deut_B = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0029231',skip_header=3))[93])
Mr_B = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0029231',skip_header=3))[49])


Deut_C = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0031781',skip_header=3))[93])
Mr_C = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0031781',skip_header=3))[49])

Deut_D = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050521',skip_header=3))[93])
Mr_D = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0050521',skip_header=3))[49])

Deut_E = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0054991',skip_header=3))[93])
Mr_E = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0054991',skip_header=3))[49])

Deut_F = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0074911',skip_header=3))[93])
Mr_F = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0074911',skip_header=3))[49])

Deut_G = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0094391',skip_header=283))[93])
Mr_G = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0094391',skip_header=283))[49])

Deut_H = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0107881',skip_header=3))[93])
Mr_H = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0107881',skip_header=3))[49])

Deut_I = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0128651',skip_header=289))[93])
Mr_I = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/Isochrones_preMS/Yoshida_Accr_Law/End_HBurning_ini_Yoshida_Accr_Law/P002z0S0.v0128651',skip_header=289))[49])



fig,ax=plt.subplots()
ax.plot(Mr_A,Deut_A,linewidth=2., label="A")
ax.plot(Mr_B,Deut_B,linewidth=2., label="B")
ax.plot(Mr_C,Deut_C,linewidth=2., label="C")
ax.plot(Mr_D,Deut_D,linewidth=2., label="D")
ax.plot(Mr_E,Deut_E,linewidth=2., label="E")
ax.plot(Mr_F,Deut_F,linewidth=2., label="F")
ax.plot(Mr_G,Deut_G,linewidth=2., label="G")
ax.plot(Mr_H,Deut_H,linewidth=2., label="H")
ax.plot(Mr_I,Deut_I,linewidth=2., label="I")


ax.set_xlabel('Mass [Mr/M$_{\odot}$]')
ax.set_ylabel('Deuterium Abundance')
#plt.xlim([0, 900])

leg = plt.legend(loc='upper right', shadow=True,prop={'size': 8})

ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()

########### Choosing colours######

color = iter(cm.rainbow(np.linspace(0, 1, n)))
for i in range(n):
   c = next(color)
   plt.plot(x, y, c=c)

#########
