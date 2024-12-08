# Linear Algebra II
##  Linear Independence, Bases, Coordinationo systems
In Vectors $\{v_1, \ldots, v_p\} \rightarrow \mathbb{R}^n$

- If $x_1v_1 + x_2v_2 + \cdots + x_pv_p = \underline{0}$ have  **trivial solution** it's **linearly independent**

- If $x_1v_1 + x_2v_2 + \cdots + x_pv_p = \underline{0}$ such $c_1, c_2, \ldots, c_p \neq 0$ it's **linearly dependent**

#### linearly independency of Polynomials

If for $P_1(x), P_2(x), P_3(x)$ you can find a relation like $P_1(x) = 1/5 (P_2(x) - P_3(x))$ then {$P_1(x), P_2(x), P_3(x)$} is **linearly dependent**
<hr>

## Bases of vector spaces

H is a subspace of V vector space. 
An indexed set of vectors $B = \{b_1, \ldots, b_p\}$ in $V$ is a basis for the subspace $H$ if:
1. $B$ is a linearly independent set
2. $B$ spans $H$, that is, $H = \text{Span}\{b_1, \ldots, b_p\}$.

Example:
Bases of $\mathbb{R}^3$ is B = {$\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} , \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} , \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$}

and Bases of $P_n = \{ a_0 + a_1t + \cdots + a_nt^n : a_0, \ldots, a_n \in \mathbb{R} \}$
is B = { 1, $t$, $\mathbb{t}^2$, $\mathbb{t}^3$ }
### Head up!

Nul(A) = Span{$\begin{bmatrix} 2 \\ 1 \\ 0 \\ 0 \end{bmatrix} , \begin{bmatrix} -1 \\ 0 \\ -2 \\ 1 \end{bmatrix}$} where $x_2,x_4 = 0$ can be a combination on answers for a homogeneous system.

Then note <ins>x</ins>= only if $x_2,x_4 = 0$ so the Nul(A) is independant
<hr>

## Coordinate systems

Coordinates of <ins>x</ins> relative to $B = \{b_1, \ldots, b_p\}$ are the weights $c_1, c_2, ...$ such that:

$\underline{x} = c_1b_1+...+c_nb_n$

Examples:

- B = {1, $t, ... ,\mathbb{t}^3$} and  $P_1(t) = 1 - t ,  P_2(t) = 1 + t , P_3(t) = t^3 - \frac{1}{2}t^2 + 1$

$    P_1(t) = 1 \cdot 1 + (-1) \cdot t + 0 \cdot t^2 + 0 \cdot t^3$
$    \text{So, the coordinate vector is } \begin{bmatrix} 1 \\ -1 \\ 0 \\ 0 \end{bmatrix}$
- $\text{Let } \mathbf{b}_1 = 
\begin{pmatrix}
1 \\
1
\end{pmatrix}
\text{ and } \mathbf{b}_2 = 
\begin{pmatrix}
4 \\
5
\end{pmatrix},
\text{ and let } B = \{\mathbf{b}_1, \mathbf{b}_2\}. 
\text{ Let }
\mathbf{x} = 
\begin{pmatrix}
5 \\
1
\end{pmatrix}
\text{ (relative to the standard basis in } \mathbb{R}^2\text{). Find } [\mathbf{x}]_B.
$
$\begin{bmatrix}
1 & 4 & | & -5 \\
1 & 5 & | & 1
\end{bmatrix}; RREF = \begin{bmatrix}
0 & 0 & | & -29 \\
0 & 0 & | & 6
\end{bmatrix}; so  [\mathbf{x}]_B = \begin{bmatrix}
-29 \\
6 
\end{bmatrix}$

## Change of coordinates matrix
Let $B = \{b_1, \ldots, b_n\} then \quad P_B = [b_1, \ldots, b_n]$ 

<ins>x</ins> = $P_B[\underline{x}]_B$

where $P_B$ is te change of coordinates matrix
If transformed vector asked we should calculate <ins>x</ins> by $P_B \cdot [\underline{x}]_B$ where $[\underline{x}]_B$ is **Coordinate vector** (transformation mapper) and <ins>x</ins> is relative to given biasis $B$
### Coordination mapping
$ T_B : \mathbb{R}^n \rightarrow \mathbb{R}^n : x \rightarrow [x]_B $,

 Note that $ T_B $ is one-to-one and onto.
While we find the RREF form of $[P]_B$ if there were a pivot in every column of $[P]_B$, then $[P]_B$ would be linearliy independent and hence invertible.