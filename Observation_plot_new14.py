##### USe this one !!!
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy.integrate import simps
custom_colormap = ListedColormap(['blue', 'cyan', 'green', 'orange', 'black'])


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

    color_mapping = {1: 'blue', 10: 'cyan', 50: 'green', 100: 'orange', 200: 'black'}
    f_values = [1,10,50,100,200]#np.logspace(-1, 3, 50)# change the range to be more reasonable for popIII stars.
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

    sc1 = plot_axes[0].scatter(log_OH_values, log_NO_values, c=[color_mapping[f] for f in f_values], s=50, cmap=custom_colormap, label=label)
    plot_axes[0].plot(log_OH_values, log_NO_values, color='gray', linestyle='dotted', linewidth=2.0)
    sc2 = plot_axes[1].scatter(log_OH_values, log_CO_values, c=[color_mapping[f] for f in f_values], s=50, cmap=custom_colormap)
    plot_axes[1].plot(log_OH_values, log_CO_values, color='gray', linestyle='dotted', linewidth=2.0)

    #plot_axes[0].annotate(label, (log_OH_values[-1] + annotation_offset[0], log_NO_values[-1] + annotation_offset[1]), textcoords="offset points", fontsize=12)
    #plot_axes2[1].annotate(label, (log_OH_values[-1] + annotation_offset[0], log_CO_values[-1] + annotation_offset[1]), textcoords="offset points", fontsize=12)


    if plot_colorbar:
        cbar_ax = fig.add_subplot(gs[:, 1])
        from matplotlib.cm import ScalarMappable

        # Create a custom colorbar with the specified colors
        norm = plt.Normalize(0, 1)
        sm = ScalarMappable(cmap=custom_colormap, norm=norm)
        sm.set_array([])
        cbar = fig.colorbar(sm, cax=cbar_ax, aspect=30, ticks=[1, 10, 50, 100, 200])
        cbar.set_ticks([0.0, 0.25, 0.5, 0.75, 1.0])
        cbar.set_ticklabels([1, 10, 50, 100, 200])
        cbar.ax.tick_params(labelsize=16)
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

fig = plt.figure(figsize=(10, 10))
gs = fig.add_gridspec(2, 2, width_ratios=[18, 1], height_ratios=[1,1])
axs = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[1, 0])]

for idx, (filepath, skip_header, m_ejecta, label, index_cutoff, annotation_offset) in enumerate(filepaths):
    process_data(filepath, skip_header, m_ejecta, label, index_cutoff, annotation_offset, plot_axes=axs, plot_axes2=axs, plot_colorbar=(idx==0))

#axs[0].axhspan(-0.3, 0.9, xmin=(7.6-axs[0].get_xlim()[0])/(axs[0].get_xlim()[1]-axs[0].get_xlim()[0]), xmax=(8.0-axs[0].get_xlim()[0])/(axs[0].get_xlim()[1]-axs[0].get_xlim()[0]), color='orange', alpha=0.5)
#axs[1].axhspan(-0.75, 1.0, xmin=(7.6-axs[1].get_xlim()[0])/(axs[1].get_xlim()[1]-axs[1].get_xlim()[0]), xmax=(8.0-axs[1].get_xlim()[0])/(axs[1].get_xlim()[1]-axs[1].get_xlim()[0]), color='orange', alpha=0.5)

axs[0].fill([7.6, 7.6, 8.0, 8.0], [0.9, -0.3, -0.3, 0.9], color='orange', alpha=0.4)
axs[1].fill([7.6, 7.6, 8.0, 8.0], [1.5, -0.75, -0.75, 1.5], color='orange', alpha=0.4)
axs[0].fill([7.05, 7.05, 8.6, 8.6], [0.9, -0.5, -0.18, 0.9], color='grey', alpha=0.4)
axs[1].fill([7.05, 7.05, 8.6, 8.6], [0.8, -0.9, -0.56, 0.8], color='grey', alpha=0.4)

