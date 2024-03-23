# Linear Algebra for Computer Scientists II


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
