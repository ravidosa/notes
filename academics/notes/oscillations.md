# Oscillations
## Linear Differential Equations
linear diff eq: $a\ddot{x} + b\dot{x} + cx + d$
	homogenous if $d = 0$, else inhomogenous
standard cases
	case 1: $\dot{x} = ax$
		$x(t) = Ae^{at}, \dot{x}(t) = aAe^{at}, \ddot{x}(t) = a^2Ae^{at}$
	case 2: $\ddot{x}=ax$
	$x(t) = Ae^{\sqrt{a}t} + Be^{-\sqrt{a}t}, v(t) = \sqrt{a}Ae^{\sqrt{a}t} + -\sqrt{a}Be^{-\sqrt{a}t}, a(t) = aAe^{\sqrt{a}t} + aBe^{-\sqrt{a}t}$
		negative $a$, $a= -\omega^2$
			oscillatory motion
			$x(t) = E\cos(\omega t + \phi_1) \text{ or } F\sin(\omega t + \phi_2)$
			$v(t) = -E\omega\sin(\omega t + \phi_1) \text{ or } F\omega\cos(\omega t + \phi_2)$
			$a(t) = -E\omega^2\cos(\omega t + \phi_1) \text{ or } -F\omega^2\sin(\omega t + \phi_2)$
		positive $a$, $a = \alpha^2$
			exponential growth/decay
			$x(t) = E\cosh(\alpha t + \phi_1) \text{ or } F\sinh(\alpha t + \phi_2)$
			$v(t) = -E\omega\sinh(\alpha t + \phi_1) \text{ or } F\omega\cosh(\alpha t + \phi_2)$
			$a(t) = -E\omega^2\cosh(\alpha t + \phi_1) \text{ or } -F\omega^2\sinh(\alpha t + \phi_2)$
	case 3: $\ddot{x} + 2\gamma\dot{x} + ax = 0$
		damped oscillator
		$x(t) = e^{-\gamma t}(Ae^{\sqrt{\gamma^2 - a} t} + Be^{-\sqrt{\gamma^2 - a}t})$
		$\gamma^2 - a < 0$, sines and cosines (underdamped)
		$\gamma^2 - a > 0$, exponential (overdamped)
		$\gamma^2 - a = 0$, exponential (critically damped)
## Simple Harmonic Motion
linear restoring force (hooke's law)
	see [Simple Harmonic Motion](small-oscillations.md#simple-harmonic-motion)
use $x(0)$, $v(0)$ to solve
conservation of energy
## Damped Oscillators
see [Simple Harmonic Motion](small-oscillations.md#damping-and-resonance)
$\ddot{x} + 2\gamma\dot{x} + \omega^2 x = 0$
	$x(t) = e^{-\gamma t}(Ae^{\Omega t} + Be^{-\Omega t})$ for $\Omega^2 = \gamma^2 - \omega^2$, $\gamma > 0$, $\omega^2 > 0$
	$\Omega^2 < 0$ ($\gamma < \omega$) (underdamped)
		$x(t) = e^{-\gamma t}C\cos(\tilde{\omega} t + \phi)$ for $\Omega = i\tilde{\omega}$
		$\dot{x}(t) = -\gamma e^{-\gamma t}(C\cos(\tilde{\omega}t + \phi)) + e^{-\gamma t}(-\tilde{\omega} C\sin(\tilde{\omega}t + \phi))$
	$\Omega^2 > 0$ ($\gamma > \omega$) (overdamped)
		$x(t) = Ae^{-(\gamma - \Omega)t} + Be^{-(\gamma + \Omega)t}$
		$\dot{x}(t) = -(\gamma - \Omega)Ae^{-(\gamma - \Omega)t} + -(\gamma + \Omega)Be^{-(\gamma + \Omega)t}$
	$\Omega^2 > 0$ ($\gamma = \omega$)
		$x(t) = e^{-\gamma t}(A + Bt)$
		$\dot{x}(t) = -\gamma e^{-\gamma t}(A + Bt) + Be^{-\gamma t}$
		only crosses $0$ once, if at all ($t = -\frac{A}{B}$)
## Driven and Coupled Oscillators
periodic driving force $f_d(t) = F_d\cos\omega_d t$
$\ddot{x} + 2\gamma\dot{x} + \omega^2 x = \sum_{n=1}^N C_n e^{i\omega_nt}$
	$x(t) = e^{-\gamma t}(Ae^{\sqrt{\gamma^2 - \omega^2}t} + Be^{-\sqrt{\gamma^2 - \omega^2}t}) + \frac{c_0}{-\omega_d^2 + 2i\gamma\omega_d +\omega^2}e^{i\omega_d t}$
damped and driven
	$x(t) = \frac{F}{R}\cos(\omega_d t - \phi) + e^{\gamma t}(Ae^{\Omega t} + Be^{-\Omega t})$ for $\Omega = \sqrt{\gamma^2 - \omega^2}$, $F = \frac{F_d}{m}$, $R = \sqrt{(\omega^2 - \omega_d^2)^2 + (2\gamma\omega_d)^2}$, $\cos\phi = \frac{\omega^2 - \omega_d^2}{R}$, $\sin\phi = \frac{2\gamma\omega_d}{R}$
coupled oscillators
	$x_1(t), x_2(t)$
	add and subtract equations
	undecoupleable
		assume form $x_1(t) = Ae^{i\alpha t}, x_2(t) = Be^{i\alpha t}$
		$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} A \\ B \end{pmatrix}e^{i\alpha t}$
		set determinant of matrix to zero, solve roots
		obtain eigenvectors and eigenfrequencies
	normal modes
		possible oscillations
		eigenfrequencies
			frequencies of oscillation