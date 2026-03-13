**Multivariate Relationships:**
   - Moving from bivariate to multivariate analyses introduces additional explanatory variables.
   - **Types of Relationships:**
     - **Spurious Association:** Both $X_1$ and $Y$ depend on $X_2$, removing the $X_1$-$Y$ association.
     - **Chain Relationship:** $X_1$ affects $X_2$, which affects $Y$.
     - **Multiple Causes:** Several variables independently influence $Y$.
     - **Interaction Effects:** The effect of $X_1$ on $Y$ depends on $X_2$.

**Simpson's Paradox:**
   - The overall association between two variables reverses when controlling for a third variable.

**Inference in Multiple Regression:**
   - **F-Test:**
     - Tests if at least one $\beta_i \neq 0$.
     - $F = \frac{R^2 / k}{(1 - R^2) / (n - k - 1)}$, where $k$ is the number of predictors.
   - **t-Test for Individual Coefficients:**
     - Tests if a specific $\beta_i = 0$.
   - **Multicollinearity:**
     - High correlation among predictors inflates standard errors, making it hard to determine individual effects.

**Modeling Interaction Effects:**
   - Formula: $E(Y) = \alpha + \beta_1 X_1 + \beta_2 X_2 + \beta_3 (X_1 \cdot X_2)$.
   - Interaction terms show how the relationship between $X_1$ and $Y$ depends on $X_2$.
