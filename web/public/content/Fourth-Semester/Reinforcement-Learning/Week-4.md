#### **Policy Iteration**:
1. Initialize a random policy.
2. **Policy Evaluation**: Calculate the value of each state for the current policy.
3. **Policy Improvement**: Update the policy by choosing the best action (greedy) for each state based on its value.
4. Repeat steps 2 and 3 until the policy converges (i.e., it doesn't change anymore).

### **2. Value Iteration**:
- **Value Iteration** combines both **policy evaluation** and **policy improvement** into a single step. Instead of separately evaluating and then improving the policy, value iteration iteratively updates the **value function** until it converges to the optimal values for all states. From these values, you can derive the optimal policy.

### **Steps of Value Iteration**:
1. **Initialize the value function** $v(s)$ for all states, typically set to 0.
2. **Repeat** the following step for each state:
   - Update the value of each state using the **Bellman Equation**:

$$

v(s) = \max_a \left[ \sum_{s'} p(s'|s,a) \left( r(s, a, s') + \gamma \cdot v(s') \right) \right]

$$

- This equation estimates the value of a state by looking at all possible actions and choosing the one that maximizes the expected future reward.
3. Repeat the value update until the values converge (the difference between old and new values becomes very small).
4. **Derive the optimal policy** by selecting the action that maximizes the value for each state:

$$

\pi^*(s) = \arg \max_a [ v(s) ]

$$

- Once the values have converged, the optimal policy can be obtained by simply choosing the action that maximizes the expected value for each state.

---
### **Key Differences**:
1. **Policy Iteration**:
   - Alternates between **policy evaluation** and **policy improvement**.
   - Converges faster in practice, but requires **two steps per iteration** (policy evaluation and improvement).
   - **Policy Iteration** tends to converge **faster** than value iteration when the state space is small to medium.

2. **Value Iteration**:
   - Performs a **single step** that combines both evaluation and improvement.
   - Can take longer because it updates the value function iteratively until it converges, but it doesn't require explicit policy evaluation.
   - **Value Iteration** can be more efficient when the problem requires fewer iterations, but it may take longer to converge on larger state spaces.