axs[0].plot(7.6, -0.25, marker='*', color='red', markersize=12, linestyle='None')
axs[0].plot(7.75, -0.38, marker='*', color='brown', markersize=12, linestyle='None')

axs[0].plot(7.70,-0.18, marker='*', color='yellow', markersize=12, linestyle='None')
axs[0].plot(10.109073569991084, -0.016867925287295537, marker='p', color='blue', markersize=10, label='90%', linestyle='None')
axs[1].plot(10.109073569991084, -1.1537218112108867, marker='p', color='blue', markersize=10, label='90%', linestyle='None')
axs[0].plot(9.141451345135723, -0.016867925287295537, marker='p', color='cyan', markersize=10, label='90%', linestyle='None')
axs[1].plot(9.141451345135723, -1.1537218112108867, marker='p', color='cyan', markersize=10, label='90%', linestyle='None')
axs[0].plot(8.445479690283769, -0.016867925287295537, marker='p', color='green', markersize=10, label='90%', linestyle='None')
axs[1].plot(8.445479690283769, -1.1537218112108867, marker='p', color='green', markersize=10, label='90%', linestyle='None')
axs[0].plot(8.144825948004701, -0.016867925287295537, marker='p', color='orange', markersize=10, label='90%', linestyle='None')
axs[1].plot(8.144825948004701, -1.1537218112108867, marker='p', color='orange', markersize=10, label='90%', linestyle='None')
axs[0].plot(7.8439842013422565, -0.016867925287295537, marker='p', color='black', markersize=10, label='90%', linestyle='None')
axs[1].plot(7.8439842013422565, -1.1537218112108867, marker='p', color='black', markersize=10, label='90%', linestyle='None')

axs[0].plot(10.25339868845647, 0.02380291467262473, marker='p', color='blue', markersize=10, label='60%', linestyle='None')
axs[1].plot(10.25339868845647, -0.9563886919738228, marker='p', color='blue', markersize=10, label='60%', linestyle='None')
axs[0].plot(9.273956163257083, 0.02380291467262473, marker='p', color='cyan', markersize=10, label='60%', linestyle='None')
axs[1].plot(9.273956163257083, -0.9563886919738228, marker='p', color='cyan', markersize=10, label='60%', linestyle='None')
axs[0].plot(8.576861472272656, 0.02380291467262473, marker='p', color='green', markersize=10, label='60%', linestyle='None')
axs[1].plot(8.576861472272656, -0.9563886919738228, marker='p', color='green', markersize=10, label='60%', linestyle='None')
axs[0].plot(8.276066461175425, 0.02380291467262473, marker='p', color='orange', markersize=10, label='60%', linestyle='None')
axs[1].plot(8.276066461175425, -0.9563886919738228, marker='p', color='orange', markersize=10, label='60%', linestyle='None')
axs[0].plot(7.975154005490858, 0.02380291467262473, marker='p', color='black', markersize=10, label='60%', linestyle='None')
axs[1].plot(7.975154005490858, -0.9563886919738228, marker='p', color='black', markersize=10, label='60%', linestyle='None')

axs[0].plot(10.334694979304546, 0.07058107428570727, marker='p', color='blue', markersize=10, label='CO core', linestyle='None')
axs[1].plot(10.334694979304546, -0.5271575432596126, marker='p', color='blue', markersize=10, label='CO core', linestyle='None')
axs[0].plot(9.352444451110248, 0.07058107428570727, marker='p', color='cyan', markersize=10, label='CO core', linestyle='None')
axs[1].plot(9.352444451110248, -0.5271575432596126, marker='p', color='cyan', markersize=10, label='CO core', linestyle='None')
axs[0].plot(8.655087855223067, 0.07058107428570727, marker='p', color='green', markersize=10, label='CO core', linestyle='None')
axs[1].plot(8.655087855223067, -0.5271575432596126, marker='p', color='green', markersize=10, label='CO core', linestyle='None')
axs[0].plot(8.354259957709539, 0.07058107428570727, marker='p', color='orange', markersize=10, label='CO core', linestyle='None')
axs[1].plot(8.354259957709539, -0.5271575432596126, marker='p', color='orange', markersize=10, label='CO core', linestyle='None')
axs[0].plot(8.05333104639898, 0.07058107428570727, marker='p', color='black', markersize=10, label='CO core', linestyle='None')
axs[1].plot(8.05333104639898, -0.5271575432596126, marker='p', color='black', markersize=10, label='CO core', linestyle='None')

