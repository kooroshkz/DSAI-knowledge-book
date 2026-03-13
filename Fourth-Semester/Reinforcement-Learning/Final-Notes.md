- **Types of Reinforcement Learning**:
  - **MDP (Markov Decision Process)**: You have clear states, actions, and rewards. The system’s next state depends only on the current state and action (Markov property).
    - **Example**: A robot vacuum cleaner deciding where to go next based on its current location and the dirt it detects.
  - **POMDP (Partially Observable MDP)**: Like MDP, but you don’t fully see the state. You get some clues (observations) about the state but not the full picture.
    - **Example**: A self-driving car in foggy weather, using limited visibility to make driving decisions.
  - **Bandit Problems**: No states, only actions and rewards. Balance exploration (trying new things) and exploitation (using what works).
    - **Example**: A website testing different ads to see which ad gets more clicks. Each ad is an action, and clicks are rewards.
    - **Common Algorithms**:
      - **ε-Greedy** – Explores randomly with probability **ε**, otherwise exploits the best-known action.
      - **UCB (Upper Confidence Bound)** – Picks actions based on confidence intervals, favoring uncertain options optimistically.
      - **Softmax (Boltzmann Exploration)**
      - **Thompson Sampling** – Uses Bayesian sampling to pick actions based on estimated reward probabilities.

    - **Applications**: A/B testing, recommendation systems, and online advertising.

    - **Types**:
      - **Multi-Armed Bandit (MAB)**: A single agent chooses between multiple actions (like pulling levers on slot machines).
        - **Example**: A recommendation system suggesting different products to users.
      - **Contextual Bandit**: Reward depends on some extra information (context). When actions also change the state (context), it becomes a Markov Decision Process (MDP).
        - **Example**: Netflix recommends a movie (**action**) based on your watch history (**state**). You watch it (**reward = 1**) or skip it (**reward = 0**). 
      - **Bayesian Bandit**: Uses Bayesian methods to update beliefs about the best action based on observed rewards.
        - **Example**: A medical trial adjusting treatment recommendations based on patient responses. 
  - **Multi-Agent RL**: Multiple agents learning together.
    - **Example**: Multiple robots in a warehouse.
  - **Model-Based RL**: Learns a model of the environment, (how states change with actions) and uses it to plan the best actions.
    - **Example**: A chess-playing AI that simulates possible moves and their outcomes before making a decision.
    - **Algorithms**:
      - **Monte Carlo Tree Search (MCTS)**
      - **Dyna**
  - **Model-Free RL**: Learns directly from experience without a model.
    - **Example**: Teaching a robot to walk by trying different movements and learning from success or failure without knowing physics equations.
    - **Types**:
      - **Policy Gradient**(Learn the policy directly):
        - **REINFORCE**
      - **Learn value functions**:
        - **Q-Learning**: Learns value of actions independent of policy.
        - **SARSA**: Learns action values based on the action actually taken.
        - **Deep Q-Networks (DQN)**: Use neural networks to approximate Q-values for complex states.
---

- **Initialization of Bandits $Q(a)$ in** $Q(a) = \mathbb{E}_{r \sim p(r|a)}[r]$
    - **Realistic Initialization**: $Q(a)=0$, starts with guessing zero expected reward till algorithm updates it based on observed rewards.
    - **Optimistic Initialization**:  $Q(a)=ψ , ψ > 0$ make initial rewards high to encourage exploration.
- **Objective function**: Maximize expected cumulative reward over time $T$ under a policy $\pi$.
    - $J_T(\pi) = \mathbb{E}_{a_t \sim \pi, r_t \sim p(r|a_t)}\left[\sum_{t=1}^{T} r_t\right]$
    - This formula is a general way to measure how good a policy is.
    - **Policies in Bandit Problems**: 
        - **Deterministic Policy**: Always choose the same action for a given state.
        - **Greedy Policy**: Highest estimated reward $\to$ action
        - **Epsilon-Greedy Policy**: Mostly greedy, but sometimes explores random actions. $\epsilon$ (Random action) $\to$ higher $\to$ exploration.
        - **Softmax Policy**: Chooses actions based on their estimated rewards, with a temperature parameter controlling exploration vs. exploitation.
        - **Thompson Sampling**: Samples actions based on their probability of being optimal, balancing exploration and exploitation. 
