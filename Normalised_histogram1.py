
# Normalised Histogram with Modified Values

import numpy as np
from scipy.interpolate import interp1d

M_tot = [491.0, 771.0, 778.0, 932.0, 1135.0, 1331.0, 1662.0, 1923.0, 3053.0, 4477.0, 6127.0]
M_CO = [104.0, 165.0, 163.0, 247.0, 440.0, 317.0, 630.0, 746.0, 650.0, 759.0, 1252.0]
X_H_10 = [0.360, 0.319, 0.299, 0.339, 0.204, 0.293, 0.198, 0.232, 0.202, 0.297, 0.173]
X_He_10 = [0.430, 0.460, 0.473, 0.588, 0.669, 0.519, 0.766, 0.577, 0.737, 0.687, 0.779]
X_C_10 = [0.002, 0.002, 0.003, 0.002, 0.003, 0.005, 0.001, 0.001, 0.0, 0.0, 0.001]
X_N_10 = [0.056, 0.053, 0.038, 0.056, 0.086, 0.067, 0.031, 0.046, 0.018, 0.015, 0.039]
X_O_10 = [0.150, 0.162, 0.18, 0.015, 0.038, 0.114, 0.004, 0.137, 0.004, 0.001, 0.006]
X_H_40 = [0.256, 0.235, 0.24, 0.185, 0.124, 0.201, 0.095, 0.181, 0.202, 0.153, 0.079]
X_He_40 = [0.450, 0.466, 0.454, 0.682, 0.691, 0.528, 0.852, 0.573, 0.737, 0.816, 0.855]
X_C_40 = [0.002, 0.002, 0.002, 0.002, 0.003, 0.003, 0.001, 0.001, 0.0, 0.001, 0.001]
X_N_40 = [0.079, 0.074, 0.058, 0.102, 0.122, 0.103, 0.047, 0.061, 0.022, 0.029, 0.056]
X_O_40 = [0.210, 0.218, 0.235, 0.028, 0.058, 0.163, 0.004, 0.174, 0.004, 0.001, 0.008]
X_H_CO = [0.235, 0.217, 0.22, 0.161, 0.115, 0.186, 0.078, 0.171, 0.157, 0.073, 0.04]
X_He_CO = [0.451, 0.465, 0.447, 0.695, 0.691, 0.528, 0.864, 0.571, 0.765, 0.884, 0.875]
X_C_CO = [0.002, 0.002, 0.002, 0.003, 0.005, 0.003, 0.002, 0.001, 0.001, 0.003, 0.004]
X_N_CO = [0.084, 0.079, 0.065, 0.108, 0.126, 0.108, 0.05, 0.064, 0.033, 0.034, 0.06]
X_O_CO = [0.224, 0.232, 0.253, 0.031, 0.063, 0.172, 0.006, 0.183, 0.012, 0.006, 0.017]
all_masses = [6127, 4477, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186, 1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491]

# Initial data arrays
all_masses = [6127, 4477, 2630, 2612, 2479, 1924, 1923, 1892, 1845, 1717, 1662, 1596, 1514, 1489, 1331, 1294, 1274, 1236, 1186, 1177, 1135, 1008, 986, 969, 965, 956, 946, 932, 924, 921, 912, 912, 887, 886, 862, 858, 856, 834, 808, 778, 771, 748, 740, 739, 732, 726, 709, 696, 689, 686, 683, 682, 667, 666, 646, 631, 625, 620, 616, 580, 567, 565, 549, 536, 515, 511, 510, 507, 507, 497, 493, 491, 479, 472, 472, 454, 444, 431, 430, 410, 398, 382, 378, 356, 347, 312, 295, 259, 236, 223, 217, 207, 205, 197, 132, 108, 106, 100, 85, 50, 40]
def interpolate_values(original_x, original_y, new_x):
    interpolator = interp1d(original_x, original_y, kind='linear', fill_value='extrapolate')
    return interpolator(new_x)

# Merging and sorting the M_tot and all_masses arrays
M_tot_updated = sorted(list(set(M_tot + all_masses)))
M_tot_10_updated = 0.1 * np.array(M_tot_updated)
M_tot_40_updated = 0.4 * np.array(M_tot_updated)

M_CO_updated = interpolate_values(M_tot, M_CO, M_tot_updated)
M_tot_CO_updated = np.array(M_tot_updated) - np.array(M_CO_updated)
# Interpolation of data arrays

