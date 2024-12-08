# Sequences
### Defenitinos:

- Monotonic: The sequence which is either increasing or decreasing. To prove:
    - $ a_1 , a_2 $ be calculate
    - Show $ a_1 = ... < or > a_2 =... $
    - Replace n in $ a_{n+1} $ with $k$ and say: Hence $ a_{k+1} = ...{a_k} < or > a_{k+2} = .. a_{k+1} $
    - Mention by induction ve infer ... for any $a_{n+1}$ for $\phi \leq n$
- Alternating sequence: when $a_n \cdot a_{n+1} < 0$.
#### Converges to the sum:
$\sum_{n=1}^{\infty} a_n = s$.

#### Partial sums of geometric series:
$
s_n = a + ar + ar^2 + \ldots + ar^{n-1} = \frac{a(1 - r^n)}{1 - r}.
$

#### Reminder:
$\lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n = e $

$ \lim_{n \to \infty} \frac{x^n}{n!} = 0
$
### Telescoping series
$ \sum_{n=1}^{\infty} \frac{1}{n(n+1)} =  \sum_{n=1}^{\infty} \frac{1}{n} - \frac{1}{n+1} = \lim_{n \to \infty} 1 - \frac{1}{n + 1} = 1$
### Harmonic series
$\sum_{n=1}^{\infty} \frac{1}{n}$ is Diverges because
$\int_{1}^{n+1} \frac{1}{x} dx = \ln{n+1}$ and $\lim_{n \to \infty} \ln(n + 1) = \infty $ and the serie is Divergence to $\infty$
### Comparison Tests

To find the Convergence or Divergence by comparing the given series with the known series.
like $  0 \leq a_n \leq Kb_n $ where we know status of $b_n$
#### A limit comparison test

$ \lim_{n \to \infty} \frac{a_n}{b_n} = L$ where if $L < \infty$ and $b_n$ converges, then $a_n$ also converges.

If $L > 0$ and $b_n$ diverges to infinity, then $a_n$ also diverges to infinity.

### The ratio test

$\rho = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$

(a) If $0 \leq \rho < 1$, then $\sum_{n=1}^{\infty} a_n$ converges.

(b) If $1 < \rho \leq \infty$, then $\lim_{n \to \infty} a_n = \infty$ and $\sum_{n=1}^{\infty} a_n$ diverges to infinity.

(c) If $\rho = 1$, this test gives no information; the series may either converge or diverge to infinity.

### The root test

Suppose $\sigma = \lim_{n \to \infty} {a_n}^{1/n}$ exists or is $\infty$.

(a) If $0 \leq \sigma < 1$, then $\sum_{n=1}^{\infty} a_n$ converges.

(b) If $1 < \sigma \leq 1$, then $\lim_{n \to \infty} a_n = \infty$ and $\sum_{n=1}^{\infty} a_n$ diverges to infinity.

(c) If $\sigma = 1$, this test gives no information; the series may either converge or diverge to infinity.


<hr>

Always divide by n while solving $\lim_{n \to \infty} $

$\lim_{n \to \infty} \frac{n}{n + 1} = \lim_{n \to \infty} \frac{1}{1 + \frac{1}{n}} = 1$
<hr>

For showing $0.\overline{xy}$ by infinite series you have to show $\sum_{n=1}^{\infty} \frac{xy}{100^{n}} $ then $ xy \sum_{n=1}^{\infty} \frac{1}{100^{n}} $ and so on...