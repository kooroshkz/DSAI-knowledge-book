### **xAI**

### White-box models (Inherently interpretable)

* Decision Trees
* Logical models
* Linear models (linear regression/classification)

### Black-box models (Not inherently interpretable)

* Neural networks
* Random forests
* Support Vector Machines (SVMs)
* Deep learning models (CNNs, Transformers, LLMs)
* Ensemble methods

---

## Categories of Explainable AI Methods

| Category                  | Description                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| **Post-hoc**              | Explain model decisions *after* training (applies to any model, especially black-boxes). |
| **Intrinsic**             | Models designed to be interpretable by themselves (white-box models).                    |
| **Model-specific**        | Methods designed for a particular type of model (e.g., linear regression coefficients).  |
| **Model-agnostic**        | Methods that work without needing to know model internals (just input-output behavior).  |
| **Local explainability**  | Explain a single prediction for one specific input instance.                             |
| **Global explainability** | Explain the overall behavior of the entire model.                                        |

---

## Local Explainability Methods

### Feature Attribution

* Assign importance scores to input features for a single prediction.
* **Gradient-based methods:** Use gradients (derivatives) to see how input changes affect output (mostly for neural networks).
* **Surrogate-based methods:** Train a simple, interpretable model (surrogate) locally around one instance to approximate the black-box model.

  * Examples: **LIME** and **SHAP**.

### Example-based Explanations

* **Counterfactuals:** Show how changing features would change the prediction (what-if scenarios).
* **Adversarial examples:** Small, possibly meaningless changes to inputs that flip predictions (helps understand model weaknesses).
* **Data influence:** Measures how much each training sample affects the prediction.

---

## Global Explainability Methods

### Probing

* Train simple models to examine what parts of a neural network (like hidden layers) learn (e.g., shapes, colors in images).

### Mechanistic Interpretability (MechInterp)

* Study individual neurons or circuits in neural nets to understand their roles.
* Use **causal interventions** (removing or altering neurons) to test effects on output.

### Concept-based Explainability (e.g., TCAV)

* Measure how strongly the model’s layers respond to human-understandable concepts (like "striped" patterns in images).
* Helps explain *what* the model “looks for” when making decisions.

---

### LIME

1. Start with an instance $x$ to explain.
2. Generate many slightly altered samples around $x$ (perturbations).
3. Get predictions for these samples from the black-box model $f$.
4. Weight these samples by how close they are to $x$.
5. Train a simple interpretable model $g$ (regression or random forest) on the weighted samples and their predictions.
6. Use $g$ to explain which features are important for the prediction on $x$.

### Limitations of LIME

* Explanations can vary each time you run it (not very stable).
* Can be manipulated or fooled (adversarial risk).
* Computationally expensive because it builds a surrogate model for every instance.