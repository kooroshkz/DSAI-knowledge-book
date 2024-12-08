# Vectors

## Definition
A column vector (or just vector for short) is a matrix in $\mathbf{R^m}$ with dimensions $m\times1$. Two vectors are equal if their entries are equal to each other.  
A sum of vectors gives you a new vector with each row being the sum of the entries in the same row, this is due to the nature of matrix addition.  
Scalar multiplication is multiplying each entry with the scalar.

## Operations and properties
The operations that can be done on matrices are similar to those that can be done on normal but there are some key differences at times.
- Order does not matter in addition and subtraction, however the dimensions need to be exactly equal for all terms added or subtracted.  
$\underline{u}+\underline{v} = \underline{v}+\underline{u}$
- Addition (and subtraction) is associative.  
$\underline{u}+(\underline{v}+\underline{w}) = (\underline{u}+\underline{v})+\underline{w}$
- Addition with 0 results with the original matrix.  
$\underline{u}+0 = \underline{u}$
- Addition of same matrix with opposite signs gives 0.  
$\underline{u} + (-\underline{u}) = 0$
- Scalars are distributive over addition.  
$c(\underline{u}+\underline{v}) = c\underline{u} + c\underline{v}$
- Scalar multiplication is associative.  
$c(d\underline{u}) = (cd)\underline{u}$
- Scalar 1 multiplied by any vector is the original vector.  
$1\underline{u} = \underline{u}$

## Linear combinations
Linear combination is the sum of multiple vectors multiplied by multiple scalars such that
$$\underline{v}_1, \underline{v}_2, ..., \underline{v}_n \in \mathbf{R}^m \text{ and } c_1, c_2, ..., c_n \in \mathbf{R}$$
give us the vector
$$\underline{u} = \Sigma^{n}_{i=1} c_1\underline{v}_1 + c_2\underline{v}_2 + ... + c_n\underline{v}_n$$
Vector $\underline{u}$ is called the linear combination of $\underline{v}_1, \underline{v}_2, ..., \underline{v}_n$ and weights $c_1, c_2, ..., c_n$.

## Span
Geometric description of sums. The sum of $\underline{u}$ and $\underline{v}$ in $\mathbf{R^2}$ is represented as the point in plane that is the fourth corner in a parallelogram whose other corners are at 0-origin, $\underline{u}$, and $\underline{v}$.[^1]  
The span is all possible linear combinations (scalars basically), the span of a single vector is the infinite extension of the vector (an infinite line), the span of two vectors is the infinite expansion of the parallelogram created by the sum of the two vectors (a 2D-plane) and so on.[^2]  
The span can be defined as
$$Span\left\lbrace v_1, v_2, ..., v_n\right\rbrace = \left\lbrace  c_1v1 + c_2v_2 + ... + c_nv_n | c_1, c_2, ..., c_n \in \mathbf{R} \right\rbrace $$  
To find if a vector is in the span, create a linear combination matrix and try to solve it. If the system is inconsistent then the vector does not exist in the span.

# Matrix multiplication

## A\underline{x} = \underline{b}
To be able to calculate the product of two matrices, the number of columns in the first matrix must be equal to the number of rows in the second matrix.  
If A is matrix with dimensions $m\times n$ such that $a_1, a_2, ..., a_n \in \mathbf{R^m}$ and \underline{x} is a matrix with n columns such that \underline{x} $\in \mathbf{R^n}$, then the product of A and \underline{x} is
$$A\underline{x} 
= \begin{bmatrix}
	\underline{a}_1 & \underline{a}_2 & \dots &\underline{a}_n
\end{bmatrix}
\begin{bmatrix}
	x_1\\
	x_2\\
	\vdots\\
	x_n\\
\end{bmatrix}
= \underline{a}_1x_1 + \underline{a}_2x_2 + \dots + \underline{a}_nx_n$$
The resulting matrix will have as many rows as the rows in the first matrix and the number of columns will be as many as the number of columns in the second matrix. Basically dimensions $(a \times b) \times (b \times c) = (a \times c)$  
For example if matrix A has dimensions $3\times2$ and matrix B has dimensions $2\times3$, the resulting matrix will have dimensions $2\times3$.
$$A = \begin{bmatrix}
	1 & 2 \\
	3 & 4 \\
	5 & 6
\end{bmatrix},
B = \begin{bmatrix}
1.1 & 1.2 & 1.3 \\
2.1 & 2.2 & 2.3
\end{bmatrix}$$
$$A \times B = \begin{bmatrix}
	(1\times1.1 + 2\times2.1) & (1\times1.2 + 2\times2.2) & (1\times1.3 + 2\times2.3) \\
	(3\times1.1 + 4\times2.1) & (3\times1.2 + 4\times2.2) & (3\times1.3 + 4\times2.3) \\
	(5\times1.1 + 6\times2.1) & (5\times1.2 + 6\times2.2) & (5\times1.3 + 6\times2.3)
\end{bmatrix}$$  
$$A \times B = \begin{bmatrix}
	5.3 & 5.6 & 5.9 \\
	11.7 & 12.4 & 13.1 \\
	18.1 & 19.2 & 20.3
\end{bmatrix}$$

A linear system is consistent if and only if there is a pivot position on every row in the coefficient matrix A.

