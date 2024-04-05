############ 10 Msun at M = 200000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 2.0E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0098451.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0098451.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0098451.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0098451.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0.v0098451',skip_header=285))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', G_rel, delimiter=' ')

############ 10 Msun at M = 300000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 3.0E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0100361.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0100361.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0100361.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0100361.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0.v0100361',skip_header=287))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', G_rel, delimiter=' ')

############ 10 Msun at M = 400000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 4.0E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0102441.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0102441.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0102441.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0102441.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0.v0102441',skip_header=285))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', G_rel, delimiter=' ')


############ 10 Msun at M = 500000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 5.0E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0104611.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0104611.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0104611.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0_StrucData_0104611.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test4/P010Z0S0.v0104611',skip_header=287))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/Test4/Test4.txt', G_rel, delimiter=' ')

##################################################
############ 1 Msun at M = 250000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 2.5E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0_StrucData_0125081.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0_StrucData_0125081.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0_StrucData_0125081.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0_StrucData_0125081.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0.v0125081',skip_header=307))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/Test5/Test5.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/Test5/Test5.txt', G_rel, delimiter=' ')


############ 1 Msun at M = 150000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.5E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0_StrucData_0111201.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0_StrucData_0111201.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0_StrucData_0111201.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0_StrucData_0111201.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test5/P010Z0S0.v0111201',skip_header=293))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/Test5/Test5.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/Test5/Test5.txt', G_rel, delimiter=' ')

###################################
############ 0.1 Msun at M = 125000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.25E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0168061.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0168061.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0168061.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0168061.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0.v0168061',skip_header=957))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', G_rel, delimiter=' ')

############ 0.1 Msun at M = 115000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.15E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0153941.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0153941.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0153941.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0153941.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0.v0153941',skip_header=637))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', G_rel, delimiter=' ')

############ 0.1 Msun at M = 105000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.05E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0144231.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0144231.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0144231.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0144231.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0.v0144231',skip_header=342))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', G_rel, delimiter=' ')

############ 0.1 Msun at M = 110000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.10E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0148921.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0148921.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0148921.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0148921.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0.v0148921',skip_header=3))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', G_rel, delimiter=' ')

############ 0.1 Msun at M = 100000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 1.00E+05
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0140121.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0140121.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0140121.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0_StrucData_0140121.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.1Msun_G_rel/P002z0S0.v0140121',skip_header=3))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/0.1Msun_G_rel/0.1Msun.txt', G_rel, delimiter=' ')


########################################

############ 0.01 Msun at M = 22616 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 22616.0
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0304481.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0304481.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0304481.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0304481.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0.v0304481',skip_header=289))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/0.01Msun_G_rel/0.01Msun.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/0.01Msun_G_rel/0.01Msun.txt', G_rel, delimiter=' ')

############ 0.01 Msun at M = 19000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 19000.0
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0270251.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0270251.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0270251.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0270251.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0.v0270251',skip_header=327))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/0.01Msun_G_rel/0.01Msun.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/0.01Msun_G_rel/0.01Msun.txt', G_rel, delimiter=' ')


############ 0.01 Msun at M = 16000 #################

M_sun=1.9885e33
pi=3.141592653589793e0
c=2.99792458e10
G=6.67428e-8
M = 16000.0
R_sun=1.066966852E+15
P = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0248621.dat',skip_header=12))[5])
rho = 10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0248621.dat',skip_header=12))[4])
Mr = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0248621.dat',skip_header=12))[2])
r = (10**(np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0_StrucData_0248621.dat',skip_header=12))[1]))

egrav = (np.transpose(np.genfromtxt('/Users/devesh/desktop/0.01Msun_G_rel/P002z0S0.v0248621',skip_header=332))[27])

# If there is an element negative error and the file have multiple iterations of the data
# egrav_b = (np.transpose(np.genfromtxt('/Users/devesh/desktop/Test2/P002z0S0.v0078491',skip_header=3))[27])




reversed_egrav = egrav[::-1]

np.savetxt('/Users/devesh/desktop/0.01Msun_G_rel/0.01Msun.txt', reversed_egrav, delimiter=' ')

First = P/(rho*(c**2))
Second = 2*G*Mr/(r*(c**2))
Third = (4*pi*P*r**3)/(Mr*(c**2))

Third_b = 3*P/(rho*(c**2))


G_rel_b = G*(1+First + Third_b)
G_rel = G*(1 + First + Second + Third)

np.savetxt('/Users/devesh/desktop/0.01Msun_G_rel/0.01Msun.txt', G_rel, delimiter=' ')
