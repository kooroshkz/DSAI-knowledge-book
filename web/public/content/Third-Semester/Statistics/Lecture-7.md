#### **Hypotheses and Tests**
- **Significance Test Goals**:
  - Test claims about population parameters.
  - Null Hypothesis ($H_0$): No effect or specific value.
  - Alternative Hypothesis ($H_a$): An effect exists or differs.
- **Five Steps**:
  1. **Assumptions**: Data type, random sampling, distribution normality, sample size.
  2. **Hypotheses**: Define $H_0$ and $H_a$.
  3. **Test Statistic**: Measure deviations using $t$- or $z$-scores.
  4. **P-value**: Likelihood of observed data under $H_0$.
  5. **Conclusion**: Interpret P-value in context.  

---

#### **Testing a Single Mean**
- **Steps**:
  1. Assumptions: Quantitative variable, random sample, normal distribution.
  2. Hypotheses: $H_0: \mu = \mu_0$, $H_a: \mu \neq \mu_0$ (two-sided).
  3. Test Statistic ($t$):

$$t = \frac{\bar{y} - \mu_0}{s / \sqrt{n}}$$

4. **P-value**: Based on $t$-distribution.
  5. **Conclusion**: Reject $H_0$ if $P \leq \alpha$ (e.g., 0.05).  

---

#### **Testing a Single Proportion**
- **Steps**:
  1. Assumptions: Categorical variable, random sampling, minimum sample size.
  2. Hypotheses: $H_0: \pi = \pi_0$, $H_a: \pi \neq \pi_0$ (two-sided).
  3. Test Statistic ($z$):

$$z = \frac{\hat{\pi} - \pi_0}{\sqrt{\pi_0(1-\pi_0)/n}}$$

4. **P-value**: Based on standard normal distribution.
  5. **Conclusion**: Contextualize findings and decide on $ H_0 $.  

---

#### **Decisions and Errors**
- **Significance Level ($ \alpha $)**:
  - $ P \leq \alpha $: Reject $ H_0 $.
  - $ P > \alpha $: Fail to reject $ H_0 $.
- **Errors**:
  - **Type I** ($ \alpha $): Reject $ H_0 $ when true.
  - **Type II** ($ \beta $): Fail to reject $ H_0 $ when false.
  - Power of a test: $ 1 - \beta $.  

---

#### 7. **Limitations of Significance Tests**
- Statistical significance ≠ practical significance.
- Effect size and confidence intervals provide better context.  
