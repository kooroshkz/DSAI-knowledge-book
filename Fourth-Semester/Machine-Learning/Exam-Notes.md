## **Chapter 1**

- **Association Rule Mining** (Descriptive ML) : relationships between variables (Basket Analysis)
- **Subgroup Discovery** $\to$ Supervides, Descriptive ML
- Modus Operandi (Model Categorization by Mode of Operation):
    - **Grouping Models**: Decision Trees
    - **Grading Models**: SVM, Linear Regression
- **Model Phases**: Training Phase $\to$ Inference Phase (Prediction Phase)

---

## **Chapter 2**

- **Accuracy:** Fraction of correct predictions
- **Error Rate:** 1 - Accuracy
- **Recall or Sensitivity**: True Positive Rate out od all actual positives
- **Specificity**: True Negative Rate
- **Precision**: True Positive Rate out of all positive predictions
- **F1 Score**: Better than accuracy, considers both precision and recall

$\text{Accuracy} = \frac{TP + TN}{P + N}$ , $\text{Recall} = \frac{TP}{TP + FN}$ , $\text{Specificity} = \frac{TN}{TN + FP}$ , $\text{Precision} = \frac{TP}{TP + FP}$ , $\text{F1 Score} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$

- **ROC Curve (Receiver Operating Characteristic)** : Plot of **True Positive Rate (Sensitivity: y-axis)** vs **False Positive Rate (1 - Specificity: x-axis)**.

#### Loss Functions

| Loss Type        | Description                                         |
| ---------------- | --------------------------------------------------- |
| 0–1 Loss         | 1 if wrong prediction, 0 if correct                 |
| Hinge Loss       | Penalizes predictions that are not confident enough |
| Exponential Loss | Penalizes wrong predictions exponentially           |
| Logistic Loss    | Smooth loss function related to probability         |
| Squared Loss     | Penalizes squared error of margin                   |

- **Assessing Ranking Performance** $\to$ **Ranking Error Rate (RER)** $\to$ Fraction of pairs of instances that are incorrectly ordered
- **Assessing Class Probability** $\to$ Mean Squared Error (MSE)

---

## **Chapter 3**

- **Multi-class Classifiers**
    - **Inherently non-binary**: Decision Trees, Naïve Bayes
    - **Inherently binary**: SVM $\to$ One-vs-All ($k$ classifiers), One-vs-One ($k(k-1)/2$ classifiers)

| Approach    | Training complexity   | Inference complexity |
| ----------- | --------------------- | -------------------- |
| One-vs-Rest | $O(k m^\alpha)$       | $O(k^\beta)$         |
| One-vs-One  | $O(k^2 (m/k)^\alpha)$ | $O(k^2 \beta)$       |

* $k$: number of classes
* $m$: number of instances
* $\alpha$, $\beta$: algorithm-specific complexities

#### ROC Curve for Multi-class

   * **Macro-average:** Calculates ROC for each class separately, then averages the results equally across classes (ignores class imbalance).
   * **Micro-average:**  Calculates ROC for all classes together, treating each instance equally (considers class imbalance).

- Common loss functions:
  - **Mean Squared Error (MSE):** Average of squared residuals.
  - **Mean Absolute Error (MAE):** Average of absolute residuals.
  - **Huber Loss:** Combines MSE and MAE, less sensitive to outliers.

- **Low bias** → complex model
- **Low variance** → simple model
- **Evaluating Clustering Performance**
    - With Ground Truth (We know the real groups)
        - **Rand Index**: Measures similarity between two data clusterings.
        - **Precision**, **Recall**, **F1 Score**
    - Without Ground Truth
        - **Davies-Bouldin Index**: Measures the average similarity ratio of each cluster with its most similar one.
        - **Calinski-Harabasz Index**: Ratio of the sum of between-cluster dispersion to within-cluster dispersion.
        - **Silhouette Coefficient**: Measures how similar an object is to its own cluster compared to other clusters.
            - $s = \frac{b - a}{\max(a,b)}$
            -  $a$: average distance to points in the same cluster
            -  $b$: average distance to points in the nearest other cluster
            -  Values close to +1 → good clustering; close to 0 → borderline; negative → wrong cluster.
    - **Evaluating Subgroups**:
        - Chi-Squared Test: Measures the association between two categorical variables.
        - Compare subgroup distributions with the overall distribution.

---

## **Chapter 4**

- **Tree models** (supervised) = **non-linear relationships** (they split data based on rules, not lines) = logical = **easy to interpret**
  - **Decision Trees** (single tree)
  - **Random Forests** (many decision trees combined)
  - **Gradient Boosting** (trees built sequentially to correct errors)
- Data of splits:
  - **Pure split**: each child has only one class (ideal)
  - **Impure split** (Lower $\to$ better): children have mixed classes (common in real life)
    - Measure:
      - **Gini Index**
      - **Entropy**
      - **Misclassification error**