- **Softmax (Boltzmann) Policy**:
    - **How it works**:
      - Assigns probabilities to actions based on their estimated rewards.
      - Higher estimated rewards lead to higher probabilities of being chosen. (So not a single highest will be chosen, sometimes lower rewards (but still high like rank 2nd, 3rd..) will be chosen too because of high probability).
      - The temperature parameter ($\tau$) controls exploration vs. exploitation:
        - **High $\tau$**: More exploration (actions are chosen more uniformly).
        - **Low $\tau$**: More exploitation (actions with higher rewards are chosen more frequently).
- **Upper Confidence Bound (UCB) Policy**:
    - Picks the action with the highest value of: $Q(a) + c \times \sqrt{\frac{\ln t}{n(a)}}$
    - Where:
      - $Q(a)$ is the estimated value of action $a$.
      - $c$ is a constant that controls exploration.
        - **Higher $c$**: More exploration (more weight on uncertainty).
        - **Lower $c$**: More exploitation (focus on known rewards).
      - $t$ is the total number of actions taken.
      - $n(a)$ is the number of times action $a$ has been selected.
---

- **Trace $\tau$**: A sequence of policy based state-action-reward pairs like $\tau = (s_0, a_0, r_1, s_1, a_1, r_2, \ldots)$.
    - **Infinite Horizon**: Sum rewards infinitely unless a terminal state is reached. $R(\tau) = \sum_{i=0}^{\infty} \gamma^i \cdot r_{t+i}$
- **Return $R(\tau)$**: The cumulative sum of rewards from a trace
    - **Discounted Return** gives less importance to future rewards. $R(\tau) = r_t + \gamma \cdot r_{t+1} + \gamma^2 \cdot r_{t+2} + \dots$
- **Value**: The expected return $v^\pi(s)$, $q^\pi(s,a)$
- **Optimal Value/Policy**: 
    - $v^*(s)$: Optimal (maximum expected) value function for state $s$.
    - $q^*(s,a)$: Optimal (maximum expected) action-value function for state $s$ and action $a$.
    - $\pi^*$: Optimal (maximum expected) policy that achieves the optimal value (maximizes expected return).
---
- **Policy Iteration**: Find optimal policy by iteratively improving the policy based on the value function. Fast converges in small states. Caulculate two step per itteration.
  - **Steps**:
    - 1. Select random initial policy.
    - 2. **Policy Evaluation**: Calculate the value function for the current policy.
    - 3. **Policy Improvement**: Update the policy based on the value function.
    - 4. Repeat **steps 2-3** until the policy converges (no changes).

- **Value Iteration**: Combines both **policy evaluation** and **policy improvement** into a single step to find optimal policy by iteratively updating the value function until convergence. A single step but takes longer due updates the value function iteratively until it converges.
    - **Steps**:
        - 1. Initialize the value function $V(s)$ arbitrarily (e.g., zeros).
        - 2. For each state $s$ we calculate the value for **all actions** at state $s$, pick the maximum, and assign that as the new $V(s)$.
        - 3. Repeat step 2 for all states until the value function converges (changes become very small).
        - 4. After convergence, we have the best policy now.
- **Policy Iteration:** Small–medium states, fewer but slower iterations while **Value Iteration:** Medium–large states, more but faster iterations.
---

