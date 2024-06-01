# Weak Interaction
mediated by massive charged $W^\pm$ bosons, couples fermions differing by 1 unit electric charge
no [parity](symmetry.md#parity) conservation
## Charged-Current
$V-A$ structure
	decompose into vector and axial vector
		$j_V^\mu = \bar{u}(p')\gamma^\mu u(p), j_A^\mu = \bar{u}(p')\gamma^\mu\gamma^5 u(p)$
	combined vector and axial vector produces parity violation
	vertex factor $\frac{-ig_W}{\sqrt{2}}\frac{1}{2}\gamma^\mu(1 - \gamma^5)$

| quantity     | form                                                          | components | boson spin |
| ------------ | ------------------------------------------------------------- | ---------- | ---------- |
| scalar       | $\bar{\psi}\phi$                                              | 1          | 0          |
| pseudoscalar | $\bar{\psi}\gamma^5\phi$                                      | 1          | 0          |
| vector       | $\bar{\psi}\gamma^\mu\phi$                                    | 4          | 1          |
| axial vector | $\bar{\psi}\gamma^\mu\gamma^5\phi$                            | 4          | 1          |
| tensor       | $\bar{\psi}(\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu)\phi$ | 6          | 2          |

chiral structure
	chiral projection operators $P_R = \frac{1}{2}(1 + \gamma^5), P_L = \frac{1}{2}(1 - \gamma^5)$
		can decompose any spinor
	for charged-current, only left-handed chiral particles, right-handed chiral antiparticles
		helicity in $E \gg m$ limit
	helicity in pion decay
		charged pions only decay through weak interaction to electron/muon final states
W boson propagator
	in $q^2 \ll m_W^2$ limit, $\frac{-ig_{\mu\nu}}{q^2 - m_W^2}$
		approximate by $i\frac{g_{\mu\nu}}{m_W^2}$
	$\frac{G_F}{\sqrt{2}} = \frac{g_W^2}{8m_W^2}, G_F = 1.16638 \cdot 10^{-1}$ GeV-2
lepton universality
	same strength for all lepton flavors
$j_+^\mu = \frac{g_W}{\sqrt{2}}\bar{\nu}\gamma^\mu\frac{1}{2}(1 - \gamma^5)e, j_-^\mu = \frac{g_W}{\sqrt{2}}\bar{e}\gamma^\mu\frac{1}{2}(1 - \gamma^5)\nu$
	$j_3^\mu = I_W^{(3)}g_W\bar{f}\gamma^\mu\frac{1}{2}(1 - \gamma^5)f$
## Electroweak Unification
neutral field mixes with photon-like field
	$A_\mu = B_\mu\cos\theta_W + W_\mu^{(3)}\sin\theta_W, Z_\mu = -B_\mu\sin\theta_W + W_\mu^{(3)}\cos\theta_W$
W boson two transverse polarization modes ($S_z = \pm1$), one longitudinal ($S_z = 0$)
	polarization 4-vectors $\epsilon_-^\mu = \frac{1}{\sqrt{2}}(0, 1, -i, 0), \epsilon_L^\mu = \frac{1}{m_W}(p_z, 0, 0, E), \epsilon_+^\mu = -\frac{1}{\sqrt{2}}(0, 1, i, 0)$
W-pair production
	$e^+e^- \to W^+W^-$ center of mass energy increases without limit in high energy
associated [symmetry](symmetry-physics.md)
photon and Z boson as linear combinations of $B_\mu, W_\mu^{(3)}$
	weak mixing angle $\theta_W$, $\sin^2\theta_W = 0.23146 \pm 0.00012$
		$e = g_W\sin\theta_W = g_Z\sin\theta_W\cos\theta_W$
	Z boson coupled to left/right handed chiral states
	Z-boson feynman rule: $-i\frac{1}{2}g_Z\gamma^\mu(c_V - c_V\gamma^5)$

| fermion                    | $Q_f$ | $I_W^{(3)}$ | $Y_L$ | $Y_R$ | $c_L$ | $c_R$ | $c_V$ | $c_A$ |
| -------------------------- | ----- | ----------- | ----- | ----- | ----- | ----- | ----- | ----- |
| $\nu_e, \nu_\mu, \nu_\tau$ | 0     | 1/2         | -1    | 0     | 1/2   | 0     | 1/2   | 1/2   |
| $e^-, \mu^-, \tau^-$       | -1    | -1/2        | -1    | -2    | -0.27 | 0.23  | -0.04 | -1/2  |
| $u, c, t$                  | 2/3   | 1/2         | 1/3   | 4/3   | 0.35  | -0.15 | 0.19  | 1/2   |
| $d, s, b$                  | -1/3  | -1/2        | 1/3   | -2/3  | -0.42 | 0.08  | -0.35 | -1/2  |

Z boson decay
	$\Gamma(Z \to f\bar{f}) = \frac{g_Z^2m_Z}{48\pi}(c_V^2 + c_A^2)$
	mostly final states with jets