axs[0].errorbar(7.70,-0.18, xerr=0.11, yerr=0.18, fmt='o', color='yellow')
axs[1].plot(7.70,-0.75,  marker='*', color='yellow', markersize=12, linestyle='None')
axs[1].errorbar(7.70,-0.75,  xerr=0.11, yerr=0.18, fmt='o', color='yellow')

axs[0].set_xlabel('log$_{10}$ (O/H) + 12', fontsize=22)
axs[0].set_ylabel('log$_{10}$ (N/O)', fontsize=22)
axs[0].tick_params(axis='both', which='major', labelsize=16)
axs[0].set_xlim(6, 10.4)
axs[0].set_ylim(-1.5, 1.25)
axs[0].grid(True)

axs[1].set_xlabel('log$_{10}$ (O/H) + 12', fontsize=22)
axs[1].set_ylabel('log$_{10}$ (C/O)', fontsize=22)
axs[1].tick_params(axis='both', which='major', labelsize=16)
axs[1].set_xlim(6, 10.4)
axs[1].set_ylim(-1.5, 1.25)
axs[1].grid(True)

plt.tight_layout()

axs[0].plot((10.109073569991084, 9.141451345135723, 8.445479690283769, 8.144825948004701, 7.8439842013422565), (-0.016867925287295537, -0.016867925287295537, -0.016867925287295537, -0.016867925287295537, -0.016867925287295537), color="blue", linestyle="-", label=None)
axs[1].plot((10.109073569991084, 9.141451345135723, 8.445479690283769, 8.144825948004701, 7.8439842013422565), (-1.1537218112108867, -1.1537218112108867, -1.1537218112108867, -1.1537218112108867, -1.1537218112108867), color="blue", linestyle="-", label=None)
axs[0].plot((10.25339868845647, 9.273956163257083, 8.576861472272656, 8.276066461175425, 7.975154005490858), (0.02380291467262473, 0.02380291467262473, 0.02380291467262473, 0.02380291467262473, 0.02380291467262473), color="brown", linestyle="-", label=None)
axs[1].plot((10.25339868845647, 9.273956163257083, 8.576861472272656, 8.276066461175425, 7.975154005490858), (-0.9563886919738228, -0.9563886919738228, -0.9563886919738228, -0.9563886919738228, -0.9563886919738228), color="brown", linestyle="-", label=None)
axs[0].plot((10.334694979304546, 9.352444451110248, 8.655087855223067, 8.354259957709539, 8.05333104639898), (0.07058107428570727, 0.07058107428570727, 0.07058107428570727, 0.07058107428570727, 0.07058107428570727), color="magenta", linestyle="-", label=None)
axs[1].plot((10.334694979304546, 9.352444451110248, 8.655087855223067, 8.354259957709539, 8.05333104639898), (-0.5271575432596126, -0.5271575432596126, -0.5271575432596126, -0.5271575432596126, -0.5271575432596126), color="magenta", linestyle="-", label=None)

plt.show()

## be clear about dilution.

## stages of quasar formation from protostar-pulsations-explosion-quasar

# Set the x and y limits for both top and bottom subplots
# Uncomment and modify the following lines as needed
# axs[0].set_xlim(xmin_top, xmax_top)
# axs[0].set_ylim(ymin_top, ymax_top)
# axs[1].set_xlim(xmin_bottom, xmax_bottom)
# axs[1].set_ylim(ymin_bottom, ymax_bottom)