- Dynamic Programming finds the best policy (best actions) when you know **everything** about the environment. $\to$ Policy Iteration.
- When we **don't have full knowledge** of the environment, we use **Monte Carlo methods** to learn from **experience**. $\to$ Model-Free RL.
- **Monte Carlo Methods**: Learn from complete episodes (traces) to estimate value functions.
  - MC estimates $v^\pi(s)$ and $q^\pi(s,a)$ by averaging returns from multiple episodes we have seen before.
    - **First-Visit MC**: Averages returns from the first time each state-action pair is visited in an episode.
    - **Every-Visit MC**: Averages returns from every time each state-action pair is visited in an episode.
  - Begin episodes from random state-action pairs to ensure all pairs get visited sometimes because if some states/action pairs are never visited, MC can’t estimate their values.
  - $\epsilon$-greedy exploration is often used in MC to ensure all state-action pairs are explored.
  - Monte Carlo can be used inside **Generalized Policy Iteration (GPI)**:
    - **Two main types**:
      - **On-Policy MC**: Evaluates and improves the policy being used to generate episodes.
      - **Off-Policy MC**: Evaluates a different policy than the one being used to generate episodes.
        - **Example**: Using a behavior policy to explore while evaluating a target policy.
          - **Behavior Policy**: The policy used to generate episodes (exploration).
          - **Target Policy**: The policy we want to improve (evaluation).
        - **Problem**: Behavior and target policies can be different and make different decisions. We can't just average rewards because episodes came from a different policy. 
          - **Solution** = **Importance Sampling**: Give a weight to each episode based on how likely it was under the target policy compared to the behavior policy.

- **Temporal Difference (TD) Learning**: another way to learn from **experience**, combines Monte Carlo and dynamic programming. It learns **step-by-step** during an episode instead of waiting until the episode ends.
  - **Update Rule**: $v(s_t) \leftarrow v(s_t) + \alpha \left[ r_{t+1} + \gamma v(s_{t+1}) - v(s_t) \right]$
    - Part in $[\cdots]$ is called the **TD error**, which will correct the value estimate right after the action is taken unlike MC. This part is **policy evaluation** and the whole update is **policy improvement**.

| Aspect              | Monte Carlo (MC)                    | Temporal Difference (TD)                     |
| ------------------- | ----------------------------------- | -------------------------------------------- |
| When update happens | After whole episode ends            | After every step                             |
| Use of next state   | No (waits for total return)         | Yes (bootstraps with estimated $v(s_{t+1})$) |
| Variance            | High (because it uses total return) | Lower (uses one-step estimate)               |
| Bias                | No bias (unbiased)                  | Slight bias due to bootstrapping             |
| Learning speed      | Slower                              | Faster and more online                       |

- **TD Control algorithms**
  - **SARSA (On-policy TD Control)**: Learns action values for the policy being followed. (Learning how good a move is based on the next move you actually make.)
    - Update rule: $Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t) \right]$
  - **Q-learning (Off-policy TD Control)**: Learns the optimal action values regardless of the policy being followed. (Uses the **maximum** estimated value of the next state (best possible action), not necessarily the action actually taken.)
    - Update rule: $Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_a Q(s_{t+1}, a) - Q(s_t, a_t) \right]$
    - **Maximization Bias**: Q-learning can overestimate action values due to always selecting the maximum Q-value in future states.
    - **Double Q-learning**: Addresses this bias by maintaining two separate Q-tables and using one to select actions and the other to evaluate them, reducing overestimation.

  - **Expected SARSA**: A variant of SARSA that uses the expected value over possible next actions instead of the single next action.
    - Update rule: $Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \sum_a \pi(a|s_{t+1}) Q(s_{t+1}, a) - Q(s_t, a_t) \right]$

- **N-step TD and N-step SARSA**: Extensions of TD and SARSA that consider multiple steps for better value estimation.

### Summary:

| Algorithm      | On-policy / Off-policy | Next state update                | Main idea                                           |
| -------------- | ---------------------- | -------------------------------- | --------------------------------------------------- |
| SARSA          | On-policy              | Uses next action actually taken  | Learns action values following policy               |
| Q-learning     | Off-policy             | Uses max action value next state | Learns optimal action values regardless of behavior |
| Expected SARSA | On or Off-policy       | Uses expected value over actions | Averages over possible next actions                 |
#### Note:

* **Monte Carlo Tree Search (MCTS)** is a **planning** method. It uses a **model** to simulate many possible future paths from the current state (reversible access) and builds a search tree to decide the best next action. It focuses on a **local solution**.

