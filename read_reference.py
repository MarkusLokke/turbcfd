from scipy.io import loadmat
import os

def read_ref(path):
    '''
    hm
    '''
    data_dict = loadmat(path)
    y_plus = data_dict["y_plus"]
    U_plus = data_dict["U_plus"]
    uu_plus = data_dict["uu_plus"]
    vv_plus = data_dict["vv_plus"]
    uv_plus = data_dict["uv_plus"]

    return y_plus, U_plus, uu_plus, vv_plus, uv_plus

