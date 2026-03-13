**Key Concepts in Regression:**
   - **Model Plausibility:** Use scatterplots to check if a linear model fits data.
   - **Sum of Squares:**
     - Total Sum of Squares (TSS): variance without $X$.
     - Regression Sum of Squares (RSS): variance explained by $X$.
     - Sum of Squared Errors (SSE): variance not explained by $X$.
   - **R-squared ($R^2$):**
     - Proportion of variance in $Y$ explained by $X$.
     - Example: $R^2 = 0.31$ means 31% of variation in $Y$ is explained by $X$.

**Correlation:**
   - **Definition:**
     - Standardized measure of linear association between $X$ and $Y$ ($-1 \leq r \leq 1$).
   - **Relation to Regression:**
     - $r = b \frac{s_x}{s_y}$, where $b$ is the slope.
   - **Properties:**
     - $r = 0$: no linear relationship.
     - $r^2$: proportion of error reduction using $X$ instead of the mean.

**Inference in Regression:**
   - **Testing Slope ($\beta$) or Correlation ($\rho$):**
     - $H_0: \beta = 0$ (no relationship); $H_a: \beta \neq 0$ (linear relationship exists).
     - Test statistic: $t = \frac{b}{se}$, where $se = s / \sqrt{\sum (x - \bar{x})^2}$.
     - P-value derived from t-distribution.
   - Example: Significant positive slope in possum dataset ($p < 0.001$).

**Limitations of Regression:**
   - **Extrapolation:** Avoid predicting beyond observed $X$-range.
   - **Outliers:** Can distort regression and correlation.
   - **Sampling Range:** Narrow $X$-range biases correlation downward.

**Conditional Standard Deviation:**
   - Measures variability of $Y$ at a fixed $X$.
   - Smaller than the total standard deviation of $Y$.