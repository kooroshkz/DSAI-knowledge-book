# Applications of Partial Derivatives
### Necessary conditions for extreme values
A function $f(x,y)$ can have a local or absolute extreme value at a point $(a,b)$ if one of the following:
- a critical point of f; that is, a point satisfying $ \nabla f(a, b) = 0 $
- a singular point of f; that is, a point where $ \nabla f(a, b) $ does not exist, or
- a boundary point of the domain of $f$.
### A second derivative test

**Hessian Matrix**

$ H(x) = 
\begin{bmatrix}
f_{11}(x) & f_{12}(x) & \cdots & f_{1n}(x) \\
f_{21}(x) & f_{22}(x) & \cdots & f_{2n}(x) \\
\vdots & \vdots & \ddots & \vdots \\
f_{n1}(x) & f_{n2}(x) & \cdots & f_{nn}(x)
\end{bmatrix}
$

- $ H(a) $ is positive definite then a local minimum at a. ($ f_{11} f_{22} - {f_{12}}^2 > 0 \land  f_{11} > 0 $)
- $ H(a) $ is negative definite then a local maximum at a. ($ f_{11} f_{22} - {f_{12}}^2 > 0 \land  f_{11} < 0 $)
- $ H(a) $ is indefinite then a saddle point at a. ($ f_{11} f_{22} - {f_{12}}^2 < 0 $)
- $ H(a) $ is non then test gives no information. ($ f_{11} f_{22} - {f_{12}}^2 = 0 $)

#### Note for Shape Optimization

Write down both S and V based on x, y and z then try to replace z using S and V