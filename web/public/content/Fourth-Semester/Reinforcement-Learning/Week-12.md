* **Planning/search:** Using a model to look ahead and find good actions.
* **Exhaustive search:** Finds the best action but needs huge computation (samples \~ b^d, where b=branching factor, d=depth).
* Search algorithms try to visit important states first to save computation.
- **Types of Planning**:
  * **Decision-time planning:** Focuses on picking the best action for the current state. (e.g., A\*, MCTS)
  * **Background planning:** Improves global policy or value function (like learning). (e.g., Dynamic Programming, Dyna)
- **Classic Planning**
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
        * Sample complexity: proportional to M (number of traces) × D (depth).
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