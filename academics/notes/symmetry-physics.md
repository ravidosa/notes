# Symmetry (physics)
bound $qqq$ state
	$\psi = \phi_{flavor}\chi_{spin}\xi_{color}\eta_{space}$
	when $L = 0$, $\phi_{flavor}\chi_{spin}$ antisymmetric
## Flavor Symmetry
isospin: proton and neutron form isospin doublet, $I = \frac{1}{2}, I_3 = \pm\frac{1}{2}$
$\hat{T} = \frac{1}{2}\sigma$
structure of $SU(2)$ generators, lie algebra
	$[\hat{T}_i, \hat{T}_j] = i\epsilon_{ijk}\hat{T}_k$
	total isospin $\hat{T}^2 = \hat{T}_i^2$
	ladder operators $\hat{T}_{\pm} = \hat{T}_1 \pm i\hat{T}_2$
up and down quarks in isospin $\frac{1}{2}$ multiplet
combine to baryons using [clebsch-gordan coefficients](quantum-mechanics-3d.md)
	three-quark combos: spin $\frac{3}{2}$ quadruplet, symmetric and antisymmetric mixed symmetry doublets
## [Parity](dirac-equation.md)
$\psi'(x, t) = \hat{P}\psi(x, t) = \psi(-x, t)$
$\hat{P}^2 = I, \hat{P}^\dagger = \hat{P}$
real eigenvalues ($\pm1$)
	spin-half particles $1$, antiparticles $-1$
	vector bosons have $-1$ parity
conserved in QED, QCD
	intrinsic parity, orbital wavefunction parity $(-1)^\ell$

| quantity     | rank | parity | ex            |
| ------------ | ---- | ------ | ------------- |
| scalar       | 0    | +      |               |
| pseudoscalar | 0    | -      | dot product   |
| vector       | 1    | -      |               |
| axial vector | 1    | +      | cross product |
not conserved in weak interaction
## Color
$8$ massless gluons for each of the generators of $SU(3)$
$r, g, b$ color charges (opposite for antiparticles)
	only nonzero colored particles couple to gluons
		leptons color neutral, quarks in three orthogonal color states
	QCD invariant under unitary transformations in color space
color isospin $I^c_3$, color hypercharge $Y^c$
feynman diagram
	$-\frac{1}{2}ig_S\lambda^a_{ji}\gamma^\mu$ for vertex, $-i\frac{g_{\mu\nu}}{q^2}\delta^{ab}$ for gluon propagator
gell-mann matrix acts on color wavefunction
	nondiagonal changes color
	gluons carry color charge
	$r\bar{g}, g\bar{r}, r\bar{b}, b\bar{r}, b\bar{b}, b\bar{g}, \frac{1}{\sqrt{2}}(r\bar{r} - g\bar{g}), \frac{1}{\sqrt{6}}(r\bar{r} + g\bar{g} - 2b\bar{b})$
color confinement: colored objects confined to color singlet states (unproved)
	nonzero color charge cannot propagate as free particle (only singlet states)
		infinite energy needed to separate quarks to infinity
	$q\bar{q}$ behaves like meson flavor (colored octet colorless singlet)
		all hadrons color singlets, $\psi^c(q\bar{q}) = \frac{1}{\sqrt{3}}(r\bar{r} + g\bar{g} + b\bar{b})$
		$qq\bar{q}, q\bar{q}\bar{q}$ don't exist (nonzero color)
	$qqq$ has single singlet state with color wavefunction
		$\psi^c(qqq) = \frac{1}{\sqrt{6}}(rbg - rbg + gbr - grb + brg - bgr)$
		all confirmed states mesons, baryons, antibaryons (higher may exist but unproven)
	if $U(3)$, not $SU(3)$, then ninth generator $\frac{1}{\sqrt{3}}(r\bar{r} + g\bar{g} + b\bar{b})$ 
		colorless ($I^c_3 = Y^c = 0$), unconfined
		behave like photon, infinite range strong force
hadronization and jets
	quark and antiquark separate, color field restricted to tube, energy forms new quark-antiquark pairs, continue until energy low enough to form colorless hadrons
## Local Gauge Principle
QED interaction term $q\gamma^0\gamma^\mu A_\mu$, QCD interaction term $q\gamma^\mu A_\mu\psi$
$U(1)$ local gauge symmetry from QED (charge)
$SU(3)$ local phase transformation from QCD (color)
	$g_ST^a\gamma^\mu G^2_\mu \psi = g_S\frac{1}{2}\lambda^a\gamma^\mu G^2_\mu \psi$
$SU(2)$ local phase transformation from weak
	$ig_WT_k\gamma^\mu W_\mu^k\varphi_L = ig_W\frac{1}{2}\sigma_k\gamma^\mu W_\mu^k\varphi_L$
	$W_\mu^\pm = \frac{1}{\sqrt{2}}(W_\mu^{(1)} \mp iW_\mu^{(2)})$
	results in [weak charged currents](weak-interaction.md)
## Violations
### CP Violation
seen in [weak interaction](weak-interaction.md) between quarks and leptons (observed in quarks)
in early universe, matter-antimatter asymmetry
	baryon number violation
	C, CP violation
	no thermal equilibrium
cabibbo hypothesis: weak interactions same strength for quarks and leptons, but quark weak eigenstates differ from mass eigenstates
	$\begin{pmatrix} d' \\ s' \end{pmatrix} = \begin{pmatrix} \cos\theta_c & \sin\theta_c\\ -\sin\theta_c & \cos\theta_c \end{pmatrix}\begin{pmatrix} d \\ s \end{pmatrix}$, cabibbo angle $\theta_c \approx 13$
	CKM matrix (extend to 3rd gen standard model)
	$\begin{pmatrix} d' \\ s' \\ b' \end{pmatrix} = \begin{pmatrix} V_{ud} & V_{us} & V_{ub} \\ V_{cd} & V_{cs} & V_{cb} \\ V_{td} & V_{ts} & V_{tb} \end{pmatrix}\begin{pmatrix} d \\ s \\ b \end{pmatrix}$
	$\begin{pmatrix} |V_{ud}| & |V_{us}| & |V_{ub}| \\ |V_{cd}| & |V_{cs}| & |V_{cb}| \\ |V_{td}| & |V_{ts}| & |V_{tb}| \end{pmatrix} = \begin{pmatrix} 0.974 & 0.225 & 0.004 \\ 0.225 & 0.973 & 0.041 \\ 0.009 & 0.040 & 0.999 \end{pmatrix}$
		nearly diagonal (wolfenstein parametrization)
first seen in neutral kaon system
	$K^0, \bar{K}^0$ decay only by weak interaction
	$K_S, K_L$ with similar masses, different lifetimes
		$K_2 \to \pi\pi, K_L \to \pi\pi\pi$
		2-pion always CP-even, 3-pion always CP-odd
	violation from $K^0, \bar{K}^0$ mixing
strangeness oscillation
	CPLEAR, $\Delta m = m(K_L) - m(K_S) = (3.483 \pm 0.006) \cdot 10^{-15}$ GeV