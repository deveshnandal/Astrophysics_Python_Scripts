import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# List of models
models = [
    {"path": '/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 2393, "label": "3053"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.v0129331.gz', "skip_header": 304, "cutoff": -87, "m_ejecta": 4865, "label": "6127"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0152721', "skip_header": 297, "cutoff": -68, "m_ejecta": 4156, "label": "4477"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1923M_SS6/P002z0S0.v0558831.gz', "skip_header": 334, "cutoff": -125, "m_ejecta": 1167, "label": "1923"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0217041.gz', "skip_header": 296, "cutoff": -118, "m_ejecta": 1022, "label": "1662"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.v0094231.gz', "skip_header": 309, "cutoff": -90, "m_ejecta": 1004, "label": "1331"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1135M_S20/P002z0S0.v0527201.gz', "skip_header": 2069, "cutoff": -117, "m_ejecta": 685, "label": "1135"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0276841.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 675, "label": "932"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/778M_SS39/P002z0S0.v0088411.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 605, "label": "778"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/771M_SS40/P002z0S0.v0090481.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 596, "label": "771"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0350111.gz', "skip_header": 310, "cutoff": -84, "m_ejecta": 377, "label": "491"},
    # Add more dictionaries for additional models
]

# Sort the models in ascending order of 'label'
models = sorted(models, key=lambda k: float(k['label']))

# Lists to hold the 90% mass abundances and star masses for the final plot
H_abundances = []
C_abundances = []
N_abundances = []
O_abundances = []
star_masses = []

# Lists to hold the 80% and 70% mass abundances for the final plot
H_abundances_80 = []
C_abundances_80 = []
N_abundances_80 = []
O_abundances_80 = []

H_abundances_70 = []
C_abundances_70 = []
N_abundances_70 = []
O_abundances_70 = []

for index, model in enumerate(models):

    file_path = model["path"]
    skip_header = model["skip_header"]
    cutoff = model["cutoff"]
    m_ejecta = model["m_ejecta"]
    label = float(model["label"])

    H1 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[6])[:cutoff][::-1]
    C12 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[8])[:cutoff][::-1]
    N14 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[33])[:cutoff][::-1]
    O16 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[9])[:cutoff][::-1]
    M_sol = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[49])[:cutoff][::-1]

    # Calculate the 90%, 80% and 70% mass points
    mass_90 = 0.9 * label
    mass_80 = 0.8 * label
    mass_70 = 0.7 * label

    # Find the indices where M_sol is closest to mass_90, mass_80, and mass_70
    idx_90 = np.abs(M_sol - mass_90).argmin()
    idx_80 = np.abs(M_sol - mass_80).argmin()
    idx_70 = np.abs(M_sol - mass_70).argmin()

    # Get the abundances at these masses
    H_90 = H1[idx_90]
    C_90 = C12[idx_90]
    N_90 = N14[idx_90]
    O_90 = O16[idx_90]

    H_80 = H1[idx_80]
    C_80 = C12[idx_80]
    N_80 = N14[idx_80]
    O_80 = O16[idx_80]

    H_70 = H1[idx_70]
    C_70 = C12[idx_70]
    N_70 = N14[idx_70]
    O_70 = O16[idx_70]

    # Print the abundances
    print(f"For star of mass {label} solar masses:")
    print(f"Abundances at 90% mass (approximately {mass_90} solar masses):")
    print(f"H: {H_90}, C: {C_90}, N: {N_90}, O: {O_90}")
    print()
    print(f"Abundances at 80% mass (approximately {mass_80} solar masses):")
    print(f"H: {H_80}, C: {C_80}, N: {N_80}, O: {O_80}")
    print()
    print(f"Abundances at 70% mass (approximately {mass_70} solar masses):")
    print(f"H: {H_70}, C: {C_70}, N: {N_70}, O: {O_70}")
    print()

    # Append the values to the lists for the final plot
    H_abundances.append(H_90)
    C_abundances.append(C_90)
    N_abundances.append(N_90)
    O_abundances.append(O_90)
    star_masses.append(label)

    H_abundances_80.append(H_80)
    C_abundances_80.append(C_80)
    N_abundances_80.append(N_80)
    O_abundances_80.append(O_80)

    H_abundances_70.append(H_70)
    C_abundances_70.append(C_70)
    N_abundances_70.append(N_70)
    O_abundances_70.append(O_70)

