########

import numpy as np
import matplotlib.pyplot as plt

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

# Calculate CO core masses, 90% mass, and 60% mass for the given models
CO_core_masses_given = []
for model in models:
    file_path = model["path"]
    skip_header = model["skip_header"]
    cutoff = model["cutoff"]
    label = float(model["label"])

    # Read M_sol array from the file
    M_sol = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[49])[:cutoff][::-1]

    # CO core mass is the total mass minus m_ejecta
    CO_core_mass = M_sol[-1] - model["m_ejecta"]
    CO_core_masses_given.append(CO_core_mass)


# Extracting the mass labels from the given models
mass_labels_given = [float(model["label"]) for model in models]

# Interpolate to find the CO core masses for the rest of the masses in full_star_masses
mass_CO_core = np.interp(full_star_masses, mass_labels_given, CO_core_masses_given)

# Rest of the code remains unchanged


# Calculate 90% and 60% mass fractions
mass_90 = [0.1 * mass for mass in full_star_masses]
mass_60 = [0.4 * mass for mass in full_star_masses]

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



############
import numpy as np
import matplotlib.pyplot as plt

# List of models
models = [
    {"path": '/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 2393, "label": "3053"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.v0129331.gz', "skip_header": 304, "cutoff": -87, "m_ejecta": 4865, "label": "6127"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0152721.gz', "skip_header": 297, "cutoff": -68, "m_ejecta": 4156, "label": "4477"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1923M_SS6/P002z0S0.v0558831.gz', "skip_header": 334, "cutoff": -125, "m_ejecta": 1167, "label": "1923"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0217041.gz', "skip_header": 296, "cutoff": -118, "m_ejecta": 1022, "label": "1662"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.v0094231.gz', "skip_header": 309, "cutoff": -90, "m_ejecta": 1004, "label": "1331"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1135M_S20/P002z0S0.v0527201.gz', "skip_header": 2069, "cutoff": -117, "m_ejecta": 685, "label": "1135"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0276841.gz', "skip_header": 3, "cutoff": -95, "m_ejecta":675, "label": "932"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/778M_SS39/P002z0S0.v0088411.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 605, "label": "778"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/771M_SS40/P002z0S0.v0090481.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 596, "label": "771"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0350111.gz', "skip_header": 310, "cutoff": -84, "m_ejecta": 377, "label": "491"},]

full_star_masses = [6127, 4477, 3053, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186,1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

# Calculate CO core masses, 90% mass, and 60% mass for the given models
CO_core_masses_given = []
for model in models:
    file_path = model["path"]
    skip_header = model["skip_header"]
    cutoff = model["cutoff"]
    label = float(model["label"])

    # Read M_sol array from the file
    M_sol = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[49])[:cutoff][::-1]

    # CO core mass is the total mass minus m_ejecta
    CO_core_mass = M_sol[-1] - model["m_ejecta"]
    CO_core_masses_given.append(CO_core_mass)

# Interpolate to find the CO core masses for the rest of the masses in full_star_masses
mass_CO_core = np.interp(full_star_masses, mass_labels_given, CO_core_masses_given)

# Calculate 90% and 60% mass fractions
mass_90 = [0.1 * mass for mass in full_star_masses]
mass_60 = [0.4 * mass for mass in full_star_masses]

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

# Calculate ratios and prepare the table
rows = [
    ("10\\% of $M_{\\text{tot}}$", total_ejected_mass_90, elements_sum['H1'][0]/total_ejected_mass_90, elements_sum['C12'][0]/total_ejected_mass_90, elements_sum['N14'][0]/total_ejected_mass_90, elements_sum['O16'][0]/total_ejected_mass_90),
    ("40\\% of $M_{\\text{tot}}$", total_ejected_mass_60, elements_sum['H1'][1]/total_ejected_mass_60, elements_sum['C12'][1]/total_ejected_mass_60, elements_sum['N14'][1]/total_ejected_mass_60, elements_sum['O16'][1]/total_ejected_mass_60),
    ("100\\% of CO core", total_ejected_mass_CO_core, elements_sum['H1'][2]/total_ejected_mass_CO_core, elements_sum['C12'][2]/total_ejected_mass_CO_core, elements_sum['N14'][2]/total_ejected_mass_CO_core, elements_sum['O16'][2]/total_ejected_mass_CO_core),
]

# LaTeX table header
latex_table = """\\begin{table}[h]
\\centering
\\begin{tabular}{|c|c|c|c|c|c|}
\\hline
Fraction & $M_{\\text{{ejecta}}} [M_{\\odot}]$ & $X_{H1}$ & $X_{C12}$ & $X_{N14}$ & $X_{O16}$ \\\\
\\hline
"""

# Adding rows to the LaTeX table
for row in rows:
    latex_table += f"{row[0]} & {row[1]:.2f} & {row[2]:.2e} & {row[3]:.2e} & {row[4]:.2e} & {row[5]:.2e} \\\\\n\\hline\n"

# LaTeX table footer
latex_table += """\\end{tabular}
\\caption{Ejected Masses and Elemental Ratios for Different Mass Fractions}
\\label{table:mass_fractions}
\\end{table}
"""

# Save LaTeX table to a file on the desktop
with open('/Users/hermit/Desktop/ejected_masses.tex', 'w') as file:
    file.write(latex_table)

print("LaTeX table has been saved to the desktop.")

##############
##############


import numpy as np
import matplotlib.pyplot as plt

# List of models
models = [
    {"path": '/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 2393, "label": "3053"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.v0129331.gz', "skip_header": 304, "cutoff": -87, "m_ejecta": 4865, "label": "6127"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0152721.gz', "skip_header": 297, "cutoff": -68, "m_ejecta": 4156, "label": "4477"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1923M_SS6/P002z0S0.v0558831.gz', "skip_header": 334, "cutoff": -125, "m_ejecta": 1167, "label": "1923"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0217041.gz', "skip_header": 296, "cutoff": -118, "m_ejecta": 1022, "label": "1662"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.v0094231.gz', "skip_header": 309, "cutoff": -90, "m_ejecta": 1004, "label": "1331"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1135M_S20/P002z0S0.v0527201.gz', "skip_header": 2069, "cutoff": -117, "m_ejecta": 685, "label": "1135"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0276841.gz', "skip_header": 3, "cutoff": -95, "m_ejecta":675, "label": "932"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/778M_SS39/P002z0S0.v0088411.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 605, "label": "778"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/771M_SS40/P002z0S0.v0090481.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 596, "label": "771"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0350111.gz', "skip_header": 310, "cutoff": -84, "m_ejecta": 377, "label": "491"},]

full_star_masses = [6127, 4477, 3053, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186,1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]


# Correct array for CO core masses
correct_mass_CO_core = np.array([
    115.4437, 175.5876, 173.9827, 205.43960035, 206.77819186, 216.66889575, 257.94213381,
    1256.402, 1207.24219429, 1190.14313143, 1188.00574857, 1173.04406857, 1160.21977143,
    1123.88426286, 1096.09828571, 1081.13660571, 1074.72445714, 1068.31230857, 1066.17492571,
    1034.11418286, 1031.9768, 989.22914286, 957.1684, 944.34410286, 933.65718857, 925.10765714,
    848.16187429, 820.37589714, 816.10113143, 781.90300571, 754.11702857, 709.23198857,
    700.68245714, 698.54507429, 692.13292571, 692.13292571, 670.75909714, 662.20956571,
    657.9348
])

# Calculate 90% and 60% mass fractions
mass_90 = [0.1 * mass for mass in full_star_masses]
mass_60 = [0.4 * mass for mass in full_star_masses]

# Sum the mass fractions
total_ejected_mass_90 = sum(mass_90)
total_ejected_mass_60 = sum(mass_60)
total_ejected_mass_CO_core = sum(correct_mass_CO_core)

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

        # Read the data for H1, C12, etc.
        H1 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[6])[:cutoff][::-1]
        C12 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[8])[:cutoff][::-1]
        N14 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[33])[:cutoff][::-1]
        O16 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[9])[:cutoff][::-1]
        M_sol = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[49])[:cutoff][::-1]

        # Calculate the desired mass point
        desired_mass = mass_fraction * M_sol[-1] if mass_fraction > 0 else correct_mass_CO_core[index]

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

    # Store the sums for the elements and print the total sum of masses
    elements_sum['H1'].append(H_sum)
    elements_sum['C12'].append(C_sum)
    elements_sum['N14'].append(N_sum)
    elements_sum['O16'].append(O_sum)

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


