### Stationary States
separation of variables
	$\Psi(x, t) = \psi(x)\phi(t)$
	time-independent schrodinger equation $-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi$
	$\phi(t) = e^{-\frac{iEt}{\hbar}}$
	stationary states: probability density not time-dependent
	hamiltonian: definite total energy
		$\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)$
		$\hat{H}\psi = E\psi$, $\langle H \rangle = E$
	general solution is linear combination of separable
		$\Psi(x, t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t)$
		$|c_n|^2$ probability of energy measurement returning $E_n$
			$\sum_{n=1}^\infty |c_n|^2 = 1$, $\langle H \rangle = \sum_{n=1}^\infty |c_n|^2 E_n$
			probability of energy level, $H$ independent of time,  energy conservation
### The Infinite Square Well
$V(x) = \begin{cases} 0 & 0 \leq x \leq a \\ \infty & \text{otherwise}\end{cases}$
boundary conditions $\psi(0) = \psi(a) = 0$
	$E_n = \frac{n^2\pi^2\hbar^2}{2ma^2}$
	$\psi_n(x) = \sqrt{\frac{2}{a}}\sin(\frac{n\pi}{a}x)$
properties of $\psi_n(x)$
	alternately even/odd
	$\psi_n$ has $n-1$ nodes
	orthonormal: $\int \psi_m(x)^*\psi_n(x) \, dx = \delta_{mn}$
	complete: represent any function (fourier series, dirichlet's theorem)
		$c_n = \int \psi_n(x)^* f(x) \, dx$
### The Harmonic Oscillator
ladder operators
	raising operator $\hat{a}_+ = \frac{1}{\sqrt{2\hbar m\omega}}(-i\hat{p} + m\omega x)$, lowering operator $\hat{a}_- = \frac{1}{\sqrt{2\hbar m\omega}}(i\hat{p} + m\omega x)$
	canonical commutation relation: $[x, \hat{p}] = i\hbar$
	$\psi_0(x) = (\frac{m\omega}{\pi \hbar})^{\frac{1}{4}}e^{-\frac{m\omega}{2\hbar}x^2}, \psi_n(x) =  \frac{1}{\sqrt{n!}}(\hat{a}_+)^n\psi_0(x)$
	$\hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1}$
	$x = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a}_+ + \hat{a}_-), \hat{p} = \sqrt{\frac{\hbar m\omega}{2}}(\hat{a}_+ - \hat{a}_-)$
hermite polynomials
	$\psi_n(x) = (\frac{m\omega}{\pi\hbar})^{\frac{1}{4}}\frac{1}{\sqrt{2^n n!}} H_n(x)e^{-\frac{x^2}{2}}$
### The Free Particle
stationary states of free particle are waves
quantum speed half of classical speed
	not normalizable, no free particle with definite energy
	$\Psi(x, t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx - \frac{\hbar k^2}{2m}t)} \, dk$
		wave packet, multiple energies and speeds
		$\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \Psi(x, 0)e^{-ikx} \, dx$ (plancherel's theorem)
	phase velocity (quantum) vs group velocity (classical)
	see [Continuous Systems](Continuous%20Systems.md)
### The Delta-Function Potential
$V(x) = -\alpha\delta(x)$
	see [Dirac Delta Function](Ordinary%20Differential%20Equations.md#Dirac%20Delta%20Function)
	bound state ($E < 0$)
		single bound state $\psi(x) = \frac{\sqrt{m\alpha}}{\hbar}e^{-\frac{m\alpha|x|}{\hbar^2}}, E = -\frac{m\alpha^2}{2\hbar^2}$
	scattering states ($E > 0$)
		reflection coefficient $R = \frac{1}{1 + (\frac{2\hbar^2E}{m\alpha^2})}$
		reflection coefficient $T = \frac{1}{1 + (\frac{2\hbar^2\alpha^2}{mE})}$
		unchanged if delta barrier instead of delta well
### The Finite Square Well
$V(x) = \begin{cases} -V_0 & -a \leq x \leq a \\ 0 & |x| > a \end{cases}$
	bound states
		$\psi(x) = \begin{cases} Fe^{-\kappa|x|} & |x| > a \\ D\cos lx & 0 \leq |x| \leq a\end{cases}$ ($\kappa = \sqrt{\frac{-2mE}{\hbar}}, l = \frac{\sqrt{2m(E + V_0)}}{\hbar}$)
		number of states increases with $z_0 =\frac{a}{\hbar}\sqrt{2mV_0}$
			$\tan z = \sqrt{(\frac{z_0}{z})^2 - 1}$ means wave function + derivative continuous at boundary ($z = la$)
			$E_n + V_0 \approx \frac{n^2\pi^2\hbar^2}{2m(2a)^2}$ for odd $n$ (not analytically solvable)
		finite bound states for finite well
		always at least one bound state
	scattering states
		$\psi(x) = \begin{cases} Ae^{ikx} + Be^{-ikx} & x < -a \\ C\sin lx + D\cos lx & -a < x < a \\ Fe^{ikx} & x > a\end{cases}$ ($k = \frac{\sqrt{2mE}}{\hbar}$)
		$A$ incident, $B$ reflected, $F$ transmitted
		$T^{-1} = 1 + \frac{V_0^2}{4E(E + V_0)}\sin^2\frac{2a}{\hbar}\sqrt{2m(E + V_0)}$
			full transmission when $E_n + V_0 = \frac{n^2\pi^2\hbar^2}{(2m)(2a)^2}$