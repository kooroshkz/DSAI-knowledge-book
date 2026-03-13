- **Chess** solved with **minimax search** and **alpha-beta pruning**.
  - **Minimax** is a *backtracking* search method in a zero-sum game tree trying utility-minmaxing. (Also used in Tic-Tac-Toe.)
    - **Utility** a number that measures how good or bad a game position is for a player.
  - **Alpha-beta pruning** reduces the search space by eliminating branches that won't affect the final decision.

- **Go** $\to$ **huge branching factor** and **depth**.
  - **Game tree complexity:** $b^d$
    - $b$ = branching factor (number of choices per move)
    - $d$ = depth (number of moves in the game)
  - **Brute force search** is (intractable) impossible:
    - There is no **heruistic function** to **truncate** (cut off/purn) the search early, unlike chess.
    
---

- **Monte Carlo Tree Search (MCTS)** finds the best move by repeatedly simulating games and building a search tree with four steps repeated:
  - **Selection:** Traverse the tree using a policy to select a node to expand
  - **Expansion:** Add new child nodes (possible moves)
  - **Simulation (Rollout):** Play random moves till the end or a cutoff to estimate the outcome
  - **Backup:** Update values in the tree nodes based on the simulation result

---

### MCTS in Detail:

- **UCT formula (Upper Confidence Bound for Trees):** a policy that choose the best action $a$ from state $s$

$$

\pi_{UCT}(s) = \arg\max_a Q(s,a) + c \sqrt{\frac{\ln n(s)}{n(s,a)}}

$$

* $Q(s,a)$ is the value estimation for action $a$ at state $s$

* $n(s)$ is how many times state $s$ was visited

* $n(s,a)$ is how many times action $a$ was chosen at $s$

* $c$ is a constant balancing exploration and exploitation

Means: Choose the action aa that has the best mix of a high value Q(s,a)Q(s,a) and an exploration bonus that favors less tried moves.

* **Q-value update:**

$$

Q_{\text{new}} \leftarrow Q_{\text{old}} + \frac{1}{n} (R_{\text{sum}} - Q_{\text{old}})

$$

* $R_{\text{sum}}$ is sum of rewards from simulations
* $n$ is the number of visits

Means: Is like a average update, to refine the value estimate based on new information.
**AlphaGo**: Leveraging prior knowledge both during learning and deployment.
    - **Behavior cloning**: Train a neural network to mimic expert moves.
    - **Monte Carlo Tree Search (MCTS)**: Uses smart search to look ahead in the game by simulating moves and outcomes before deciding what to do.
    - **Reinforcement learning**: Trial and error learning from self-play to improve the model over time.
    - **Self-play**: Curriculum learning by playing against itself, starting from random moves and gradually improving.
    
- **AlphaGo Neural Network**: 
    - **Rollout Policy $p_{\pi}$:** NN trained by vlassification on human expert positions, plays quick, random moves (rollouts).
    - **Supervised Learning Policy $p_{\sigma}$:** Trained on many **human expert moves**. Learns to predict expert moves by **classifying** the next move given a board state, copying expert behavior (behavior cloning).
    - **Reinforcement Learning (RL) Policy Network $p_{\rho}$:** Starts from the SL policy network $p_{\sigma}$ by improves by playing against itself (**self-play**) using **policy gradient** methods.
    - **Value Network $v_{\theta}$:** NN **predict the chance of winning** from any board position. Trained by **regression** on results of self-play games.

---

### Summary of the flow:

* Start with expert data (human games) → train rollout and SL policy networks.
* Use SL policy as a base and improve by self-play → train RL policy network.
* Use self-play results to train value network that predicts winning chances.
* All these networks help AlphaGo play much better than just copying humans.

---


* **KL divergence** measures how different two probability distributions are, minimizing KL divergence means **making your model’s policy close to the expert’s policy**.
  - $\theta = \arg\min_\theta KL(p_\mu(\cdot | s) \| p_\theta(\cdot | s))$ : Means you find the best parameters $\theta$ that minimize the difference as
    - $p_\mu(\cdot | s)$: The expert’s policy — how the expert chooses moves given state $s$.
    - $p_\theta(\cdot | s)$: Your model’s policy — how your AI chooses moves given state $s$, controlled by parameters $\theta$.
  - **Maximum Likelihood Estimation (MLE)** is used to find parameters $\theta$ that maximize the likelihood of expert moves, meaning you adjust your model to make it think the expert’s moves are very likely.
    - $\arg\max_\theta \sum \mu(c) \log p_\theta(c|s)$
    

---

- **AlphaGo Algorithm Notation:**
  - **Policy Prior $P(s,a) \in [0,1]$:** Probability of taking action $a$ in state $s$.
  - **# value function evaluation $N_v(s,a) \in N_0$:** Number of times state $s$ has been evaluated.
  - **# rollout evaluations $N_r(s,a) \in N_0$:** Number of times action $a$ has been rolled out from state $s$.
  - **Cumlative evaluated values $W_v(s,a) \in R$:** Sum of values from evaluating state $s$ with action $a$.
  - **Cumlative evaluated rollouts $W_r(s,a) \in R$:** Sum of values from rolling out action $a$ from state $s$.
  - **Transition value $Q(s,a) \in [-1,1]$:** Estimated value of taking action $a$ in state $s$. The average quality (value) of taking action $a$ in state $s$. It represents the expected outcome (win or lose) of making that move.

  - **Reward function $r(s_t, a_t)$**:

$$

r(s_t, a_t) = \begin{cases}
+1 & \text{if win (terminal state)} \\
-1 & \text{if lose (terminal state)} \\
0 & \text{otherwise} \end{cases}

$$