* **Monte Carlo methods in RL** are **model-free learning** methods. They learn from **real experience** by averaging returns from full episodes. They don’t use a model and update values globally for all states visited.

So, MCTS = planning with a model, and Monte Carlo RL = learning from experience without a model.

---


- **Back-up**: update estimation of state values $V(s)$ or state-action values $Q(s,a)$ (future reward) in reinforcement learning.
    - **Expected Back-ups**: used in planning with a full model of the environment. (e.g., Dynamic Programming)
    - **Sample Back-ups**: used in reinforcement learning without a full model, updating values based on sampled experiences. (e.g., TD learning, Monte Carlo methods)
- **On-policy Back-ups**: updates values based on the policy being followed. The agent learns about the consequences of its current behavior. 
  * Example: **SARSA** — updates use the next action that the agent actually takes.
- **Off-policy Back-ups**: updates values based on a different policy than the one being followed. The agent learns about the consequences of actions that may not be taken in the current behavior.
  * Example: **Q-learning** — updates use the best possible next action, regardless of what action the agent actually took.
* **1-Step Back-ups (Shallow updates):**
  * Updates use information from only one step ahead (the immediate next state).
  * Faster but may be less accurate.
  * Examples:
    * **TD(0)** updates values using the reward and the value estimate of the next state only.
    * **Monte Carlo** can be considered 1-step if it updates only after an episode ends (looking at total return).
* **Multi-Step Back-ups (Deep updates):**
  * Updates consider multiple steps into the future, often the entire remaining episode or a sequence of states.
  * More accurate but computationally heavier.
  * Examples:
    * **Monte Carlo** updates after entire episodes (multi-step).
    * **TD(λ)** uses a weighted average of different multi-step returns.
    * **Dynamic Programming** computes expected returns over all possible future steps.

| Algorithm                    | Type of Back-up  | Step-size  | Explanation                                                        |
| ---------------------------- | ---------------- | ---------- | ------------------------------------------------------------------ |
| **TD(0)**                    | Sample Back-up   | 1-step     | Uses one sample, updates values after one step                     |
| **Monte Carlo (MC)**         | Sample Back-up   | Multi-step | Uses full episode returns, updates after episode ends              |
| **Dynamic Programming (DP)** | Expected Back-up | Multi-step | Uses full model to calculate expected returns over all next states |

- **MDP Dynamics**
    - **Models** (Reversible access):
        - **Distribution model:** Give you full probability distribution from next till target state.
        - **Sample model:** We don’t get the whole distribution, just one possible next state from the randomness.
    - **Environments** (Irreversible access):
        - **Sample Environment:** You almost always get only samples, because you actually take an action and observe what happens next, you don't get full distributions.

- **MDP Approaches**:
    - **Planning**:  assumes reversible access to the environment dynamics, meaning you have a model that you can query at any state-action pair, anytime (you can simulate outcomes without actually moving).
    - **Learning**: (specifically model-free RL) assumes irreversible access, meaning you can only interact with the real environment step-by-step, moving forward and learning from experience.

| Access Type        | Solution Type   | Method Category                 | Example Algorithm(s)           |
| ------------------ | --------------- | ------------------------------- | ------------------------------ |
| Reversible (Model) | Local solution  | **Planning**                    | Monte Carlo Tree Search (MCTS) |
| Reversible (Model) | Global solution | **Model-based RL** (borderline) | Dynamic Programming (DP)       |
| Irreversible (Env) | Global solution | **Model-free RL**               | Q-learning, SARSA              |

