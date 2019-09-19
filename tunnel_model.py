from plotly.offline import plot, iplot
import plotly.io as pio
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import scipy.io as sio
import math
# pio.templates.default = 'plotly_white'
pd.set_option('precision', 2)

# CONSTANTS
NU = 1.13 * 1e-6  # m2.s-1 kinematic viscosity
RHO_AIR = 1.2  # m3/kg density


def lamb(roughness, d_hyd, rey):
    return 1.325 / (np.log(roughness / (3.7 * d_hyd) + 5.74 / rey ** 0.9)) ** 2


def reynolds(velocity, d_hyd):
    nu = NU
    return velocity * d_hyd / nu


def friction_loss(velocity, roughness, d_hyd, length):
    rho_air = RHO_AIR
    return - 1/2 * rho_air * lamb(roughness, d_hyd, reynolds(velocity, d_hyd)) * length / d_hyd * velocity ** 2


def exp_con_loss(a0, a1, velocity, expansion_bool=True):
    rho_air = RHO_AIR
    if expansion_bool:
        betta = 1
    else:
        betta = 0.63 + 0.37 * (a0 / a1) ** 3
    return - 1/2 * rho_air * (1 + betta * a1 / a0) ** 2 * velocity ** 2


def extension_loss():
    pass


def in_out_loss(velocity, zetta):
    rho_air = RHO_AIR
    return - 1/2 * rho_air * zetta * velocity ** 2


def area_loss():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
