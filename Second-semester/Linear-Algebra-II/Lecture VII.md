# The Gram-Schmidt Process and Least-Squares Problems
## The Gram-Schmidt Process


Given a basis $\{x_1, \ldots, x_p\}$ for a non-zero subspace $W$ of $\mathbb{R}^n$, define:
\begin{align*}
v_1 &= x_1 \\
v_2 &= x_2 - \frac{x_2 \cdot v_1}{v_1 \cdot v_1}v_1 \\
&\vdots \\
v_p &= x_p - \frac{x_p \cdot v_1}{v_1 \cdot v_1}v_1 - \frac{x_p \cdot v_2}{v_2 \cdot v_2}v_2 - \ldots - \frac{x_p \cdot v_{p-1}}{v_{p-1} \cdot v_{p-1}}v_{p-1}.
\end{align*}

Then $\{\frac{v_1}{||v_1||}, \ldots, \frac{v_p}{||v_p||}\}$ is an orthogonal basis for $W$, and, in addition,

**Note** : Each least-squares solution of $Ax = b$ satisfies the normal equations.

$ ( A^{T} A ) \underline{x} = ( A^{T} \underline{b} )$

So by $A $ and $ B$ we can find $\underline{\hat x} = (A^{T} A)^{-1} A^{T} \underline{b}$
**Head Up**:

If $\alpha^{-1}$ was hard to calculate we can convert a normal equation to augmented matrix like:

$ ( A^{T} A ) \underline{x} = ( A^{T} \underline{b} )$ will be [  $ ( A^{T} A ) | ( A^{T} \underline{b} )$   ] $\to RREF$ then $\underline{\hat x} =$ right most column  if it was consistent.
<hr>
## least-squares solution

$\underline{\hat x}$ in $R^{n}$ where $A\underline{x} = \underline{b}$ where $b$ is in $R^{m}$ of A $M \times N$ matrix

$|| \underline{b} - A\underline{\hat x} || \le || \underline{b} - A\underline{x} ||$
## least-squares Error

least-squares Error $= || \underline{b} - A\underline{\hat x} ||$ where $\underline{b} - A\underline{\hat x}$ is distance