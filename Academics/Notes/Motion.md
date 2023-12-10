### Vectors
vector
	definition: quantity with both magnitude and direction
	notation: $\vec{A}$, $|\vec{A}| = A$ is magnitude of $\vec{A}$
	representation: arrow
	components
		$A_x = A\cos{\theta}$
		$A_y = A\sin{\theta}$
	addition/subtraction: add individual components
		$\vec{C} = \vec{A} + \vec{B}$
		$C_x = A_x + B_x$
		$C_y = A_y + B_y$
		$C_z = A_z + B_z$
	unit vectors: vector with magnitude 1 in same direction
		notation: $\hat{A}$
		representation: arrow with length 1
		$\vec{A} = A\hat{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}$
		column matrices
			$\hat{i} = \begin{pmatrix}1\\0\\0\end{pmatrix}$, $\hat{j} = \begin{pmatrix}0\\1\\0\end{pmatrix}$, $\hat{k} = \begin{pmatrix}0\\0\\1\end{pmatrix}$
			$\hat{A} = \begin{pmatrix}\cos{\theta}\\\sin{\theta}\\0\end{pmatrix}$
### Vector Multiplication
scalar/dot product
	$\vec{A} \cdot \vec{B} = AB\cos{\theta}$ where $\theta$ is the angle between $\vec{A}$ and $\vec{B}$
	measure of how much vectors are parallel to each other
	$0$ if perpendicular, $AB$ if parallel
	$\vec{A} \cdot \vec{A} = A^2\cos{0^{\circ}} = A^2$
	$\vec{i} \cdot \vec{i} = \vec{j} \cdot \vec{j} = \vec{k} \cdot \vec{k} = 1$
	$\vec{i} \cdot \vec{j} = \vec{j} \cdot \vec{k} = \vec{k} \cdot \vec{i} = 0$
	$\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$
	commutative: $\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$
	result is scalar
vector/cross product
	$|\vec{A} \times \vec{B}| = AB\sin{\theta}$ where $\theta$ is the angle between $\vec{A}$ and $\vec{B}$
	measure of how much vectors are perpendicular to each other
	$AB$ if perpendicular, $0$ if parallel
	not commutative: $\vec{A} \times \vec{B} \neq \vec{A} \times \vec{B}$
	result is vector
	right hand rule
		index finger is $\vec{A}$, middle finger is $\vec{B}$, thumb is $\vec{A} \times \vec{B}$
	$\vec{A} \times \vec{B} = -\vec{B} \times \vec{A}$
	$\hat{i} \times \hat{j} = \hat{k}$, $\hat{j} \times \hat{k} = \hat{i}$, $\hat{k} \times \hat{i} = \hat{j}$ (right-handed coordinate system)
	$\vec{A} \times \vec{A} = \vec{0}$
	$\vec{A} \times \vec{B} = \begin{pmatrix}A_x\\A_y\\A_z\end{pmatrix} \times \begin{pmatrix}B_x\\B_y\\B_z\end{pmatrix} = \begin{pmatrix}A_yB_z-A_zB_y\\A_zB_x-A_xB_z\\A_xB_y-A_yB_x\end{pmatrix}$
### Straight Line Motion
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
motion diagrams
### Kinematics
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
### Graphing
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
### Motion in Multiple Dimensions
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
### Examples of 2D Motion
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
### Relative Motion
$\vec{v}$ magnitude and direction dependent on reference frame
relative velocity vector ($\to$ = relative to)
	$\vec{v}_{B \to A} = -\vec{v}_{A \to B}$
	$\vec{v}_{A \to B} + \vec{v}_{B \to C} = \vec{v}_{A \to C}$