- **Tabular Model Learning**: This is a way to learn a model of the environment when you don’t have it beforehand, by collecting experience from the environment.
* Keep arrays for $n(s,a,s')$ and $R_{sum}(s,a,s')$, size $|S| \times |A| \times |S|$.
- **Dyna**: Model-based RL algorithm that combines learning and planning.
    - **Steps**:
        1. Learn a model of the environment from experience.
            - Store in table the reward of taking action $a$ in state $s$ and ending up in state $s'$
        2. Use the model to simulate experiences and update the value function or policy.

        3. Update the value function or policy based on real experiences.
        - Update Q-values by simulating transitions as simulated the transitions without actually taking actions in the environment.
    - **Benefits**: Combines the strengths of model-based and model-free approaches, allowing for faster learning and better exploration.
    - **Parameters**:
        - Number of planning updates K: How many simulated updates you do using the model for every real experience.
        - Learning rate αα: How much you update the Q-values each time.
        - Discount factor γγ: How much future rewards count compared to immediate rewards.
        - Exploration parameter ϵϵ: Probability of choosing a random action (to explore).
    - **Algorithm**:
        1. Start with Q-values and model counts all zero.
        2. At each step, pick an action using epsilon-greedy policy.
        3. Take the action, get reward and next state from the real environment.
        4. Update the model (counts and rewards) based on this experience.
        5. Update Q-value using the real experience (Q-learning update).
        6. Do extra updates by simulating experiences from the model K times, updating Q-values each time.

- **Prioritized Sweeping**: Extension of Dyna (Model-Based) that instead of updating all states equally or randomly, it focuses on the most important or most promising states that need an update. This speeds up learning by spending effort where it matters most.

    - **Steps**:
        1. Keep a **priority queue** of states prioritized by their TD error magnitude (Higher priority $p \to$ higher TD error $\to$ more important to update).
            - Priority queue is a data structure keeps items sorted by their priority $\to$ when pop $p$ the highest priority item is removed first.
        2. Update the most important states first, ensuring that the learning process focuses on the most impactful changes.
    - **Key Parameter**: 
        - **Threshold $\theta$:** Minimum priority for a state-action to be added to the queue. Controls how sensitive the algorithm is to changes.
    - **Algorithm**:
        - 1. **Initialize** Q-values, model counts, and an empty priority queue.
        - 2. **Interact** with the environment:
            * Take action in current state using exploration (like epsilon-greedy).
            * Observe reward and next state.
            * Update the model with this transition.
        - 3. **Calculate priority** for that state-action: $p = |r + \gamma \max_{a'} Q(s', a') - Q(s, a)|$ If $p > \theta$ (threshold), add $(s, a)$ to the priority queue.

        - 4. **Planning updates (repeat K times):**
            * Pop the highest priority $(s, a)$ from the queue.
            * Use the model to simulate next state and reward.
            * Update Q-value for $(s, a)$ with TD update.
            * For all state-actions leading to $s$, calculate their priority and add to queue if above threshold.

---

- **Types of Planning**:
  * **Decision-time planning:** Focuses on picking the best action for the current state. (e.g., A\*, MCTS)
  * **Background planning:** Improves global policy or value function (like learning). (e.g., Dynamic Programming, Dyna)
  - **Classic Planning:**
    * **Problems:** 
        - 1-Need a good heuristic to reduce depth. 
        - 2- Pruning is risky and harder with stochasticity.
        - 3- Often need exact transition models, which may not be available (only simulators).
    * **Tree search:** Explores states like a tree, but can waste time on repeated states.
    * **Graph search:** Avoids repeated states by tracking explored (closed list) and frontier (open list).
    * **Uninformed search:** BFS, DFS, Iterative Deepening. Downsides: may miss better paths because they ignore costs/rewards/weights.
    * **Uniform cost search (Dijkstra):** Considers cost so far but ignores future potential.
    * **Heuristic search (A\*):** Actual cumulative cost from start to state $s$ $(g(s))$ + estimated cumulative cost from $s$ to end $(h(s))$.
        * Heuristic $h(s)$ must be **admissible** (never overestimate) to guarantee finding the best path.
        * Perfect heuristic = optimal value function $V^*(s)$.
        * $f(s) = g(s) \to \text{Dijkstra’s algorithm/Uniform-cost search} + h(s) \to \text{cumulative cost from s to end} = \text{A* search}$.
* **Forward pruning:** Limits actions explored (like beam search), but risks removing the best action.
* **Stochastic planning:** Extends classic algorithms (e.g., A\* → AO\*) by expanding all possible outcomes of actions.
  * Problems: Needs analytic model and heuristic, but often only simulators are available; large branching in stochastic cases.

**Rollouts**: A technique to estimate the value of actions by simulating random future states. (Simulation)
- **Sample-based Planning**:
  * **Monte Carlo (MC) methods** to estimate action values by sampling instead of enumerating all possibilities.
    * **Benefits:**

      * No need for heuristic (use rollouts).
      * No need to prune actions (use uncertainty to guide search).
      * Can work with simulators, no exact model needed.
    - **a) Monte Carlo Search (MCS)**
      * For each action, sample N trajectories (rollouts) until depth D with a rollout policy (random or better).
      * Estimate action value Q(s,a) by average returns, pick action with highest Q.
      * **Downside:** Does not improve policy below the current step; no memory of past samples.
    - **b) Sparse Sampling**
        * Like MCS but repeats sampling at every level up to depth D (policy improvement at all depths).
        * Sample complexity grows exponentially with D: (A \* N)^D. Very expensive.
    - **c) Monte Carlo Tree Search (MCTS)**
        * Improves on Sparse Sampling by focusing sampling on promising actions using **adaptive bandit algorithms** (e.g., UCT).
        * Builds an asymmetric tree, deeper where returns are better.
        * Four phases:

          1. **Selection:** Use UCT to select action balancing exploration/exploitation.
          2. **Expansion:** Add new state when an unvisited action is chosen.
          3. **Simulation:** Rollout from new state to estimate value.
          4. **Backup:** Update statistics (visit counts and mean returns) up the tree.
        * Sample complexity: proportional to $M$ (number of traces) $\cdot D$(depth).
            - **Sparse Sampling**: $(A \cdot N )^D$ and MCTS complexity is $M \cdot D$ due promising paths.
        * Very effective especially without a good heuristic (used in AlphaGo).
