### Works for one cutoff at 90%

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

# Sort the models in ascending order of 'label'
models = sorted(models, key=lambda k: float(k['label']))
star_masses = [6127, 4477, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186, 1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

# Lists to hold the 90% mass abundances and star masses for the final plot
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

    # Calculate the 90% mass point
    mass_90 = 0.9 * M_sol[-1]

    # Find the index where M_sol is closest to mass_90
    idx_90 = np.abs(M_sol - mass_90).argmin()

    # Calculate differential mass
    dM = np.diff(M_sol)

    # Calculate cumulative abundances
    X_H1 = np.sum(H1[idx_90:-1] * dM[idx_90:]) / (M_sol[-1] - M_sol[idx_90])
    X_C12 = np.sum(C12[idx_90:-1] * dM[idx_90:]) / (M_sol[-1] - M_sol[idx_90])
    X_N14 = np.sum(N14[idx_90:-1] * dM[idx_90:]) / (M_sol[-1] - M_sol[idx_90])
    X_O16 = np.sum(O16[idx_90:-1] * dM[idx_90:]) / (M_sol[-1] - M_sol[idx_90])

    # Append the values to the lists for the final plot
    H_abundances.append(X_H1)
    C_abundances.append(X_C12)
    N_abundances.append(X_N14)
    O_abundances.append(X_O16)
    star_masses.append(label)

# Plotting the 90% abundances against star mass for all models

plt.figure(figsize=(10, 7))

# Plot the actual data
plt.plot(star_masses, H_abundances, 'o-', label='H')
plt.plot(star_masses, C_abundances, 'o-', label='C')
plt.plot(star_masses, N_abundances, 'o-', label='N')
plt.plot(star_masses, O_abundances, 'o-', label='O')

plt.xlabel('Star Mass (Solar Masses)')
plt.ylabel('Abundance at 90% Mass')
plt.title('Abundance at 90% Mass for Different Star Models')
plt.legend()

plt.show()



########## for 60 and CO core cutoff

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

plt.figure(figsize=(15, 15))

for idx, (mass_fraction, title) in enumerate(zip([0.9, 0.6, 0.0], ['Abundance at 90% Mass', 'Abundance at 60% Mass', 'Abundance up to CO Core Mass'])):
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
        X_H1 = np.sum(H1[idx_mass:-1] * dM[idx_mass:]) / (M_sol[-1] - M_sol[idx_mass])
        X_C12 = np.sum(C12[idx_mass:-1] * dM[idx_mass:]) / (M_sol[-1] - M_sol[idx_mass])
        X_N14 = np.sum(N14[idx_mass:-1] * dM[idx_mass:]) / (M_sol[-1] - M_sol[idx_mass])
        X_O16 = np.sum(O16[idx_mass:-1] * dM[idx_mass:]) / (M_sol[-1] - M_sol[idx_mass])

        # Append the values to the lists for the final plot
        H_abundances.append(X_H1)
        C_abundances.append(X_C12)
        N_abundances.append(X_N14)
        O_abundances.append(X_O16)
        star_masses.append(label)

    # Plotting the abundances for this mass fraction
    plt.subplot(3, 1, idx + 1)
    plt.plot(star_masses, H_abundances, 'o-', label='H')
    plt.plot(star_masses, C_abundances, 'o-', label='C')
    plt.plot(star_masses, N_abundances, 'o-', label='N')
    plt.plot(star_masses, O_abundances, 'o-', label='O')
    plt.xlabel('Star Mass (Solar Masses)')
    plt.ylabel(f'Abundance at {mass_fraction * 100}% Mass')
    plt.title(title)
    plt.legend()

plt.tight_layout()
plt.show()
