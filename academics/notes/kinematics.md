# Kinematics
## Classical Mechanics
### Translational
displacement
	definition: change in position
	$\Delta x = x_f - x_i$
	independent of intermediate points
average velocity
	$v_{ave} = \frac{\Delta x}{\Delta t} = \frac{x_f -x_0}{t_f - t_0}$
	only equal to average of initial and final velocity if constant acceleration
instantaneous velocity
	$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$
acceleration
	$a_{ave} = \frac{\Delta v}{\Delta t} = \frac{v_f-v_0}{t_f-t_0}$
	$a = \lim_{\Delta t \to 0} \frac{\Delta v}{\Delta t} = \frac{dv}{dt} = \frac{d^2x}{dt^2}$
#### Motion Diagrams
position
	+/- → position wrt origin
	integral of velocity
velocity
	+/- → direction of velocity wrt origin
	0 = stationary
	derivative of position, integral of acceleration
acceleration
	+/- → direction of acceleration wrt origin
	0 = constant velocity
	derivative of velocity
	same sign as velocity → speeding up
	different sign as velocity → slowing down

motion w/ constant acceleration
	$a = \frac{dv}{dt}$
	$v(t) = \int a dt = at + v_0$
	$v = \frac{dx}{dt}$
	$x(t) = \int vdt = \int (at+v_0)dt = \frac{1}{2}at^2 + v_0t + x_0$
	kinematic equations
		$v = v_0 + at$
		$x_f - x_0 = v_0t + \frac{1}{2}at^2$
		$x_f - x_0 = vt - \frac{1}{2}at^2$
		$x_f - x_0 = \frac{v + v_0}{2}t$
		$v^2 = v_0^2 + 2a(x_f-x_0)$
free fall
	$a = g = 9.8 m/s^2$
	independent of mass
#### Motion in Multiple Dimensions
position/displacement
	$\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$
	$\Delta \vec{r} = \vec{r}_f - \vec{r}_0 = (x_f-x_0)\hat{i} + (y_f-y_0)\hat{j} + (z_f-z_0)\hat{j}$
velocity
	$\vec{v}_{ave} = \frac{\Delta \vec{r}}{\Delta t} = \frac{\Delta x}{\Delta t}\hat{i} + \frac{\Delta y}{\Delta t}\hat{j} + \frac{\Delta z}{\Delta t}\hat{k}$
	$\vec{v} = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} + \frac{dz}{dt}\hat{k}$
	parallel and perpendicular components
		$\vec{r} = r\hat{r}$
		$\vec{v} = \frac{d\vec{r}}{dt} = r\frac{d\hat{r}}{dt} + \hat{r}\frac{dr}{dt}$
		$\vec{v}_{\parallel} = \hat{r}\frac{dr}{dt} = \vec{v} \cdot \hat{r}$ (change in magnitude)
		$\vec{v}_{\perp} = r\frac{d\hat{r}}{dt}$ (change in direction)
acceleration
	$\vec{a}_{ave} = \frac{\Delta \vec{v}}{\Delta t} = \frac{\Delta v_x}{\Delta t}\hat{i} + \frac{\Delta v_y}{\Delta t}\hat{j} + \frac{\Delta v_z}{\Delta t}\hat{k}$
	$\vec{a} = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2} = \frac{dv_x}{dt}\hat{i} + \frac{dv_y}{dt}\hat{j} + \frac{dv_z}{dt}\hat{k}$
	parallel and perpendicular components
		$\vec{v} = v\hat{v}$
		$\vec{a} = \frac{d\vec{v}}{dt} = v\frac{d\hat{v}}{dt} + \hat{v}\frac{dv}{dt}$
		$\vec{a}_{\parallel} = \hat{v}\frac{dv}{dt} = \vec{a} \cdot \hat{v}$ (change in magnitude)
		$\vec{a}_{\perp} = v\frac{d\hat{v}}{dt}$ (change in direction)
##### Examples of 2D Motion
uniform circular motion
	$\vec{a}_{\parallel} = 0$
	$\vec{a}_{\perp} = \frac{v^2}{r} = r\omega^2$ (centripetal acceleration)
projectile motion
	$v_{0,x} = v_0\cos\theta$
	$v_{0,y} = v_0\sin\theta$
	$v_x(t) = v_{0,x}$
	$v_y(t) = v_{0,t} - gt$
	$x(t) = v_{0,x}t$
	$y(t) = v_{0,t}t - \frac{1}{2}gt^2$
#### Relative Motion
$\vec{v}$ magnitude and direction dependent on reference frame
relative velocity vector ($\to$ = relative to)
	$\vec{v}_{B \to A} = -\vec{v}_{A \to B}$
	$\vec{v}_{A \to B} + \vec{v}_{B \to C} = \vec{v}_{A \to C}$
### Rotational
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
#### Non-Inertial Frames
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
#### Rotational Inertia
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