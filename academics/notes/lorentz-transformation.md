# Lorentz Transformation
einstein’s postulates
	laws of physics are the same in all inertial (non-accelerated) reference frames
	the speed of light in a vacuum has the same value c ($3*10^8$) in all reference frames
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