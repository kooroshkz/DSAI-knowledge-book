## Linera Algebra II
### Lecture 1
| Name           | Notation   | Info                                                                  | Example                                   |
|----------------|------------|-----------------------------------------------------------------------|-------------------------------------------|
| Span           | Span{u}    | Set of all possible linear combinations of `u`                       | If $v = \begin{bmatrix}V_1\\V_2\\V_3\end{bmatrix}$, then Span{u} = {αv : α ∈ ℝ} |
| Null           | Nul(A)     | Set of all `x` where `Ax = 0`                                         |                                           |
| Column         | Col(A)     | Set of all linear combinations of the columns of `A`                  | If $A$ is $RREF = B$ and $b_1,b_3$ are pivot column, then Col(A) = {$a_1, a_3$}         |
| Kernel  | Ker(T)     | set of all vectors that get mapped to the zero vector under T | ker(T) = {v ∈ V I T(v)=0}              |
| Image (Range) | Im(T) | set of all possible outputs obtained by applying T to every vector in its domain | Im(T) = {w ∈ W I T(v) = w for some v ∈ V} |

## Vector and Subspace

A vector space can be R^2, R^3, or a polynomial.

**Trivial subspace** = {0}: It contains only the zero vector of that space.

R^2 is not a subspace of R^3 because subspaces of R^3 should have 3 components like (x, y, z).

**Definition of Subspace** (Prove subspace V ⊆ W):
- Zero vector v ∈ W.
- If u, v ∈ W, then u + v ∈ W.
- If u ∈ W and c ∈ R, then c * u ∈ W.
<hr>

## Span{u}

Span{u} is the set of all possible linear combinations of the vector u.

If $v = \begin{bmatrix}V_1\\V_2\\V_3\end{bmatrix}$, then Span{u} = {αv : α ∈ ℝ}

To show Span{u} in subspace R^n:

- 0 = 0u ∈ span{u}
- mu + nu = (m + n)u ∈ span{u}
- c(mu) = (cm)u ∈ span{u}

**Prove I:**

W = $\left\{ \begin{bmatrix} a - 3b \\ 2b \\ -a + 7b \\ b \end{bmatrix} \in \mathbb{R}^4 : a, b \in \mathbb{R} \right\}$

To show that W is a subset of $\mathbb{R}^4$:

$\begin{bmatrix} a - 3b \\ 2b \\ -a + 7b \\ b \end{bmatrix} = a \begin{bmatrix} 1 \\ 0 \\ -1 \\ 0 \end{bmatrix} + b \begin{bmatrix} -3 \\ 2 \\ 7 \\ 1 \end{bmatrix} = au + bv \Rightarrow W = \text{Span}\{u, v\}$

**Prove II:**

If $v_1, v_2,... \in$ Vector space V$ show span{$v_1, v_2,..$.} is subspace of V

assume $W$ = span{$v_1, v_2,..$.}

- <ins>0</ins> = <ins>0</ins>$v_1$ + <ins>0</ins>$v_2$ $\in W$
- $a_1.\underline{v_1}$ + $a_2.\underline{v_2}$ + $b_1.\underline{v_1}$ + $b_2.\underline{v_2}$ = ($a_1 + b_1$)$\underline{v_1}$ $\in W$
- c($a_1.\underline{v_1}$ + $a_2.\underline{v_2}$) = $(c a_1 )\underline{v_1}$ + $(c a_2 )\underline{v_2}$ $\in W$

**Head up**

W = $\left\{ \begin{bmatrix} a + b \\ b \\ 1 \end{bmatrix} \in \mathbb{R}^3 , a, b \in \mathbb{R} \right\}$

$W$ is **not** in subspace $\mathbb{R}^3$ due:

$\begin{bmatrix} a_1 + b_1 \\ b_1 \\ 1 \end{bmatrix}$ + $\begin{bmatrix} a_2 + b_2 \\ b_2 \\ 1 \end{bmatrix}$ = $\begin{bmatrix} a_1 + b_1 + a_2 + b_2 \\ b_1 + b_2 \\ 2 \end{bmatrix}$  then $2 \neq 1$

also it doesnt contain zero vector for any $a, b$

<hr>

## Null space

The null space of an m*n matrix A is the set of all x where Ax = 0 (homogeneous equation).

$\text{Nul}(A)$ = {x ∈ R^n | Ax = 0}.

Proof of "The null space of an m*n matrix A is a subspace of R^n":

- $ A0 = 0 \Rightarrow 0 \in \text{Nul}(A) $, if $ u, v \in \text{Nul}(A) $, then $ Au = 0 = Av $
- $ A(u + v) = Au + Av = 0 + 0 = 0 \Rightarrow u + v \in \text{Nul}(A) $
- $ A(cu) = cAu = c0 = 0 \Rightarrow cu \in \text{Nul}(A) $
### Generating set of Nul(A):

$A = \begin{bmatrix}
-3 & 6 & -1 & 1 \\
1 & -2 & 2 & 3 \\
2 & -4 & 5 & 8
\end{bmatrix}$

$RREF = \begin{bmatrix}
1 & -2 & 0 & -1 \\
0 & 0 & 1 & 2 \\
0 & 0 & 0 & 0
\end{bmatrix}$

$Nul(A) = \{ \begin{bmatrix}2x_2 + x_4 \\x_2 \\-2x_4 \\ x_4\end{bmatrix} | x_2,x_4 \in R\}$

$Span(A) = \{ \begin{bmatrix}2 \\ 1 \\ 0 \\ 0 \end{bmatrix},\begin{bmatrix}1 \\ 0 \\ -2 \\ 1 \end{bmatrix} \} $

<hr>

## Column space

The column space of an m × n matrix A is the set of all linear combinations of the columns of A.

Col(A) = Span{a1, ..., an} $→ R^{m}$.

Note that Col(A) is the range of the linear transformation $x \to Ax$.

Col(A) = Range($Ax = b$) = {b ∈ $R^{m}$ | There exists x ∈ $R^{m}$ such that $Ax = b$}.

The column space of an m × n matrix A is a subspace of R^m since span is a subspace.
<hr>

## In Linear Transformation

In a linear transformation:

- $ \text{ker}(T) = \text{Nul}(A) $
- $ \text{Im}(T) = \text{Col}(A) $ 

$ T $ is **one-to-one** if and only if $ \text{ker}(T) = \{0\} $.

$ T $ is **onto** $ \mathbb{R}^m $ if and only if $ \text{Im}(T) = \mathbb{R}^m $ if $T: \mathbb{R}^n \to \mathbb{R}^m$

Linear transformation $ T $ from a vector space $ V $ to a vector space $ W $, denoted $ T: V \rightarrow W $:

- The kernel of $ T $ is $ \text{ker}(T) = \{v \in V | T(v) = 0\} $.
- The range (image) of $ T $ is $ \text{Im}(T) = \{w \in W | w = T(v) \text{ for some } v \in V\} $.

