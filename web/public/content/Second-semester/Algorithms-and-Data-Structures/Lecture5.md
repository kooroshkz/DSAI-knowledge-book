### Brute Force:
Often has high computational complexity and not efficient for large inputs.
Complexity examples:
- Selection Sort: $O(n^2)$
- Pattern Matching: $O(n⋅m)$
#### Exhaustive search is currently the only known solution for:
- Traveling Salesman Problem (TSP)
- Knapsack Problem

NP-hard, meaning no known polynomial-time algorithms can solve them.
### Convex Hull:

- Definition: Smallest convex set containing a given set of points.
- Algorithm: Check if all points are on the same side of each line segment formed by the points.
- Complexity: $O(n^3)$
### Hamiltonian circuitis
A circuit that visits every vertex, except for the starting vertex, exactly once.
Time complexity $ O(n!) $