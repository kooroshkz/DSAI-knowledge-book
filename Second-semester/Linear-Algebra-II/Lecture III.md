#  The Dimension, Rank, Basis Change
## Rank & Row space

Row space shows the RREF rows where we have pivot in them

Column space shows the inital columns where we have pivots

**Dimension:** D(H) is the n of basis of Col(H)
**Dim(Nul(A)) =**  #{Free var RREF}

**Rank(A) = Dim(Col(A)) = Dim(Row(A)) =** #{Pivot columns of RREF}

n = Rank(A) + Dim(Nul(A))
#### Head up:

In $A_{n \times m}: Rank(A) \leq min(n, m)$
<hr>

## Change of Basis
- Coordinate mapping: $\underline{x} = P_b[\underline{x}]_B$
- Mapper From B to C: $P_{B \to C} = {P_C}^{-1} \cdot P_{B} $
- Mapping with mapper: $[\underline{x}]_C$ = $ P_{B \to C} [\underline{x}]_B$

Note:
    ${P_{B \to C}}^{-1} = P_{C \to B}$
