######### 90, 60, CO core integrated mass plots with interpolation

import numpy as np
import matplotlib.pyplot as plt

N_ini = 0.0
O_ini = 0.0
C_ini = 0.0
H_ini = 7.515977428571429e-01

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
]

models = sorted(models, key=lambda k: float(k['label']))

full_star_masses = [6127, 4477,3053, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186, 1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

for mass_fraction in [0.9, 0.6, 0.0]:
    H_abundances = []
    C_abundances = []
    N_abundances = []
    O_abundances = []
    star_masses = []

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

        # Calculate the desired mass point
        desired_mass = mass_fraction * M_sol[-1] if mass_fraction > 0 else M_sol[0]

        # Find the index where M_sol is closest to desired_mass
        idx_mass = np.abs(M_sol - desired_mass).argmin()

        # Calculate differential mass
        dM = np.diff(M_sol)

        # Calculate cumulative abundances
        X_H1 = np.sum(H1[idx_mass:-1] * dM[idx_mass:])
        X_C12 = np.sum(C12[idx_mass:-1] * dM[idx_mass:])
        X_N14 = np.sum(N14[idx_mass:-1] * dM[idx_mass:])
        X_O16 = np.sum(O16[idx_mass:-1] * dM[idx_mass:])

        # Append the values to the lists for the final plot
        H_abundances.append(X_H1)
        C_abundances.append(X_C12)
        N_abundances.append(X_N14)
        O_abundances.append(X_O16)
        star_masses.append(label)

    H_interp = np.interp(full_star_masses, star_masses, H_abundances)
    C_interp = np.interp(full_star_masses, star_masses, C_abundances)
    N_interp = np.interp(full_star_masses, star_masses, N_abundances)
    O_interp = np.interp(full_star_masses, star_masses, O_abundances)

    plt.figure(figsize=(10, 7))

    plt.plot(star_masses, H_abundances, 'o-', label='H')
    plt.plot(star_masses, C_abundances, 'o-', label='C')
    plt.plot(star_masses, N_abundances, 'o-', label='N')
    plt.plot(star_masses, O_abundances, 'o-', label='O')

    plt.plot(full_star_masses, H_interp, 'x-', label='H (interpolated)', color='blue', linestyle='dashed')
    plt.plot(full_star_masses, C_interp, 'x-', label='C (interpolated)', color='orange', linestyle='dashed')
    plt.plot(full_star_masses, N_interp, 'x-', label='N (interpolated)', color='green', linestyle='dashed')
    plt.plot(full_star_masses, O_interp, 'x-', label='O (interpolated)', color='red', linestyle='dashed')

    plt.xlabel('Mass $[M_{\\odot}]$')
    plt.ylabel('Integrated mass ejected$[M_{\\odot}]$')
    plt.title(f'Integrated mass ejected at {mass_fraction * 100}% of each model')
    plt.legend()

    plt.show()



###############

import numpy as np
import matplotlib.pyplot as plt

# Initialization
N_ini = 0.0
O_ini = 0.0
C_ini = 0.0
H_ini = 7.515977428571429e-01

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
]

full_star_masses = [6127, 4477, 3053, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186, 1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

mass_fractions = [0.9, 0.6, 0.0]
mass_fraction_labels = ['90%', '60%', 'CO core']
elements_sum = {'H1': [], 'C12': [], 'N14': [], 'O16': []}

for mass_fraction in mass_fractions:
    H_sum = C_sum = N_sum = O_sum = 0

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

        # Calculate the desired mass point
        desired_mass = mass_fraction * M_sol[-1] if mass_fraction > 0 else M_sol[0]

        # Find the index where M_sol is closest to desired_mass
        idx_mass = np.abs(M_sol - desired_mass).argmin()

        # Calculate differential mass
        dM = np.diff(M_sol)

        # Calculate cumulative abundances
        X_H1 = np.sum(H1[idx_mass:-1] * dM[idx_mass:])
        X_C12 = np.sum(C12[idx_mass:-1] * dM[idx_mass:])
        X_N14 = np.sum(N14[idx_mass:-1] * dM[idx_mass:])
        X_O16 = np.sum(O16[idx_mass:-1] * dM[idx_mass:])

        # Summing the integrated masses for each element
        H_sum += X_H1
        C_sum += X_C12
        N_sum += X_N14
        O_sum += X_O16

    elements_sum['H1'].append(H_sum)
    elements_sum['C12'].append(C_sum)
    elements_sum['N14'].append(N_sum)
    elements_sum['O16'].append(O_sum)

plt.figure(figsize=(10, 7))

# Plotting the sum of integrated masses for each element
for element, values in elements_sum.items():
    plt.plot(mass_fraction_labels, values, 'o-', label=element)

plt.xlabel('Mass Fraction Index')
plt.ylabel('Sum of Integrated Masses $[M_{\\odot}]$')
plt.title('Sum of Integrated Masses for Different Mass Fraction Indices')
plt.legend()

plt.show()

##############
import numpy as np
import matplotlib.pyplot as plt

# Initialization
N_ini = 0.0
O_ini = 0.0
C_ini = 0.0
H_ini = 7.515977428571429e-01

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
]

