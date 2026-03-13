#### **Comparing Two Groups**
- **Dependent Samples** (Paired Test):
  - Same or related subjects in both groups.
  - Lower variability due to controlled factors.
  - E.g., Before-and-after tests or related pairs.
- **Independent Samples** (Unpaired Test):
  - Two groups selected independently.
  - E.g., Men vs. women, different populations.

---

#### **Comparing Means**
- **CI for Difference in Means**:
  - **Formula**:

$$\bar{y}_2 - \bar{y}_1 \pm t^* \cdot se se = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$$

- If CI does not include 0, the means are significantly different.
- **Significance Test**:
  - Test statistic:

$$t = \frac{\bar{y}_2 - \bar{y}_1}{se}$$

- Use degrees of freedom (df):

$$df = n_1 + n_2 - 2 \quad \text{(if variances are equal)}.$$

- If $p < \alpha$, reject $H_0$.

---

#### **Paired $t$-Test**
- Used for dependent samples.
- Calculate difference scores and treat as a single sample $t$-test.
- **Example**: Compare close friends between partners:
  - Difference scores:

$$\text{Partner 1} - \text{Partner 2}.$$

---

#### **Comparing Proportions**
- **CI for Difference in Proportions**:

$$\hat{\pi}_2 - \hat{\pi}_1 \pm z^* \cdot se, \quad se = \sqrt{\frac{\hat{\pi}_1 (1-\hat{\pi}_1)}{n_1} + \frac{\hat{\pi}_2 (1-\hat{\pi}_2)}{n_2}}$$

- **Significance Test**:

$$z = \frac{\hat{\pi}_2 - \hat{\pi}_1}{se_0}, \quad se_0 = \sqrt{\frac{\hat{\pi}(1-\hat{\pi})}{n_1} + \frac{\hat{\pi}(1-\hat{\pi})}{n_2}}.$$

- $\hat{\pi}$: Pooled proportion.

---

#### **Statistical Models**
- **Comparing Distributions**:
  - $H_0: Y_1 \sim N(\mu, \sigma_1)$ and $Y_2 \sim N(\mu, \sigma_2)$.
  - $H_a: Y_1 \sim N(\mu_1, \sigma_1)$ and $Y_2 \sim N(\mu_2, \sigma_2)$.
- **Effect Size**:
  - Formula:

$$\text{Effect size} = \frac{\bar{y}_1 - \bar{y}_2}{s}.$$

- Large if $ |\text{Effect size}| > 1 $.
