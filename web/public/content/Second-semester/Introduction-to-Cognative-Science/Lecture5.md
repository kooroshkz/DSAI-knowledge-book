# Neural Networks
Non Symbolic AI approach = Connectionism (Connection of Perceptrons)
#### Delta rule
It aims to minimize the error between the predicted output and the actual target output. 
Neural networks are algorithmic in a limited sense
- units/neurons have algorithms for updating activation levels
- learning rules are algorithmic

But not algorithmic in the same way as PSS
- algorithms are not task-specific
- algorithms do not operate over explicit representations(instead, they change weights and thresholds of individual unit
If we use the symbol $\Delta$ (big delta) to indicate the adjustment that we will make after each application of the rule, then the perceptron convergence rule can be written like this (remembering that $T$ is the threshold and $W_i$ is the $i$ th input):

$\Delta T = \eta \cdot \delta$

$\Delta W_i = \eta \cdot \delta \cdot I_i$


# Checklist

## Neurally Inspired Information Processing

1. A fundamental question in thinking about how the brain processes information is how the activities of large populations of neurons give rise to complex sensory and cognitive abilities.
2. Existing techniques for directly studying the brain do not allow us to study what happens inside populations of neurons.
   - Current brain imaging methods, like fMRI and PET, do not provide insights into the workings of neuron populations.
3. Computational neuroscientists use mathematical models (neural networks) to study populations of neurons.

## Single-Layer Networks

1. We can use single-layer networks to compute some Boolean functions, in particular AND, OR, and NOT.
2. Any digital computer can be simulated by a network of single-layer networks appropriately chained together.

## Biological Plausibility

1. Neural network units are much more homogeneous than real neurons. And real neural networks are likely to be both much larger and less parallel than network models.
2. However, there are other learning algorithms. Competitive networks using Hebbian learning do not require explicit feedback, and there is evidence for local learning in the brain.
   - More biologically plausible algorithms like Hebbian learning exist, which do not need explicit feedback.

## Information Processing in Neural Networks

1. There are no clear distinctions to be drawn within neural networks either between information storage and information processing or between rules and representations.
   - In neural networks, information storage and processing, as well as rules and representations, are intertwined.
