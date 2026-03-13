**Artificial General Intelligence :** reasoning, learning, problem solving, generalisation

**Strong AI:** Machines that act intelligently can eventually also possess consciousness
Swarm intelligence: agents interacting locally with one another and with the environment
### Classical (Symbolic) AI or Good Old-fashioned AI (GOFAI)

focusses on knowledge representation and general purpose “reasoning” mechanisms.

- Separation between knowledge and reasoning.
- Generic reasoning (problem-solving) based on search and logic.

### **Environment Properties:**
- **Deterministic:** The next state is entirely predictable from the current state and action (e.g., a puzzle game like Tetris).
- **Stochastic:** There is some randomness in the outcome of actions (e.g., Pacman, where ghosts can move unpredictably).

### **Types of Agents:**

1. **Simple Reflex Agents:**
   - Act on current percepts using predefined condition–action rules.
   - Limitations: Fail in partially observable environments.

2. **Model-Based Reflex Agents:**
   - Handle **partially observable environments** by maintaining an internal state.

3. **Goal-based Agents:**
4. **Utility-based Agents:**
#### **Task Environments (PEAS Framework)**
- **PEAS:** Performance measure, Environment, Actuators, Sensors.

---

#### **Graph vs. Tree Search**
- **Tree Search**: Considers all paths, including loops.
- **Graph Search**: Avoids revisiting states by using an explored set.


- **Uninformed Search**: No additional information about states beyond the problem definition.
- **Informed Search**: Uses heuristics to estimate the quality of non-goal states (covered in Section 3.5).

## Uninformed Search Methods

Don’t have prior knowledge of the problem domain.

- **Breadth-first search**
- **Uniform-cost search**: Expands the node with the lowest path cost, $g(n)$, and is optimal for general step costs.
Memory efficient, time efficient
```bash
    A
   / \
  2   3
 /     \
B       C    
|\     /|
4 1   2 5
|  \ /  |
D   E   F
 \  |  /
  \ | /
   \|/
    G   
```
Steps:
1. `(A, cost=0)`,              2. `[(B, cost=2), (C, cost=3)]`,             3. `[(C, cost=3), (E, cost=3), (D, cost=6)]`
4. `[(E, cost=3), (D, cost=6), (E, cost=5), (F, cost=8)]`,    5. `[(D, cost=6), (E, cost=5), (F, cost=8), (G*, cost=4)]`

- **Depth-first search**
- **Iterative deepening search**: 
```bash
        A
       / \
      B   C
     / \   \
    D   E   G

```
Depth = 0 :`A`, Depth = 1 :`A → B, A → C`, Depth = 2 :`A → B → D, A → B → E, A → C → G`
- **Bidirectional search**: Can enormously reduce time complexity, but it is not always applicable and may require too much space.

## Informed Search Methods

Informed search methods may have access to a heuristic function $h(n)$ that estimates the cost of a solution from $n$.

- **Best-first search**: A generic algorithm that selects a node for expansion according to an evaluation function.
- **Greedy best-first search**: Expands nodes with minimal $h(n)$. It is not optimal but is often efficient.
- **A\* search**: Expands nodes with minimal $f(n) = g(n) + h(n)$. 
  - A\* is complete and optimal, provided that $h(n)$ is admissible (for Tree-Search) or consistent (for Graph-Search). 
  - However, the space complexity of A\* is still prohibitive.
  - <img src="https://d18l82el6cdm1i.cloudfront.net/uploads/hevQ7EbwVU-output_prgol9.gif" alt="Breadth-First Search" width="250">
- **RBFS (Recursive Best-First Search)** and **SMA\* (Simplified Memory-Bounded A\*)**: Robust, optimal search algorithms that use limited amounts of memory. Given enough time, they can solve problems that A\* cannot solve due to memory constraints.

## Heuristic Search Performance

The performance of heuristic search algorithms depends on the quality of the heuristic function. Good heuristics can be constructed by:
- Relaxing the problem definition.
- Storing precomputed solution costs for subproblems in a **pattern database**.
- Learning from experience with the problem class.

- **BFS and UCS** are exhaustive but memory-intensive.
- **DFS and DLS** save memory but risk incompleteness.
- **IDS** combines benefits of BFS and DFS for large state spaces.
- **Bidirectional Search** is efficient but requires a well-defined goal state.

#### **Admissible vs. Consistent Heuristics**
- **Admissible**: Never overestimates the cost to the goal.  
- **Consistent**: Satisfies the triangle inequality ($h(n) \leq c(n, a, n') + h(n')$).