- **Iterated Planning & Learning**

  * Pure planning is expensive and may lack good heuristics.
  * Pure learning may have errors in value/policy estimates.
  * Combining both is powerful:

    * Use planning to fix errors in learned values at decision-time.
    * Use planning to generate data for learning in background.
  * **AlphaGo** is an example that combines planning and learning iteratively.
  * Analogy:

    * Learned value function = "Thinking fast" (quick decisions).
    * Decision-time planning = "Thinking slow" (careful analysis).
  * Both work together for better decisions.

---


- **Monte Carlo Tree Search (MCTS)** finds the best move by repeatedly simulating games and building a search tree with four steps repeated:
  - **Selection:** Traverse the tree using a policy to select a node to expand
  - **Expansion:** Add new child nodes (possible moves)
  - **Simulation (Rollout):** Play random moves till the end or a cutoff to estimate the outcome
  - **Backup:** Update values in the tree nodes based on the simulation result

---

### MCTS in Detail:

- **UCT formula (Upper Confidence Bound for Trees):** a policy that choose the best action $a$ from state $s$

$$\pi_{UCT}(s) = \arg\max_a Q(s,a) + c \sqrt{\frac{\ln n(s)}{n(s,a)}}$$

* $Q(s,a)$ is the value estimation for action $a$ at state $s$

* $n(s)$ is how many times state $s$ was visited

* $n(s,a)$ is how many times action $a$ was chosen at $s$

* $c$ is a constant balancing exploration and exploitation

Means: Choose the action aa that has the best mix of a high value Q(s,a)Q(s,a) and an exploration bonus that favors less tried moves.

* **Q-value update:**

$$Q_{\text{new}} \leftarrow Q_{\text{old}} + \frac{1}{n} (R_{\text{sum}} - Q_{\text{old}})$$

* $R_{\text{sum}}$ is sum of rewards from simulations
* $n$ is the number of visits

Means: Is like a average update, to refine the value estimate based on new information.
---

- **AlphaGo**: Leveraging prior knowledge both during learning and deployment.
    - **Behavior cloning**: Train a neural network to mimic expert moves.
    - **Monte Carlo Tree Search (MCTS)**: Uses smart search to look ahead in the game by simulating moves and outcomes before deciding what to do.
    - **Reinforcement learning**: Trial and error learning from self-play to improve the model over time.
    - **Self-play**: Curriculum learning by playing against itself, starting from random moves and gradually improving.
    