#######
#####
import numpy as np
import matplotlib.pyplot as plt

# List of models
models = [
    {"path": '/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 2393, "label": "3053"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.v0129331.gz', "skip_header": 304, "cutoff": -87, "m_ejecta": 4865, "label": "6127"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0152721.gz', "skip_header": 297, "cutoff": -68, "m_ejecta": 4156, "label": "4477"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1923M_SS6/P002z0S0.v0558831.gz', "skip_header": 334, "cutoff": -125, "m_ejecta": 1167, "label": "1923"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0217041.gz', "skip_header": 296, "cutoff": -118, "m_ejecta": 1022, "label": "1662"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.v0094231.gz', "skip_header": 309, "cutoff": -90, "m_ejecta": 1004, "label": "1331"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1135M_S20/P002z0S0.v0527201.gz', "skip_header": 2069, "cutoff": -117, "m_ejecta": 685, "label": "1135"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0276841.gz', "skip_header": 3, "cutoff": -95, "m_ejecta":675, "label": "932"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/778M_SS39/P002z0S0.v0088411.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 605, "label": "778"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/771M_SS40/P002z0S0.v0090481.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 596, "label": "771"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0350111.gz', "skip_header": 310, "cutoff": -84, "m_ejecta": 377, "label": "491"},]

full_star_masses = [6127, 4477, 3053, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186,1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

# Create an array filled with NaN for the CO core masses
mass_CO_core = [np.nan] * len(full_star_masses)

# Fill the CO core masses for the 11 models loaded in the correct spot
for model, CO_core_mass in zip(models, CO_core_masses_given):
    label = float(model["label"])
    index = full_star_masses.index(label)
    mass_CO_core[index] = CO_core_mass

# Use interpolation to fill the rest of the elements in the mass_CO_core array
not_nan_indices = ~np.isnan(mass_CO_core)
interpolated_CO_core_masses = np.interp(full_star_masses, np.array(full_star_masses)[not_nan_indices], np.array(mass_CO_core)[not_nan_indices])

# Replace mass_CO_core with the interpolated values
mass_CO_core = interpolated_CO_core_masses

# ... (Rest of the code remains unchanged)


# Calculate 90% and 60% mass fractions
mass_90 = [0.1 * mass for mass in full_star_masses]
mass_60 = [0.4 * mass for mass in full_star_masses]

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





import math

# Define the data from the table
data = [
    (10, 8267.30, 6.52e-2, 7.37e-4, 1.01e-2, 1.05e-2),
    (40, 33069.20, 4.07e-2, 1.57e-3, 1.50e-2, 1.42e-2),
    (100, 49744.04, 3.5e-2, 5.05e-3, 2.0e-2, 1.7e-2),
]

# Loop through the data and calculate the required values
for fraction, _, X_H1, X_C12, X_N14, X_O16 in data:
    log_N_O = math.log10(X_N14 / X_O16)
    log_C_O = math.log10(X_C12 / X_O16)
    print(f"For {fraction}%:")
    print(f"log_base10(N/O) = {log_N_O}")
    print(f"log_base10(C/O) = {log_C_O}")

    # Loop through the f values for log_base10(O/H)
    for f in [0, 1, 10,50,100,200]:
        log_O_H = math.log10(X_O16 / (X_H1 + 0.7516 * f))+12.0
        print(f"log_base10(O/H) with f = {f} is {log_O_H}")

    print()  # Line break between different fractions