| Criterion        | Breadth-First      | Uniform-Cost          | Depth-First | Depth-Limited | Iterative Deepening | Bidirectional (if applicable) |
|------------------|--------------------|------------------------|-------------|---------------|---------------------|-------------------------------|
| **Complete?**    | Yes $^a$           | Yes $^{a,b}$           | No          | No            | Yes $^a$            | Yes $^{a,d}$                  |
| **Time**         | $O(b^d)$          | $O(b^{1+C^*/\epsilon})$ | $O(b^m)$    | $O(b^\ell)$   | $O(b^d)$           | $O(b^{d/2})$                 |
| **Space**        | $O(b^d)$          | $O(b^{1+C^*/\epsilon})$ | $O(bm)$     | $O(b^\ell)$   | $O(bd)$            | $O(b^{d/2})$                 |
| **Optimal?**     | Yes $^c$           | Yes                   | No          | No            | Yes $^c$            | Yes $^{c,d}$                  |
1. **Local Search Methods:**
     - **Hill Climbing:** A greedy approach that moves towards increasing value but can get stuck at local maxima, ridges, or plateaus.
     - **Simulated Annealing:** Allows downhill moves probabilistically to escape local maxima, with the probability decreasing as the "temperature" decreases over time.

4. **Nondeterministic Environments:**
   - Require **AND–OR search trees** to handle contingencies.

5. **Partially Observable Environments:**
   - Use **belief states** to represent the agent’s knowledge about the possible physical states it could be in.

---

### Inference Methods:

**Model Checking:** Enumerates all possible models to verify entailment. Simple and guarantees correctness but computationally expensive ($O(2^n)$) for large KBs.

**Logical Inference:** Uses rules like **Modus Ponens** and **Resolution** to derive new sentences.

**Resolution:** A single, powerful inference rule for CNF sentences.

## **- Boolean/Propositional logic**:

##### Convert Propositional Logic to CNF:
1. **Eliminate Implications (⇒)**:
   - `A ⇒ B` becomes `¬A ∨ B`.
