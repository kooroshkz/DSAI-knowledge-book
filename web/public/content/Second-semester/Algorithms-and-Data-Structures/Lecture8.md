## Topological sorting 
A ordering of vertices in a directed acyclic graph 
Time Complexity: $O(V+E)$
<img src="../../Files/second-semester/dsa/ts.jpg" style="height: 400px">
- Make inverted adjacency list
- Look for a node without entity like C1
- Write C1 as a first item of list and cross it from other lists
- Repeat the with C2 then others to reach
```py
[C1,C2,C3,C4,C5]
```
### Closest Pair of Points time complexity ($\sqrt{a^2 + b^2} $)
$ = O(n^2) $
#### Closest Pair Problem:

- Problem: Given n points, find the closest pair of points.
- Brute Force: Compare all pairs, complexity $O(n^2)$
- Divide and Conquer:  Divide points, solve recursively, merge results, complexity $O(n\log{⁡n}). $
```py
def merge_halves(leftPx, leftPy, rightPx, rightPy, dleft, dright):
    # Determine the smallest distance in two halves.
    d = min(dleft, dright)
    x_mid = leftPx[-1]  # or rightPx[0] (does not matter)
    left_within, right_within = [], []

    # Collect the points that are within d-distance from middle
    for l in range(len(leftPx)):
        if abs(leftPx[l] - x_mid) < d:
            left_within.append((leftPx[l], leftPy[l]))

    for r in range(len(rightPx)):
        if abs(rightPx[r] - x_mid) < d:
            right_within.append((rightPx[r], rightPy[r]))

    # Compare the points to the left and right of middle
    for lpair in left_within:
        for rpair in right_within:
            d = min(d, distance(lpair, rpair))

    return d

def closest_pair(Px, Py):
    # Base cases
    if len(Px) == 1:
        return float('inf')
    elif len(Px) == 2:
        return distance((Px[0], Py[0]), (Px[1], Py[1]))

    # Divide
    mid = len(Px) // 2  # Integer division
    leftPx, leftPy = Px[:mid], Py[:mid]
    rightPx, rightPy = Px[mid:], Py[mid:]

    # Solve partitions
    dleft = closest_pair(leftPx, leftPy)
    dright = closest_pair(rightPx, rightPy)

    return merge_halves(leftPx, leftPy, rightPx, rightPy, dleft, dright)

# Note: Ensure the `distance` function is defined before using it.

#### Binary Search:

- Problem: Search for a value in a sorted array.
- Solution: Divide array, search in subarray, complexity O(log⁡n).
### Master Theorem

The Master Theorem provides a straightforward way to determine the time complexity of recurrence relations that are common in divide-and-conquer algorithms. It applies to recurrences of the form:

$ T(n) = aT\left(\frac{n}{b}\right) + f(n) $

where:
- $ n $ is the size of the problem.
- $ a \geq 1 $ is the number of subproblems in the recurrence.
- $ b > 1 $ is the factor by which the subproblem size is reduced in each recursive call.
- $ f(n) $ is the cost outside the recursive calls, also known as the "combine" cost. In case of using the formula below, $d$ is the exponent in the polynomial term that represents the cost outside the recursive calls.

If $T(n) = aT\left(\left\lceil \frac{n}{b} \right\rceil\right) + O(n^d)$ (for constants $a > 0$, $b > 1$, $d \geq 0$), then:

$$
T(n) = 
\begin{cases} 
O(n^d) & \text{if } d > \log_b a \\
O(n^d \log n) & \text{if } d = \log_b a \\
O(n^{\log_b a}) & \text{if } d < \log_b a 
\end{cases}
$$
