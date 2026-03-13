- **The Hopfield Network (HN)**
- **Fully connected** Network with **weight matrix**
- Neurons have two possible states: **-1** (inactive) or **+1** (active)., which is a thresholded output.
- **Bidirectional connections** between neurons.
- The network stores a set of patterns $\xi_1, \xi_2, \dots, \xi_p$ helps in pattern recognition and memory recall.
- The network can store approximately **0.15N** patterns, where $N$ is the number of neurons.
- **Improve Capacity**:
    - **Sparse Coding**: Store patterns with less active neurons, improving efficiency.
    - **Modified Learning Rules**: Use organizing **Storkey Learning Rule** to improve the separation between stored patterns.
    - **Increase the Number of Neurons**: More neurons directly increase the capacity to store patterns.
    - **Hierarchical Networks**: Structuring the memory storage, make seperated layers and groups of network to enhances capacity.
- **HN Model formula**:
    - $O_i (t+1) = \text{sgn} \left( \sum_j w_{ij} O_j(t) + b_i \right)$, where $O_i$ is the output of neuron $i$, $w_{ij}$ is the weight from neuron $j$ to neuron $i$, and $b_i$ is the bias for neuron $i$. $g()$ can be tanh or sigmoid function.
- **Weights**: The weight is defined as $w_{ij} = \frac{1}{N}\xi_i \xi_j$ (Also shows stability)
    - **Hebbian (Superposition) Form**: $w_{ij} = \frac{1}{N} \sum_{\mu=1}^p \xi_i^\mu \xi_j^\mu$, where $\xi_i^\mu$ is the $i$-th component of the $\mu$-th stored pattern.
    - The weights are symmetric, i.e., $w_{ij} = w_{ji}$, and $w_{ii} = 0$ (no self-connections).
- **Update Function**: Input pattern $\to$ update states (1 at the time) $\to$ get closer to one of patterns. 
    - $O_i (t+1) = \text{sgn} \left( \sum_j w_{ij} O_j(t) \right)$.
- **Stability**: A stored pattern $\vec{\xi}$ is **stable** if, when updated, it remains unchanged: $O_i = \text{sgn}\left(\sum_j w_{ij} \xi_j \right) = \xi_i$
- **Attractors**: Patterns that attract nearby states under the update dynamics are called **attractors**. If starting from an input close to $\vec{\xi}$, the network converges to $\vec{\xi}$: $O_i(t+1) = \text{sgn}\left(\sum_j w_{ij} O_j(t)\right) \to \vec{\xi}$ * All stable patterns are attractors, but attractors can also be **spurious** (unwanted).
    - **$h_i^\nu = \sum_{j=1}^N w_{ij} \xi_j^\nu$**: Total input that neuron $i$ receives when the network is showing pattern $v$.
    - **Crosstalk term**: $h_i^\nu$ expansion by Hebbian rule is $h_i^\nu = \xi_i^\nu + A$ where $A$ is the interference caused by all the other stored patterns that are not $v$.
        - $A = \frac{1}{N} \sum_{\mu \neq \nu} \sum_{j=1}^N \xi_i^\mu \xi_j^\mu \xi_j^\nu$
- **Energy Behavior**: Network tend to have low / stable energy, when new input comes, by updates it tries to minimize the energy function, to reach a stable state.
    - **Energy Function**: $E(\vec{x}) = -\frac{1}{2} \vec{x}^T \mathbf{W} \vec{x} - \vec{x}^T \vec{b}$
    - $H = -\frac{1}{2} \sum_{i,j} w_{ij} x_i x_j = -\frac{1}{2} \mathbf{x}^\top W \mathbf{x}$
- **Hamming Distance**: The goal is to minimize the Hamming distance between the input pattern and the stored patterns.
    - $d(\vec{x}, \vec{\xi}) = \sum_{i=1}^N [ \xi_i (1 - x_i) + (1 - \xi_i) x_i ] =$ no mismatch between patterns 
    - Instead binary state

$$\begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

we use $\text{FIRING} = \text{unit value} +1$ and $\text{Inhibit (NOT FIRING)} = \text{unit value} -1$.
- **Hebbian Rule**: Networks which fire together, wire together" $w_{ij} = \frac{1}{N} \sum_{\mu=1}^p \xi_i^\mu \xi_j^\mu$ (Generalized Hebbian Rule)
    - The weight between two neurons $i$ and $j$ is strengthened if they are both active (have the same sign) in the stored patterns $\xi^\mu$.
