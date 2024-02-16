# Lorentz Transformation
einstein’s postulates
	laws of physics are the same in all inertial (non-accelerated) reference frames
	the speed of light in a vacuum has the same value c ($3*10^8$) in all reference frames
	principle of equivalence: form of physical law same in all locally inertial reference frames
event: location in space and time
$(x,y,z,v,t)$ in $S$ (”stationary” frame), $(x',y',z',v',t')$ in $S'$ (”moving” frame)
	align $x$ with direction of $v$
	$x' = \gamma(x-vt), y' = y, z' = z, t' = \gamma(-\frac{v}{c^2}x+t)$ ($\gamma = \frac{1}{\sqrt{1-\frac{v^2}{c^2}}}, \beta = \frac{v}{c}$)
	inverse transformation: $x = \gamma(x' + vt), y = y', z = z', t = \gamma(t' + \frac{v}{c^2}x'$)
	for $\Delta x = x_2 - x_1$ and $\Delta t = t_2 - t_1$:
		$\Delta x' = \gamma(\Delta x - v\Delta t)$
		$\Delta t' = \gamma(-\frac{v}{c^2}\Delta x + \Delta t)$
		$\Delta x = \gamma(\Delta x' + v\Delta t')$
		$\Delta t = \gamma(\frac{v}{c^2}\Delta x' + \Delta t')$
proper time $d\tau = \frac{dt}{\gamma}$, proper velocity $\eta = \frac{dx}{d\tau} = \gamma v$ (lab frame)
relativistic momentum
	$\vec{p} = \gamma_u m\vec{u}$
relativistic energy
	$E = \gamma mc^2$
	relativistic kinetic energy $T = mc^2(\gamma - 1)$, internal energy $E_{int} = mc^2$
	$E = |p|c$ for massless particles (defined by frequency $E = hf$)
## Formalism
lorentz tensor $\Lambda = \begin{pmatrix}\gamma & -\gamma\beta & 0 & 0 \\ -\gamma\beta & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$
## Consequences
relative simultaneity: events simultaneous in one frame are not in another frame
time dilation: durations in one frame are not the same in another frame
length contraction: lengths in one frame are not the same in another frame
velocity addition
	$u$ in $S$ (”stationary” frame), $u'$ in $S'$ (”moving” frame) moving with relative velocity $v$
	$u = \frac{u' + v}{1 + \frac{u'v}{c^2}}$
	$u' = \frac{u-v}{1-\frac{uv}{c^2}}$
twin paradox
	non-inertial reference frame for twin in spaceship
doppler effect
	toward observer (blue shift)
		$f = f'\sqrt{\frac{1+\frac{v}{c}}{1-\frac{v}{c}}}$
	away from observer (red shift)
		$f = f'\sqrt{\frac{1-\frac{v}{c}}{1+\frac{v}{c}}}$