import numpy as np
import matplotlib.pyplot as plt

U_tau = 1

def u1_std(k):
    return 2/3 * k

def u2_std(k, U2, y, nut):
     return 2/3 * k - 2 * nut * np.gradient(U2, y)

def u1u2(U1, y, nut):
     return - nut * np.gradient(U1, y)


def plotter_same_mesh(modelpaths, models):
     return 0


def plotter_same_model(gridpaths, grids):
     return 0