- **Spurious attractors**: Wrong memories made by mixing stored patterns. They happen when patterns are too similar or too many.
    - $\vec{\xi}^\mu \cdot \vec{\xi}^\nu = 0$ means orthogonal patterns, no spurious attractors, else with bigger $A$ the more spurious attractors.
- **$C_i^\nu = -\xi_i^\nu A = 1 - \xi_i^\nu h_i^\nu$** ($\xi_i^\nu$ is the true pattern bit for neuron $i$ in pattern $\nu$. * $h_i^\nu$ is the total input to neuron $i$ when pattern $\nu$ is active.)
- $1 - \xi_i^\nu h_i^\nu > 1 \implies \xi_i^\nu h_i^\nu < 0$ $\to$ $C_i^\nu \leq 1$, then $\xi_i^\nu h_i^\nu \geq 0$ **unstable**
- **Probability of error**: $P_{error} = \text{Probability that } C_i^\nu > 1$**, Optimal $P_{error} < 0.01$.
- **Calculate variance:** $\sigma^2 = \frac{p}{N}$
- **Error probability** $P_{error}$ using Gaussian tail: $P_{error} = \frac{1}{\sqrt{2\pi}\sigma} \int_1^\infty e^{-\frac{x^2}{2\sigma^2}} dx$
- **Choose max error** $P_{error}$ and find corresponding $\frac{p_{max}}{N}$ from tables or calculation.
- **Calculate max patterns:** $p_{max} = \left(\frac{p_{max}}{N}\right) \times N$
---

## **Proves and Exercises**:

#### Stability Condition

**Definition.** Let’s consider one stored pattern $\vec{\xi}$. The condition for $\vec{\xi}$ to be a stable pattern (attractor) is

$$O_i = \text{sgn} \left[ \sum_{j=1}^N w_{ij} \xi_j \right] = \xi_i \tag{5}$$

**Statement.** We obtain this if $w_{ij} = w_{ji} = \alpha \xi_i \xi_j$, $\alpha > 0 \quad$($w_{ij} \propto \xi_i \xi_j$).

**Proof.** Let $W = \alpha \xi \xi^T$ be the weight matrix:

$$O_i = \text{sgn} \left[ \sum_j w_{ij} \xi_j \right] = \text{sgn} \left[ \sum_j \propto \xi_i \xi_j \xi_j \right] = \text{sgn} \left[ \alpha \xi_i \sum_{j=1}^N 1 \right] = \text{sgn}(\alpha N \xi_i) = \text{sgn}(\xi_i) = \xi_i$$

$$\Rightarrow O_i = \xi_i \text{ STABLE!} \Rightarrow \text{We can take } \alpha = \frac{1}{N} \text{ when } N = \# \text{nodes} \Rightarrow w_{ij} = \frac{1}{N} \xi_i \xi_j$$

### Example

Design a network of 3 neurons that resembles a pattern $(1, 1, -1)$:

$$W = \frac{1}{N} \vec{\xi} \vec{\xi}^T = \frac{1}{3} \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} (1, 1, -1) = \frac{1}{3} \begin{bmatrix} 1 & 1 & -1 \\ 1 & 1 & -1 \\ -1 & -1 & 1 \end{bmatrix}$$

1. Is $\vec{\xi}$ stable?

$$\vec{0} = \text{sgn}(W \cdot \vec{\xi}) = \text{sgn} \left[ \frac{1}{3} \begin{bmatrix} 1 & 1 & -1 \\ 1 & 1 & -1 \\ -1 & -1 & 1 \end{bmatrix} \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \right] = \text{sgn} \left[ \frac{1}{3} \begin{pmatrix} 3 \\ 3 \\ -3 \end{pmatrix} \right] = \text{sgn} \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} = \vec{\xi} \Rightarrow \text{the answer is YES!}$$

2. Is $\vec{\xi}$ an attractor? Let’s try a test pattern

$$\vec{x} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$$

By help of the update function $O_i (t+1) = \text{sgn} \left( \sum_j w_{ij} O_j(t) \right)$ we can calculate the output:

