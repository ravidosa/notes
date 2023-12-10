### Newton's Laws
see [Newton's Laws](Force.md#Properties%20and%20Effects%20of%20Forces)
implications
	1st
		definition of zero force
		defines inertial frame, holds for all free particles
	2nd
		quantitative relation
		implies 1st
		relation of outside quantity (F) to property of body (m)
			mass = resistance to movement under applied force
	3rd
		momentum conservation
	inertial mass vs gravitational mass
		$\frac{a_1}{a_2} = \frac{m_1}{m_2}$
		$\sum F = m_i a$
		$F_G = G\frac{m_gM_g}{r^2}$
		general relativity
			matter tells space to bend, space shows matter how to move
### Free Body Diagrams
see [Free Body Diagrams](Force.md#Properties%20and%20Effects%20of%20Forces)
### Solving Differential Equations
see [Scalar Autonomous ODEs](Scalar%20Autonomous%20ODEs.md)
second order (displacement, velocity, acceleration)
$m\ddot{x} = F(x, v, t)$
	dependence only on $t$: oscillatory driving forces, $\ddot{x} = \frac{dv}{dt}$
	dependence only on $x$: mass-spring system, $\ddot{x} = v\frac{dv}{dx}$
	dependence only on $v$: drag force, $\ddot{x} = \frac{dv}{dt}$
	separate variables, solve for $x(t)$
### Projectile Motion
see [Kinematics Equations](Motion.md#Kinematics)
motion in 2d
	$x(t)$, $y(t)$
	$\ddot{x} = 0$, $\ddot{y} = -g$
### Motion in a Plane, Polar Coordinates
see [Polar Coordinates](Vector%20Analysis.md#Spherical%20Coordinates)
newton's laws in polar coordinates
	$\sum F = m\vec{a} = m\ddot{\vec{r}}$
		radial vector $\hat{r}$, $\hat{\theta}$ perpendicular to $\hat{r}$ pointing towards growing $\theta$
		$\vec{r} = r\hat{r}$, $\vec{v} = \dot{\vec{r}} = \dot{r}\hat{r} + r\dot{\theta}\hat{\theta}$, $\vec{a} = \dot{\vec{v}} = \ddot{\vec{r}} = (\ddot{r} - r\dot{\theta}^2)\hat{r} + (2\dot{r}\dot{\theta} + r\ddot{\theta})\hat{\theta}$
			$\hat{r} = \cos\theta\hat{x} + \sin\theta\hat{y}$, $\dot{\hat{r}} = \dot{\theta}\hat{\theta}$
			$\hat{\theta} = -\sin\theta\hat{x} + \cos\theta\hat{y}$, $\dot{\hat{\theta}} = -\dot{\theta}\hat{r}$
			radial acceleration, centripetal term, angular acceleration, coriolis term