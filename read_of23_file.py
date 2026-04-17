####################### Imports #######################
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



####################### Read nut file #######################

def read_nut_file(path, skip_lines = 23, read_length = 1000):
    """
    Reads a _nut_ datafile and splits creates a numpy array from file. 
    The function requires that the elements are separated using space and not comma. 

    Args:
        path (_string_): Path is the relative path of the file you want to read and convert to a np.array
        skip_lines (_int_): is the amount of lines to skip before adding to your dataset datset. 23 Lines by default
        read_Length (_int_): is the length of the dataset you want to read. 1000 lines by default
    """
    
    #### Creating Output and parameters ####
    nu_t = np.zeros( [read_length] )
    counter = 0

    with open(path, 'r') as file:
        lines = file.readlines()
        #### find data size ####        
        for line in lines:
            #### count lines and check if it should skip ####
            counter +=1 
            if counter <= skip_lines:
                continue
            elif counter > read_length + skip_lines:
                break

            #### Processing line into list ####
            line = line.strip()
            line = line.replace(")", "").replace('(', '')
            lines_list = line.split() 
            
            #### Adding to output ####
            nu_t [counter - skip_lines - 1] = lines_list[0]
    return nu_t

#### Usage Example ####

# from read_of23_file import read_nut_file
# path3 = "DNS1000/kwsst/nut"

# nut = read_nut_file(path3)
# # nut = read_nut_file(path3, 23, 1000) #Use when the file does not follow standard layout, I.E not: 23, 1000

# print(nut)
# print(len(nut))
# print(type(nut))



####################### Read wallShearStress file #######################

def read_wallShearStress_file(path):
    """
    Reads a _wallShearStress_ datafile and returns the last element. 
    The function requires that the elements are separated using space and not comma. 

    Args:
        path (_string_): Path is the relative path of the file you want to read
        u_tau (_float_): Output value for u_tau
    """
    #### Creating Output and parameters ####
    with open(path, 'r') as file:
        last_line = file.readlines()[-1]
        u_tau = np.sqrt(abs(float(last_line.split()[2].strip('()'))))
    return u_tau

#### Usage Example ####: 

# from read_of23_file import read_wallShearStress_file
# path4 = "DNS1000/kwsst/wallShearStress.dat"

# u_tau_1 = read_wallShearStress_file(path4)

# print(u_tau_1)
# print(type(u_tau_1))



####################### Read k file #######################

def read_k_file(path, skip_lines = 23, read_length = 1000):
    """
    Reads a _k_ datafile and splits creates a numpy array from file. 
    The function requires that the elements are separated using space and not comma. 

    Args:
        path (_string_): Path is the relative path of the file you want to read and convert to a np.array
        skip_lines (_int_): is the amount of lines to skip before adding to your dataset datset. 23 Lines by default
        read_Length (_int_): is the length of the dataset you want to read. 1000 lines by default
    """
    
    #### Creating Output and parameters ####
    k = np.zeros( [read_length] )
    counter = 0

    with open(path, 'r') as file:
        lines = file.readlines()
        #### find data size ####        
        for line in lines:
            #### count lines and check if it should skip ####
            counter +=1 
            if counter <= skip_lines:
                continue
            elif counter > read_length + skip_lines:
                break

            #### Processing line into list ####
            line = line.strip()
            line = line.replace(")", "").replace('(', '')
            lines_list = line.split() 
            
            #### Adding to output ####
            k [counter - skip_lines - 1] = lines_list[0]
    return k

#### Usage Example ####

# from read_of23_file import read_k_file
# path6 = "DNS1000/kwsst/k"

# k = read_k_file(path6)
# # k = read_k_file(path3, 23, 1000) #Use when the file does not follow standard layout, I.E not: 23, 1000

# print(k)
# print(len(k))
# print(type(k))



####################### Read U file #######################

