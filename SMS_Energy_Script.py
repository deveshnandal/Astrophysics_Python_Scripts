gtb.loadS('Observatory/StarCalc/SMS/Z0_Accr_1e-2_fitm0.990_vcorrected_nodeut/P002z0S0.v0063961',1)
gtb.loadS('Observatory/StarCalc/SMS/Z0_Accr_1e-2_fitm0.990_vcorrected_nodeut/P002z0S0.v0063971',2)

L_sun = gtb.Cst.Lsol
M_sun = gtb.Cst.Msol
H1_frac1 = gtb.Get_Var('H1', 1)
M_r1 = gtb.Get_Var('Mr', 1)
L_r_prime = gtb.Get_Var('L', 1)
eps_reac1=gtb.Get_Var('eps_reac',1)
epsnu1=gtb.Get_Var('epsnu',1)
eps_nuc1=eps_reac1
My_mass=433.5805#56058.4013#47151.8234#12261.7898###14.8086
avg_H1_frac1 = np.full(shape=(len(H1_frac1)-1), fill_value=np.nan)
delta_M_r1 = np.full(shape=(len(M_r1)-1), fill_value=np.nan)

myindex = np.where(M_r1-My_mass < 1.e-5)[0][0]

for k in range(len(H1_frac1)-2,myindex,-1):
  avg_H1_frac1[k] = 0.5 * (H1_frac1[k+1] + H1_frac1[k])
  delta_M_r1[k] = M_r1[k] - M_r1[k+1]

H1_integral1 = np.full(shape=(len(avg_H1_frac1)), fill_value=np.nan)
H1_integral1[len(avg_H1_frac1)-1] = 0
for k in range(len(avg_H1_frac1)-2,myindex,-1):
  H1_integral1[k] = H1_integral1[k + 1] + avg_H1_frac1[k] * delta_M_r1[k] * (M_sun)


avg_eps_nuc1 = np.full(shape=(len(eps_nuc1)-1), fill_value=np.nan)


for k in range(len(eps_nuc1)-1):
  avg_eps_nuc1[k] = 0.5 * (eps_nuc1[k+1] + eps_nuc1[k])


L_nuc1 = np.full(shape=(len(avg_eps_nuc1)), fill_value=np.nan)

L_nuc1[len(avg_eps_nuc1)-1] = 0
for k in range(len(avg_eps_nuc1)-2,myindex,-1):
  L_nuc1[k] = L_nuc1[k + 1] + avg_eps_nuc1[k] * delta_M_r1[k] * (M_sun)

H1_frac2 = gtb.Get_Var('H1', 2)
M_r2 = gtb.Get_Var('Mr', 2)
L_r_prime2 = gtb.Get_Var('L', 2)
eps_reac2=gtb.Get_Var('eps_reac',2)
epsnu2=gtb.Get_Var('epsnu',2)
eps_nuc2=eps_reac2

avg_H1_frac2 = np.full(shape=(len(H1_frac2)-1), fill_value=np.nan)
delta_M_r2 = np.full(shape=(len(M_r2)-1), fill_value=np.nan)

myindex = np.where(M_r2-My_mass < 1.e-5)[0][0]

for k in range(len(H1_frac2)-2,myindex,-1):
  avg_H1_frac2[k] = 0.5 * (H1_frac2[k+1] + H1_frac2[k])
  delta_M_r2[k] = M_r2[k] - M_r2[k+1]

H1_integral2 = np.full(shape=(len(avg_H1_frac2)), fill_value=np.nan)
H1_integral2[len(avg_H1_frac2)-1] = 0
for k in range(len(avg_H1_frac2)-2,myindex,-1):
  H1_integral2[k] = H1_integral2[k + 1] + avg_H1_frac2[k] * delta_M_r2[k] * (M_sun)


avg_eps_nuc2 = np.full(shape=(len(eps_nuc2)-1), fill_value=np.nan)


for k in range(len(eps_nuc2)-1):
  avg_eps_nuc2[k] = 0.5 * (eps_nuc2[k+1] + eps_nuc2[k])


L_nuc2 = np.full(shape=(len(avg_eps_nuc2)), fill_value=np.nan)

L_nuc2[len(avg_eps_nuc2)-1] = 0
for k in range(len(avg_eps_nuc2)-2,myindex,-1):
  L_nuc2[k] = L_nuc2[k + 1] + avg_eps_nuc2[k] * delta_M_r2[k] * (M_sun)

H1 = H1_integral1[myindex+1]
L1 = L_nuc1[myindex+1]

H2 = H1_integral2[myindex+1]
L2 = L_nuc2[myindex+1]

Energy_nuc = (H1-H2)*0.007*gtb.Cst.c**2.#reservoir energy
Energy_lum = 0.5*(L1 + L2)*(gtb.Get_Var('age',2)-gtb.Get_Var('age',1))*365.25*24.*3600.#energy from actual burning

print("reservoir energy(Energy_nuc):",Energy_nuc)
print("actual energy(Energy_lum):",Energy_lum)
