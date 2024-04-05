
###################################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.391713135E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test3/P010z0S0_StrucData_0132111.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test3/P010z0S0_StrucData_0132111.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test3/P010z0S0_StrucData_0132111.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test3/P010z0S0_StrucData_0132111.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test3/P010z0S0.v0132111',skip_header=311))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])



reversed_egrav = egrav[::-1]


First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

#np.savetxt('/Users/devesh/desktop/Test3/Test3.txt', reversed_egrav, delimiter=' ')
np.savetxt('/Users/devesh/desktop/Test3/Test3.txt', G_rel, delimiter=' ')

######################################



np.delete(Mr, -1)
np.delete(P, -1)
np.delete(rho, -1)
np.delete(r, -1)

############### Plot G_rel vs Mr #################
M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.391713135E+05
R_sun=1.066966852E+15


P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0_StrucData_0197321.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0_StrucData_0197321.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0_StrucData_0197321.dat',skip_header=12))[2])/M_sun
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0_StrucData_0197321.dat',skip_header=12))[1]))
First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))

G_rel = G*(1 + First + Second + Third)
G_rel_b = G*(1+First + Third_b)
G_rel_G = (1 + First + Second + Third)


fig,ax=plt.subplots()
ax.plot(Mr,G_rel_b,color='tab:blue',linewidth=4.,label='I$_1$')
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('Grel [$cm^{3}g^{-1}s{-2}$]')
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()
############### Plot G_rel vs Mr #################
M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.391713135E+05
R_sun=1.066966852E+15


P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0_StrucData_0197321.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0_StrucData_0197321.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0_StrucData_0197321.dat',skip_header=12))[2])/M_sun
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0_StrucData_0197321.dat',skip_header=12))[1]))
First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))

G_rel = G*(1 + First + Second + Third)
G_rel_b = G*(1+First + Third_b)
G_rel_G = (1 + First + Second + Third)


fig,ax=plt.subplots()
ax.plot(Mr,G_rel_b/G,color='tab:blue',linewidth=4.,label='I$_1$')
#ax.legend(loc='upper center', shadow=True,prop={'size': 8})
ax.set_xlabel('Mass [M$_{\odot}$]')
ax.set_ylabel('Grel/G')
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.show()

################ Same exercise for the 10Msun/yr model####################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 6.699665823E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0_StrucData_0108841.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0_StrucData_0108841.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0_StrucData_0108841.dat',skip_header=12))[2])/M_sun
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0_StrucData_0108841.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/Observatory/StarCalc/SMS/Z0_1e1_0.999/P010Z0S0.v0108841',skip_header=290))[27])
reversed_egrav = egrav[::-1]
# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))

G_rel = G*(1 + First + Second + Third)
G_rel_b = G*(1+First + Third_b)
G_rel_G = (1 + First + Second + Third)



#np.savetxt('/Users/devesh/desktop/Test3/Test3.txt', reversed_egrav, delimiter=' ')
np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', G_rel, delimiter=' ')
