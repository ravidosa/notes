# Complex Numbers
real numbers
	represented along real number line $-\infty < x < \infty$
	certain algebraic operations not defined for all real numbers ($\sqrt{-1})$
complex numbers
	$i = \sqrt{-1}$
	$z = x + iy$
represented along complex plane
	$\mathbb{C}$ is $\mathbb{R}^2$ with multiplication defined, unordered field
		$\mathbb{R}$ is $\mathbb{C}$ with zero imaginary part
		all polynomials factorizable into product of linear terms
		$\mathbb{C} = \{z = x + iy : x, y \in \mathbb{R}\}, i^2 = -1$
	real part on x-axis, imaginary part on y-axis
	$z = r(\cos\theta+\sin\theta) = re^{i\theta}$
		$e^{i\theta} = \cos\theta + i\sin\theta$
		$r = \sqrt{x^2+y^2}$
		$\tan\theta=\frac{y}{x}$
	complex conjugate
		$\bar{z} = x - iy = re^{-i\theta}$
		$\overline{z} = x - iy, |z|^2 = z\overline{z} = x^2 + y^2$
		$\overline{z_1 \cdot z_2} = \overline{z}_1 \cdot \overline{z}_2, \overline{z_1 + z_2} = \overline{z}_1 + \overline{z}_2$
		$\frac{1}{2}(z + \overline{z}) = x, \frac{1}{2}(z - \overline{z}) = iy$
## Operations
addition/subtraction
	$z_1 + z_2 = (x_1 + x_2) + i(y_1 + y_2)$ ($-z = -x - iy$)
absolute value
	$|z| = r = \sqrt{z\bar{z}}$
	$|z| \geq 0$ unless $z = 0$
multiplication/division
	$z_1 \cdot z_2 = (x_1x_2 - y_1y_2) + i(x_1y_2 + x_2y_1)$ ($z^{-1} = \frac{x}{x^2 + y^2} - i\frac{y}{x^2 + y^2}$)
	$z_1z_2 = r_1r_2e^{\theta_1+\theta_2}$
	$\frac{z_1}{z_2}=\frac{r_1}{r_2}e^{\theta_1-\theta_2}$
powers/roots
	$z^n = (re^{i\theta})^n = r^n(\cos{n\theta}+i\sin{n\theta})$
	$z^{\frac{1}{n}} = (re^{i\theta})^n = \sqrt[n]{r}(\cos{\frac{\theta}{n}}+i\sin{\frac{\theta}{n}})$
	$\theta$ can be offset by multiples of $2\pi$
logarithms
	$\ln{z}=\ln{re^{i\theta}}=\operatorname{Ln}{r}+i\theta$
complex roots and powers
	$a^b=e^{b\ln{a}}$ for complex $a$ and $b$
## Hyperbolic Functions
exponential/trig
	$e^z = e^{x+iy} = e^x(\cos{y}+i\sin{y})$
	$\sin{\theta}=\frac{e^{i\theta}-e^{-i\theta}}{2i}$
	$\cos{\theta}=\frac{e^{i\theta}+e^{-i\theta}}{2}$
	$\sin{z}=\frac{e^{iz}-e^{-iz}}{2i}$
	$\cos{z}=\frac{e^{iz}+e^{-iz}}{2}$
hyperbolic functions
	$\sinh{z}=\frac{e^z-e^{-z}}{2}$
	$\cosh{z}=\frac{e^z+e^{-z}}{2}$
	$\sin{iy}=i\sinh{y}$
	$\cos{iy}=\cosh{y}$