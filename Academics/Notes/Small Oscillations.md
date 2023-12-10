### Simple Harmonic Motion
$F=-kx$ for displacement from equilibium $x$, spring constant $k$
	$x(t)=A\sin(\omega t + \phi)$ for $\omega=\sqrt{\frac{k}{m}}$
	period $T=\frac{2\pi}{\omega}=2\pi f=2\pi\sqrt{\frac{m}{k}}$
$v_{max}=A\sqrt{\frac{k}{m}}$
$E_{tot}=\frac{1}{2}kA^2$
	elastic potential energy, cons of energy
### Other Restoring Forces
pendulum
	$\omega = \sqrt{\frac{g}{L}}$
	$E_{tot}=\frac{1}{2}mgl\theta_{max}^2$
	$T=2\pi\sqrt{\frac{I}{mgd}}$
potential wells
	$\omega=\sqrt{\frac{k}{\mu}}$, $\mu=\frac{m_1m_2}{m_1+m_2}$
### Damping and Resonance
damping
	$x(t)=Ae^{-\frac{\beta}{2m}t}\sin(\omega t + \phi)$, $\omega = \sqrt{\frac{k}{m}-\frac{\beta^2}{4m^2}}$
resonance
	$A=\dfrac{F_o}{\sqrt{m^2\left(\omega_d^2-\omega_o^2\right)^2+\beta^2\omega_d^2}}$
### Coupled Oscillators and Normal Modes
parallel add, series harmonic
$\frac{d^2x_1}{dt^2}+\frac{2k}{m}x_1-\frac{k}{m}x_2=0$, $\frac{d^2x_2}{dt^2}+\frac{2k}{m}x_2-\frac{k}{m}x_1=0$
	add $(1)+\beta(2)$, $q(t)=x_1(t)+\beta x_2(t)$
	eliminate $\omega$, find solutions for $\beta$ or vice versa
	two simple harmonic equations $q_1,q_2=q_i(t)=A_i\sin(\omega_i t + \phi_i)$
	find $x_1(t)$ and $x_2(t)$ as function of $q_1(t), q_2(t)$
normal modes masses oscillate at same frequency
	2 masses → $(1, 1), (1, -1)$
	3 masses → $(1, 1, 1), (\sqrt{2}, 0, -\sqrt{2}), (1, -1, 1)$