full_star_masses = [6127, 4477, 3053, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186, 1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

# Calculate the mass fractions
mass_90 = [0.1 * mass for mass in full_star_masses]
mass_60 = [0.4 * mass for mass in full_star_masses]
mass_CO_core = [0.0 * mass for mass in full_star_masses]  # This will be an array of zeros

# Sum the mass fractions
total_ejected_mass_90 = sum(mass_90)
total_ejected_mass_60 = sum(mass_60)
total_ejected_mass_CO_core = sum(mass_CO_core)

# Print the total ejected masses
print("Total Ejected Mass at 90%:", total_ejected_mass_90)
print("Total Ejected Mass at 60%:", total_ejected_mass_60)
print("Total Ejected Mass at CO core:", total_ejected_mass_CO_core)

mass_fractions = [0.9, 0.6, 0.0]
mass_fraction_labels = ['90%', '60%', 'CO core']
elements_sum = {'H1': [], 'C12': [], 'N14': [], 'O16': []}


for mass_fraction in mass_fractions:
    H_sum = C_sum = N_sum = O_sum = 0

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

        # Calculate the desired mass point
        desired_mass = mass_fraction * M_sol[-1] if mass_fraction > 0 else M_sol[0]

        # Find the index where M_sol is closest to desired_mass
        idx_mass = np.abs(M_sol - desired_mass).argmin()

        # Calculate differential mass
        dM = np.diff(M_sol)

        # Calculate cumulative abundances
        X_H1 = np.sum(H1[idx_mass:-1] * dM[idx_mass:])
        X_C12 = np.sum(C12[idx_mass:-1] * dM[idx_mass:])
        X_N14 = np.sum(N14[idx_mass:-1] * dM[idx_mass:])
        X_O16 = np.sum(O16[idx_mass:-1] * dM[idx_mass:])

        # Summing the integrated masses for each element
        H_sum += X_H1
        C_sum += X_C12
        N_sum += X_N14
        O_sum += X_O16

    elements_sum['H1'].append(H_sum)
    elements_sum['C12'].append(C_sum)
    elements_sum['N14'].append(N_sum)
    elements_sum['O16'].append(O_sum)


plt.figure(figsize=(10, 7))

# Plotting the sum of integrated masses for each element
for element, values in elements_sum.items():
    plt.plot(mass_fraction_labels, values, 'o-', label=element)

plt.xlabel('Mass Fraction Index')
plt.ylabel('Sum of Integrated Masses $[M_{\\odot}]$')
plt.title('Sum of Integrated Masses for Different Mass Fraction Indices')
plt.legend()

plt.show()



##########

import numpy as np
import matplotlib.pyplot as plt

# Initialization
N_ini = 0.0
O_ini = 0.0
C_ini = 0.0
H_ini = 7.515977428571429e-01

# List of models
models = [
    {"path": '/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 2393, "label": "3053"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.v0129331.gz', "skip_header": 304, "cutoff": -87, "m_ejecta": 4865, "label": "6127"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0152721.gz', "skip_header": 297, "cutoff": -68, "m_ejecta": 4156, "label": "4477"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1923M_SS6/P002z0S0.v0558831.gz', "skip_header": 334, "cutoff": -125, "m_ejecta": 1167, "label": "1923"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0217041.gz', "skip_header": 296, "cutoff": -118, "m_ejecta": 1022, "label": "1662"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.v0094231.gz', "skip_header": 309, "cutoff": -90, "m_ejecta": 1004, "label": "1331"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1135M_S20/P002z0S0.v0527201.gz', "skip_header": 2069, "cutoff": -117, "m_ejecta": 685, "label": "1135"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0276841.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 675, "label": "932"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/778M_SS39/P002z0S0.v0088411.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 605, "label": "778"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/771M_SS40/P002z0S0.v0090481.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 596, "label": "771"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0350111.gz', "skip_header": 310, "cutoff": -84, "m_ejecta": 377, "label": "491"},
]

full_star_masses = [6127, 4477, 3053, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186, 1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

# Calculate 90% and 60% mass fractions
mass_90 = [0.1 * mass for mass in full_star_masses]
mass_60 = [0.4 * mass for mass in full_star_masses]

# Calculate CO core masses for the given models
CO_core_masses_given = [float(model["label"]) - model["m_ejecta"] for model in models]
mass_labels_given = [float(model["label"]) for model in models]

# Create a dictionary to match CO core mass with the full star mass label
CO_core_dict = {label: CO_core for label, CO_core in zip(mass_labels_given, CO_core_masses_given)}

# Sort the full_star_masses in ascending order
sorted_full_star_masses = sorted(full_star_masses)

# Create an array to store the CO core masses in ascending order according to the full_star_masses
sorted_CO_core_masses = [CO_core_dict.get(mass, None) for mass in sorted_full_star_masses]

# Remove None values and keep only the matched CO core masses and corresponding full star masses
matched_CO_core_masses = [mass for mass in sorted_CO_core_masses if mass is not None]
matched_full_star_masses = [mass for mass, CO_core in zip(sorted_full_star_masses, sorted_CO_core_masses) if CO_core is not None]

# Interpolate to find the CO core masses for the rest of the masses in full_star_masses
mass_CO_core = np.interp(full_star_masses, matched_full_star_masses, matched_CO_core_masses)

# Rest of the code remains the same


# Sum the mass fractions
total_ejected_mass_90 = sum(mass_90)
total_ejected_mass_60 = sum(mass_60)
total_ejected_mass_CO_core = sum(mass_CO_core)

print("Total Ejected Mass at 90%:", total_ejected_mass_90)
print("Total Ejected Mass at 60%:", total_ejected_mass_60)
print("Total Ejected Mass at CO core:", total_ejected_mass_CO_core)

mass_fractions = [0.9, 0.6, 0.0]
mass_fraction_labels = ['90%', '60%', 'CO core']
elements_sum = {'H1': [], 'C12': [], 'N14': [], 'O16': []}

for mass_fraction, fraction_label in zip(mass_fractions, mass_fraction_labels):
    H_sum = C_sum = N_sum = O_sum = 0

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

        # Calculate the desired mass point
        desired_mass = mass_fraction * M_sol[-1] if mass_fraction > 0 else mass_CO_core[index]

        # Find the index where M_sol is closest to desired_mass
        idx_mass = np.abs(M_sol - desired_mass).argmin()

        # Calculate differential mass
        dM = np.diff(M_sol)

        # Calculate cumulative abundances
        X_H1 = np.sum(H1[idx_mass:-1] * dM[idx_mass:])
        X_C12 = np.sum(C12[idx_mass:-1] * dM[idx_mass:])
        X_N14 = np.sum(N14[idx_mass:-1] * dM[idx_mass:])
        X_O16 = np.sum(O16[idx_mass:-1] * dM[idx_mass:])

        # Summing the integrated masses for each element
        H_sum += X_H1
        C_sum += X_C12
        N_sum += X_N14
        O_sum += X_O16

    # Store the sums for the elements
    elements_sum['H1'].append(H_sum)
    elements_sum['C12'].append(C_sum)
    elements_sum['N14'].append(N_sum)
    elements_sum['O16'].append(O_sum)

    # Print the total sum of masses for H1, C12, etc for 90, 60, and CO core
    print(f"Total sum of masses for H1 at {fraction_label}: {H_sum}")
    print(f"Total sum of masses for C12 at {fraction_label}: {C_sum}")
    print(f"Total sum of masses for N14 at {fraction_label}: {N_sum}")
    print(f"Total sum of masses for O16 at {fraction_label}: {O_sum}")

plt.figure(figsize=(10, 7))

# Plotting the sum of integrated masses for each element
for element, values in elements_sum.items():
    plt.plot(mass_fraction_labels, values, 'o-', label=element)

plt.xlabel('Mass Fraction Index')
plt.ylabel('Sum of Integrated Masses $[M_{\\odot}]$')
plt.title('Sum of Integrated Masses for Different Mass Fraction Indices')
plt.legend()

plt.show()
