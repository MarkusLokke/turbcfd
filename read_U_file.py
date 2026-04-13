import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_U_file(path):
    """
    _summary_
        The function reads U file and outputs U1(y), U2(y), from a given "path"
    _Arguments_
        Inputs:
            path    : input file path  (str)
        Output: 
            y       : y-output value   (npArray)
            U1      : U1-output value  (npArray)
            U2      : U2-output value  (npArray)
    """
    # Reading U file
