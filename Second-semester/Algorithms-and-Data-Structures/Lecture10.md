#### Example Problems

##### Knapsack Problem
- **Problem:** Given items with weights and values, and a knapsack with a weight capacity, find the most valuable subset of items that fits in the knapsack.
- **Subproblem:** Decide to include or exclude an item.
- **Recursive Relation:**
  $$
  F(i, j) = 
  \begin{cases}
  \max(F(i-1, j), v_i + F(i-1, j-w_i)) & \text{if } j \geq w_i \\
  F(i-1, j) & \text{if } j < w_i
  \end{cases}
  $$
- **Base Cases:** $F(i, 0) = 0$, $F(0, j) = 0$ for $i, j \geq 0$

##### Bus-Trip Problem
- **Problem:** Given a matrix of prices for traveling between cities, find the cheapest itinerary from city 0 to city $n$.
- **Subproblem:** Choose a destination city.
- **Recursive Relation:**
  $$
  F(n) = 
  \begin{cases}
  0 & \text{if } n = 0 \\
  \min_{0 \leq i < n} (F(i) + \text{price}(i, n)) & \text{if } n \neq 0
  \end{cases}
  $$

##### Subset Sum Problem
- **Problem:** Given a set of positive numbers and a target sum $d$, determine if there is a subset with sum equal to $d$.
- **Subproblem:** Include or exclude an element.
- **Recursive Relation:**
  $$
  F(i, j) = 
  \begin{cases}
  \text{True} & \text{if } j = 0 \\
  \text{False} & \text{if } j < 0 \text{ or } i = 0 \\
  F(i-1, j) \lor F(i-1, j-s_i) & \text{otherwise}
  \end{cases}
  $$

##### Sawmill Problem
- **Problem:** Minimize the cost of sawing a tree trunk into specified lengths, with a cost equal to the length of the trunk at each cut.
- **Subproblem:** Determine where to make the cut.
- **Recursive Relation:**
  $$
  F(i, j) = 
  \begin{cases}
  L(i, j) + \min_{i \leq k < j} (F(i, k) + F(k+1, j)) & \text{if } i < j \\
  0 & \text{if } i = j
  \end{cases}
  $$
