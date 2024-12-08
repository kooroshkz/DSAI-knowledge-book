# Integration
### Integration by parts

$ \int U dV = UV - \int V dU $

<hr>
$\int \sec^2 x \, dx = \tan x + C$

$\int \sec x \tan x \, dx = \sec x + C$

$\int \csc^2 x \, dx = -\cot x + C$



$ \int \sec^2(ax) \, dx = \frac{1}{a} \tan(ax) + C $

$ \int \csc^2(ax) \, dx = -\frac{1}{a} \cot(ax) + C $

$ \int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \sin^{-1}\left(\frac{x}{a}\right) + C \quad (a > 0) $

$ \int \frac{1}{a^2 + x^2} \, dx = \frac{1}{a} \tan^{-1}\left(\frac{x}{a}\right) + C $


$ \int b^{ax} \, dx = \frac{1}{a \ln b} b^{ax} + C $

$ \int \cosh(ax) \, dx = \frac{1}{a} \sinh(ax) + C $

$ \int \sinh(ax) \, dx = \frac{1}{a} \cosh(ax) + C $

$ \int \tan x \, dx = \ln |\sec x| + C $

$ \int \cot x \, dx = \ln |\sin x| + C = -\ln |\csc x| + C $

The case of a quadratic denominator

$$ \int \frac{x \, dx}{x^2 + a^2} = \frac{1}{2} \ln(x^2 + a^2) + C; $$

$$ \int \frac{x \, dx}{x^2 - a^2} = \frac{1}{2} \ln |x^2 - a^2| + C; $$

$$ \int \frac{dx}{x^2 + a^2} = \frac{1}{a} \tan^{-1}\left(\frac{x}{a}\right) + C; $$

$$ \int \frac{dx}{x^2 - a^2} = \frac{1}{2a} \ln \left| \frac{x - a}{x + a} \right| + C. $$

Partial fraction decomposition

$ \frac{P(x)}{Q(x)} = \frac{A_1}{x - a_1} + \frac{A_2}{x - a_2} + \cdots + \frac{A_n}{x - a_n} $

Corresponding to each factor \((x - a)^m\) of \(Q(x)\), the decomposition contains a sum of fractions of the form

$\frac{A_1}{x - a} + \frac{A_2}{(x - a)^2} + \cdots + \frac{A_m}{(x - a)^m}$




##### Since $ \sin 2x = 2 \sin x \cos x $
$ \int \cos^2 x \, dx = \frac{1}{2} (x + \sin x \cos x) + C $

$ \int \sin^2 x \, dx = \frac{1}{2} (x - \sin x \cos x) + C $

## Sin-Cos Power replacements

$ \cos^2 x = \frac{1}{2} (1 + \cos 2x) $

$ \sin^2 x = \frac{1}{2} (1 - \cos 2x) $

The triangle inequality for sums extends to definite integrals. If $ a \leq b $, then
$ \left| \int_{a}^{b} f(x) \, dx \right| \leq \int_{a}^{b} |f(x)| \, dx. $

The Mean-Value Theorem for integrals

$\int_{a}^{b} f(x) \, dx = f(c) (b - a)$
Average Value of a Function

$f_{\text{avg}} = \frac{1}{b - a} \int_{a}^{b} f(x) \, dx$
## Improper Integrals
$$ \int_{a}^{\infty} f(x) \, dx = \lim_{R \to \infty} \int_{a}^{R} f(x) \, dx. $$

$$ \int_{-\infty}^{\infty} f(x) \, dx = \int_{-\infty}^{0} f(x) \, dx + \int_{0}^{\infty} f(x) \, dx. $$

### \( p \)-integrals

If \( 0 < a < 1 \), then

(a) $ \int_{a}^{1} x^{-p} \, dx = \left\{ \begin{array}{ll}
\frac{a^{1-p}}{p - 1} & \text{if } p > 1 \\
\infty & \text{if } p \leq 1
\end{array} \right. $

(b) $ \int_{0}^{a} x^{-p} \, dx = \left\{ \begin{array}{ll}
\frac{a^{1-p}}{1 - p} & \text{if } p < 1 \\
\infty & \text{if } p \geq 1
\end{array} \right. $

#### Note

If an integral range pass through where y = 0 we should divide the integral into two parts and sum them up.

$$ \int_{-\infty}^{\infty} \frac{\ln |x| \, dx}{\sqrt{1 - x}} = \int_{-\infty}^{0} \frac{\ln |x| \, dx}{\sqrt{1 - x}} + \int_{0}^{\frac{1}{2}} \frac{\ln |x| \, dx}{\sqrt{1 - x}} + \int_{\frac{1}{2}}^{\infty} \frac{\ln |x| \, dx}{\sqrt{1 - x}}. $$