---

## **Chapter 5**

### **Distance metric** validity

1. **Zero distance to itself:** $Dis(x, x) = 0$
2. **Positive for different points:** $Dis(x, y) > 0$ if $x \neq y$
3. **Symmetry:** $Dis(x, y) = Dis(y, x)$
4. **Triangle inequality:** $Dis(x, z) \leq Dis(x, y) + Dis(y, z)$

If the 2nd condition allows zero even if points differ, it's called a **pseudo-metric**.

- K in KNN
    - **Small k**: Low bias, High variance (sensitive to noise) ,overfitting
    - **Large k**: High bias, Low variance (smoother decision boundary), underfitting
    - **Optimal k**: usually between 3 and 10.
    - Use cross-validation to find the best k for your data.
    - **Weighted voting**: give more weight to closer neighbours.

- **KNN Curse of Dimensionality**: In high-dimension $\to$ distance between points becomes less meaningful distance $\to$ hard to find nearest neighbours

- **K-means**
    - Uses Euclidean distance
    - Need to know $k$
    - Sensitive to initial centroids
- **k-medoids**
    - Use any distance metric
    - More robust to noise/outliers but more expensive computationally (O(n²))
    - Less sensitive to initial centroids
- **Evaluate**:
    - Inertia: total within-cluster scatter distance from the centroid.
    - Silhouette score: measures how similar an object is to its own cluster compared to other clusters.
        - Range: -1 to 1
        - Higher = better clustering

---

## **Chapter 6**

- **Least Squares Method** find that best-fitting line by minimizing squared errors in linear regression.
- **Evaluating Regression Models**:
    - **R² (Coefficient of Determination)**: Proportion of variance explained by the model.
        - R² = 1: perfect fit
        - R² = 0: no fit
        - $R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}}$ where:
            - **Residual Sum of Squares**(RSS): $\mathrm{RSS} = \sum_{i=1}^n (f(x_i) - \hat{f}(x_i))^2$
            - **Total Sum of Squares**(TSS): $\mathrm{TSS} = \sum_{i=1}^n (f(x_i) - \bar{f})^2$
    - **Residual Plot**: 
    - **Mean Absolute Error (MAE)**: Average absolute difference between predicted and actual values.
    - **Mean Squared Error (MSE)**: Average squared difference between predicted and actual values.
    - **Root Mean Squared Error (RMSE)**: Square root of MSE, variance of the errors.
- **Remove Effect of Outliers**:
    - Residual Plot $\to$ Retrain model
    - Total Least Squares $\to$ Adjusts for errors in both x and y
- **Regularised Regression (Ridge Regression)**: Adds penalty term to reduce overfitting.
---

## **Chapter 7**

- **Statistics of central tendency:** Mean, Median, Mode
- **Statistics of dispersion:** Variance, Standard deviation, Range, Midrange, Quantiles, Interquartile range
- **Shape statistics:** Skewness, Kurtosis (Peak Sharpness)
- **Feature Transformation**: 
    - **Calibration:** Assigns numbers to categories
    - **Thresholding:** Converts numeric/ordinal features into boolean (e.g., age > 18 = True)
    - **Discretisation:** Group ranges of values into bins (e.g., Low, Medium, High)
- **Normalisation**
    - **Min-Max normalisation:** Scales data between 0 and 1.
    - **Z-score normalisation:** Centers data around mean 0 and standard deviation 1.
- **Principal Component Analysis (PCA)**: PCA helps reduce redundancy (features) when features are correlated. It make some calculations to find two new not correlated features:
  - **PC1**: First principal component, explains the most variation
  - **PC2**: Second principal component, orthogonal to PC1, explains the next most variation
- **PCA calculations Methods**:
  -  **Singular Value Decomposition (SVD)**
  -  **Eigenvalue decomposition**

---
## **Chapter 8**

- **Decision rules:**
    - **Maximum a posteriori (MAP) decision rule:** Consider both likelihood and prior.
    - **Maximum likelihood (ML) decision rule:** Consider only likelihood, assume priors are equal.
- **Probability Distributions for Categorical Variables**
    - **Multivariate Bernoulli distribution:** models presence or absence of words (0 or 1).
    - **Multinomial distribution:** models counts of word occurrences (how many times each word appears).
- **Naïve Bayes Classifier**: Assumes features are conditionally independent given the class label.
- **Gaussian Mixture Models (GMM)**: Models data as a mixture of multiple Gaussian distributions.
    - Goal: Estimate parameters (means μj, covariances Σj) of each Gaussian without knowing the class labels.
    - Classify points: Need Parameters $\to$ Needs lables
    - Use **Expectation-Maximization (EM)** algorithm to estimate parameters
        - Initialize parameters randomly $\to$ E-step: calculate probabilities of each point belonging to each Gaussian ...
        - ... $\to$ M-step: update parameters based on probabilities $\to$ Repeat until convergence

