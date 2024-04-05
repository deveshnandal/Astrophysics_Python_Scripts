#Coloured table, use this file !!!!!
######## With He ########

import numpy as np
import os

# List of models
models = [
    {"path": '/Users/hermit/Observatory/StarCalc/SMS/1e-3Msun_yr/P002z0S0.v0177201.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 2393, "label": "3053"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test1_6127M_SS0/P002z0S0.v0129331.gz', "skip_header": 304, "cutoff": -87, "m_ejecta": 4865, "label": "6127"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/4477M_SS1/P002z0S0.v0152721', "skip_header": 297, "cutoff": -68, "m_ejecta": 3718, "label": "4477"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1923M_SS6/P002z0S0.v0558831.gz', "skip_header": 334, "cutoff": -125, "m_ejecta": 1167, "label": "1923"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1662M_SS10/P002z0S0.v0217041.gz', "skip_header": 296, "cutoff": -118, "m_ejecta": 1022, "label": "1662"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1331M_SS14/P002z0S0.v0094231.gz', "skip_header": 309, "cutoff": -90, "m_ejecta": 1004, "label": "1331"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/1135M_S20/P002z0S0.v0527201.gz', "skip_header": 2069, "cutoff": -117, "m_ejecta": 685, "label": "1135"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/932M_SS27/P002z0S0.v0276841.gz', "skip_header": 3, "cutoff": -95, "m_ejecta": 675, "label": "932"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/778M_SS39/P002z0S0.v0088411.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 605, "label": "778"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/771M_SS40/P002z0S0.v0090481.gz', "skip_header": 310, "cutoff": -85, "m_ejecta": 596, "label": "771"},
    {"path": '/Users/hermit/Observatory/StarCalc/SMS_Var_Accr/Test2_491M_SS71/P002z0S0.v0350111.gz', "skip_header": 310, "cutoff": -84, "m_ejecta": 377, "label": "491"}
]

# Sort the models in ascending order of 'label'
models = sorted(models, key=lambda k: float(k['label']))

# List to store table rows
table_rows = []

for index, model in enumerate(models):
    file_path = model["path"]
    skip_header = model["skip_header"]
    cutoff = model["cutoff"]
    m_ejecta = model["m_ejecta"]
    label = float(model["label"])
    CO_core_mass = label - (m_ejecta + 10)

    # Load data
    H1 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[6])[:cutoff][::-1]
    He4 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[7])[:cutoff][::-1]
    C12 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[8])[:cutoff][::-1]
    N14 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[33])[:cutoff][::-1]
    O16 = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[9])[:cutoff][::-1]
    M_sol = (np.transpose(np.genfromtxt(file_path, skip_header=skip_header))[49])[:cutoff][::-1]

    # Calculate the differences in mass
    dM = np.diff(M_sol)

    # Calculate the 90% and 60% mass points
    mass_90 = 0.9 * label
    mass_60 = 0.6 * label

    # Find the indices where M_sol is closest to mass_90 and mass_60
    idx_90 = np.abs(M_sol - mass_90).argmin()
    idx_60 = np.abs(M_sol - mass_60).argmin()
    idx_CO = np.abs(M_sol - CO_core_mass).argmin()

    # Initialize lists to store the cumulative abundances
    H_list = []
    He_list = []
    C_list = []
    N_list = []
    O_list = []

    # Calculate cumulative abundances for each element
    for i in range(len(dM)):
        H_cumulative = np.sum(H1[i:-1]*dM[i:]) / np.sum(dM[i:])
        He_cumulative = np.sum(He4[i:-1]*dM[i:]) / np.sum(dM[i:])
        C_cumulative = np.sum(C12[i:-1]*dM[i:]) / np.sum(dM[i:])
        N_cumulative = np.sum(N14[i:-1]*dM[i:]) / np.sum(dM[i:])
        O_cumulative = np.sum(O16[i:-1]*dM[i:]) / np.sum(dM[i:])

        H_list.append(H_cumulative)
        He_list.append(He_cumulative)
        C_list.append(C_cumulative)
        N_list.append(N_cumulative)
        O_list.append(O_cumulative)

    # Extract the abundances at these masses
    values_90 = [H_list[idx_90], He_list[idx_90], C_list[idx_90], N_list[idx_90], O_list[idx_90]]
    values_60 = [H_list[idx_60], He_list[idx_60], C_list[idx_60], N_list[idx_60], O_list[idx_60]]
    values_CO = [H_list[idx_CO], He_list[idx_CO], C_list[idx_CO], N_list[idx_CO], O_list[idx_CO]]

    # Form the row for the LaTeX table
    row = f"{label:.0f} & {CO_core_mass:.0f} "
    for v in values_90 + values_60 + values_CO:
        row += f"& \\cellcolor{{lightgray}}{v:.3f} "
    row += "\\\\"
    table_rows.append(row)

# Combine the table rows into a single string
table = "\n".join(table_rows)

# The LaTeX table
latex_table = f"""
\\documentclass{{article}}
\\usepackage{{geometry}}
\\usepackage{{xcolor}}
\\usepackage{{colortbl}}
\\usepackage{{tabularx}}
\\geometry{{a4paper, total={{170mm,257mm}}, left=20mm, top=20mm}}

\\definecolor{{lightgray}}{{rgb}}{{0.83, 0.83, 0.83}}
\\definecolor{{lightblue}}{{rgb}}{{0.67, 0.84, 0.90}}
\\definecolor{{lightgreen}}{{rgb}}{{0.56, 0.93, 0.56}}

\\begin{{document}}

\\begin{{table*}}[t]
\\centering
\\begin{{tabularx}}{{\\textwidth}}{{*{{17}}{{X}}}}
\\caption{{Abundances at 90\\%, 60\\%, and CO core mass for different stellar models.}} \\\\ \\hline
& & \\multicolumn{{5}}{{c}}{{\\cellcolor{{lightgray}}10\\%}} & \\multicolumn{{5}}{{c}}{{\\cellcolor{{lightblue}}40\\%}} & \\multicolumn{{5}}{{c}}{{\\cellcolor{{lightgreen}}CO core}} \\\\ \\hline
M_{{\\text{{tot}}}} (M_{{\\odot}}) & M_{{\\text{{CO}}}} (M_{{\\odot}}) & X_{{\\text{{H}}}} & X_{{\\text{{He}}}} & X_{{\\text{{C}}}} & X_{{\\text{{N}}}} & X_{{\\text{{O}}}} & X_{{\\text{{H}}}} & X_{{\\text{{He}}}} & X_{{\\text{{C}}}} & X_{{\\text{{N}}}} & X_{{\\text{{O}}}} & X_{{\\text{{H}}}} & X_{{\\text{{He}}}} & X_{{\\text{{C}}}} & X_{{\\text{{N}}}} & X_{{\\text{{O}}}} \\\\ \\hline
{table}
\\end{{tabularx}}
\\end{{table*}}

\\end{{document}}
"""

# Write the LaTeX table to a .tex file on your desktop
with open(os.path.expanduser("~/Desktop/table.tex"), "w") as f:
    f.write(latex_table)
