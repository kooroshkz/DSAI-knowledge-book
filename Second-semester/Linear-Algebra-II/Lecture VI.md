# Orthogonal Sets Projections
#### Orthogonal set
Each pair of $S = \{ u_1, . . . , u_p \}$ is orthogonal ($u \cdot v = 0$)

Hence:
- It's linearly independent
- It is a basis of Span(S)
$w$ is weights in the linear combination

$\underline{w} = c_1 \underline{u}_1 + c_2 \underline{u}_2 + \ldots + c_n \underline{u}_n$

$c_j = \frac{\underline{w} \cdot \underline{u}_j}{||\underline{u}_j||^{2}}$
#### Orthonormal set

Orthogonal set of unit vectors

$S = \{ u_1, . . . , u_p \}$, If W = Span(S), then S is an **orthonormal basis** for
W .
An $m \times n$ matrix $U$ has orthonormal columns if and only if $U^{T} U = I_n$.
$\underline{y} = \underline{\hat y} + \underline{z}$
where $\underline{\hat y} = \alpha \underline{u} $ and $ \underline{u} \cdot \underline{z} = 0$
#### Orthogonal Projection

$L = Span(\underline{u})$ linear transformation $proj_L : R_n \to L$ defined by

$proj_L(\underline{v}) = \frac{\underline{v} \cdot \underline{u}}{||\underline{u}||^{2}} \underline{u} =  \underline{\hat v} $
### The Orthogonal Decomposition Theorem

![Image 3](../../../DSAI-knowledge-book/Files/second-semester/laII/3.jpg)
### The Best Approximation


Let $W$ be a subspace of $\mathbb{R}^n$, $y$ be a vector and $\hat{y}$ orthogonal projection of $y$.

Then $\hat{y}$ is the closest point in $W$ to $y$, that is, 

$
\| y - \hat{y} \| < \| y - v \|$
for all $v$ in $W$ distinct from $\hat{y}$.

<hr>
 Show **$x \to proj_L x$ is a linear transformation** where L = Span{u}

Should satisfies the two properties

$$
\text{proj}_L(x + y) = \frac{(x + y) \cdot u}{u \cdot u}u = \frac{x \cdot u + y \cdot u}{u \cdot u}u = \frac{x \cdot u}{u \cdot u}u + \frac{y \cdot u}{u \cdot u}u = \text{proj}_L(x) + \text{proj}_L(y).
$$

$$
\text{proj}_L(\lambda x) = \frac{(\lambda x) \cdot u}{u \cdot u}u = \frac{\lambda(x \cdot u)}{u \cdot u}u = \lambda \text{proj}_L(x).
$$

<hr>