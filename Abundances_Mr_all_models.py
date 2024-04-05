# Abundances of all models

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
    # Add more dictionaries for additional models
]

# Create a figure with subplots arranged in a grid
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(15, 15))
axs = axs.flatten()

for index, model in enumerate(models):
    ax = axs[index]

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
    dM = np.diff(M_sol)

    X_H1_list = []
    X_C12_list = []
    X_N14_list = []
    X_O16_list = []

    # Calculate cumulative mass from outside to inside
    cumulative_mass = np.cumsum(dM[::-1])[::-1]

    for i in range(len(dM)):
        X_H1 = np.sum(H1[i:-1]*dM[i:]) / cumulative_mass[i]
        X_C12 = np.sum(C12[i:-1]*dM[i:]) / cumulative_mass[i]
        X_N14 = np.sum(N14[i:-1]*dM[i:]) / cumulative_mass[i]
        X_O16 = np.sum(O16[i:-1]*dM[i:]) / cumulative_mass[i]

        X_H1_list.append(X_H1)
        X_C12_list.append(X_C12)
        X_N14_list.append(X_N14)
        X_O16_list.append(X_O16)


    ax.plot(M_sol[:-1], X_H1_list, linewidth=2.0, label="X_H1")
    ax.plot(M_sol[:-1], X_C12_list, linewidth=2.0, label="X_C12")
    ax.plot(M_sol[:-1], X_N14_list, linewidth=2.0, label="X_N14")
    ax.plot(M_sol[:-1], X_O16_list, linewidth=2.0, label="X_O16")

    x_position = label - m_ejecta
    ax.axvline(x=x_position, color='grey', linestyle='-.', alpha=0.5)

    ax.set_title(f'{int(label)}', fontsize=12)
    ax.set_xlabel('M$_{\mathrm{r}}[M_{\odot}]$', fontsize=10)
    ax.set_ylabel('Abundance', fontsize=10)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)

# Adding legends to the last subplot
# Adding legends to the last subplot
ax = axs[11]
ax.axis('off')

legend_labels = ["X_H1", "X_C12", "X_N14", "X_O16"]
for label in legend_labels:
    ax.plot(0, 0, linewidth=2.0, label=label)

ax.legend(loc='center', shadow=True, prop={'size': 12})


# Adjust layout
plt.tight_layout()
plt.savefig('/Users/hermit/Observatory/Abundance_ind.jpg', facecolor='none', dpi=300, transparent=True)

# Show the plot
plt.show()
