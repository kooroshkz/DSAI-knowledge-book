## Vector Space

A vector space can be R^2, R^3, or a polynomial.

**Trivial subspace**: It contains only the zero vector of that space.

R^2 is not a subspace of R^3 because subspaces of R^3 should have 3 components like (x, y, z).

To show (denote) subspacity:

- [x1, x2, 0] + [y1, y2, 0] = [x1 + y1, x2 + y2, 0] ∈ W
- c[x1, x2, 0] = [cx1, cx2, 0] ∈ W

## Span{u}

Span{u} is the set of all possible linear combinations of the vector u.

If v = [[1], [2], [3]], then Span{v} = {α⋅v | α ∈ R}.

To show Span{u} in subspace R^n:

- 0 = 0u ∈ span{u}
- mu + nu = (m + n)u ∈ span{u}
- c(mu) = (cm)u ∈ span{u}

W = {[[a - 3b], [2b], [-a + 7b], [b]] ∈ R^4 : a, b ∈ R}

To show that W is a subset of R^4:

[[a - 3b], [2b], [-a + 7b], [b]] = a[[1], [0], [-1], [0]] + b[[-3], [2], [7], [1]] = au + bv ⇒ W = Span{u, v}

## Null space

The null space of an m*n matrix A is the set of all x where Ax = 0 (homogeneous equation).

Nul(A) = {x ∈ R^n | Ax = 0}.

Proof of "The null space of an m*n matrix A is a subspace of R^n":

- A0 = 0 ⇒ 0 ∈ Nul(A)
- u, v ∈ Nul(A), then A*u = 0 = 0*A*v
- A(u + v) = Au + Av = 0 + 0 = 0 ⇒ u + v ∈ Nul(A)
- A(cu) = cAu = c0 = 0 ⇒ cu ∈ Nul(A)

## Column space

The column space of an m × n matrix A is the set of all linear combinations of the columns of A.

Col(A) = Span{a1, ..., an} → R^m.

Note that Col(A) is the range of the linear transformation x → Ax.

Col(A) = Range(x → Ax) = {b ∈ R^m | There exists x ∈ R^m such that Ax = b}.

The column space of an m × n matrix A is a subspace of R^m since span is a subspace.

In a linear transformation:

- ker(T) = Nul(A)
- Im(T) = Col(A)

T is one-to-one if and only if ker(T) = {0}.

T is onto R^m if and only if Im(T) = R^m.

Linear transformation T from a vector space V to a vector space W, denoted T: V → W:

- The kernel of T is ker(T) = {v ∈ V | T(v) = 0}.
- The range (image) of T is Im(T) = {w ∈ W | w = T(v) for some v ∈ V}.

For example, in the linear transformation D: C^1[a, b] → C[a, b] (derivative):

- ker(D) = {f ∈ C'[a, b] | f' = 0}
- Im(D) = C[a, b]

| Name    | Notation   | Info                                          | Example                                   |
|---------|------------|-----------------------------------------------|-------------------------------------------|
| Span    | Span{u}    | set of all possible linear combinations of u  | if v = [[1],[2],[3]] -> Span{u}={αv : α ∈ ℝ} |
| Null    | Nul(A)     | set of all x where Ax=0                       |                                           |
| Column  | Col(A)     | set of all linear combinations of the columns of A | x = [x1,x2,x3] Col(x) = {x1,x2,x3}         |
| Kernel  | Ker(T)     | set of all vectors that get mapped to the zero vector under T | ker(T) = {v ∈ V I T(v)=0}              |
| Image (Range) | Im(T) | set of all possible outputs obtained by applying T to every vector in its domain | Im(T) = {w ∈ W I T(v) = w for some v ∈ V} |