## Dot product
The dot product is the product of two vectors $x,y \in \mathbf{R^n}$ with the first one being transposed (rows become columns).
$$\underline{y}\cdot\underline{x}
= \underline{y}^{T}\times\underline{x}
=\begin{bmatrix}
	y_1  &  \dots & y_n
\end{bmatrix}
\begin{bmatrix}
	x_1\\
	\vdots\\
	x_n
\end{bmatrix}
= \Sigma^{n}_{i=1}y_ix_i = y_1x_1 + \dots + y_nx_n \in \mathbf{R^1}$$
The dot product of two vectors is always a number.

# Solution sets

## Homogeneous linear systems
A system of equations that has a coefficient matrix A, the right hand-side of the system consists of only zeros (zero vector).  
A homogeneous system always has a solution. If the A matrix is multiplied by the zero vector, the solution is called a trivial solution.  
There is a nontrivial solution if and only if there is at least one free variable.  
To find if there is a nontrivial solution, preform row reduction and find the row echelon form, if there is no pivot point at for at least one coefficient row it has a nontrivial solution. [^3]

## Parametric vector form
After confirming it has a nontrivial, find the reduced echelon form of the matrix, solve for the coefficients using the free variable, then factor out the free variable.
<hr>
# Algorithm for writing a solution set
- Turn system into matrix.
- Check if the system is consistent.
- Begin by row reducing to get to reduced row echelon form.
- Express the basic variables in terms of the free ones (return to matrix).
- Write a typical solution equation.
- Decompose.

Typical solution equation is setting a vector equal to all variables and having it equal to their expression system of equations.

## Linear independence
An indexed set of vectors is linearly independent if the vector equal is equal to 0 has only one trivial solution.
If a weighted sum of vectors is equal to 0, it is called linearly dependent.
If the set of vectors has a homogeneous solution, it only has a trivial solution (if and only if apparently).
It is linearly dependent if it has a non-homogeneous solution.
If the number of columns is larger than the number of rows, it is linearly dependent.
If one of the vectors in the list of vectors is a zero vector, then the set is a linearly dependent set.

## Application of linear systems
### Input-Output model in economics
Introduced in 1949 in Harvard, winning the creator a Nobel prize in economics.
An economy can be divided into multiple sectors that interact with each other, the theory says that there is always a solution which has the meaning of equilibrium prices.
It is one of the first examples of mathematical modeling (using computers), being the first model that consisted of 500 equations.

<hr>
# Transformations
A transformation (also known as mapping or function) is a rule that assigns each vector $\underline{x}$ in domain $\mathbf{R}^n$ a vector in the co-domain $\mathbf{R}^m$ (this is called the image).

## Matrix transformation
A matrix transformation is a matrix multiplication. There exists a matrix A of size $m \times n$ such that $T(x) = Ax$ for all $x \in R$. Remember what are the dimensions of the matrix we used for the matrix transformation. For T, the domain is $\mathbf{R}^n$, co-domain is $\mathbf{R}^m$, range is the subset of $\mathbf{R}^m$. To check if vector c is in the range of T, we have to check if there exists an x vector such that T(x) = Ax = c. If the solution to this is inconsistent (due to having a pivot position in the rightmost column of the augmented matrix), then there is no vector x that satisfies the condition that T(x) = c. If there are no free variables in the consistent solution matrix, then the solution is unique. Matrix transformations can be thought of as linear systems and vice versa.

## Linear transformations
They are transformations that satisfy the conditions:
- $T(\underline{u}+\underline{v}) = T(\underline{u}) + T(\underline{v})$ for all $\underline{u},\underline{v} \in \mathbf{R}^n$
- $T(c\underline{u}) = cT(\underline{u})$ for all $\underline{u} \in \mathbf{R}^n$ and $c \in \mathbf{R}$

All matrix transformations are linear transformations. The conditions can be combined to $T(c\underline{u} + d\underline{v}) = cT(\underline{u}) + dT(\underline{v})$ for all $\underline{u},\underline{v} \in \mathbf{R}^n$ and $c,d \in \mathbf{R}$.

### Standard basis
The standard basis of $\mathbf{R}^n$ is the collection of n vectors such that every vector x in $\mathbf{R}^n$ can be written uniquely as a linear combination of the standard basis vectors.

For a linear transformation, there exists a unique matrix A called the standard matrix of T such that T(x) = Ax for all x in $\mathbf{R}^n$. In fact, A is the matrix of size $m \times n$ whose j column is the vector $T(e_j)$ in $\mathbf{R}^m$.

## Types of transformation
### Onto
A transformation is called onto if each vector in the co-domain is the image of at least one vector in the domain. Equivalently, the range of T is all of $\mathbf{R}^m$. (Existence)

### One-to-one
A transformation is called one-to-one if each vector in the co-domain $\mathbf{R}^m$ is the image of at most one vector in $\mathbf{R}^n$. Equivalently, T(x) = b admits a unique solution or none (uniqueness).

The span is equal to the number of row pivot positions. The transformation is never one-to-one if there are free variables in a solution (columns of A are linearly independent). The transformation is onto if the A matrix spans the co-domain.

A linear transformation is one-to-one if and only if the equation T(x) = 0 has only the trivial solution (as each solution can have at most one solution).