---
## **Chapter 9**

- **Bootstrapping**: Train/Test on different samples of data $\to$ reduce mistakes by one fixed training set
- **Bagging** Aggregating: Create multiple bootstraps $\to$ train multiple models $\to$ combine predictions (Aggregate)
    - Reduces variance
- **Subspace Sampling**: Instead of using all features, you randomly pick only a small set of features for each model. 
    - Different models look at different parts of the data, so their errors won’t be the same. 
    - This helps the combined model (ensemble) perform better and avoid overfitting.
- **Random Forest**: Ensemble of decision trees
    - Each tree is trained on a different bootstrap sample of the data.
    - Each split in the tree considers only a random aspect of data.
    - Predictions are made by averaging the predictions of all trees (for regression) or by majority vote (for classification).
- **Boosting**: Sequentially train models, each focusing on the errors of the previous one.
    - Each model gives more weight to misclassified instances than correctly classified ones to learn from mistakes.
    - Like: XGBoost, AdaBoost, LightGBM, Gradient Boosting
- **Bias:** Error from wrong assumptions (systematic error). Mostly in simple models (e.g., linear regression for non-linear data)
    - **Reduce** $\to$ Boosting $\to$ by focusing on mistakes from previous models
- **Variance:** Error from sensitivity to small fluctuations in the training set (overfitting). Mostly in complex models (e.g., decision trees).
    - **Reduce** $\to$ Bagging $\to$ by training models independently on different data samples
- **Total expected error** = Bias² + Variance + Irreducible error.
- **Stacking:** Train multiple base models (e.g., decision trees, SVMs) and combine their predictions using a meta-model (e.g., logistic regression).
- **t-test**: Statistical test to compare two models. If p-value < 0.05, models are significantly different.
    - **Independent t-test**: Compares means of two independent groups (like comparing scores of men vs women).
    - **Paired t-test**: Compares means of two related groups (like comparing scores of the same group before and after a treatment)
    - **t-test, not good for Multiple datasets**
- **Wilcoxon Signed-Rank Test**: Compare algorithms by finding performance differences per dataset, ranking absolute differences, summing positive and negative ranks, and using the smaller sum as the test statistic.
- **Friedman Test**: Compare **more than two algorithms** over multiple datasets. Rank algorithms per dataset, find each algorithm’s average rank, and test if average rank differences show they perform differently.
- **Post-hoc Tests (like Nemenyi Test)**: After diffrence revealed in Friedman test, we aim for **which pairs** of algorithms are different. $\to$ Calculate a **Critical Difference (CD)** value $\to$ If the difference between the average ranks of two algorithms is greater than CD, their performance difference is significant.

---
## **Chapter 10**

| Task                       | Output Unit  | Loss Function      |
| -------------------------- | ------------ | ------------------ |
| Regression                 | Linear unit  | Mean Squared Error |
| Binary Classification      | Sigmoid unit | Cross-entropy loss |
| Multi-class Classification | Softmax unit | Cross-entropy loss |

- **Sigmoid** outputs probabilities for two classes.
- **Softmax** generalizes sigmoid for multi-class outputs, ensuring probabilities sum to 1.
- **Gradient descent** is an iterative algorithm that updates weights to reduce loss, moves weights opposite to the gradient (slope) of the loss.
    1. Calculate gradient (how loss changes w\.r.t. weights).
    2. Update weights by a small step (learning rate × gradient).
    3. Repeat until loss stops decreasing.
- **Back-propagation** computes gradients from the output layer back to the input layer for all weights efficiently using the **chain rule** of calculus.
- **Improving Efficiency** and Speed of Training:
    - **Batch Gradient Descent:** Uses the whole dataset per update. (SLOW)
    - **Stochastic Gradient Descent (SGD):** Updates weights after each training example.
    - **Mini-batch Gradient Descent:** Uses small groups (batches) of data per update (common in practice).

---

## **Chapter 11**

- **Intrinsic xAI**: Explainability is built into the model itself (Decision Trees, Linear Regression, Naïve Bayes).
- **Post-hoc xAI**: Explainability is added after the model is trained (e.g., LIME, SHAP).
- **Gradient-based methods:** Use gradients (derivatives) to see how input changes affect output (mostly for neural networks).
- **Surrogate-based methods:** create similar datapoints and pass model through input, later explain the model using simpler models (e.g., linear regression, decision trees) like **LIME** and **SHAP**.
- **LIME Limitations**: 
    - Explanations can vary each time you run it (not very stable).
    - Can be manipulated or fooled (adversarial risk).
    - Computationally expensive because it builds a surrogate model for every instance.
