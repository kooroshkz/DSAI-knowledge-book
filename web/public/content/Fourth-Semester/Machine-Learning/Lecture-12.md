### Core Components of AutoML:

1. **Search Algorithm:**

   * The method used to explore different models and hyperparameters.
   * Examples:

     * **Random/Grid Search:** Try many options randomly or systematically.
     * **Bayesian Optimization:** Uses past results to pick promising options next.
     * **Hyperband:** Efficiently allocates resources to many configurations and quickly drops bad ones.

2. **Search Space:**

   * All the possible models and hyperparameter settings AutoML can try.
   * Includes ranges for hyperparameters (like learning rate, number of layers) and different model types.

3. **Evaluation Mechanism:**

   * How the AutoML system measures model quality.
   * Usually uses train/validation/test splits or cross-validation to evaluate performance.
   * May use methods like multi-armed bandits or learning curves to decide which models to test more.

---

### Types of Problems in AutoML:

* **Algorithm Selection Problem:** Pick the best model for the dataset.
* **Hyperparameter Optimization Problem (HPO):** For a chosen model, find the best hyperparameters.
* **Combined Algorithm Selection and Hyperparameter Optimization (CASH):** Find the best model **and** its best hyperparameters together.
* Other advanced problems: Neural Architecture Search (NAS), Few-shot Learning.

### Common Search Algorithms:

* **Grid Search:** Simple but does not scale well with many parameters.
* **Random Search:** Tries random points; better than grid for high dimensions, easy to parallelize.
* **Bayesian Optimization:** Builds a probabilistic model of the function and uses it to select promising hyperparameters to try next. More data efficient but harder to parallelize.

---

### How Bayesian Optimization Works:

1. Fit a surrogate probabilistic model (e.g., Gaussian Process) on observed points.
2. Use an **acquisition function** (like Expected Improvement) to decide which hyperparameters to test next.
3. Evaluate the model with those hyperparameters.
4. Update the surrogate model with the new result.
5. Repeat.

---

### Search Space Details:

* Hyperparameters can be:

  * **Categorical:** Choices like activation function ("relu", "sigmoid").
  * **Numerical:** Continuous (learning rate) or integer (number of layers).
  * **Conditional:** Some hyperparameters only matter if others have certain values (e.g., "beta1" only if using Adam optimizer).
* Sampling strategies decide how to pick values in the search space.

---

### Multi-Armed Bandits & Successive Halving:

* Treat each model/hyperparameter setting as a slot machine arm to pull.
* **Successive Halving:** Start with many candidates, test briefly, drop the worst half, test remaining longer, repeat until one winner remains.
* Used to save time by not fully training poor configurations.

---

### Extensions:

* **Hyperband:** An improved version of Successive Halving with better budget allocation.
* Combining Bayesian optimization with bandit methods improves efficiency.

---

### Learning Curve Models:

* Predict how well a model will perform if trained longer, allowing early stopping of bad configurations.