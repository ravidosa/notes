# Dynamics
## Classical Mechanics
### Translational
newton’s laws
	body at rest tends to stay at rest, body in motion tends to stay in motion unless acted upon by external unbalanced force
		definition of zero force
		defines inertial frame, holds for all free particles
	acceleration of center of mass is net force divided by mass ($\vec{a}_{cm} = \frac{\vec{F}_{net}}{m} = \frac{\sum\vec{F}}{m}$)
		quantitative relation
		implies 1st
		relation of outside quantity (F) to property of body (m)
			mass = resistance to movement under applied force
	for every action there is an equal and opposite reaction ($\vec{F}_{A\to B} = \vec{F}_{B\to A}$)
		momentum conservation
inertial mass vs gravitational mass
		$\frac{a_1}{a_2} = \frac{m_1}{m_2}$
		$\sum F = m_i a$
		$F_G = G\frac{m_gM_g}{r^2}$
		general relativity
			matter tells space to bend, space shows matter how to move
types of forces
	gravity
		$\vec{F}_{gravity} = m\vec{g}$
	tension (massless strings = force transmission)
		forces equal on both sides for massless string
	normal (contact) force
		balancing force, magnitude depends on other forces
	friction
		kinetic friction (if sliding)
			$f_k = \mu_kN$ for normal force with magnitude $N$ and coefficient of kinetic friction $\mu_k$
		static friction (if not sliding)
			$f_s \leq \mu_sN$ for normal force with magnitude $N$ and coefficient of static friction $\mu_s$
			if $f_s > \mu_sN$, object slips and force becomes kinetic
		$\mu_s > \mu_k$
		air resistance/drag
			cross sectional area, speed, air density
		elastic (spring) force
			$\vec{F}_{elastic} = -k\Delta\vec{x}$
#### Free Body Diagrams
forces acting on system, not by system
#### Solving Differential Equations
see [Scalar Autonomous ODEs](scalar-autonomous-odes.md)
second order (displacement, velocity, acceleration)
$m\ddot{x} = F(x, v, t)$
	dependence only on $t$: oscillatory driving forces, $\ddot{x} = \frac{dv}{dt}$
	dependence only on $x$: mass-spring system, $\ddot{x} = v\frac{dv}{dx}$
	dependence only on $v$: drag force, $\ddot{x} = \frac{dv}{dt}$
	separate variables, solve for $x(t)$
#### Projectile Motion
see [Kinematics Equations](kinematics.md)
motion in 2d
	$x(t)$, $y(t)$
	$\ddot{x} = 0$, $\ddot{y} = -g$
#### Motion in a Plane, Polar Coordinates
see [Polar Coordinates](vector-analysis.md#spherical-coordinates)
newton's laws in polar coordinates
	$\sum F = m\vec{a} = m\ddot{\vec{r}}$
		radial vector $\hat{r}$, $\hat{\theta}$ perpendicular to $\hat{r}$ pointing towards growing $\theta$
		$\vec{r} = r\hat{r}$, $\vec{v} = \dot{\vec{r}} = \dot{r}\hat{r} + r\dot{\theta}\hat{\theta}$, $\vec{a} = \dot{\vec{v}} = \ddot{\vec{r}} = (\ddot{r} - r\dot{\theta}^2)\hat{r} + (2\dot{r}\dot{\theta} + r\ddot{\theta})\hat{\theta}$
			$\hat{r} = \cos\theta\hat{x} + \sin\theta\hat{y}$, $\dot{\hat{r}} = \dot{\theta}\hat{\theta}$
			$\hat{\theta} = -\sin\theta\hat{x} + \cos\theta\hat{y}$, $\dot{\hat{\theta}} = -\dot{\theta}\hat{r}$
			radial acceleration, centripetal term, angular acceleration, coriolis term
### Rotational
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
#### Torque
see [Torque](torque.md)
### Static Equilibrium
conditions for static equilibrium
	$\vec{F}_{net}=0$, $\vec{\tau}_{net}=0$ regardless of reference point
conditions for tipping