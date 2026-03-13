### Classical Planning

**Definition of Classical Planning**:
   - Involves fully observable, deterministic, static environments with a single agent.
   - Planning problem represented using **PDDL (Planning Domain Definition Language)**.
   - Components of a planning problem:
     - **Initial state**: Conjunction of fluents (e.g., `At(Truck1, Melbourne)`).
     - **Actions**: Defined by schemas with **Preconditions** and **Effects**.
     - **Result function**: Updates the state by applying action effects (add and delete lists).
     - **Goal test**: Conjunction of fluents to be satisfied.

#### Algorithms for State-Space Search

- **Forward (Progression) Search**
- **Backward (Regression) Search**

- **Heuristics**:
   - **Ignore Preconditions**: Simplify actions by removing preconditions.
   - **Ignore Delete Lists**: Allow monotonic progress (ignore action negations).
   - **State Abstraction**: Ignore irrelevant fluents to simplify state space.
   - **Subgoal Independence**: Approximate cost by summing subgoal costs.

---

#### Planning Graphs and GRAPHPLAN

- **Planning Graph**

- **Mutual Exclusion (Mutex)**:
   - Defines conflicts between actions or states at the same level.
   - Types: **Inconsistent effects**, **Interference**, **Competing needs**.

- **Heuristic Estimation**:
   - **Level Cost**: Level where a goal first appears.
   - **Max-Level**: Maximum level cost of subgoals (admissible but loose).
   - **Level Sum**: Sum of level costs (inadmissible but effective in practice).
   - **Set-Level**: First level where all subgoals appear non-mutex (admissible, accurate).

- **GRAPHPLAN Algorithm**:
   - Expands the planning graph until goals are non-mutex.
   - Uses backward search (`EXTRACT-SOLUTION`) to find plans.
   - Terminates when the graph and no-goods level off without finding a solution.
