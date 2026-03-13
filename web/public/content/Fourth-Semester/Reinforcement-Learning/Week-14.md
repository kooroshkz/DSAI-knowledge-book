- **Value Function Approximation**: Instead of storing $v_\pi(s)$ for each state in large scale of state-actions, use a function $\hat{v}(s, w)$ with parameters $w$ to approximate the value function.
  - **$w$ approximation**: $w$  could be weights in a linear function or parameters of a neural network.
  - **Goal**: Find $w$ such that $\hat{v}(s, w)$ is close to $v_\pi(s)$ for all states $s$.
    - Define an error function: $VE(w) = \sum_s \mu(s) \left[v_\pi(s) - \hat{v}(s, w)\right]^2$
      - Use **gradient descent** to reduce this error by updating $w$:
        - $w \leftarrow w - \alpha \nabla VE(w)$
    - Use **sample estimates** instead from experience:
      - **Monte Carlo (MC):** Use full return $G_t$ after an episode.
        - **Gradient Monte Carlo:** Adjust parameters so the estimated value $\hat{v}$ moves closer to the observed return $G_t$.
          - $w \leftarrow w + \alpha (G_t - \hat{v}(S_t, w)) \nabla \hat{v}(S_t, w)$
          - where $G_t$ id the total return from time $t$ like $G_t = R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + ...$.
      - **Temporal Difference (TD):** Use current reward plus estimated value of next state. 
        - **Gradient TD(0) Algorithm**: Use one-step TD target instead of full return:
          - $w \leftarrow w + \alpha \big(R_{t+1} + \gamma \hat{v}(S_{t+1}, w) - \hat{v}(S_t, w)\big) \nabla \hat{v}(S_t, w)$
          - Update happens after every step, not after full episode. (More efficient and online)
  - **Approximating Values** $\hat{v}(s, w)$: We can’t store values for all states, so we use a **function** with parameters $w$ to guess values. Types:
    - 1) **State Aggregation**: Group similar states and assign one value to each group.
    - 2) **Linear Approximation**: Use features $x(s)$ of the state to compute value as a weighted sum:
      - $\hat{v}(s, w) = w_1 x_1(s) + w_2 x_2(s) + \cdots$
    - **Feature Types**: 
      - **Polynomial**: Use powers of state variables (e.g., $s, s^2, s^3$).
      - **Fourier**: Use sine/cosine functions to represent states.
      - **Coarse Coding**: Divide state space into overlapping regions; feature is 1 if state in region, else 0.
  - Control with **Action-Value Function Approximation**: Learn optimal policy by approximating action-value function $q_*(s, a)$ using parameterized function $q(s, a, w)$.
      - **Update Rules**:
        - **SARSA with Function Approximation**:
          - Update $w$ using observed transitions $(S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1})$:

$$

w \leftarrow w + \alpha \big(R_{t+1} + \gamma q(S_{t+1}, A_{t+1}, w) - q(S_t, A_t, w)\big) \nabla q(S_t, A_t, w)

$$

- **Q-learning with Function Approximation**:
          - Use greedy action for next state:

$$

w \leftarrow w + \alpha \big(R_{t+1} + \gamma \max_{a'} q(S_{t+1}, a', w) - q(S_t, A_t, w)\big) \nabla q(S_t, A_t, w)

$$

- **Challenge**: Instability and divergence possible with off-policy methods and nonlinear function approximators.
  - **Policy-Based Methods**
      - **Directly parameterize the policy** $\pi(a|s, \theta)$.
        - **Advantages**:
          - Can learn stochastic policies.
          - Better for high-dimensional or continuous action spaces.
          - Avoids need to estimate value for every action.
      - **Policy Gradient Theorem**:
        - Provides formula for gradient of expected return with respect to policy parameters.
  - **Actor-Critic Architecture**:
    - **Actor**: Updates policy parameters $\theta$ (chooses actions).
    - **Critic**: Updates value function parameters $w$ (evaluates actions).
    - **Update**:
      - Critic computes TD error:

$$

\delta_t = R_{t+1} + \gamma \hat{v}(S_{t+1}, w) - \hat{v}(S_t, w)

$$

- Actor updates $\theta$ in direction suggested by $\delta_t$:

$$

\theta \leftarrow \theta + \alpha \delta_t \nabla \log \pi(A_t|S_t, \theta)

$$

- Critic updates $w$ to reduce value error.