def read_U_file(path, skip_lines = 23, read_length = 1000):
    """
    Reads a _U_ datafile and splits creates a numpy array from file. 
    The function requires that the elements are separated using space and not comma. 

    Args:
        path (_string_): Path is the relative path of the file you want to read and convert to a np.array
        skip_lines (_int_): is the amount of lines to skip before adding to your dataset datset. 23 Lines by default
        read_Length (_int_): is the length of the dataset you want to read. 1000 lines by default
    """
    
    #### Creating Output ####
    # file_data = np.zeros( [read_length, cols])
    U1 = np.zeros( [read_length])
    U2 = np.zeros( [read_length])
    U3 = np.zeros( [read_length])

    with open(path, 'r') as file:
        lines = file.readlines()
        #### find data size ####
        rows = len(lines)
        counter = 0
        
        for line in lines:
            #### count lines and check if it should skip ####
            counter +=1 
            if counter <= skip_lines:
                continue
            elif counter > read_length + skip_lines:
                break

            #### Processing line into list ####
            line = line.strip()
            line = line.replace(")", "").replace('(', '')
            lines_list = line.split() 
            
            #### Adding to output ####
            U1 [counter - skip_lines - 1] = lines_list[0]
            U2 [counter - skip_lines - 1] = lines_list[1]
            U3 [counter - skip_lines - 1] = lines_list[2]
            # outlist = []
            # for idx in range(len(lines_list)):
            #     try:
            #         outlist.append( float(lines_list[idx]) )
            #     except Exception:
            #         continue
            # file_data[ counter - skip_lines - 1 ] = outlist
    return U1, U2, U3
    # return file_data

#### Usage Example ####: 
# from read_of23_file import read_U_file
# path2 = "DNS1000/kwsst/U"

# u1, u2, u3 = read_U_file(path2)
# # u1, u2, u3 = read_U_file(path2, 23, 1000) #Use when the file does not follow standard layout, I.E not: 23, 1000

# print(u1)
# print(len(u1))
# print(type(u1))



####################### Read CFD SIM RAW DATA #######################

def read_cfd_sim(folder_path, skip_lines = 23, read_length = 1000):
    """
    U1, U2, U3, nut, u_tau = read_cfd_sim(folder_path)
    
    Reads _U_, _nut_ and _wallShearStress_ datafiles and returns all relevant variables. 
    The function requires that the files use the standard names to properly read the data. 

    Args:
        folder_path (_string_): relative path to the folder containing the given simulation
        
        U1 (_np.Array_): Output np.array for U1
        U2 (_np.Array_): Output np.array for U2
        U3 (_np.Array_): Output np.array for U3
        nut (_np.Array_): Output np.array for nut
        u_tau (_np.float_): Output value for u_tau
    """
    try:
        nut_path = folder_path + "/nut"
        nut = read_nut_file(nut_path)
    except FileNotFoundError: 
        print(nut_path + "not found")
        nut = np.zeros([read_length])
        
    try:
        tau_path = folder_path + "/wallShearStress.dat"
        u_tau = read_wallShearStress_file(tau_path)
    except FileNotFoundError: 
        print(tau_path + "not found")
        u_tau = np.zeros([read_length])
        
    try:
        k_path = folder_path + "/k"
        k = read_k_file(k_path)
    except FileNotFoundError: 
        print(k_path + "not found")
        k = 0
        
    U_path = folder_path + "/U"
    U1, U2, U3 = read_U_file(U_path)

    return U1, U2, U3, nut, k, u_tau
    
#### Usage Example ####
# from read_of23_file import read_cfd_sim

# folder_path = "DNS1000/kwsst"
# U1, U2, U3, nut, k, u_tau = read_cfd_sim(folder_path)


# print(" %%%%%%%%%%%%%%%%%%% Test Output %%%%%%%%%%%%%%%%%%% ")
# print()

# print("U1")
# print(len(U1))
# print(type(U1))
# print()

# print("U2")
# print(len(U2))
# print(type(U2))
# print()

# print("U3")
# print(len(U3))
# print(type(U3))
# print()

# print("nut")
# print(len(nut))
# print(type(nut))
# print()

# print("k")
# print(len(k))
# print(type(k))
# print()

# print("u_tau")
# print(u_tau)
# print(type(u_tau))
# print()

# print(" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
# print()