- **AlphaGo Neural Network**: 
    - **Rollout Policy $p_{\pi}$:** NN trained by vlassification on human expert positions, plays quick, random moves (rollouts).
    - **Supervised Learning Policy $p_{\sigma}$:** Trained on many **human expert moves**. Learns to predict expert moves by **classifying** the next move given a board state, copying expert behavior (behavior cloning).
    - **Reinforcement Learning (RL) Policy Network $p_{\rho}$:** Starts from the SL policy network $p_{\sigma}$ by improves by playing against itself (**self-play**) using **policy gradient** methods.
    - **Value Network $v_{\theta}$:** NN **predict the chance of winning** from any board position. Trained by **regression** on results of self-play games.
- **Summary of the flow**:
    * Start with expert data (human games) → train rollout and SL policy networks.
    * Use SL policy as a base and improve by self-play → train RL policy network.
    * Use self-play results to train value network that predicts winning chances.
    * All these networks help AlphaGo play much better than just copying humans.

* **KL divergence** measures how different two probability distributions are, minimizing KL divergence means **making your model’s policy close to the expert’s policy**.
  - $\theta = \arg\min_\theta KL(p_\mu(\cdot | s) \| p_\theta(\cdot | s))$ : Means you find the best parameters $\theta$ that minimize the difference as
    - $p_\mu(\cdot | s)$: The expert’s policy — how the expert chooses moves given state $s$.
    - $p_\theta(\cdot | s)$: Your model’s policy — how your AI chooses moves given state $s$, controlled by parameters $\theta$.
  - **Maximum Likelihood Estimation (MLE)** is used to find parameters $\theta$ that maximize the likelihood of expert moves, meaning you adjust your model to make it think the expert’s moves are very likely.
    - $\arg\max_\theta \sum \mu(c) \log p_\theta(c|s)$

- **AlphaGo Algorithm Notation:**
  - **Policy Prior $P(s,a) \in [0,1]$:** Probability of taking action $a$ in state $s$.
  - **# value function evaluation $N_v(s,a) \in N_0$:** Number of times state $s$ has been evaluated.
  - **# rollout evaluations $N_r(s,a) \in N_0$:** Number of times action $a$ has been rolled out from state $s$.
  - **Cumlative evaluated values $W_v(s,a) \in R$:** Sum of values from evaluating state $s$ with action $a$.
  - **Cumlative evaluated rollouts $W_r(s,a) \in R$:** Sum of values from rolling out action $a$ from state $s$.
  - **Transition value $Q(s,a) \in [-1,1]$:** Estimated value of taking action $a$ in state $s$. The average quality (value) of taking action $a$ in state $s$. It represents the expected outcome (win or lose) of making that move.

  - **Reward function $r(s_t, a_t)$**:

$$r(s_t, a_t) = \begin{cases}
+1 & \text{if win (terminal state)} \\
-1 & \text{if lose (terminal state)} \\
0 & \text{otherwise} \end{cases}$$

---

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

$$w \leftarrow w + \alpha \big(R_{t+1} + \gamma q(S_{t+1}, A_{t+1}, w) - q(S_t, A_t, w)\big) \nabla q(S_t, A_t, w)$$

- **Q-learning with Function Approximation**:
          - Use greedy action for next state:

$$w \leftarrow w + \alpha \big(R_{t+1} + \gamma \max_{a'} q(S_{t+1}, a', w) - q(S_t, A_t, w)\big) \nabla q(S_t, A_t, w)$$

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

$$\delta_t = R_{t+1} + \gamma \hat{v}(S_{t+1}, w) - \hat{v}(S_t, w)$$

- Actor updates $\theta$ in direction suggested by $\delta_t$:

$$\theta \leftarrow \theta + \alpha \delta_t \nabla \log \pi(A_t|S_t, \theta)$$

- Critic updates $w$ to reduce value error.