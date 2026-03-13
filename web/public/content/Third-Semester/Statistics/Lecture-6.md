
#### **Cumulative Distribution Function (CDF)**
- **Definition**:
  - $F_X(x) = P(X \leq x)$.
  - For discrete variables: $F_X(x) = \sum_{x_i \leq x} f_X(x_i)$.
  - For continuous variables: $F_X(x) = \int_{-\infty}^x f_X(t) \, dt$.
- **Properties**:
  - Monotonically increasing.
  - $F_X(x): \mathbb{R} \to [0, 1]$.

#### **Probability Distributions Covered**
  - **Bernoulli**: Mean = $p$, Variance = $p(1-p)$
  - **Binomial**: Mean = $np$, Variance = $np(1-p)$
  - **Normal**: Mean = $\mu$, Variance = $\sigma^2$  

#### **Statistical Functionals**
- **Definition**:
  - Functions of a distribution $F$, such as:
    - Mean: $\mu = \int x \, dF(x)$.
    - Variance: $\sigma^2 = \int (x - \mu)^2 \, dF(x)$.
    - Median: $m = F^{-1}(0.5)$.
- **Plug-In Estimators**:
  - Use empirical CDF $\hat{F}_n$ in place of $F$.
  - E.g., Sample mean: $\hat{\mu}_n = \frac{1}{n} \sum_{i=1}^n x_i$.

#### **Multivariate Distributions**
- **Bivariate Distributions**:
  - Joint PMF/PDF: $f(x, y)$.
  - Marginal Distribution: $f_X(x) = \sum_y f(x, y)$ (discrete) or $\int f(x, y) \, dy$ (continuous).
  - Conditional Distribution: $f_{X|Y}(x|y) = \frac{f(x, y)}{f_Y(y)}$.
