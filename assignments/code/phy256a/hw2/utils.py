import numpy as np
import matplotlib.pyplot as plt
from sympy import Poly, lambdify
from scipy.integrate import odeint

def cobweb(a_function, var, start, mask = 0, iterations = 10, xmin = 0, xmax = 1):
    f = plt.figure()
    iter_list = []
    current = start
    for i in range(mask):
        current = a_function.subs(var, current)
    for i in range(iterations):
        iter_list.append([current,a_function.subs(var, current)])
        current = a_function.subs(var, current)
        iter_list.append([current,current])
    its = np.array(iter_list)
    plt.plot(its.T[0],its.T[1],'ro-')
    plt.plot(np.array([0,1]),np.array([0,1]),'k:')
    lam_var = lambdify(var, a_function, modules=['numpy'])
    x_vals = np.linspace(0, 1, 100)
    y_vals = lam_var(x_vals)
    plt.plot(x_vals, y_vals,'b-')
    #    lam_var = lambdify(var, a_function.subs(var,a_function), modules=['numpy'])
    #    x_vals = np.linspace(0, 1, 100)
    #    y_vals = lam_var(x_vals)
    #    plt.plot(x_vals, y_vals,'b-')
    return f

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

def PlotStatesVParameter(list_of_states,p_min,p_max,x_label,y_label):
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

def Phase_Portrait(ODE_rhs, xlims, ylims, ax=plt, nICs=100, time=10, polar=False):
    """Draw trajectories in the plane.
    """
    ICs = [(xlims[0] + (xlims[1] - xlims[0]) * np.random.random(), ylims[0] + (ylims[1] - ylims[0]) * np.random.random()) for _ in range(nICs)]
    t = np.linspace(0, time, 500)
    for ic in ICs:
        trajectory = odeint(ODE_rhs, ic, t)
        if polar:
            xs = trajectory[:, 0]
            ys = trajectory[:, 1]
            xs, ys = xs * np.cos(ys), xs * np.sin(ys)
            ax.plot(xs, ys, 'b-')
            ax.plot(ic[0] * np.cos(ic[1]), ic[0] * np.sin(ic[1]), 'r.')
        else:
            ax.plot(trajectory[:, 0], trajectory[:, 1], 'b-')
            ax.plot(ic[0], ic[1], 'r.')
    if ax == plt:
        ax.xlabel("x")
        ax.ylabel("y")
        ax.title("Phase Portrait")
    else:
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Phase Portrait")

def PlotStatesStabilitiesVParameter(stable_states, unstable_states, p_min, p_max, x_label, y_label):
    p, y = zip(*stable_states)
    y_min = np.amin(y)
    y_max = np.amax(y)
    pp, yy = zip(*unstable_states)
    yy_min = np.amin(yy)
    yy_max = np.amax(yy)
    if yy_min < y_min:
        y_min = yy_min
    if yy_max > y_max:
        y_max = yy_max
    fig = plt.figure()
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title("Bifurcation diagram")
    plt.plot(p, y, 'o', color='blue',markersize=2)
    plt.plot(pp, yy, 'o', color='red',markersize=2)
    y_range = y_max - y_min
    plt.xlim(p_min,p_max)
    plt.ylim(y_min-0.1*y_range,y_max+0.1*y_range)
    plt.axvline(0)
    plt.axhline(0)
    return fig

def fixed_points_1DODE(f, dvar, ivar, low_lim, high_lim):
    """
    """
    sfps = []
    ufps = []
    step = (high_lim - low_lim)/1000.0
    for r_val in np.arange(low_lim, high_lim, step):
        func = f.subs({dvar: r_val})
        dfunc = func.diff(ivar)
        roots = RealRoots1D(func,ivar,threshold=1e-8)
        for root in roots:
            if dfunc.subs({ivar: root}) < 0:
                sfps.append((r_val, root))
            else:
                ufps.append((r_val, root))
    return PlotStatesStabilitiesVParameter(sfps,ufps,low_lim,high_lim,dvar,'Fixed Points (blue stable, red unstable)')

def fixed_points_1DMap(f, dvar, ivar, low_lim, high_lim):
    """
    """
    sfps = []
    ufps = []
    step = (high_lim - low_lim)/1000.0
    for r_val in np.arange(low_lim, high_lim, step):
        func = f.subs({dvar: r_val})
        dfunc = func.diff(ivar)
        roots = RealRoots1D(func-ivar,ivar,threshold=1e-8)
        for root in roots:
            if abs(dfunc.subs({ivar: root})) < 1:
                sfps.append((r_val, root))
            else:
                ufps.append((r_val, root))
    return PlotStatesStabilitiesVParameter(sfps,ufps,low_lim,high_lim,dvar,'Fixed Points (blue stable, red unstable)')

def plot_1d_vfield(x_dot, xlims, ax=plt):
    x_dot = np.vectorize(x_dot)
    x, y = np.meshgrid(np.linspace(xlims[0],xlims[1],20),np.linspace(0,0.5,6))
    ax.quiver(x, y, x_dot(x), 0 * x)
    if ax == plt:
        ax.xlabel("x")
        ax.ylabel("y")
    else:
        ax.set_xlabel("x")
        ax.set_ylabel("y")

def plot_2d_vfield(x_dot, y_dot, xlims, ylims, ax):
    x_dot = np.vectorize(x_dot)
    y_dot = np.vectorize(y_dot)
    x, y = np.meshgrid(np.linspace(xlims[0],xlims[1],20),np.linspace(ylims[0],ylims[1],20))
    ax.quiver(x, y, x_dot(x, y), y_dot(x, y))
    if ax == plt:
        ax.xlabel("x")
        ax.ylabel("y")
    else:
        ax.set_xlabel("x")
        ax.set_ylabel("y")