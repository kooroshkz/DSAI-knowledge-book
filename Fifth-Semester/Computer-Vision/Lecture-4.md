### Loss Functions

- **Cross-entropy Loss**: used with softmax for multi-class classification tasks.
    - If the correct class has low probability → **high loss**
    - If correct class has high probability → **low loss**
    - $L = - \log(p_{correct})$
- **Hinge loss (SVM)**:
    - Encourages correct class to be at least a margin away from incorrect classes.
    - $L = \max(0, 1 - y \cdot f(x))$
- **Why not** Squared Error for classification?
    - Bad gradients
    - Slower learning
    - Poor probabilistic interpretation

- **Gradient Decent**
    - **Batch Gradient Descent**: uses the entire dataset to compute gradients. $\to$ slow
    - **Stochastic Gradient Descent (SGD)**: uses a **mini-batch** $\to$ faster, noisy

- **Regularization**: prevents overfitting by adding a penalty to the loss function.
    - **L2 Regularization** (Ridge): penalizes large weights.
    - **Early Stopping**: stop training when validation loss starts to increase.

- **Activation Functions**:
    - **Step Function**:

$$f(x) = \begin{cases} 1 & \text{if } x \geq 0 \\ 0 & \text{if } x < 0 \end{cases}$$

Not differentiable $\to$ Cannot use gradient decent.
    - **ReLU**: $f(x) = \max(0, x)$ $\to$ default choice, but make neurons die $\to$ Leaky ReLU: Fixed dead neurons by allowing small negative slope.
    - **Sigmoid**: $f(x) = \frac{1}{1 + e^{-x}}$ ouput [0, 1] $\to$ vanishing gradient problem.
    - **Tanh**: $f(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$ Better than sigmoid as it is zero-centered $\to$ vanishing gradient problem still exists.

- **Backpropagation**: algorithm to compute gradients efficiently using the chain rule.
    - Forward pass: compute outputs
    - Backward pass: compute gradients layer by layer from output to input.
    - **Backprop with vectorization**: use matrix operations to speed up computations like **Jacobians**
    - **Other usecases**:
        - Feature visualization
        - DeepDream: modify input image to maximize certain neuron activations.
        - Adversarial attacks: slightly add noise to input to fool the network.

- **Optimization tricks**:
    - **Learning Rate Scheduling**: decrease learning rate over time.
    - **Momentum**: Make gradient decent doesn't fall in pit (local minima) by adding a fraction of the previous update to the current update.
    - **Adam Optimizer**: combines momentum and adaptive learning rates in scale for each parameter. $\to$ Default choice