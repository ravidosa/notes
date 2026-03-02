import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import scipy as sp

# system of units
# hbar/2m = 1
# may take some minutes to run (iterations printed as tracker)

# initial wavefunctions
def psi0_gaussian(x, y, x0, y0, s, k): # gaussian wavepacket
    # initial position: (x0, y0)
    # width of wave packet: s
    # wavenumber: k
    psi = np.exp(-1/2 * ((x - x0) ** 2 + (y - y0) ** 2) / s ** 2) * np.exp(1j * k * (x - x0))
    psi[0, :], psi[-1, :], psi[:, 0], psi[:, -1] = 0, 0, 0, 0 # boundary conditions
    return psi
def psi0_plane(x, x0, w, k):
    wi, ax, bx, nx = w
    psi = np.piecewise(x, [x > x0, x <= x0], [lambda x: np.exp(1j * k * (x - x0)), 0])
    psi[0:int(nx/2 * (1 - wi / (bx - ax))), :], psi[int(nx/2 * (1 + wi / (bx - ax))):, :] = 0, 0
    return psi

# potentials
def V_free_particle(x, y, t):
    return 0+0j
def V_hard_sphere(x, y, t, a, v0):
    r = np.sqrt(x ** 2 + y ** 2)
    if r < a:
        return v0+0j
    return 0+0j
def V_double_slit(x, y, t, a, s, w, v0):
    if x > -w/2 and x < w/2:
        if y > s/2 + a or y < -s/2 - a or (y > -s/2 and y < s/2):
            return v0+0j
    return 0+0j

# store psi, |psi|
psi_arr = []
mod_arr = []

test = 1
# 0: gaussian wavepacket in a box
# 1: hard-sphere scattering
if test == 0:
    nx, ny, nt = 50, 50, 500 # mesh points
    ax, ay, at = -5, -5, 0 # boundaries of mesh
    bx, by, bt = 5, 5, 5
    k = 15 * np.pi
    fcn = lambda x, y: psi0_gaussian(x, y, 2.5, 0, 0.5, k)
    V = V_free_particle
    t_ind = True
    ttl1 = "2D Gaussian Wavepacket"
    ttl2 = "Gaussian Wavepacket in a Box"
if test == 1:
    nx, ny, nt = 100, 100, 500 # mesh points
    ax, ay, at = -20, -20, 0 # boundaries of mesh
    bx, by, bt = 20, 20, 10
    k = 15 * np.pi
    fcn = lambda x, y: psi0_plane(x, 2.5, (10, ax, bx, nx), k)
    V = lambda x, y, t: V_hard_sphere(x, y, t, 2, 1000)
    t_ind = True
    ttl1 = "Plane Wave"
    ttl2 = "Hard-Sphere Scattering"
if test == 2:
    nx, ny, nt = 100, 100, 500 # mesh points
    ax, ay, at = -10, -10, 0 # boundaries of mesh
    bx, by, bt = 10, 10, 5
    k = 15 * np.pi
    fcn = lambda x, y: psi0_plane(x, 5, (10, ax, bx, nx), k)
    V = lambda x, y, t: V_double_slit(x, y, t, 0.4, 1.6, 1.2, 1000000)
    t_ind = True
    ttl1 = "Plane Wave"
    ttl2 = "Double-Slit in a Box"

dx, dy, dt = (bx - ax)/nx, (by - ay)/ny, (bt - at)/nt # mesh spacing
mx, my = -dt / (2j * dx ** 2), -dt / (2j * dy ** 2)
n = (nx) * (ny)
x = np.linspace(ax, bx, nx)
y = np.linspace(ay, by, ny)
x, y = np.meshgrid(x, y)
psi = fcn(x, y)
    
def mod(psi): # |psi|
    re = np.real(psi)
    im = np.imag(psi)
    return np.sqrt(re ** 2 + im ** 2)
