### Solving Problems by Searching

#### **Problem Solving Steps**(define):
- States
- Initial State
- Actions
- Transition Model
- Goal Test
- Path Cost (For Real-world problems and not Toy problems)


- **Frontier**: Set of leaf nodes available for expansion.

#### **Graph vs. Tree Search**
- **Tree Search**: Considers all paths, including loops.
- **Graph Search**: Avoids revisiting states by using an explored set.
### Real-world problems solved by AI

1. **VLSI Layout Problem**:
   - **Definition**: A problem in designing Very-Large-Scale Integration (VLSI) chips, where millions of components and their connections must be arranged.
   - **Goals**: Minimize chip area, delay, stray capacitances (unwanted effects caused by proximity of components) and manufacturing yield (efficiency in production).
   - **Channel Routing**(Challenge): Route the connecting wires through the gaps between cells made by the search and placement algorithm (a form of pathfinding)
   
2. **The traveling salesperson problem (TSP)**:
   - **Definition**: A problem where a salesperson must visit a set of cities exactly once and return to the starting city, minimizing the total distance traveled.

3. **Automatic Assembly Sequencing**:
   - **Definition**: The process of determining the order to assemble parts of an object.
   
4. **Protein Design**:
   - **Definition**: Finding a sequence of amino acids that will fold into a specific 3D protein with desired properties (e.g., curing a disease)s imilar to the assembly problem, as it requires generating sequences that result in functional, stable protein structures.

5. **Touring Problems**:
   - **Definition**: Problems where an agent must visit a set of locations, such as the TSP, the Traveling Repairman Problem (TRP), and the Traveling Tournament Problem (TTP).
- Search algorithms are judged on the basis of completeness, optimality, time complexity, and space complexity. Complexity depends on $b$, the branching factor in the state space, and $d$, the depth of the shallowest solution.
- The **branching factor $(b)$** in a search algorithm refers to the **average number of child nodes**.
---

- **Uninformed Search**: No additional information about states beyond the problem definition.
- **Informed Search**: Uses heuristics to estimate the quality of non-goal states (covered in Section 3.5).

## Uninformed Search Methods

Uninformed search methods have access only to the problem definition. The basic algorithms are as follows:

- **Breadth-first search**: Expands the shallowest nodes first; it is complete, optimal for unit step costs, but has exponential space complexity.
- **Uniform-cost search**: Expands the node with the lowest path cost, $g(n)$, and is optimal for general step costs.
- **Depth-first search**: Expands the deepest unexpanded node first. It is neither complete nor optimal, but has linear space complexity. Depth-limited search adds a depth bound.
- **Iterative deepening search**: Calls depth-first search with increasing depth limits until a goal is found. It is complete, optimal for unit step costs, has time complexity comparable to breadth-first search, and has linear space complexity.
- **Bidirectional search**: Can enormously reduce time complexity, but it is not always applicable and may require too much space.

## Informed Search Methods

Informed search methods may have access to a heuristic function $h(n)$ that estimates the cost of a solution from $n$.

- **Best-first search**: A generic algorithm that selects a node for expansion according to an evaluation function.
- **Greedy best-first search**: Expands nodes with minimal $h(n)$. It is not optimal but is often efficient.
- **A\* search**: Expands nodes with minimal $f(n) = g(n) + h(n)$. 
  - A\* is complete and optimal, provided that $h(n)$ is admissible (for Tree-Search) or consistent (for Graph-Search). 
  - However, the space complexity of A\* is still prohibitive.
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
- **Consistent**: Satisfies the triangle inequality ($ h(n) \leq c(n, a, n') + h(n') $).