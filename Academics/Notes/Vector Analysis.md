### Vector Differentiation and Integration
differentiation
	$\vec{r}(t)=x(t)\hat{i}+y(t)\hat{j}+z(t)\hat{k}$
	$\vec{v}(t) = \frac{d\vec{r}(t)}{dt} = \frac{dx}{dt}\hat{i} + \ldots$
similar for integration
### Fields
scalar field
	single valued function of point in space
	$f(x,y,z)$
### Directional Derivative and Gradient
partial derivative ($\frac{\partial f}{\partial x}, \ldots$)
	treat other variables as constants
directional derivative ($\frac{df}{ds}$) along $\hat{u}$
	$\frac{df}{ds} = \hat{u} \cdot (\frac{\partial f}{\partial x}\hat{i} + \frac{\partial f}{\partial y}\hat{j} + \frac{\partial f}{\partial z}\hat{k}) = \nabla f \cdot \hat{u}$ (gradient)
	spherical coordinates
		$\nabla = \hat{r}\frac{\partial}{\partial r} + \frac{1}{r}\hat{\theta}\frac{\partial}{\partial \theta} + \frac{1}{r\sin\theta}\hat{\phi}\frac{\partial}{\partial \phi}$
### Divergence
$\operatorname{div}(\vec{v}) = \nabla \cdot \vec{v}$
divergence theorem
	$\iiint \nabla \cdot \mathbf{V} \, d\tau = \iint \mathbf{V} \cdot \mathbf{n} \, d\sigma$
### Curl
$\operatorname{curl}(\vec{v})=\nabla \times \vec{v}$
$\operatorname{curl}(\nabla \vec{v})=0$
stokes theorem
	$\oint \mathbf{V} \cdot \, d\mathbf{r} = \int \int (\nabla \times \mathbf{V}) \cdot \mathbf{n} \, d\sigma$
### Laplacian
$\operatorname{div}(\nabla f) = \nabla^2f$
### Volume Integrals
$\iiint f(x, y, z) \, dx \, dy \, dz$
$\int \vec{v} dt = \int v_x \, dt \, \hat{i} + \ldots$
### Line Integrals
$\oint \vec{v} \cdot d\vec{r}$
### Spherical Coordinates