2. **Move NOTs (`¬`) Inside** (De Morgan's Laws):
   - `¬(A ∨ B)` becomes `¬A ∧ ¬B`.
   - `¬(A ∧ B)` becomes `¬A ∨ ¬B`.
3. **Distribute OR (`∨`) Over AND (`∧`)**:
   - `(A ∧ B) ∨ C` becomes `(A ∨ C) ∧ (B ∨ C)`.

#### **Definite Clauses**
- Form: `(A ∧ B ∧ …) ⇒ C` or `¬A ∨ ¬B ∨ … ∨ C`.
- Advantage:
  - Simplifies chaining proofs.
  - Human-readable format.

#### **Horn Clauses:**
- A special subset of CNF with at most one positive literal.
- Used in efficient inference methods (e.g., forward/backward chaining).

## **First order logic**:
- Representation of **objects**, **relations**, and **facts** with **quantifiers** $∀x ∃y$ relation $(x, y)$.

#### **FOL Reduction to Propositional Logic**
1. **Universal Instantiation**:
   - Drop (`∀`) and replace the variable with a specific object.

2. **Existential Instantiation**:
   - Replace (`∃`) with a **Skolem constant** (Just write C).

#### **Resolution in First-Order Logic**
1. **Convert FOL to CNF**

2. **Negate the Query**

3. **Apply Resolution**

4. **Contradiction → Query Proven**.



#### **Example:**
**Knowledge Base (KB):**
- `∀y (∃x owns(y, x) ⇒ hasProperty(y))`
- `owns(joost, house)`

**Query**: Prove `hasProperty(joost)`.

#### **Step-by-Step Solution:**
1. **Convert KB to CNF**:
   - `∀y (∃x owns(y, x) ⇒ hasProperty(y))`
   - Eliminate `⇒`: `∀y (¬∃x owns(y, x) ∨ hasProperty(y))`.
   - Move `¬` inside: `∀y ∀x (¬owns(y, x) ∨ hasProperty(y))`.
   - Skolemize: `¬owns(y, f(y)) ∨ hasProperty(y)` (replace `∃x` with Skolem function `f(y)`).
   - CNF: `¬owns(y, f(y)) ∨ hasProperty(y)`.

2. **Add Query Negation**:
   - Add `¬hasProperty(joost)` to KB.

3. **Resolution**:
   - Unify `y = joost` and resolve:
     - From KB: `¬owns(joost, f(joost)) ∨ hasProperty(joost)`
     - Negation: `¬hasProperty(joost)`
   - Resolving gives `¬owns(joost, f(joost))`.
   - Unify `owns(joost, house)` with `¬owns(joost, f(joost))` (substituting `f(joost) = house`).
   - Contradiction: `owns(joost, house)` and `¬owns(joost, house)`.

4. **Conclusion**:
   - Contradiction proves the query: `hasProperty(joost)` is **true**.

---

**Mutex** in Graphplan: Forward Search with Heuristics $\rightarrow$ identifies **conflicts** between actions or conditions
- Examples of mutexes:  
  - Two actions have contradictory effects.  
  - Two actions need conditions that can’t both be true at the same time. 

### **Agent Program Structure**
1. **Percept Rules:**
   - Triggered when the agent senses the world.
   - Add new facts to the belief base.
   - Example: `at(X) & passage(Y) → +link(X, Y)`

2. **Program Rules:**
   - Define reasoning processes and determine:
     - Which actions are appropriate (intentions).
     - Which goals to pursue (desires).
     - What is true or false (beliefs).

3. **Action Rules:**
   - Define the effects of actions (postconditions).

---

### **Applications of Bayes' Rule**
1. **Bayes' Rule**:
   - $P(A | B) = \frac{P(B | A)P(A)}{P(B)} = \frac{P(a \land b)}{P(b)}$, where $P(B) \neq 0$.

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

- **MDPs**: Framework for sequential decisions in fully observable stochastic settings.
- **POMDPs**: Extensions for partially observable environments.
- **Key Algorithms**:
  - **Value Iteration** and **Policy Iteration** for MDPs.
  - **Belief State-based Approaches** for POMDPs.
- Decision-making balances **risk, reward**, and **information gathering**.

#### **Decision Strategies**:
- **Finite Horizon**: Optimize decisions for a fixed number of steps into the future.
- **Infinite Horizon**: Decisions are made without a fixed endpoint, focusing on long-term rewards.

### **Dynamic Programming (DP)**
- **Goal**: Solve for optimal value function and policy.
- **Approaches**:
  - **Policy Iteration**:
    1. Evaluate policy until convergence.
    2. Improve policy.
  - **Value Iteration**:
    1. Partial policy evaluation (1 sweep).
    2. Policy improvement.
    3. Repeat until convergence.


### **Differences Between Policy Iteration, Value Iteration, and Q-Value Iteration**

| **Aspect**               | **Policy Iteration**                                          | **Value Iteration**                                              | **Q-Value Iteration**                                          |
|--------------------------|-------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------|
| **Goal**                 | Find the **optimal policy** $\pi^*$.                    | Find the **optimal value function** $V^*(s)$.                | Find the **optimal state-action value** $Q^*(s, a)$.      |
| **Representation**       | Explicitly maintains and updates a policy $\pi(a\|s)$.   | Implicitly derives the policy from $V(s)$.                  | Policy is derived implicitly from $Q(s, a)$.              |
| **Evaluation Step**      | Performs **full policy evaluation** (until convergence).    | Performs **partial policy evaluation** (1 iteration per cycle). | Updates $Q(s,a)$ for each state-action pair in one step.  |
| **Improvement Step**     | Improves the policy after full evaluation.                  | Combines policy evaluation and improvement in one equation.     | Directly updates $Q(s,a)$ using Bellman optimality.       |
| **Formula Used**         | Bellman equation for $V(s)$.                            | Bellman optimality equation for $V(s)$.                     | Bellman optimality equation for $Q(s,a)$.                 |
| **Algorithm Complexity** | Higher computational cost due to full evaluation per step.  | Faster convergence due to single-step evaluation.               | Similar to Value Iteration but operates in action space.      |
| **Output**               | Optimal policy $\pi^*(a\|s)$.                            | Optimal value function $V^*(s)$.                            | Optimal state-action value function $Q^*(s,a)$.           |
| **Usage**                | Suitable for small state spaces.                            | Suitable for large state spaces with fewer actions.             | Preferred for environments where actions play a key role.     |

- **Policy Iteration** is slower per iteration but converges in fewer iterations.
- **Value Iteration** is faster per iteration and simpler but requires more iterations to converge.
- **Q-Value Iteration** is more computationally expensive due to operating on state-action pairs.

---

## **SFOL**

#### **Operators in SFOL:**
- **Belief Updates:**
  - `+`: Add fact to the belief base.
  - `-`: Remove fact from the belief base.

- **Goals and Intentions:**
  - `*`: Add goal (adopt).
  - `~`: Remove goal (drop automatically when achieved).
  - `_`: Add intention (action).

---

## **Prolog**

#### **Substitution & Unification**:
- **Unification**: Matches terms in a query with facts/rules. HERE PROLOG RETURN TRUE/FALSE
- **Substitution**: Assigns variables specific values during unification. HERE PROLOG RETURN THE VALUE OF THE VARIABLE
  - Example:
    ```prolog
    ?- parent(joost, X). %Query
    X = sacha ; %Answer
    X = leon. %Answer
    ```

#### **Working with Lists**:
- Lists are structured as `[Head | Tail]`.
- Example:
  ```prolog
  append([], X, X).
  append([H|T], Y, [H|Z]) :- append(T, Y, Z).
  ```