def crank_nicolson(V, t, d, m, n): #crank-nicolson finite difference method
    dx, dy, dt = d
    mx, my = m
    A, M = np.zeros((n, n), dtype="complex"), np.zeros((n, n), dtype="complex")
    for k in range(n):
        i = k // (nx) + 1 # retrieve i, j from k
        j = k % (ny) + 1
        A[k, k] = 1 + 2 * mx + 2 * my + 1j * dt / 2 * V(ax + i * dx, ay + j * dy, t)
        M[k, k] = 1 - 2 * mx - 2 * my - 1j * dt / 2 * V(ax + i * dx, ay + j * dy, t)

        if i != 1:
            A[k, (i - 2) * (ny) + j - 1] = -my
            M[k, (i - 2) * (ny) + j - 1] = my
        if i != nx:
            A[k, i * (ny) + j - 1] = -my
            M[k, i * (ny) + j - 1] = my
        if j != 1:
            A[k, k - 1] = -mx
            M[k, k - 1] = mx
        if j != ny:
            A[k, k + 1] = -mx
            M[k, k + 1] = mx
    return sp.sparse.csc_matrix(A), M

# fit final wavefunction to expected
def fit_func(mesh, A, a, b, c, d):
    x, y = mesh
    theta = np.arctan(y / x)
    return A * (np.exp(1j * k * x) + (a * theta ** 3 + b * theta ** 2 + c * theta + d) * np.exp(1j * k * np.sqrt(x ** 2 + y ** 2)) / np.sqrt(x ** 2 + y ** 2) ** 0.5)
def fit_mod(mesh, A, a, b, c, d):
    return np.reshape(mod(fit_func(mesh, A, a, b, c, d)), (n))

fig1 = plt.figure(1) # initial wavefunction as 3d contour
axs = plt.axes(projection='3d')
axs.contour3D(x, y, mod(psi), 50, cmap=plt.get_cmap("hot"))
axs.contour3D(x, y, np.vectorize(V)(x, y, 0), 50, cmap='binary')
axs.set_xlabel('x')
axs.set_ylabel('y')
axs.set_zlabel('$|\psi|$')
plt.title(ttl1)
psi_arr.append(np.copy(psi))
if t_ind:
    A, M = crank_nicolson(V, 0, (dx, dy, dt), (mx, my), n)
for i in range(1, nt):
    if i % 10 == 0: print(i)
    t = at + i * dt
    if not t_ind:
        A, M = crank_nicolson(V, t, (dx, dy, dt), (mx, my), n)
    psi_vec = np.reshape(psi, (n))
    psi_vec = sp.sparse.linalg.spsolve(A, np.matmul(M, psi_vec))
    psi = np.reshape(psi_vec, (nx, ny))
    psi_arr.append(np.copy(psi))
    mod_arr.append(mod(psi))

fig2 = plt.figure(2) # wavefunction over time as heatmap
plt.title(ttl2)
img = plt.imshow(mod_arr[0], extent=[ax, bx, ay, by], cmap=plt.get_cmap("hot"), vmin=0, vmax=np.max(mod_arr), zorder=1)
def animate(i):
    img.set_data(mod_arr[i])
    img.set_zorder(1)
    return img,
anima = anim.FuncAnimation(fig2, animate, interval=1, frames=np.arange(0, nt, 2), repeat=True, blit=0)

fig3 = plt.figure(3) # |f(theta)| as 3d contour
axs = plt.axes(projection='3d')
popt, pcov = sp.optimize.curve_fit(fit_mod, (x, y), np.reshape(mod(psi), (n)))
A, a, b, c, d = popt
axs.contour3D(x, y, mod(fit_func((x, y), A, a, b, c, d)), 50, cmap='binary')
axs.set_xlabel('x')
axs.set_ylabel('y')
axs.set_zlabel('$|f(\\theta)|$')

print("[4th degree polynomial approximation]\nf(theta) = {0} * theta^3 + {1} * theta^2 + {2} * theta + {3}".format(a, b, c, d))
sigma, err = sp.integrate.quad(lambda x: (a * x ** 3 + b * x ** 2 + c * x + d) ** 2, 0, np.pi)
print("sigma =", sigma)
plt.show()