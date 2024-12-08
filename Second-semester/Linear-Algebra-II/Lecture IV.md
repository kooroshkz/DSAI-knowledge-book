# Eigenvectors and Eigenvalues, The Characteristic Equation 
### Eigenvector

Find a non-zero vector $\underline{x}$ such that $A\underline{x} = \lambda\underline{x}$ for some scalar $\lambda \in \mathbb{R}$ where $\lambda$ is called **eigenvalue**.

To find eignvector from eignvalue:
- $A\underline{x} = \lambda\underline{x}$ so $A\underline{x} - \lambda\underline{x} = 0$
- $A - \lambda I$ RREF parametric $\underline{x}$ can show eignvector
### Characteristic equation

det(A - $\lambda I_n$) = 0

Where det(A - $\lambda I_n$) is Characteristic polynomial
Multiplicity: Times a characteristic equation has a root in a polynomial
- det(A - I3) = $(λ - 5)^{3}$ (λ - 3)
λ = 5 has Multiplicity of 3

**Head up**:

The eigenvalues of a triangular matrix are the entries on its main
diagonal.

 $\lambda_1 = a_11 , \lambda_2 = a_22, \lambda_n = a_nn$

 So $det(A - I_3) = (a -\lambda)(b -\lambda)...$
<hr>

### similar matrixes
- $B = P A P^{-1}$
- A and B have same characteristic polynomial
**Note**: Stochastic Matrix is a square matrix whose columns are probability vectors with sum 1 of each row.