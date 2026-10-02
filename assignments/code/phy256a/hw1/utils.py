import numpy as np
import matplotlib.pyplot as plt
from sympy import Poly
from scipy.integrate import odeint

# Find real roots of sympy symbolic 1d function f, which is a function of a parameter dvar and a coordinate ivar, both sympy symbols
#  But use numpy numerical root finder
def RealRoots1D(func, ivar, threshold=1e-8):
    func_poly = Poly(func, ivar)
    # Convert given sympy polynomial func to list of coefficients, that of highest power first.
    polyCoef = func_poly.all_coeffs()
    pp = np.poly1d(polyCoef)
    rr = np.roots(pp)
    real_valued = rr.real[abs(rr.imag) < threshold]
    return(real_valued.tolist())

def fixed_points(f, dvar, ivar, low_lim, high_lim, step):
    """
    Find fixed points of 1D function 'f' with
    'dvar' the dependent or control variable
    'ivar' the independent variable
    for 'dvar' within limits 'low_lim' to 'high_lim'
    stepping 'dvar' incrementally in steps of size 'step'.
    """
    fps = []
    for r_val in np.arange(low_lim, high_lim, step):
        func = f.subs({dvar: r_val})
        fps.extend([r_val, root] for root in RealRoots1D(func, ivar))
    return fps

# Set the font dictionaries (for plot title and axis titles)
title_font = {'fontname':'DejaVu Sans', 'size':'20', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'DejaVu Sans', 'size':'18'}

def PlotStatesVParameter(list_of_states, p_min, p_max, x_label, y_label):
    p, y = zip(*list_of_states)
    y_min = np.amin(y)
    y_max = np.amax(y)
    f = plt.figure()
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title("Bifurcation diagram")
    plt.plot(p, y, 'o', color='black',markersize=2)
    y_range = y_max - y_min
    plt.xlim(p_min,p_max)
    plt.ylim(y_min - 0.1 * y_range, y_max + 0.1 * y_range)
    plt.axvline(0)
    plt.axhline(0)
    return f

def Phase_Portrait(ODE_rhs, xlims, ylims, nICs=100, time=10, polar=False):
    """Draw trajectories in the plane.
    """
    ICs = [(xlims[0] + (xlims[1] - xlims[0]) * np.random.random(), ylims[0] + (ylims[1] - ylims[0]) * np.random.random()) for _ in range(nICs)]
    t = np.linspace(0, time, 500)
    f = plt.figure()
    for ic in ICs:
        trajectory = odeint(ODE_rhs, ic, t)
        if polar:
            xs = trajectory[:, 0]
            ys = trajectory[:, 1]
            xs, ys = xs * np.cos(ys), xs * np.sin(ys)
            plt.plot(xs, ys, 'b-')
            plt.plot(ic[0] * np.cos(ic[1]), ic[0] * np.sin(ic[1]), 'r.')
        else:
            plt.plot(trajectory[:, 0], trajectory[:, 1], 'b-')
            plt.plot(ic[0], ic[1], 'r.')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Phase Portrait")
    return f