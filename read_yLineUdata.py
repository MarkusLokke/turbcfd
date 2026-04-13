#### Imports ####

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#### Function ####

def read_yLineUdata(path):
    """
    Summary:
    The function reads yLine_U_non_uniform.xy file and outputs y, U1, U2, from a given "path"
        
    Inputs:
    path    : input file path  (str)
        
    Output:
    y       : y-output value   (np.Array)
    U1      : U1-output value  (np.Array)
    U2      : U2-output value  (np.Array)
    """
    # Reading yLine_U_non_uniform.xy
    data = np.loadtxt(path, delimiter='\t')
    y = np.array(data[:, 0])
    U1 = np.array(data[:, 1])
    U2 = np.array(data[:, 2])
    return y, U1, U2

#### Usage Example ####

# from read_yLineUdata import read_yLineUdata
# path1 = "DNS1000/kwsst/yLine_U_non_uniform.xy"

# y, u1, u2 = read_yLineUdata(path1)

# print(u2)
# print(len(u2))
# print(type(u2))