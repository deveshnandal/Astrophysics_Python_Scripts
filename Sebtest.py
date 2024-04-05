L_sun = gtb.Cst.Lsol
M_sun = gtb.Cst.Msol
H1_frac = gtb.Get_Var('H1', 1)
M_r = gtb.Get_Var('Mr', 1)
Shell = gtb.Get_Var('shell',1)
L_r_prime = gtb.Get_Var('L', 1)
eps_reac=gtb.Get_Var('eps_reac',1)
epsnu=gtb.Get_Var('epsnu',1)
eps_nuc=eps_reac
Shell_min = int(Shell[M_r<=12261.7898][0])
avg_H1_frac = np.full(shape=(len(H1_frac)), fill_value=np.nan)
delta_M_r = np.full(shape=(len(M_r)), fill_value=np.nan)
for k in range(len(H1_frac)-2,len(H1_frac)-2-Shell_min,-1):
    avg_H1_frac[k] = 0.5 * (H1_frac[k+1] + H1_frac[k])
    delta_M_r[k] = M_r[k] - M_r[k+1]
H1_integral = np.full(shape=(len(avg_H1_frac)), fill_value=np.nan)
H1_integral[len(avg_H1_frac)-1] = 0
for k in range(len(H1_frac)-2,len(H1_frac)-2-Shell_min,-1):
    H1_integral[k] = H1_integral[k + 1] + avg_H1_frac[k] * delta_M_r[k] * (M_sun)
avg_eps_nuc = np.full(shape=(len(eps_nuc)), fill_value=np.nan)
for k in range(len(H1_frac)-2,len(H1_frac)-2-Shell_min,-1):
    avg_eps_nuc[k] = 0.5 * (eps_nuc[k+1] + eps_nuc[k])
L_nuc = np.full(shape=(len(avg_eps_nuc)), fill_value=np.nan)
L_nuc[len(avg_eps_nuc)-1] = 0
for k in range(len(H1_frac)-2,len(H1_frac)-2-Shell_min,-1):
    L_nuc[k] = L_nuc[k + 1] + avg_eps_nuc[k] * delta_M_r[k] * (M_sun)
#""add a new variable that is the integral upto the point 12500""
plt.figure()
# #plt.plot(M_r[1:], H1_integral, linestyle='dashed', label=r'$H1_{integral}$')""
plt.plot(M_r[1:], H1_integral, linestyle='dashed', label=r'$H1_{integral}$')
plt.legend(loc='lower right')
plt.show()