$$\vec{O} = \text{sgn} \left[ \frac{1}{3} \begin{bmatrix} 1 & 1 & -1 \\ 1 & 1 & -1 \\ -1 & -1 & 1 \end{bmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \right] = \text{sgn} \left[ \frac{1}{3} \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \right] = \text{sgn} \begin{pmatrix} 1/3 \\ 1/3 \\ -1/3 \end{pmatrix} = \vec{x}$$

$$\rightarrow \vec{\xi} = \text{attractor state}$$

---

**Statement.** $\vec{\xi}$ is an attractor of the network defined by the weights $w_{ij} = \frac{1}{N} \xi_i \xi_j$.

**Proof.** Let’s consider the total net input:

$$h_i = \sum_{j=1}^N w_{ij} x_j$$

$$\Rightarrow h_i = \sum_j \frac{1}{N} \xi_i \xi_j x_j = \frac{1}{N} \xi_i \sum_j \xi_j x_j = \frac{1}{N} \xi_i \left[ \sum_{j=\text{correct}} \xi_j x_j + \sum_{j=\text{wrong}} \xi_j x_j \right] = \frac{\xi_i}{N} (N_{\text{correct}} - N_{\text{wrong}})

$$

$$

\Rightarrow O_i = \text{sgn}(h_i) = \text{sgn} \left( \xi_i \left[ \frac{N_{\text{correct}} - N_{\text{wrong}}}{N} \right] \right) = \begin{cases} \xi_i & \text{if more than or exactly } \frac{N}{2} \text{ are correct} \\ -\xi_i & \text{otherwise/opposite case} \end{cases}

$$

$$

\Rightarrow \xi_i \text{ is an attractor! AND in this simple case we also have another attractor at the reversed state } -\xi.$$

---

#### **Stability Condition**

The **Stability Condition** for a pattern $\xi_i^\nu$ is $O_i = \mathrm{sgn}(h_i^\nu) = \xi_i^\nu, \quad \forall i = 1, \ldots, N.$

**Proof:**
Let’s consider the net input

$$h_i^\nu \equiv \sum_{j=1}^N w_{ij} \xi_j^\nu = \frac{1}{N} \sum_{j=1}^N \sum_{\mu=1}^p \xi_i^\mu \xi_j^\mu \xi_j^\nu =$$

$$= \frac{1}{N} \left(\sum_{j=1}^N \xi_i^\nu \xi_j^\nu \xi_j^\nu \right) + \sum_{j=1}^N \sum_{\mu \neq \nu} \xi_i^\mu \xi_j^\mu \xi_j^\nu =

$$

$$

= \frac{1}{N} \sum_{j=1}^N \xi_i^\nu + \frac{1}{N} \sum_{j=1}^N \sum_{\mu \neq \nu} \xi_i^\mu \xi_j^\mu \nu_j^\nu =

$$

$$

= \xi_i^\nu + \frac{1}{N} \sum_{j=1}^N \sum_{\mu \neq \nu} \xi_i^\mu \xi_j^\mu \xi_j^\nu \equiv \xi_i^\nu + A$$

Now, if $|A| < 1$, then $O_i = \mathrm{sgn}(h_i^\nu) = \mathrm{sgn}(\xi_i^\nu + A) = \mathrm{sgn}(\xi_i^\nu) = \xi_i^\nu \implies \mathbf{Stability}.$
$A$ is named as *crosstalk* term and refers to the undesired interactions between stored patterns, generating interference, and hence retrieval error.
---

### Proof: Energy $H$ decreases with each update

- Energy function: $H = -\frac{1}{2} \sum_{ij} w_{ij} x_i x_j$
- Split $H$ as: $H = C - \sum_{i \neq j} w_{ij} x_i x_j$ where $C$ is constant.
- Update rule for neuron $i$: $O_i(t+1) = \text{sgn}\left(\sum_j w_{ij} O_j(t)\right)$
- Two cases:
   - 1. If $O_i(t+1) = O_i(t)$ (no energy change) $H(t+1) = H(t)$
   - 2. If $O_i(t+1) = -O_i(t)$ (energy decreases). $Difference:$H(t+1) - H(t) = 2 O_i(t) \sum_j w_{ij} O_j(t) - 2 w_{ii}$- Since$O_i(t+1)$flips sign, the weighted sum$\sum_j w_{ij} O_j(t)$has opposite sign to$O_i(t)$. - This makes the product$O_i(t) \sum_j w_{ij} O_j(t)$negative. Also,$w_{ii}$is positive or zero. - So,$ H(t+1) - H(t) < 0 $- Energy$H$**always decreases or stays the same** after an update. Therefore, the network converges to a **local minimum** of$H$. These minima correspond to **stable states** of the network.