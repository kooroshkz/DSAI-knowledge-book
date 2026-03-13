* **Activation functions** add non-linearity so the network can learn complex patterns. Examples:

  * ReLU: $g(z) = \max(0, z)$
  * Sigmoid: $g(z) = \frac{1}{1+e^{-z}}$
  * Tanh: $g(z) = \tanh(z)$

---

### Neural Network Tasks and Output Units

* Different tasks use different output units and loss functions:

| Task                       | Output Unit  | Loss Function      |
| -------------------------- | ------------ | ------------------ |
| Regression                 | Linear unit  | Mean Squared Error |
| Binary Classification      | Sigmoid unit | Cross-entropy loss |
| Multi-class Classification | Softmax unit | Cross-entropy loss |

* **Sigmoid** outputs probabilities for two classes.
* **Softmax** generalizes sigmoid for more than two classes, outputs probability distribution over all classes.

---

### Loss Optimization — Training Neural Networks

* Goal: Find weights $W$ that minimize the loss function (error between prediction and true label).
* For simple linear regression, you solve for weights by setting derivative to zero (closed-form).
* For neural networks, the loss function is **non-convex**, so no simple closed form solution exists.

---

### Gradient Descent

* **Gradient descent** is an iterative algorithm that updates weights to reduce loss.
* It moves weights opposite to the gradient (slope) of the loss.
* Steps:

  1. Calculate gradient (how loss changes w\.r.t. weights).
  2. Update weights by a small step (learning rate × gradient).
  3. Repeat until loss stops decreasing.

---

### Back-propagation

* Back-propagation computes gradients for all weights efficiently using the **chain rule** of calculus.
* It calculates gradients layer by layer from the output layer back to the input layer.
* This lets gradient descent know how to update each weight.

---

### Improving Efficiency

* Calculating gradients over the whole dataset (batch gradient descent) is slow.
* Variants to speed up training:

  * **Batch Gradient Descent:** Uses the whole dataset per update.
  * **Stochastic Gradient Descent (SGD):** Updates weights after each training example.
  * **Mini-batch Gradient Descent:** Uses small groups (batches) of data per update (common in practice).