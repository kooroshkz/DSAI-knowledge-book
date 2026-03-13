1. **Chi-squared Test of Independence:**
   - Used for two categorical variables to test independence.
   - Hypotheses:
     - $H_0$: Variables are independent.
     - $H_a$: Variables are dependent.
   - Test statistic: $\chi^2 = \sum \frac{(f_o - f_e)^2}{f_e}$.
   - P-value derived from the chi-squared distribution.

2. **Dependence vs. Independence:**
   - Independence: Conditional distributions are identical across categories.
   - Dependence: Conditional distributions differ.

3. **Assumptions for Chi-squared Test:**
   - Random sampling.
   - Expected cell counts ≥ 5.

4. **Expected Frequencies:**
   - Computed as: $f_e = \frac{\text{row total} \times \text{column total}}{\text{grand total}}$.

5. **Patterns of Association:**
   - Residuals:
     - Residual = $f_o - f_e$.
     - Standardized Residual = $\frac{f_o - f_e}{SE}$.
     - Residuals help understand the nature and strength of association.