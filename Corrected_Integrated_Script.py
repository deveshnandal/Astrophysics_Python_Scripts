import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import simps

def process_data(filepath, skip_header, m_ejecta, label, index_cutoff, annotation_offset=(0, 0), plot_axes=None, plot_axes2=None, plot_colorbar=False):
    H1 = (np.transpose(np.genfromtxt(filepath, skip_header=skip_header))[6])[:index_cutoff][::-1]
    C12 = (np.transpose(np.genfromtxt(filepath, skip_header=skip_header))[8])[:index_cutoff][::-1]
    N14 = (np.transpose(np.genfromtxt(filepath, skip_header=skip_header))[33])[:index_cutoff][::-1]
    O16 = (np.transpose(np.genfromtxt(filepath, skip_header=skip_header))[9])[:index_cutoff][::-1]
    M_sol = (np.transpose(np.genfromtxt(filepath, skip_header=skip_header))[49])[:index_cutoff][::-1]

    # Default constants
    N_ini = 0.0
    O_ini = 0.0
    C_ini = 0.0
    H_ini = 7.515977428571429e-01

    # Constants for filepaths containing "1e-6"
    if "1e-6" in filepath:
        N_ini = 4.705414495276072e-08
        O_ini = 4.084625123020800e-07
        C_ini = 1.630823182090076e-07
        H_ini = 7.515977428571429e-01

    # Constants for filepaths containing "0.014"
    if "0.014" in filepath:
        N_ini = 6.587580293386503e-04
        O_ini = 5.718475172229120e-03
        C_ini = 2.283152454926108e-03
        H_ini = 7.200000000000000e-01

    log_NO_values = []
    log_OH_values = []
    log_CO_values = []

    f_values = np.logspace(-1, 3, 50)# change the range to be more reasonable for popIII stars.
    dM = np.diff(M_sol)

    for f in f_values:
        X_H1 = np.sum(H1[:-1] * dM) / m_ejecta
        X_N14 = np.sum(N14[:-1] * dM) / m_ejecta
        X_O16 = np.sum(O16[:-1] * dM) / m_ejecta
        X_C12 = np.sum(C12[:-1] * dM) / m_ejecta

        log_NO_num = ((X_N14 + (N_ini*f))*16.0)
        log_NO_den = ((X_O16 + (O_ini*f))*14.0)
        log_NO = np.log10(log_NO_num/log_NO_den)
        log_NO_values.append(log_NO)

        log_OH_num = ((X_O16 + (O_ini*f))*1.0)
        log_OH_den = ((X_H1 + (H_ini*f))*16.0)
        log_OH = np.log10(log_OH_num/log_OH_den) + 12.0
        log_OH_values.append(log_OH)

        log_CO_num = ((X_C12 + (C_ini*f))*16.0)
        log_CO_den = ((X_O16 + (O_ini*f))*12.0)
        log_CO = np.log10(log_CO_num/log_CO_den)
        log_CO_values.append(log_CO)

    sc1 = plot_axes[0].scatter(log_OH_values, log_NO_values, c=f_values, s=20, cmap='tab20', label=label)
    sc2 = plot_axes[1].scatter(log_OH_values, log_CO_values, c=f_values, s=20, cmap='tab20')

    plot_axes[0].annotate(label, (log_OH_values[-1] + annotation_offset[0], log_NO_values[-1] + annotation_offset[1]), textcoords="offset points", fontsize=12)
    plot_axes2[1].annotate(label, (log_OH_values[-1] + annotation_offset[0], log_CO_values[-1] + annotation_offset[1]), textcoords="offset points", fontsize=12)

    if plot_colorbar:
        cbar = plt.colorbar(sc1, ax=plot_axes[0])
        cbar.set_label('Dilution factor', fontsize=22)


