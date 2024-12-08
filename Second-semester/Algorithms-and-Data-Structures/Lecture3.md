# Time Complexity

## Big O notation (O)
##### Worst Case Scenario
Big O notation describes the upper limit or worst-case scenario of an algorithm's performance. When we say $f(n) = O(g(n))$, it means that the function f grows no faster than g, up to a constant factor.

**Note**: $ n!∈O(n^n) $

## Theta notation (Θ)
##### Average or typical case
Theta notation gives a tight bound on the growth rate of a function. If $f(n) = \Theta(g(n))$, it means that the function f grows exactly at the same rate as g, within constant factors.

## Omega notation (Ω)
##### Best-case scenario
Omega notation represents the lower bound of an algorithm's performance. If $f(n) = \Omega(g(n))$, it means that the function f grows at least as fast as g, up to a constant factor.

### Asymptotic complexity
Analyzes the complexity of algorithms when the inputs are really large (n goes to
infinity)
- $0 < \lim_{n \to \infty} \frac{f(n)}{g(n)} < \infty \quad \Longleftrightarrow \quad f \in \Theta(g)$
- $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0 \quad \Longrightarrow \quad f \in O(g), \text{ but } f \not\in \Theta(g)$
- $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty \quad \Longleftrightarrow \quad g \in O(f), \text{ but } g \not\in \Theta(f)$
Complexity classes


<img src="../../Files/second-semester/dsa/3.jpg" style="height: 300px">
In binary tree (search) we have $O(\log{n})$ because by each step the half of search path will be ignored till

In heap search and Merge sort we have $O(n \log{n})$