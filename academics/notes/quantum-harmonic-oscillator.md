# Quantum Harmonic Oscillator
see [Schrodinger Equation](schrodinger-equation.md)
$V(x) = \frac{1}{2}m\omega x^2$
ladder operators
	raising operator $\hat{a}_+ = \frac{1}{\sqrt{2\hbar m\omega}}(-i\hat{p} + m\omega x)$, lowering operator $\hat{a}_- = \frac{1}{\sqrt{2\hbar m\omega}}(i\hat{p} + m\omega x)$, mutual adjoints
		hamiltonian becomes $\hat{H} = \hbar\omega(\hat{a}_-\hat{a}_+ - \frac{1}{2})$
	canonical commutation relation: $[x, \hat{p}] = i\hbar$
	$\psi_0(x) = (\frac{m\omega}{\pi \hbar})^{\frac{1}{4}}e^{-\frac{m\omega}{2\hbar}x^2}, \psi_n(x) =  \frac{1}{\sqrt{n!}}(\hat{a}_+)^n\psi_0(x)$
		$E_n = (n + \frac{1}{2})\hbar\omega$
	$\hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1}$
	$x = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a}_+ + \hat{a}_-), \hat{p} = \sqrt{\frac{\hbar m\omega}{2}}(\hat{a}_+ - \hat{a}_-)$
hermite polynomials
	$\psi_n(x) = (\frac{m\omega}{\pi\hbar})^{\frac{1}{4}}\frac{1}{\sqrt{2^n n!}} H_n(x)e^{-\frac{x^2}{2}}$
wag the dog