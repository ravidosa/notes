# Finite Potential Well
see [Schrodinger Equation](schrodinger-equation.md)
$V(x) = \begin{cases} -V_0 & -a \leq x \leq a \\ 0 & |x| > a \end{cases}$
## Bound States
$\psi(x) = \begin{cases} Fe^{-\kappa|x|} & |x| > a \\ D\cos lx & 0 \leq |x| \leq a\end{cases}$ ($\kappa = \sqrt{\frac{-2mE}{\hbar}}, l = \frac{\sqrt{2m(E + V_0)}}{\hbar}$)
number of states increases with $z_0 =\frac{a}{\hbar}\sqrt{2mV_0}$
	$\tan z = \sqrt{(\frac{z_0}{z})^2 - 1}$ means wave function + derivative continuous at boundary ($z = la$)
	$E_n + V_0 \approx \frac{n^2\pi^2\hbar^2}{2m(2a)^2}$ for odd $n$ (not analytically solvable)
finite bound states for finite well
always at least one bound state
depth of penetration $\delta = \frac{1}{\alpha}$, quantum mechanical tunneling
## Scattering States
$\psi(x) = \begin{cases} Ae^{ikx} + Be^{-ikx} & x < -a \\ C\sin lx + D\cos lx & -a < x < a \\ Fe^{ikx} & x > a\end{cases}$ ($k = \frac{\sqrt{2mE}}{\hbar}$)
$A$ incident, $B$ reflected, $F$ transmitted
$T^{-1} = 1 + \frac{V_0^2}{4E(E + V_0)}\sin^2\frac{2a}{\hbar}\sqrt{2m(E + V_0)}$
	full transmission when $E_n + V_0 = \frac{n^2\pi^2\hbar^2}{(2m)(2a)^2}$