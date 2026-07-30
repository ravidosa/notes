from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def PlotTimeSeries(time_vals, x_vals, time_axis_label, variable_label, plot_label, ax=plt):
    """
    Plots a time series.
    
    Parameters
    ----------
    time_vals, x_vals : array-like or scalar
        The horizontal / vertical coordinates of the data points. These are typically 1D arrays. If the parameters are 2-dimensional, the columns are treated as separate data sets.
        
    TimeAxisLabel, VariableLabel, PlotLabel : str
        The labels for the x/y axes and the plot title, respectively.  
    """
    if ax == plt:
        ax.xlabel(time_axis_label)
        ax.ylabel(variable_label)
        ax.title(plot_label)
    else:
        ax.set_xlabel(time_axis_label)
        ax.set_ylabel(variable_label)
        ax.set_title(plot_label)
    ax.plot(time_vals,x_vals)
    ax.plot(0.0,x_vals[0],'.')

def TimeSeries3DODE(ODE_rhs, parameters, initial_condition, n_transients, n_iterations, time_step, variable, time_axis_label, variable_label, plot_label, ax=plt):
    """
    Plot a time series for each coordinate of a specified `ODE_3D`.
    
    Evolves `3D_ODE` via the finite difference method with time step `TimeStep`.
    
    Parameters
    ----------
    ODE_rhs : callable(state, t, Parameters)
        A function which takes a 3D array-like `state` vector and some set of `Parameters` and returns the RHS of the ODE.
        That is, `ODE_rhs(state, t, Parameters)` returns the the time derivative of `state` at time `t`.
        
    Parameters : array-like, dict, etc.
        The parameters of the ODEs. 
        The main requirement here is that `Parameters` should pass into `ODE_rhs` such that `ODE_rhs` behaves as expected.
        
    InitialCondition : array-like
        The intial conditions from which to evolve. Gets passed as the first argument into `ODE_rhs`.
        
    nTransients, nIterations : int
        The number of evolution steps to throw out before plotting (transients) and the number of evolution steps to plot after that, respectively.
        
    TimeStep : float
        The size of finite time step with which to evolve.
        
    Variable : int, specifically 0, 1, or 2
        The variable index for which to plot a time series. For example, if `state` has the form [x, y, z], `Variable = 0` will plot x(t).
        
    TimeAxisLabel, VariableLabel, PlotLabel : str
        The x/y axis labels and plot title, respectively.
    """
    
    # First, a new function to take the RHS of a 3D ODE and turn it into a discrete step evolution.
    def evolve_ODE_3D(ODE_rhs, state, t, parameters, time_step):
        next_state = []
        for i, ddt in enumerate(ODE_rhs(state, t, parameters)):
            next_state.append(state[i] + time_step * ddt)
        return next_state    
    
    # Now the main body (mostly old code).
    import numpy as np
    
    state = initial_condition
    Time = 0
    for i in range(n_transients):
        # state = ODE_3D(state,Parameters) # OLD VERSION
        state = evolve_ODE_3D(ODE_rhs, state, Time, parameters, time_step) # NEW VERSION
        Time += time_step
    orbit = []
    for i in range(n_iterations):
        # state = ODE_3D(state,Parameters) # OLD VERSION
        state = evolve_ODE_3D(ODE_rhs, state, Time, parameters, time_step) # NEW VERSION
        orbit.append((Time,state[variable]))
        Time += time_step
    orb = np.array(orbit)
    time_vals = orb.T[0]
    x_vals = orb.T[1]
    PlotTimeSeries(time_vals, x_vals, time_axis_label, variable_label, plot_label, ax)

def Phase_Portrait_3DODE(ODE_rhs, Name, parameters, initial_condition, ax=plt, time=10, horizontal_var=0, vertical_var=1):
    """
    Plots a 2D phase portrait for a 3D ODE.
    
    Parameters
    ----------
    ODE_rhs : callable(state, t, Parameters)
        A function which takes a 3D array-like `state` vector and some set of `Parameters` and returns the RHS of the ODE.
        That is, `ODE_rhs(state, t, Parameters)` returns the the time derivative of `state` at time `t`.
    
    Name : str
        The title of the plots will be "[Name] Phase Portrait".
        
    Parameters : array-like, dict, etc.
        The parameters of the ODEs. 
        The main requirement here is that `Parameters` should pass into `ODE_rhs` such that `ODE_rhs` behaves as expected.
        
    InitialCondition : array-like
        The intial conditions from which to evolve. Gets passed as the first argument into `ODE_rhs`.
        
    time : float, optional
        How long (in time units) you want to simulate. Default is 10.
        
    HorizontalVar, VerticalVar : int, specifically 0, 1, or 2, optional
        The variable indices for which to plot a phase portrait.
        For example, if `state` has the form [x, y, z], `HorizontalVar = 0, VerticalVar = 1` will plot x(t) on the x-axis and y(t) on the y-axis.
        Defaults are 0, 1.
    """
    
    axis_labels = ["$x$","$y$","$z$"]
    h_label = axis_labels[horizontal_var]
    v_label = axis_labels[vertical_var]
    plot_label = Name + " Phase Portrait"
    if ax == plt:
        ax.xlabel(h_label)
        ax.ylabel(v_label)
        ax.title(plot_label)
    else:
        ax.set_xlabel(h_label)
        ax.set_ylabel(v_label)
        ax.set_title(plot_label)
    t = np.linspace(0, time, 5000)
    trajectory = odeint(ODE_rhs, initial_condition, t, args=tuple([parameters]))
    ax.plot(trajectory[:, horizontal_var], trajectory[:, vertical_var])
    ax.plot(trajectory[:, horizontal_var][0],trajectory[:, vertical_var][0], '.')

def Lorenz_ODE(state, t, parameters=[10.0, 28.0, 8/3]):
    sigma, r, b = parameters
    x, y, z = state
    return [sigma * (y - x), x * (r - z) - y, x * y - b * z]