filepaths = [
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.v0129331.gz', 304, 4865, '6127', -87, (0, 0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1923M_SS6/P002z0S0.v0558831.gz', 334, 1167, '1923', -125, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/771M_SS40/P002z0S0.v0090481.gz', 310, 596, '771', -85, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0350111.gz', 310, 114, '491', -84, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0217041.gz', 296, 1022, '1662', -118, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0170821.gz', 296, 2390, '3050', -93, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_1e-6/P002z0S0.v0187401.gz', 295, 2640, '3250_1e-6', -95, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr_0.014/P002z0S0.v0114971', 312, 2385, '3440_0.014', -105, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS/6.5e-4Msun_yr/P002z0S0.v0188381', 300, 1624, '2100', -87, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS/3.5e-3Msun_yr/P002z0S0.v0173871', 310, 7774, '8904', -72, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS/1e-2Msun_yr/P002z0S0.v0102701', 1583, 11501, '21197', -145, (0, -0.05)),
    ('/Users/hermit/Observatory/StarCalc/SMS/Z0_Accr_1e-1_fitm0.999_vvx_n10_iover0/P002z0S0.v0149011.gz', 3, 42704, '110100', -189, (0, -0.05)),
]

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

for idx, (filepath, skip_header, m_ejecta, label, index_cutoff, annotation_offset) in enumerate(filepaths):
    process_data(filepath, skip_header, m_ejecta, label, index_cutoff, annotation_offset, plot_axes=axs, plot_axes2=axs, plot_colorbar=(idx==0))

axs[0].axhspan(-0.3, 0.9, xmin=(7.6-axs[0].get_xlim()[0])/(axs[0].get_xlim()[1]-axs[0].get_xlim()[0]), xmax=(8.0-axs[0].get_xlim()[0])/(axs[0].get_xlim()[1]-axs[0].get_xlim()[0]), color='orange', alpha=0.5)
axs[1].axhspan(-0.75, 1.0, xmin=(7.6-axs[1].get_xlim()[0])/(axs[1].get_xlim()[1]-axs[1].get_xlim()[0]), xmax=(8.0-axs[1].get_xlim()[0])/(axs[1].get_xlim()[1]-axs[1].get_xlim()[0]), color='orange', alpha=0.5)

axs[0].fill([7.05, 7.05, 8.6, 8.6], [0.9, -0.5, -0.18, 0.9], color='grey', alpha=0.4)
axs[1].fill([7.05, 7.05, 8.6, 8.6], [0.8, -0.9, -0.56, 0.8], color='grey', alpha=0.4)

axs[0].plot(7.6, -0.25, marker='*', color='blue', markersize=12, linestyle='None')
axs[0].plot(7.75, -0.38, marker='*', color='brown', markersize=12, linestyle='None')

axs[0].plot(7.70,-0.18, marker='*', color='magenta', markersize=12, linestyle='None')
axs[0].errorbar(7.70,-0.18, xerr=0.11, yerr=0.18, fm# Add the new calculations to the plot
results, data = additional_calculations()  # Unpacking data as well
f_labels = ['90%', '60%', 'C0core']
for i, (log_N_O, log_C_O, log_O_H_values) in enumerate(results):
    label_fraction = data[i][0]
    axs[0].plot(log_N_O, log_C_O, label=f'{label_fraction}%', marker='o')  # Plot log(N/O) vs log(C/O)
    for j, log_O_H in enumerate(log_O_H_values):
        axs[1].plot(label_fraction, log_O_H, label=f'{f_labels[j]}', marker='o')explosion-quasar

def additional_calculations():
    data = [
        (10, 8900.70, 0.28, 0.002, 0.05, 0.08),
        (40, 32602.20, 0.21, 0.002, 0.08, 0.12),
        (100, 65866.04, 0.17, 0.002, 0.08, 0.12),
    ]
    results = []
    for fraction, _, X_H1, X_C12, X_N14, X_O16 in data:
        log_N_O = math.log10(X_N14 / X_O16)
        log_C_O = math.log10(X_C12 / X_O16)

        log_O_H_values = []
        for f in [0, 1, 10, 100]:
            log_O_H = math.log10(X_O16 / (X_H1 + 0.7516 * f)) + 12.0
            log_O_H_values.append(log_O_H)

        results.append((log_N_O, log_C_O, log_O_H_values))

    return results, data  # Returning data as well