# List of all masses, including the ones not in the 'models' list
all_masses = [6127, 4477, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186, 1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

# Create interpolation functions
interp_H = interp1d(star_masses, H_abundances, kind='linear', fill_value='extrapolate')
interp_C = interp1d(star_masses, C_abundances, kind='linear', fill_value='extrapolate')
interp_N = interp1d(star_masses, N_abundances, kind='linear', fill_value='extrapolate')
interp_O = interp1d(star_masses, O_abundances, kind='linear', fill_value='extrapolate')

interp_H_80 = interp1d(star_masses, H_abundances_80, kind='linear', fill_value='extrapolate')
interp_C_80 = interp1d(star_masses, C_abundances_80, kind='linear', fill_value='extrapolate')
interp_N_80 = interp1d(star_masses, N_abundances_80, kind='linear', fill_value='extrapolate')
interp_O_80 = interp1d(star_masses, O_abundances_80, kind='linear', fill_value='extrapolate')

interp_H_70 = interp1d(star_masses, H_abundances_70, kind='linear', fill_value='extrapolate')
interp_C_70 = interp1d(star_masses, C_abundances_70, kind='linear', fill_value='extrapolate')
interp_N_70 = interp1d(star_masses, N_abundances_70, kind='linear', fill_value='extrapolate')
interp_O_70 = interp1d(star_masses, O_abundances_70, kind='linear', fill_value='extrapolate')

# Calculate and print the interpolated abundances
for mass in all_masses:
    if mass not in star_masses:
        H_interp = interp_H(mass)
        C_interp = interp_C(mass)
        N_interp = interp_N(mass)
        O_interp = interp_O(mass)
        print(f"For interpolated star of mass {mass} solar masses:")
        print(f"Interpolated abundances at 90% mass: H: {H_interp}, C: {C_interp}, N: {N_interp}, O: {O_interp}")
        print()

        H_interp_80 = interp_H_80(mass)
        C_interp_80 = interp_C_80(mass)
        N_interp_80 = interp_N_80(mass)
        O_interp_80 = interp_O_80(mass)
        print(f"For interpolated star of mass {mass} solar masses:")
        print(f"Interpolated abundances at 80% mass: H: {H_interp_80}, C: {C_interp_80}, N: {N_interp_80}, O: {O_interp_80}")
        print()

        H_interp_70 = interp_H_70(mass)
        C_interp_70 = interp_C_70(mass)
        N_interp_70 = interp_N_70(mass)
        O_interp_70 = interp_O_70(mass)
        print(f"For interpolated star of mass {mass} solar masses:")
        print(f"Interpolated abundances at 70% mass: H: {H_interp_70}, C: {C_interp_70}, N: {N_interp_70}, O: {O_interp_70}")
        print()

        # Append the interpolated values to the lists for the final plot
        H_abundances.append(H_interp)
        C_abundances.append(C_interp)
        N_abundances.append(N_interp)
        O_abundances.append(O_interp)
        star_masses.append(mass)

        H_abundances_80.append(H_interp_80)
        C_abundances_80.append(C_interp_80)
        N_abundances_80.append(N_interp_80)
        O_abundances_80.append(O_interp_80)

        H_abundances_70.append(H_interp_70)
        C_abundances_70.append(C_interp_70)
        N_abundances_70.append(N_interp_70)
        O_abundances_70.append(O_interp_70)

# Sort the final lists in ascending order of star mass
order = np.argsort(star_masses)
star_masses = np.array(star_masses)[order]
H_abundances = np.array(H_abundances)[order]
C_abundances = np.array(C_abundances)[order]
N_abundances = np.array(N_abundances)[order]
O_abundances = np.array(O_abundances)[order]

H_abundances_80 = np.array(H_abundances_80)[order]
C_abundances_80 = np.array(C_abundances_80)[order]
N_abundances_80 = np.array(N_abundances_80)[order]
O_abundances_80 = np.array(O_abundances_80)[order]

H_abundances_70 = np.array(H_abundances_70)[order]
C_abundances_70 = np.array(C_abundances_70)[order]
N_abundances_70 = np.array(N_abundances_70)[order]
O_abundances_70 = np.array(O_abundances_70)[order]

# Plotting the 90%, 80%, and 70% abundances against star mass for all models, with interpolated points marked differently
plt.figure(figsize=(10, 7))

# Plot the actual data
plt.plot(star_masses, H_abundances, 'o-', label='H (90%)')
plt.plot(star_masses, C_abundances, 'o-', label='C (90%)')
plt.plot(star_masses, N_abundances, 'o-', label='N (90%)')
plt.plot(star_masses, O_abundances, 'o-', label='O (90%)')

plt.plot(star_masses, H_abundances_80, 'o--', label='H (80%)')
plt.plot(star_masses, C_abundances_80, 'o--', label='C (80%)')
plt.plot(star_masses, N_abundances_80, 'o--', label='N (80%)')
plt.plot(star_masses, O_abundances_80, 'o--', label='O (80%)')

plt.plot(star_masses, H_abundances_70, 'o-.', label='H (70%)')
plt.plot(star_masses, C_abundances_70, 'o-.', label='C (70%)')
plt.plot(star_masses, N_abundances_70, 'o-.', label='N (70%)')
plt.plot(star_masses, O_abundances_70, 'o-.', label='O (70%)')

# Overplot the interpolated data
plt.plot(all_masses, interp_H(all_masses), 'x', label='H (interp)', markersize=4)
plt.plot(all_masses, interp_C(all_masses), 'x', label='C (interp)', markersize=4)
plt.plot(all_masses, interp_N(all_masses), 'x', label='N (interp)', markersize=4)
plt.plot(all_masses, interp_O(all_masses), 'x', label='O (interp)', markersize=4)

plt.plot(all_masses, interp_H_80(all_masses), 'x', label='H (interp 80%)', markersize=4)
plt.plot(all_masses, interp_C_80(all_masses), 'x', label='C (interp 80%)', markersize=4)
plt.plot(all_masses, interp_N_80(all_masses), 'x', label='N (interp 80%)', markersize=4)
plt.plot(all_masses, interp_O_80(all_masses), 'x', label='O (interp 80%)', markersize=4)

plt.plot(all_masses, interp_H_70(all_masses), 'x', label='H (interp 70%)', markersize=4)
plt.plot(all_masses, interp_C_70(all_masses), 'x', label='C (interp 70%)', markersize=4)
plt.plot(all_masses, interp_N_70(all_masses), 'x', label='N (interp 70%)', markersize=4)
plt.plot(all_masses, interp_O_70(all_masses), 'x', label='O (interp 70%)', markersize=4)

plt.xlabel('Star Mass (Solar Masses)')
plt.ylabel('Abundance')
plt.title('Abundance at 90%, 80%, and 70% Mass for Different Star Models')

# Put the legend below the plot
plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=5)

#plt.savefig('Abundance.jpg', dpi=300, bbox_inches='tight')  # Use bbox_inches='tight' to include the outside legend in the saved figure
plt.tight_layout()
plt.show()
