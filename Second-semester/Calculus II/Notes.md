- $ wz = rs ( \cos(\theta + \phi) + i \sin(\theta + \phi) )$.
- $e^{z} = e^{x+iy} = e^{x}e^{iy} = e^{x}(\cos(y) + i\sin(y))$
- $e^{\pi i} = -1$
- $e^z = r(\cos \phi + i\sin \phi)$ has solutions $z_k = \ln r + (\phi + 2k\pi)i$, $k \in \mathbb{Z}$.
<hr>
- Monotonic: The sequence which is either increasing or decreasing. To prove:
    - $ a_1 , a_2 $ be calculate
    - Show $ a_1 = ... < or > a_2 =... $
    - Replace n in $ a_{n+1} $ with $ k $ and say: Hence $ a_{k+1} = ...{a_k} < or > a_{k+2} = .. a_{k+1} $
    - Mention by induction ve infer ... for any $a_{n+1}$ for $\phi \leq n$
- Alternating sequence: when $a_n \cdot a_{{n+1}} < 0$.
$\lim_{n \to \infty} \frac{x^n}{n!} = 0$

$\lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n = e $

$\rho = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$

- $0 \leq \rho < 1$ Converge
- $\rho = 1 $ Unknown
- $1 < \rho \leq \inf$ diverge
<hr>
Average Value of a Function

$f_{\text{avg}} = \frac{1}{b - a} \int_{a}^{b} f(x) \, dx$
The Mean-Value Theorem for integrals

$\int_{a}^{b} f(x) \, dx = f(c) (b - a)$
### Sin-Cos Power replacements

$ \cos^2 x = \frac{1}{2} (1 + \cos 2x) $

$ \sin^2 x = \frac{1}{2} (1 - \cos 2x) $

hence

$ \int \cos^2 x \, dx = \frac{1}{2} (x + \sin x \cos x) + C $

$ \int \sin^2 x \, dx = \frac{1}{2} (x - \sin x \cos x) + C $

### The case of a quadratic denominator

$$ \int \frac{x \, dx}{x^2 + a^2} = \frac{1}{2} \ln(x^2 + a^2) + C; $$

$$ \int \frac{x \, dx}{x^2 - a^2} = \frac{1}{2} \ln |x^2 - a^2| + C; $$

$$ \int \frac{dx}{x^2 + a^2} = \frac{1}{a} \tan^{-1}\left(\frac{x}{a}\right) + C; $$

$$ \int \frac{dx}{x^2 - a^2} = \frac{1}{2a} \ln \left| \frac{x - a}{x + a} \right| + C. $$

$ \int \tan x \, dx = \ln |\sec x| + C $

$ \int \cot x \, dx = \ln |\sin x| + C = -\ln |\csc x| + C $


$ \int \sec^2(ax) \, dx = \frac{1}{a} \tan(ax) + C $

$ \int \csc^2(ax) \, dx = -\frac{1}{a} \cot(ax) + C $

$ \int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \sin^{-1}\left(\frac{x}{a}\right) + C \quad (a > 0) $

$ \int \frac{1}{a^2 + x^2} \, dx = \frac{1}{a} \tan^{-1}\left(\frac{x}{a}\right) + C $


$ \int b^{ax} \, dx = \frac{1}{a \ln b} b^{ax} + C $

$ \int \cosh(ax) \, dx = \frac{1}{a} \sinh(ax) + C $

$ \int \sinh(ax) \, dx = \frac{1}{a} \cosh(ax) + C $

$\int \sec^2 x \, dx = \tan x + C$

$\int \sec x \tan x \, dx = \sec x + C$

$\int \csc^2 x \, dx = -\cot x + C$


<hr>
## Normal Vector

A normal vector to $z = f(x, y)$ at $(a, b, f(a, b))$ is
$n = f_x(a, b) \mathbf{i} + f_y(a, b) \mathbf{j} - \mathbf{k}$

## An equation of the tangent plane 

for $ z = f(x, y) $ at $ (a, b, f(a, b)) $

$z = f(a, b) + f_1(a, b)(x - a) + f_2(a, b)(y - b)$
<hr>
### A second derivative test

**Hessian Matrix**
- $ H(a) $ is positive definite then a local minimum at a. ($ f_{11} f_{22} - {f_{12}}^2 > 0 \land  f_{11} > 0 $)
- $ H(a) $ is negative definite then a local maximum at a. ($ f_{11} f_{22} - {f_{12}}^2 > 0 \land  f_{11} < 0 $)
- $ H(a) $ is indefinite then a saddle point at a. ($ f_{11} f_{22} - {f_{12}}^2 < 0 $)
- $ H(a) $ is non then test gives no information. ($ f_{11} f_{22} - {f_{12}}^2 = 0 $)

<hr>
$ (\tan{x})' = \frac{1}{{\cos{x}}^{2}}$

$ (\cot{x})' = \frac{-1}{{\sin{x}}^{2}}$

$ \int{x \ln{x} dx = x \ln{x} - x + C} $
In complex equations when we asked for solution always mention $z$ as $z_k$ and for $ \theta = \phi $ we should consider writing $ \theta = \phi + 2k\pi $ and in the answer mention for $k = 0,1,2,3,..., n$ where $ n $ is the power of $ z^{n} $ in the question $ - 1 $ in the question
When the bound of the integral is on edge of function range always write:

$ \lim{a \to 0^{+}} \int_{1}^{a} f(x) = {F(x) ]_{a}}^{1} $