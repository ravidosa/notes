# Rotations and Rigid Bodies
## Rotational Kinematics
angular position $\theta$ in radians
angular displacement $\Delta \theta = \theta_f - \theta_i$
velocity
	average angular velocity $\omega_{avg} = \frac{\Delta \theta}{\Delta t}$
	instantaneous angular velocity $\omega(t) = \frac{d\theta}{dt}$
acceleration
	average angular acceleration $\alpha_{avg} = \frac{\Delta \omega}{\Delta t}$
	instantaneous angular acceleration $\alpha(t) = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$
	$a_c = r\omega^2$, $a_t = r\alpha$
not same for all points on body
linear vs rotational
	$s = r\theta$ , $v = r\omega$, $a = r\alpha$
RHR for direction (clockwise up, counterclockwise down)
## Non-Inertial Frames
inertial is non-accelerated, non-inertial has non-constant v
transformation relations in inertial $(x, y, z, t) \to (x',y',z',t')$
	$t = t'$
	$x' = x - v_xt$, $\frac{dx'}{dt} = \frac{dx}{dt} - v_x$, $\frac{d^2x'}{dt^2} = \frac{d^2x}{dt^2} - \frac{dv_x}{dt} = \frac{d^2x}{dt^2}$
	$y' = y - v_yt$, $\frac{dy'}{dt} = \frac{dy}{dt} - v_y$, $\frac{d^2y'}{dt^2} = \frac{d^2y}{dt^2} - \frac{dv_y}{dt} = \frac{d^2y}{dt^2}$
	$z' = z - v_zt$, $\frac{dz'}{dt} = \frac{dz}{dt} - v_z$, $\frac{d^2z'}{dt^2} = \frac{d^2z}{dt^2} - \frac{dv_z}{dt} = \frac{d^2z}{dt^2}$
transformation relations in non-inertial
	$t = t'$
	$x' = x - v_xt$, $\frac{dx'}{dt} = \frac{dx}{dt} - v_x$, $\frac{d^2x'}{dt^2} = \frac{d^2x}{dt^2} - \frac{dv_x}{dt}$
	$y' = y - v_yt$, $\frac{dy'}{dt} = \frac{dy}{dt} - v_y$, $\frac{d^2y'}{dt^2} = \frac{d^2y}{dt^2} - \frac{dv_y}{dt}$
	$z' = z - v_zt$, $\frac{dz'}{dt} = \frac{dz}{dt} - v_z$, $\frac{d^2z'}{dt^2} = \frac{d^2z}{dt^2} - \frac{dv_z}{dt}$
	do not agree on acceleration, and fictitious force $\mathcal{F}$
		same acceleration for all objects, proportional to mass
		gravity is fictitious (principle of equivalence)
rotating frame (constant $\omega$)
	at rest in $(x', y', z', t')$, rotating in $(x, y, z, t)$
	$\vec{v}' = \vec{v} - \vec{\omega} \times \vec{r}$
	$\frac{d}{dt}_{stat} = \frac{d}{dt}_{rot} + \vec{\omega} \times$
	$\vec{a} = \vec{a}' + 2\vec{\omega}\times\vec{v}' + \vec{\omega}\times(\vec{\omega}\times\vec{r})$
	$\vec{F}' = \vec{F}- 2m\vec{\omega}\times\vec{v}' - m\vec{\omega}\times(\vec{\omega}\times\vec{r})$ (coriolis, centrifugal)
centrifugal is fictitious, centripetal is sum of forces
## Rotational Inertia
$K_{rot} = \frac{1}{2}I\omega^2$, $I = \sum_i m_ir_i^2 = \sum_0^L dm x^2$

| Body | Moment of Inertia |
| ---- | ----------------- |
|  solid cylinder, symmetry axis    | $\frac{1}{2}MR^2$ |
| solid cylinder, central diameter | $\frac{1}{2}MR^2+\frac{1}{12}ML^2$ |
| hoop, symmetry axis | $MR^2$ |
| hoop, central diameter | $\frac{1}{2}MR^2$ |
| solid sphere | $\frac{2}{5}MR^2$ |
|spherical shell | $\frac{2}{3}MR^2$ |
| rod, center | $\frac{1}{12}ML^2$ |
| rod, end | $\frac{1}{3}ML^2$ |

additivity around common axis
	$I = I_1 + I_2$
parallel axis theorem
	$I = I_{cm} + Md^2$
minimum for center of mass
if rotating freely in space, axis of rotation must pass through center of mass
## Dynamics of Rotating Objects
rolling without slipping and pulleys
	total kinetic energy (sum of linear and rotational) constant if no loss to thermal
		$K_{tot} = \frac{1}{2}mv_{cm}^2 + \frac{1}{2}I_{cm}\omega^2$
larger final velocity does not mean arrive first
unwinding spool
	$v_f = \sqrt{\frac{4mgh}{2m+M}}$
massive pulley
	unequal tensions
massive pendulum
	$\frac{1}{2}mv_{cm}^2 + \frac{1}{2}I_{cm}\omega^2 = \frac{1}{2}I_{pivot}\omega^2$
## Torque
torque
	$\vec{\tau}=\vec{r}\times\vec{F}$
rotational 2nd law
	$\vec{\tau}=I\vec{\alpha}$
rotational work
	$\int_A^B \vec{\tau} \vec{d\theta}=\Delta K=\frac{1}{2}I\omega_B^2-\frac{1}{2}I\omega_A^2$
rotational power
	$P=\vec{\tau}\cdot\vec{\omega}$
## Static Equilibrium
conditions for static equilibrium
	$\vec{F}_{net}=0$, $\vec{\tau}_{net}=0$ regardless of reference point
conditions for tipping