- **Example-based Explanations**
  - **Counterfactual:** Show how changing features would change the prediction (what-if scenarios).
  - **Adversarial Examples:** Small, possibly meaningless changes to inputs that flip predictions (helps understand model weaknesses).
  - **Data Influence:** Measures how much each training sample affects the prediction.
- **Global Explainability Methods**:
    - **Probing:** Train simple models to examine what parts of a neural network (like hidden layers) learn (e.g., shapes, colors in images).
- **Mechanistic Interpretability (MechInterp)** $\to$ study indivisual neurons $\to$ Use **causal interventions** (removing or altering neurons) to test effects on output
- **Concept-based Explainability (e.g., TCAV)**: Helps explain *what* the model “looks for” when making decisions which is human understandable.
---
## **Chapter 12**

- **AutoML Core Components**
    - **Search Algorithm**: Finds the best model and hyperparameters.
        - **Random/Grid Search**: Randomly or systematically explores combinations of hyperparameters.
            - **Grid Search:** Simple but does not scale well with many parameters.
            - **Random Search:** Tries random points; better than grid for high dimensions, easy to parallelize.
        - **Bayesian Optimization**: Uses past result to guide the search for better hyperparameters.
            - Fit surrogate probabilistic model (e.g., Gaussian Process)
            - Use an **acquisition function** (like Expected Improvement) to decide which hyperparameters to test next.
            - Evaluate $\to$ Update the surrogate model $\to$ Repeat.
        - **Hyperband**: Combines random search with early stopping to efficiently explore hyperparameter space.
    - **Search Space**: Defines what models and hyperparameters to consider. **Hyperparameters**:
        - **Categorical:** Choices like activation function ("relu", "sigmoid").
        - **Numerical:** Continuous (learning rate) or integer (number of layers).
        - **Conditional:** Some hyperparameters only matter if others have certain values (e.g., "beta1" only if using Adam optimizer).
    - **Evaluation Mechanism**: Measures model performance
        - Train/Validation/Test
        - Cross-validation
        - Multi-armed bandit (Treat each model/hyperparameter setting as a slot machine arm $\to$ **Successive Halving**)
            - **Hyperband**: Improved version of successive halving with improving configurations by Bayesian optimization.
        - Learning curve analysis (Longer training, more data, early stopping)
- **AutoML Problems**:
    - **Algorithm Selection Problem**
    - **Hyperparameter Optimization Problem (HPO)**
    - **Combined Algorithm Selection and Hyperparameter Optimization (CASH)**
    - **Neural Architecture Search (NAS)**
    - **Few-shot Learning** (Learning from very few examples)

**Surrogate Models**: These methods explain a complex (black-box) model by creating a simpler, easy-to-understand model called a surrogate. The surrogate model tries to imitate the behavior of the black-box model, but only locally—meaning around one specific example or instance you want to explain. (e.g., LIME, SHAP)
---

### Sample exam notes

- Basic decision trees tend to overfit if not pruned or controlled
- Decision tree $\to$ Both numerical and categorical features
- Decision trees don’t need feature scaling or normalization
- Grading models are usually about ranking or scoring, often dividing data into ordered groups or segments, which is different from linear regression. Linear regression doesn’t do grading in that sense.
- Grading models have a fixed and a finite resolution. **(Check)**
- Prior probability is the probability of a class, not feature/values.
- Posterior odds = Likelihood ratio $\times$ Prior odds.
- MAP (Maximum A Posteriori) decision rule uses both likelihood and prior probabilities to make decisions.
- One-vs-One can be used with SVM
- Kernel transform data into higher dimensions to make it linearly separable. (Useful for SVM)
- **C** parameter in SVM controls the trade-off between maximizing the margin and minimizing classification error.
    - small C $\to$ wider margin, more misclassifications
    - Large C $\to$ soft margin, fewer misclassifications
- curse of dimensionality: Number of features (dimensions) in data becomes very large which making distance metrics less meaningful.
- MLE can ignore easier the prior probabilities, while MAP considers them.
- Error purning $\to$ reduce overfitting
- **K-Lasso**: Regularization technique $\to$ penalizes large coefficients in linear regression.
    - Pick the best K features out of many.
    - Build a model using only those K features.
    - The rest of the features get zero weight.
- **Gini index** measures the impurity or how often a randomly chosen item would be incorrectly labeled.
- **Entropy** measures the uncertainty or randomness in a dataset.
- **Gini** vs **Entropy**:
    - Both are used to decide the best splits in a decision tree.   
    - Gini is simpler and faster, while entropy is more sensitive but computationally heavier.
- Lime consider surrogate model complexity and tries to keep it simple.
- Probing unlike LIME, is global explainability method and indivisually examines each neuron in a neural network to see what it learns.
