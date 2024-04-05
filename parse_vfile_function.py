
import numpy as np
import pandas as pd



def parse_vfile(v_filename):
    """
    Reads and parses vfile
    
    Parameters:
        v_filename: (str) filename of v file to parse
    
    Outputs:
        df_vfile: (pd.DataFrame) df containing data from v file
        
    """
    # Reads in v file
    with open(v_filename, 'r') as f:
        vFile = f.readlines()

    # Gets last set of profiles in v file (there can be multiple)
    first_character = [x[:10].strip()[0] for x in vFile][::-1]
    istart = len(first_character) - next((x[0] for x in enumerate(first_character) if x[1] == '#'), 0) - 1
    iheader = istart - 1
    iskip = istart

    # Get model number, age, mtot, nshell, deltat
    head_values = [x for x in vFile[iheader][:-1].split(' ') if x != '']
    header_values = [float(x) for x in head_values]
    header_params = ['model_number', 'star_age', 'star_mass', 'num_zones', 'time_step']
    header_dict = dict(zip(header_params, header_values))

    ordered_header_params = ['model_number', 'num_zones', 'star_age', 'star_mass', 'time_step']

    ordered_header_dict = {k: header_dict[k] for k in ordered_header_params}

    # v file data
    vf = np.genfromtxt(v_filename, skip_header=iskip)

    # Parses columns
    v_columns = [x for x in vFile[istart][:-1].split(' ') if x != '']
    v_columns[0] = v_columns[0][1:]
    v_col_remove = ['correction']
    v_columns = [x for x in v_columns if x not in v_col_remove]

    # Pull out abundances from v file and renames as appropriate
    v_col_abund = ['X', 'Y'] + [x for x in v_columns if x[-1].isdigit() and x != 'N^2']
    mesa_col_abund = [x.lower() for x in v_col_abund]
    v_to_mesa_dict = dict(zip(v_col_abund, mesa_col_abund))
    v_to_mesa_dict['X'] = 'h1'
    v_to_mesa_dict['Y'] = 'he4'
    v_to_mesa_dict['Y3'] = 'he3'
    mesa_to_v_dict = {v: k for k, v in v_to_mesa_dict.items()}
    
    # converts to DataFrame
    df_vfile = pd.DataFrame(vf, columns=v_columns)
    vfile_header = ordered_header_dict
    
    return df_vfile, vfile_header, mesa_to_v_dict, ordered_header_dict



if __name__ == '__main__':
    vfilename = '/path/to/vfile/P002z0S0.v0070661'
    df_vfile, vfile_header, mesa_to_v_dict, ordered_header_dict = parse_vfile(vfilename)