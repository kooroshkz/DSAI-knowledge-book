- **Bandit**: One-time action, no state.
    - **Example**: Imagine you're at a casino with slot machines (bandits). Each time you pull a lever, you get a random reward (e.g., coins). There's no state or context to consider—just pick a machine and try your luck.
- **Contextual Bandit**: Action influenced by the current state (context).
    - **Example**: Imagine you're a restaurant owner, and you need to offer different meals to customers based on their preferences (context). If you know the customer's preference (e.g., vegetarian or non-vegetarian), your choice of meal (action) will have a different reward.
- **MDP**: Sequence of decisions, where actions influence future states and rewards.
    - **Example**: Think of a video game where you control a character (e.g., a maze). Every action you take (e.g., moving left or right) changes the environment (state). You may choose a path that gives you a lower reward now but leads to a higher reward later (sequential thinking).

| **Item**               | **Symbol**    | **Description**                                                  |
|------------------------|---------------|------------------------------------------------------------------|
| **State Space**         | $S$            | All possible states the system can be in                        |
| **Action Space**        | $A$           | All possible actions the agent can take                         |
| **Transition Function** |$p(s'\|s,a)$     | Probability of transitioning to a state given an action         |
| **Reward Function**     | $r(s,a,s')$   | Immediate reward for transitioning between states                |
| **Discount Factor**     | $γ$          | Factor that determines how much future rewards are valued       |
- **Policy**: Describes how the agent chooses actions in different states ($\pi(a|s)$).
- **Trace**: A sequence of state-action-reward pairs induced by the policy ($\tau$).
- **Return**: The cumulative sum of rewards from a trace ($R(\tau)$).
- **Value**: The expected return from each state or action under a policy ($v^\pi(s)$, $q^\pi(s,a)$).
- **Optimal Value/Policy**: There exists one optimal value function with a greedy policy that maximizes the return ($v^*(s)$, $q^*(s,a)$, $\pi^*(s)$).

## State
##### Atomic State:
- **Unique states, no relation**  
- **Example**: A vending machine with each product as a separate state (e.g., Coke = state 1, Chips = state 2).

##### Factorized State:
- **State is a set of related features**  
- **Example**: A self-driving car, where the state includes variables like speed, direction, and distance to obstacles (e.g., speed = 50 km/h, distance = 10m, direction = right). 

## Policy

A **policy** specifies the probability of taking each action in a given state.

- **Random Policy**: Each action has an equal chance of being selected in any state.
- **Deterministic Policy**: Always chooses the same action in a given state.
- **Greedy Policy**: Chooses the action that maximizes immediate reward, often focusing on short-term gains.

### Trace:
- **Trace** refers to the sequence of state-action-reward pairs observed when an agent acts in an MDP.
- **Notation**: $\tau = \{s_t, a_t, r_t, s_{t+1}, a_{t+1}, r_{t+1}, \dots\}$
  - **Subscript $t$**: Denotes the timestep.
  - **Greek letter $\tau$**: Represents the entire sequence (trace).

### Trace Probability:
- To calculate the probability of a trace, multiply the individual probabilities of actions, transiti`ons, and rewards along the trace.
- **Formula**:

$$

p(\tau) = \pi(a_t | s_t) \cdot p(r_t, s_{t+1} | s_t, a_t) \cdot \pi(a_{t+1} | s_{t+1}) \cdot p(r_{t+1}, s_{t+2} | s_{t+1}, a_{t+1}) \dots

$$

- This product rule combines the probabilities of each action, reward, and state transition along the trace.

### Return:
- **Return** is the total sum of rewards obtained over a trace.
- **Formula**: $R(\tau) = r_t + r_{t+1} + r_{t+2} + \dots$

### Discounted Return:
- **Discounted Return** gives less importance to future rewards.
- **Formula**: $R(\tau) = r_t + \gamma \cdot r_{t+1} + \gamma^2 \cdot r_{t+2} + \dots$
  - **$\gamma$** is the discount factor ($0 \leq \gamma \leq 1$).

### Trace Horizon:
- **Infinite Horizon**: Sum rewards infinitely unless a terminal state is reached.
- **Formula**: $R(\tau) = \sum_{i=0}^{\infty} \gamma^i \cdot r_{t+i}$

### Value:
- **Value of a State**: It represents the expected cumulative reward when starting from state $s$ under a given policy $\pi$.
- **Formula**:

$$

v^\pi(s) = E_{\tau \sim p^\pi(\tau)} [r_t + \gamma \cdot r_{t+1} + \gamma^2 \cdot r_{t+2} + \dots | s_t = s]

$$

- This gives the expected total reward from a state, considering future rewards.

- Each policy $π$ has its own value function shown with $v^\pi(s)$ , which can be optimal ($v^*$) and if it's based on action-state pairs, it's shown with $q^\pi(s,a)$.