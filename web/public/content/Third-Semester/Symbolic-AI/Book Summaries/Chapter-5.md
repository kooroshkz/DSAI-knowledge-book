1. **Local Search Methods:**
   - Operate on **complete-state formulations**, retaining only a small number of nodes in memory.
   - Methods include:
     - **Hill Climbing:** A greedy approach that moves towards increasing value but can get stuck at local maxima, ridges, or plateaus.
     - **Simulated Annealing:** Allows downhill moves probabilistically to escape local maxima, with the probability decreasing as the "temperature" decreases over time.
   - Effective for **optimization problems** like the 8-queens puzzle, where the path to the solution is irrelevant.

2. **Continuous Search Spaces:**
   - Problems such as linear programming and convex optimization involve continuous variables and often admit **polynomial-time algorithms**.
   - Techniques include **gradient descent** and the **Newton–Raphson method**, which exploit mathematical properties of smooth functions.

3. **Genetic Algorithms:**
   - Inspired by evolutionary biology, they maintain a population of states and evolve them using mutation, crossover, and selection.
   - Useful for problems like the traveling salesperson problem (TSP).

4. **Nondeterministic Environments:**
   - Require **AND–OR search trees** to handle contingencies.
   - Solutions are **contingent plans** rather than sequences, specifying actions for all possible outcomes.

5. **Partially Observable Environments:**
   - Use **belief states** to represent the agent’s knowledge about the possible physical states it could be in.
   - **Sensorless problems** rely on actions to coerce the environment into a goal state.
   - Algorithms such as **belief-state AND–OR search** or **incremental belief-state search** are applied to these environments.

6. **Exploration and Online Search:**
   - Online agents interleave computation and execution, making them suited for **dynamic and unknown environments**.
   - Algorithms include:
     - **Online Depth-First Search (DFS):** Explores the state space systematically but requires reversibility of actions.
     - **Learning Real-Time A\* (LRTA\*):** Updates heuristic estimates during exploration to improve decisions and escape local minima.

7. **Heuristic Improvements:**
   - Agents can update heuristic values during search, enabling more efficient exploration.
   - Random restarts and simulated annealing help tackle local minima in large state spaces.

---

1. **Special Cases of Algorithms:**
   - Local beam search (k = 1): **Hill climbing.**
   - Beam search with no state limit: **Breadth-first search.**
   - Simulated annealing with T = 0: **Greedy search.**
   - Simulated annealing with T = ∞: **Random walk.**
   - Genetic algorithm with N = 1: **Random restart hill climbing.**

2. **Formulating Problems for Simulated Annealing:**
   - Example: Real-world railway track alignment allows slight misalignments. Represent states as track configurations and the cost as the degree of misalignment. Neighboring states correspond to small rotations.

3. **Hill Climbing and Genetic Algorithms for TSP:**
   - Hill climbing explores neighboring cities, comparing solutions to A\* with the MST heuristic.
   - Genetic algorithms use crossover and mutation to evolve paths.

4. **Evaluating Local Search Variants:**
   - Generate problem instances for the 8-puzzle and 8-queens problems.
   - Analyze performance metrics (e.g., success rate, search cost).

5. **Improving AND–OR Search:**
   - Use state labels to track previously visited states and avoid redundant computation.
   - Allow cyclic plans for slippery or erratic environments.

6. **Belief State Optimization:**
   - Sensorless problems: Use heuristics like $ h(b) = \min_{s \in b} h^*(s) $, ensuring admissibility.
   - Subset-superset relationships enable pruning of belief states during search.

7. **Online Search Challenges:**
   - Represent the initial belief state as all possible configurations.
   - Generate contingency plans that adapt to all observations.

8. **Advanced Problem Solving:**
   - Use online agents to navigate dynamic environments, handling errors and replanning.
   - Modify hill climbing with depth-k lookahead or LRTA\* to escape local minima.

9. **Infinite State Spaces:**
   - Online DFS is incomplete for infinite reversible spaces. A complete algorithm must dynamically track and prioritize unvisited states.
