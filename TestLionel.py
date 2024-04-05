gtb.loadS('Observatory/StarCalc/SMS/Z0_Accr_1e-2_fitm0.990_vcorrected_nodeut/P002z0S0.v0064961',1)
gtb.loadS('Observatory/StarCalc/SMS/Z0_Accr_1e-2_fitm0.990_vcorrected_nodeut/P002z0S0.v0064971',2)

L_sun = gtb.Cst.Lsol
M_sun = gtb.Cst.Msol
H1_frac1 = gtb.Get_Var('H1', 1)
M_r1 = gtb.Get_Var('Mr', 1)
L_r_prime = gtb.Get_Var('L', 1)
eps_reac1=gtb.Get_Var('eps_reac',1)
epsnu1=gtb.Get_Var('epsnu',1)
eps_nuc1=eps_reac1

avg_H1_frac1 = np.full(shape=(len(H1_frac1)-1), fill_value=np.nan)
delta_M_r1 = np.full(shape=(len(M_r1)-1), fill_value=np.nan)

myindex1 = np.where(M_r1-11644.6326 < 1.e-5)[0][0]

for k in range(len(H1_frac1)-2,myindex1,-1):
  avg_H1_frac1[k] = 0.5 * (H1_frac1[k+1] + H1_frac1[k])
  delta_M_r1[k] = M_r1[k] - M_r1[k+1]

H1_integral1 = np.full(shape=(len(avg_H1_frac1)), fill_value=np.nan)
H1_integral1[len(avg_H1_frac1)-1] = 0
for k in range(len(avg_H1_frac1)-2,myindex1,-1):
  H1_integral1[k] = H1_integral1[k + 1] + avg_H1_frac1[k] * delta_M_r1[k] * (M_sun)


avg_eps_nuc1 = np.full(shape=(len(eps_nuc1)-1), fill_value=np.nan)


for k in range(len(eps_nuc1)-1):
  avg_eps_nuc1[k] = 0.5 * (eps_nuc1[k+1] + eps_nuc1[k])


L_nuc1 = np.full(shape=(len(avg_eps_nuc1)), fill_value=np.nan)

L_nuc1[len(avg_eps_nuc1)-1] = 0
for k in range(len(avg_eps_nuc1)-2,myindex1,-1):
  L_nuc1[k] = L_nuc1[k + 1] + avg_eps_nuc1[k] * delta_M_r1[k] * (M_sun)

H1_frac2 = gtb.Get_Var('H1', 2)
M_r2 = gtb.Get_Var('Mr', 2)
L_r_prime2 = gtb.Get_Var('L', 2)
eps_reac2=gtb.Get_Var('eps_reac',2)
epsnu2=gtb.Get_Var('epsnu',2)
eps_nuc2=eps_reac2

avg_H1_frac2 = np.full(shape=(len(H1_frac2)-1), fill_value=np.nan)
delta_M_r2 = np.full(shape=(len(M_r2)-1), fill_value=np.nan)

myindex2 = np.where(M_r2-11644.6326 < 1.e-5)[0][0]

for k in range(len(H1_frac2)-2,myindex2,-1):
  avg_H1_frac2[k] = 0.5 * (H1_frac2[k+1] + H1_frac2[k])
  delta_M_r2[k] = M_r2[k] - M_r2[k+1]

H1_integral2 = np.full(shape=(len(avg_H1_frac2)), fill_value=np.nan)
H1_integral2[len(avg_H1_frac2)-1] = 0
for k in range(len(avg_H1_frac2)-2,myindex2,-1):
  H1_integral2[k] = H1_integral2[k + 1] + avg_H1_frac2[k] * delta_M_r2[k] * (M_sun)


avg_eps_nuc2 = np.full(shape=(len(eps_nuc2)-1), fill_value=np.nan)


for k in range(len(eps_nuc2)-1):
  avg_eps_nuc2[k] = 0.5 * (eps_nuc2[k+1] + eps_nuc2[k])


L_nuc2 = np.full(shape=(len(avg_eps_nuc2)), fill_value=np.nan)

L_nuc2[len(avg_eps_nuc2)-1] = 0
for k in range(len(avg_eps_nuc2)-2,myindex2,-1):
  L_nuc2[k] = L_nuc2[k + 1] + avg_eps_nuc2[k] * delta_M_r2[k] * (M_sun)

print(H1_integral1)
H1 = H1_integral1[myindex1+1]
print(len(H1_integral1))
print(myindex1)
print(myindex2)
print(M_r1[myindex1])
print(M_r2[myindex2])
print(M_r2[myindex2-1])
L1 = L_nuc1[myindex1+1]

H2 = H1_integral2[myindex2+1]
L2 = L_nuc2[myindex2+1]
print(H1)
print(H2)
Energy_nuc = (H1-H2)*0.007*gtb.Cst.c**2.
Energy_lum = 0.5*(L1 - L2)*(gtb.Get_Var('age',2)-gtb.Get_Var('age',1))*365.25*24.*3600.

Energy_nuc
Energy_lum
