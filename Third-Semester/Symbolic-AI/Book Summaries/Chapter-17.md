### Chapter 17: **Making Complex Decisions**

- Sequential decision-making in **stochastic environments** $\rightarrow$ Incorporates **uncertainty, sensing**, and **utilities** $\rightarrow$ MDP
  
#### **Markov Decision Processes (MDPs)**:

**Framework for sequential decisions in fully observable stochastic settings.**

- **Policy (π)**:
  - A strategy specifying the best action $`π(s)`$ for each state.
  - **Optimal Policy $(π*)$** maximizes the **expected utility** of the sequence.

#### **Key Features of MDPs**:
1. **Stationary Policies**:
   - Optimal policies depend only on the current state, not the time step.
2. **Utility of a State**:
   - Sum of **discounted rewards** over time:
     $$
     \text{Bellman Equation} U(s) = R(s) + \gamma \max_{a \in A} \sum_{s'} P(s'|s, a) U(s')
     $$
     $$
     \text{Value Iteration: Start with $U(s) = 0$ and iteratively update to convergence and reach optimal policy.}
     $$

#### **Decision Strategies**:
- **Finite Horizon**: Optimize decisions for a fixed number of steps into the future.
- **Infinite Horizon**: Decisions are made without a fixed endpoint, focusing on long-term rewards.

---

- **MDPs**: Framework for sequential decisions in fully observable stochastic settings.
- **POMDPs**: Extensions for partially observable environments.
- **Key Algorithms**:
  - **Value Iteration** and **Policy Iteration** for MDPs.
  - **Belief State-based Approaches** for POMDPs.
- Decision-making balances **risk, reward**, and **information gathering**.