X_H_10_updated = interpolate_values(M_tot, X_H_10, M_tot_updated)
X_He_10_updated = interpolate_values(M_tot, X_He_10, M_tot_updated)
X_C_10_updated = interpolate_values(M_tot, X_C_10, M_tot_updated)
X_N_10_updated = interpolate_values(M_tot, X_N_10, M_tot_updated)
X_O_10_updated = interpolate_values(M_tot, X_O_10, M_tot_updated)
X_H_40_updated = interpolate_values(M_tot, X_H_40, M_tot_updated)
X_He_40_updated = interpolate_values(M_tot, X_He_40, M_tot_updated)
X_C_40_updated = interpolate_values(M_tot, X_C_40, M_tot_updated)
X_N_40_updated = interpolate_values(M_tot, X_N_40, M_tot_updated)
X_O_40_updated = interpolate_values(M_tot, X_O_40, M_tot_updated)
X_H_CO_updated = interpolate_values(M_tot, X_H_CO, M_tot_updated)
X_He_CO_updated = interpolate_values(M_tot, X_He_CO, M_tot_updated)
X_C_CO_updated = interpolate_values(M_tot, X_C_CO, M_tot_updated)
X_N_CO_updated = interpolate_values(M_tot, X_N_CO, M_tot_updated)
X_O_CO_updated = interpolate_values(M_tot, X_O_CO, M_tot_updated)

M_H_ejecta_10 = (np.array(X_H_10_updated) * np.array(M_tot_10_updated))
M_He_ejecta_10 = (np.array(X_He_10_updated) * np.array(M_tot_10_updated))
M_C_ejecta_10 = (np.array(X_C_10_updated) * np.array(M_tot_10_updated))
M_N_ejecta_10 = (np.array(X_N_10_updated) * np.array(M_tot_10_updated))
M_O_ejecta_10 = (np.array(X_O_10_updated) * np.array(M_tot_10_updated))
M_H_ejecta_40 = (np.array(X_H_40_updated) * np.array(M_tot_40_updated))
M_He_ejecta_40 = (np.array(X_He_40_updated) * np.array(M_tot_40_updated))
M_C_ejecta_40 = (np.array(X_C_40_updated) * np.array(M_tot_40_updated))
M_N_ejecta_40 = (np.array(X_N_40_updated) * np.array(M_tot_40_updated))
M_O_ejecta_40 = (np.array(X_O_40_updated) * np.array(M_tot_40_updated))
M_H_ejecta_CO = (np.array(X_H_CO_updated) * np.array(M_tot_CO_updated))
M_He_ejecta_CO = (np.array(X_He_CO_updated) * np.array(M_tot_CO_updated))
M_C_ejecta_CO = (np.array(X_C_CO_updated) * np.array(M_tot_CO_updated))
M_N_ejecta_CO = (np.array(X_N_CO_updated) * np.array(M_tot_CO_updated))
M_O_ejecta_CO = (np.array(X_O_CO_updated) * np.array(M_tot_CO_updated))

# Merging and sorting the M_tot and all_masses arrays
M_tot_updated = sorted(list(set(M_tot + all_masses)))

# Creating bins and extracting hist_vals
bins = np.arange(400, np.max(M_tot_updated) + 100, 100)
hist_vals, bin_edges = np.histogram(all_masses, bins=bins)

# Normalizing hist_vals
normalized_hist_vals = hist_vals / np.sum(hist_vals)



#############
import numpy as np



trimmed_length = len(normalized_hist_vals)

# 10% Case
M_H_ejecta_10_n = np.array(M_H_ejecta_10[:trimmed_length]) * normalized_hist_vals
M_He_ejecta_10_n = np.array(M_He_ejecta_10[:trimmed_length]) * normalized_hist_vals
M_C_ejecta_10_n = np.array(M_C_ejecta_10[:trimmed_length]) * normalized_hist_vals
M_N_ejecta_10_n = np.array(M_N_ejecta_10[:trimmed_length]) * normalized_hist_vals
M_O_ejecta_10_n = np.array(M_O_ejecta_10[:trimmed_length]) * normalized_hist_vals

# 40% Case
M_H_ejecta_40_n = np.array(M_H_ejecta_40[:trimmed_length]) * normalized_hist_vals
M_He_ejecta_40_n = np.array(M_He_ejecta_40[:trimmed_length]) * normalized_hist_vals
M_C_ejecta_40_n = np.array(M_C_ejecta_40[:trimmed_length]) * normalized_hist_vals
M_N_ejecta_40_n = np.array(M_N_ejecta_40[:trimmed_length]) * normalized_hist_vals
M_O_ejecta_40_n = np.array(M_O_ejecta_40[:trimmed_length]) * normalized_hist_vals

# CO Core Case
M_H_ejecta_CO_n = np.array(M_H_ejecta_CO[:trimmed_length]) * normalized_hist_vals
M_He_ejecta_CO_n = np.array(M_He_ejecta_CO[:trimmed_length]) * normalized_hist_vals
M_C_ejecta_CO_n = np.array(M_C_ejecta_CO[:trimmed_length]) * normalized_hist_vals
M_N_ejecta_CO_n = np.array(M_N_ejecta_CO[:trimmed_length]) * normalized_hist_vals
M_O_ejecta_CO_n = np.array(M_O_ejecta_CO[:trimmed_length]) * normalized_hist_vals
