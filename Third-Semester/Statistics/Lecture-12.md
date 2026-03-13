**Model Fit:**
   - **Underfitting:** Model too simple, high bias, low variance, poor data capture.
   - **Overfitting:** Model too complex, low bias, high variance, fits noise, poor generalization.
   - **Good Fit:** Balanced bias and variance, captures relationships without noise.

**Model Selection:**
   - **Comparing Models:**
     - **Nested Models:** One model fully contains another (e.g., adding/removing predictors).
     - **Unnested Models:** Models differ in variables used, not comparable with F-test.
   - **F-Test:** For nested models, tests if additional parameters significantly improve fit.
   - **Model Fit Indices:**
     - Adjusted $R^2$: Penalizes for extra parameters, decreases if they don't improve the model.
     - PRESS: Predicted sum of squared errors via cross-validation.
     - AIC/BIC: Penalize model complexity, lower is better.
     - MDL: Balances model simplicity and residual error.

**Model Selection Strategies:**
   - **Backward Elimination:** Start with all predictors, remove insignificant ones.
   - **Forward Selection:** Start with no predictors, add significant ones iteratively.
   - **Automated Methods (AutoML):** Software-based selection strategies.

**Model Validation:**
   - **Purpose:** Confirm the model generalizes well to new data.
   - **Methods:**
     - Split data into training and testing sets (e.g., 70/30 split).
     - Cross-validation:
       - **Leave-One-Out (LOOCV):** Each observation is left out once, slow but uses all data.
       - **k-Fold:** Divide data into $k$ parts, train on $k-1$ folds, test on the remaining.
     - **Train/Validate/Test Split:**
       - Separate test set for final evaluation.
       - Use cross-validation on train + validate set to select the model.
   - **Symptoms of Overfitting/Underfitting:**
     - Overfitting: Low train error, high test error.
     - Underfitting: High error on both train and test sets.